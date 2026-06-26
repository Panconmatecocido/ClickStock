#!/usr/bin/env python

import wx
import wx.adv
from wx.lib.wordwrap import wordwrap

#----------------------------------------------------------------------

class PanelCreditos(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Ayuda", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):

        info = wx.adv.AboutDialogInfo()

        info.Name = "ClickStock"

        info.Version = "1.0.0"

        info.Copyright = "© 2026 clickstock Programación Orientada a Objetos"

        info.Description = wordwrap(
            "ClickStock es una aplicación de escritorio desarrollada en Python "
            "utilizando la biblioteca wxPython para facilitar la gestión de inventarios. "
            "Permite administrar categorías y productos, registrar entradas y salidas "
            "de stock y generar reportes filtrados por categoría. "
            "Su objetivo es ayudar a pequeños comercios y emprendimientos a mantener "
            "un control organizado de su inventario, optimizando la administración "
            "de la mercadería y reduciendo errores en el manejo del stock.",
            350,
            wx.ClientDC(self)
        )

        info.WebSite = (
            "https://github.com/",
            "Repositorio del proyecto"
        )

        info.Developers = [
            "Iván Rodriguez",
            "Materia: Programación Orientada a Objetos",
            "Universidad: Universidad Nacional de Pilar(UNPILAR)"
        ]

        info.License = wordwrap(
            licenseText,
            500,
            wx.ClientDC(self)
        )

        wx.adv.AboutBox(info)


#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#----------------------------------------------------------------------



overview = """<html><body>
<h2><center>wx.AboutBox</center></h2>

This function shows the native standard about dialog containing the
information specified in info. If the current platform has a native
about dialog which is capable of showing all the fields in info, the
native dialog is used, otherwise the function falls back to the
generic wxWidgets version of the dialog.

</body></html>
"""


licenseText = """
Licencia MIT

Copyright (c) 2026

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una
copia de este software y de los archivos de documentación asociados para
utilizarlo, copiarlo, modificarlo y distribuirlo, siempre que se conserve
este aviso de copyright y la presente licencia.

Este software ha sido desarrollado con fines académicos para la materia
Programación Orientada a Objetos.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO,
EXPRESA O IMPLÍCITA, INCLUYENDO, ENTRE OTRAS, LAS GARANTÍAS DE
COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN.
EN NINGÚN CASO LOS AUTORES SERÁN RESPONSABLES POR DAÑOS O CUALQUIER OTRA
RESPONSABILIDAD DERIVADA DEL USO DEL SOFTWARE.
"""


if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
