import wx
import os

class PanelInicio(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.WHITE)
        texto_titulo = wx.StaticText(self, label="Bienvenido a ClickStock")
        fuente = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        texto_titulo.SetFont(fuente)
        ruta = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "Imagen",
            "logo.png"
        )
        imagen = wx.Image(ruta, wx.BITMAP_TYPE_ANY)
        imagen = imagen.Scale(220, 220)
        logo = wx.StaticBitmap(self, bitmap=wx.Bitmap(imagen))

        # DESCRIPCIÓN
        descripcion = wx.StaticText(
            self,
            label="Sistema de gestión de stock simple,\n"
                  "eficiente y fácil de usar."
        )
        descripcion.SetForegroundColour(wx.Colour(90, 90, 90))

        # SUBTÍTULO
        subtitulo = wx.StaticText(
            self,
            label="Funcionalidades principales:"
        )
        subtitulo.SetFont(wx.Font(
            11,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD
        ))
        subtitulo.SetForegroundColour(wx.Colour(25, 75, 180))

        # LISTA
        funcionalidades = [

            "✔ Gestión de categorías",
            "✔ Gestión de productos",
            "✔ Control de stock",
            "✔ Reportes y estadísticas"

        ]
        lista = wx.BoxSizer(wx.VERTICAL)
        for texto in funcionalidades:
            item = wx.StaticText(self, label=texto)
            item.SetForegroundColour(wx.Colour(70, 70, 70))
            lista.Add(item, 0, wx.BOTTOM, 8)

        # MENSAJE INFERIOR
        mensaje = wx.StaticText(
            self,
            label="ℹ  Seleccione una opción del menú lateral\n"
                  "    para comenzar."
        )
        mensaje.SetBackgroundColour(wx.Colour(235, 244, 255))
        mensaje.SetForegroundColour(wx.Colour(30, 60, 130))

        # PANEL DERECHO
        derecha = wx.BoxSizer(wx.VERTICAL)
        derecha.Add(texto_titulo, 0, wx.BOTTOM, 15)
        derecha.Add(descripcion, 0, wx.BOTTOM, 25)
        derecha.Add(subtitulo, 0, wx.BOTTOM, 15)
        derecha.Add(lista, 0, wx.BOTTOM, 25)
        derecha.Add(mensaje, 0)

        # PANEL PRINCIPAL
        principal = wx.BoxSizer(wx.HORIZONTAL)
        principal.AddStretchSpacer()
        principal.Add(
            logo,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.RIGHT,
            50
        )
        principal.Add(
            derecha,
            0,
            wx.ALIGN_CENTER_VERTICAL
        )
        principal.AddStretchSpacer()
        exterior = wx.BoxSizer(wx.VERTICAL)
        exterior.AddStretchSpacer()
        exterior.Add(principal, 0, wx.EXPAND)
        exterior.AddStretchSpacer()

        self.SetSizer(exterior)