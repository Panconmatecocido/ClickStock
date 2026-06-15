import wx

class PanelReportes(wx.Panel):

    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        titulo = wx.StaticText(self, label="Reportes de Stock")
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
        wx.MessageBox("Todavía no implementado")