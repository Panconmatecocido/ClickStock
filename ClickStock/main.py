import wx
from modelos.sistema import Sistema
from interfaz.ventana_principal import VentanaPrincipal

app = wx.App()

sistema = Sistema()

ventana = VentanaPrincipal(sistema)
ventana.Show()

app.MainLoop()