import wx
from interfaz.ventana_principal import VentanaPrincipal
from modelos.sistema_stock import SistemaStock

app = wx.App()
sistema = SistemaStock()  # Crear instancia del sistema de stock
frame = VentanaPrincipal(sistema)
frame.Show()
app.MainLoop()
