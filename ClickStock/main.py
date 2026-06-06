import wx
from interfaz.ventana_principal import VentanaPrincipal

app = wx.App()
frame = VentanaPrincipal()
frame.Show()
app.MainLoop()
