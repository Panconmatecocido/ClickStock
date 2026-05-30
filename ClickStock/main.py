import wx
from interfaz.ventana_principal import VentanaPrincipal
from modelos.sistema import Sistema

app = wx.App()

sistema = Sistema()

ventana = VentanaPrincipal(sistema)
ventana.Show()

app.MainLoop()