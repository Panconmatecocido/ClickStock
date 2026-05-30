import wx
from interfaz import panel_inicio

class VentanaPrincipal(wx.Frame):
    def __init__(self, sistema):
        super().__init__(parent=None, title="ClickStock", size=(800,600))
        self.sistema = sistema
        self.CreateStatusBar()
        self.SetStatusText("Sistema Listo")

        menu_bar = wx.MenuBar()

        archivo_menu = wx.Menu()
        salir_item = archivo_menu.Append(wx.ID_EXIT, "Salir")

        menu_bar.Append(archivo_menu, "Archivo")

        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.salir, salir_item)

        self.panel_actual = panel_inicio.PanelInicio(self, self.sistema)
        self.Show()

    def salir(self, event):
        self.Close()