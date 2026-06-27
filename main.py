import wx

from modelos.sistema_stock import SistemaStock
from interfaz.splash import SplashScreen


app = wx.App()

sistema = SistemaStock()

SplashScreen(sistema)

app.MainLoop()