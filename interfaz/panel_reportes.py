import wx

    #Clase que se encarga de maquetar y 'dibujar' el reporte en la hoja física
    #Hereda de wx.Printout para interactuar directamente con el motor de impresión del sistema
class DocumentoImpresion(wx.Printout):
    def __init__(self, productos, categoria_filtro):
        #Guarda la lista de productos y el filtro elegido para saber qué imprimir
        super().__init__("Reporte de Productos")
        self.productos = productos
        self.categoria_filtro = categoria_filtro

    def OnPrintPage(self, page):
        #Método obligatorio que se ejecuta automáticamente cuando se manda a imprimir la página.
        #Se usa el Device Context (dc) como si fuera un lienzo de dibujo.
        dc = self.GetDC() #Obtenemos el contexto de dibujo de la impresora
        
        #Calculo de Escala
        #Comparamos los píxeles por pulgada (PPI) de la pantalla vs la impresora
        ppi_pantalla_x, ppi_pantalla_y = self.GetPPIScreen()
        ppi_impresora_x, ppi_impresora_y = self.GetPPIPrinter()
        
        #Sacamos el factor de conversión para que lo dibujado mantenga la proporción en papel
        factor_escala_x = float(ppi_impresora_x) / float(ppi_pantalla_x)
        factor_escala_y = float(ppi_impresora_y) / float(ppi_pantalla_y)
        
        #Aplicamos la escala al lienzo de dibujo
        dc.SetUserScale(factor_escala_x, factor_escala_y)

        #Configuracion Título Principal
        dc.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        dc.DrawText(f"REPORTE DE STOCK - CATEGORÍA: {self.categoria_filtro.upper()}", 50, 50)
        dc.DrawLine(50, 80, 550, 80)
        
        #Configuracion Encabezados de Tabla
        dc.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        dc.DrawText("Producto", 50, 100)
        dc.DrawText("Categoría", 230, 100)
        dc.DrawText("Precio", 400, 100)
        dc.DrawText("Stock", 500, 100)
        dc.DrawLine(50, 125, 550, 125)
        
        #Dibujar los Productos Filtrados
        dc.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        y = 145 #Posición vertical de arranque para la primera fila
        hay_productos = False
        
        for p in self.productos:
            #Si el filtro está activo y el producto no coincide, saltamos de largo
            if self.categoria_filtro != "Todas" and p.categoria.nombre != self.categoria_filtro:
                continue
                
            hay_productos = True
            #Dibujamos cada dato en su respectiva columna
            dc.DrawText(p.nombre, 50, y)
            dc.DrawText(p.categoria.nombre, 230, y)
            dc.DrawText(f"${p.precio:.2f}", 400, y)
            dc.DrawText(str(p.stock), 500, y)
            y += 25 #Bajamos un poco la posición 'Y' para escribir la siguiente fila
            
        #Si recorrimos toda la lista y no coincidió ninguno, avisamos en la hoja
        if not hay_productos:
            dc.DrawText("No existen productos para mostrar en esta categoría.", 50, y)
            
        return True #Le avisamos a wx que la página se dibujó joya y termino

class PanelReportes(wx.Panel):

    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        #Componentes de texto y títulos
        titulo = wx.StaticText(self, label="Reportes")
        fuente_titulo = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        titulo.SetFont(fuente_titulo)
        texto_categorias = wx.StaticText(self, label="Categoría")

        #Desplegable para seleccionar el filtro de categorías
        self.combo_categoria = wx.ComboBox(self, style=wx.CB_READONLY)
        self.cargar_categorias()

        #Botones de acción
        boton_generar = wx.Button(self, label="Generar Reporte")
        boton_imprimir = wx.Button(self, label="Imprimir Reporte")

        #Metemos un icono nativo de impresora al botón de imprimir
        bitmap_impresora = wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_BUTTON)
        boton_imprimir.SetBitmap(bitmap_impresora)

        #Caja de texto multilinea y de solo lectura para la previsualización en pantalla
        self.texto_reporte = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)

        #Enlazamos los eventos de click
        boton_generar.Bind(wx.EVT_BUTTON, self.generar_reporte)
        boton_imprimir.Bind(wx.EVT_BUTTON, self.imprimir_reporte)

        #Acomodo con Sizers
        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        sizer_principal.Add(titulo, 0, wx.ALL, 10)
        sizer_principal.Add(texto_categorias, 0, wx.ALL, 5)
        sizer_principal.Add(self.combo_categoria, 0, wx.EXPAND | wx.ALL, 5)

        #Sizer horizontal para los dos botones de acción pegados
        sizer_botones = wx.BoxSizer(wx.HORIZONTAL)
        sizer_botones.Add(boton_generar, 0, wx.EXPAND | wx.ALL, 5)
        sizer_botones.Add(boton_imprimir, 0, wx.EXPAND | wx.ALL, 5)
        sizer_principal.Add(sizer_botones, 0, wx.ALL, 5)

        #La caja de previsualización se estira para usar todo el espacio de abajo
        sizer_principal.Add(self.texto_reporte, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer_principal)

    def cargar_categorias(self):
        #Llena el desplegable sumando la opción comodín 'Todas' al principio
        self.combo_categoria.Append("Todas")
        for categoria in self.sistema.obtener_categorias():
            self.combo_categoria.Append(categoria.nombre)
        self.combo_categoria.SetSelection(0)

    def generar_reporte(self, event):
        #Arma el texto del reporte según el filtro y lo estampa en la caja de previsualización
        categoria_seleccionada = self.combo_categoria.GetStringSelection()
        reporte = ""

        for producto in self.sistema.obtener_productos():
            #Filtramos si no corresponde a la categoría elegida
            if categoria_seleccionada != "Todas" and producto.categoria.nombre != categoria_seleccionada:
                continue
            
            #Concatenamos la fila de texto formateando el precio a dos decimales
            reporte += (
                f"{producto.nombre} | "
                f"{producto.categoria.nombre} | "
                f"${producto.precio:.2f} | "
                f"Stock: {producto.stock}\n"
            )
        
        if reporte == "":
            reporte = "No existen productos para mostrar."
        
        self.texto_reporte.SetValue(reporte)

        #Abre la ventana de impresión nativa del sistema operativo para tirar el papel
    def imprimir_reporte(self, event):
        categoria_seleccionada = self.combo_categoria.GetStringSelection()
        
        #Configuramos los parámetros base de la impresión tamaño A4)
        datos_impresion = wx.PrintData()
        datos_impresion.SetPaperId(wx.PAPER_A4)
        
        #Levantamos el cuadro de diálogo típico para elegir impresora o guardar PDF
        dialogo = wx.PrintDialog(self, datos_impresion)
        
        #Si el usuario le dio al botón 'Aceptar/Imprimir' en el cuadro
        if dialogo.ShowModal() == wx.ID_OK:
            dc_impresora = dialogo.GetPrintDC()
            
            if dc_impresora:
                productos = self.sistema.obtener_productos()
                documento = DocumentoImpresion(productos, categoria_seleccionada)
                impresor = wx.Printer(dialogo.GetPrintDialogData())
                impresor.Print(self, documento, prompt=False)           
                documento.Destroy()
        dialogo.Destroy()