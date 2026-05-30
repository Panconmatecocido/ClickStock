import wx

class PanelInicio(wx.Panel):
    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        vbox = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Bienvenido a ClickStock")
        titulo.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(titulo, 0, wx.ALL | wx.CENTER, 20)

        btn_categoria = wx.Button(self, label="Categorias")
        btn_productos = wx.Button(self, label="Productos")
        btn_stock = wx.Button(self, label="Stock")
        btn_reportes = wx.Button(self, label="Reportes")

        vbox.Add(btn_categoria, 0, wx.ALL | wx.EXPAND, 10)
        vbox.Add(btn_productos, 0, wx.ALL | wx.EXPAND, 10)
        vbox.Add(btn_stock, 0, wx.ALL | wx.EXPAND, 10)
        vbox.Add(btn_reportes, 0, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(vbox)