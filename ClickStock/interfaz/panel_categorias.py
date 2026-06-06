import wx


class PanelCategorias(wx.Panel):
    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        vbox = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Gestión de Categorías")
        titulo.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(titulo, 0, wx.ALL | wx.CENTER, 20)

        # Aquí puedes agregar botones y funcionalidades para gestionar categorías
        

        self.SetSizer(vbox)