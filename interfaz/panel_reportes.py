import wx

#Esta clase la pase por IA para implementar la Impresion de los reportes de manera filtrada
class DocumentoImpresion(wx.Printout):
    def __init__(self, productos, categoria_filtro):
        super().__init__("Reporte de Productos")
        self.productos = productos
        self.categoria_filtro = categoria_filtro

    def OnPrintPage(self, page):
        dc = self.GetDC()
        
        ppi_pantalla_x, ppi_pantalla_y = self.GetPPIScreen()
        ppi_impresora_x, ppi_impresora_y = self.GetPPIPrinter()
        
        factor_escala_x = float(ppi_impresora_x) / float(ppi_pantalla_x)
        factor_escala_y = float(ppi_impresora_y) / float(ppi_pantalla_y)
        
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
        
        y = 145
        hay_productos = False
        
        for p in self.productos:
            if self.categoria_filtro != "Todas" and p.categoria.nombre != self.categoria_filtro:
                continue
                
            hay_productos = True
            dc.DrawText(p.nombre, 50, y)
            dc.DrawText(p.categoria.nombre, 230, y)
            dc.DrawText(f"${p.precio:.2f}", 400, y)
            dc.DrawText(str(p.stock), 500, y)
            y += 25 
            
        if not hay_productos:
            dc.DrawText("No existen productos para mostrar en esta categoría.", 50, y)
            
        return True

class PanelReportes(wx.Panel):

    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        titulo = wx.StaticText(self, label="Reportes")
        fuente_titulo = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        titulo.SetFont(fuente_titulo)
        texto_categorias = wx.StaticText(self, label="Categoría")

        self.combo_categoria = wx.ComboBox(self, style=wx.CB_READONLY)

        self.cargar_categorias()

        boton_generar = wx.Button(self, label="Generar Reporte")
        boton_imprimir = wx.Button(self, label="Imprimir Reporte")

        bitmap_impresora = wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_BUTTON)
        boton_imprimir.SetBitmap(bitmap_impresora)

        self.texto_reporte = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)

        boton_generar.Bind(wx.EVT_BUTTON, self.generar_reporte)
        boton_imprimir.Bind(wx.EVT_BUTTON, self.imprimir_reporte)

        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        sizer_principal.Add(titulo, 0, wx.ALL, 10)
        sizer_principal.Add(texto_categorias, 0, wx.ALL, 5)
        sizer_principal.Add(self.combo_categoria, 0, wx.EXPAND | wx.ALL, 5)

        sizer_botones = wx.BoxSizer(wx.HORIZONTAL)
        sizer_botones.Add(boton_generar, 0, wx.EXPAND | wx.ALL, 5)
        sizer_botones.Add(boton_imprimir, 0, wx.EXPAND | wx.ALL, 5)
        sizer_principal.Add(sizer_botones, 0, wx.ALL, 5)

        sizer_principal.Add(self.texto_reporte, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer_principal)

    def cargar_categorias(self):
        self.combo_categoria.Append("Todas")
        for categoria in self.sistema.obtener_categorias():
            self.combo_categoria.Append(categoria.nombre)
        self.combo_categoria.SetSelection(0)

    def generar_reporte(self, event):
        categoria_seleccionada = self.combo_categoria.GetStringSelection()
        reporte = ""

        for producto in self.sistema.obtener_productos():
            if categoria_seleccionada != "Todas" and producto.categoria.nombre != categoria_seleccionada:
                continue

            reporte += (
                f"{producto.nombre} | "
                f"{producto.categoria.nombre} | "
                f"${producto.precio:.2f} | "
                f"Stock: {producto.stock}\n"
            )
        
        if reporte == "":
            reporte = "No existen productos para mostrar."
        
        self.texto_reporte.SetValue(reporte)


    def imprimir_reporte(self, event):
        categoria_seleccionada = self.combo_categoria.GetStringSelection()
        datos_impresion = wx.PrintData()
        datos_impresion.SetPaperId(wx.PAPER_A4)
        dialogo = wx.PrintDialog(self, datos_impresion)
        
        if dialogo.ShowModal() == wx.ID_OK:
            dc_impresora = dialogo.GetPrintDC()
            
            if dc_impresora:
                productos = self.sistema.obtener_productos()
                documento = DocumentoImpresion(productos, categoria_seleccionada)
                impresor = wx.Printer(dialogo.GetPrintDialogData())
                impresor.Print(self, documento, prompt=False)           
                documento.Destroy()
        dialogo.Destroy()