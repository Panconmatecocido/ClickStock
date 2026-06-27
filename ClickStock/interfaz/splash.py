import wx
import wx.adv
import os


class SplashScreen(wx.adv.SplashScreen):

    def __init__(self, sistema):

        ruta = os.path.join(
            os.path.dirname(__file__),
            "..",
            "Imagen",
            "logo.png"
        )

        ruta = os.path.abspath(ruta)

        imagen = wx.Image(ruta, wx.BITMAP_TYPE_PNG)

        imagen = wx.Image(ruta, wx.BITMAP_TYPE_PNG)
        imagen = imagen.Scale(300, 300, wx.IMAGE_QUALITY_HIGH)

        bitmap = wx.Bitmap(imagen)

        super().__init__(
            bitmap,
            wx.adv.SPLASH_CENTRE_ON_SCREEN |
            wx.adv.SPLASH_TIMEOUT,
            2500,          # 2,5 segundos
            None,
            -1
        )

        self.sistema = sistema

        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):

        self.Hide()

        from interfaz.ventana_principal import VentanaPrincipal

        frame = VentanaPrincipal(self.sistema)
        frame.Show()

        event.Skip()