import wx

class PanelInicio(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        
        texto_titulo = wx.StaticText(self, label="Bienvenido a ClickStock")

        fuente = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        texto_titulo.SetFont(fuente)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(texto_titulo, 0, wx.ALL | wx.CENTER, 20)
        self.SetSizer(sizer)