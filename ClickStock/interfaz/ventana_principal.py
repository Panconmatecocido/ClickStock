import wx
from interfaz.panel_inicio import PanelInicio
from interfaz.panel_categorias import PanelCategorias
from interfaz.panel_productos import PanelProductos
from interfaz.panel_stock import PanelStock
from interfaz.panel_reportes import PanelReportes

class VentanaPrincipal(wx.Frame):
    def __init__(self, sistema):
        super().__init__(None, title="ClickStock", size=(1000, 600))
        
        self.sistema = sistema

        panel_principal = wx.Panel(self)

        #Sizer horizontal para dividir la ventana en dos partes
        sizer_horizontal = wx.BoxSizer(wx.HORIZONTAL)

        #Panel izquierdo (menú)
        self.panel_menu = wx.Panel(panel_principal, size=(200, -1))
        self.panel_menu.SetBackgroundColour("#2c3E50")
        
        #Panel derecho (contenido)
        self.panel_contenido = wx.Panel(panel_principal)
        self.panel_contenido.SetBackgroundColour("white")

        #Agregar paneles al sizer horizontal
        sizer_horizontal.Add(self.panel_menu, 0, wx.EXPAND)
        sizer_horizontal.Add(self.panel_contenido, 1, wx.EXPAND)

        panel_principal.SetSizer(sizer_horizontal)
        
        self.crear_menu()
        
        self.mostrar_inicio(None)

    def crear_menu(self):

        sizer_menu = wx.BoxSizer(wx.VERTICAL)

        boton_inicio = wx.Button(self.panel_menu, label="Inicio")
        boton_categorias = wx.Button(self.panel_menu, label="Categorías")
        boton_productos = wx.Button(self.panel_menu, label="Productos")
        boton_stock = wx.Button(self.panel_menu, label="Stock")
        boton_reportes = wx.Button(self.panel_menu, label="Reportes")

        sizer_menu.Add(boton_inicio, 0, wx.EXPAND | wx.ALL, 10)
        sizer_menu.Add(boton_categorias, 0, wx.EXPAND | wx.ALL, 10)
        sizer_menu.Add(boton_productos, 0, wx.EXPAND | wx.ALL, 10)
        sizer_menu.Add(boton_stock, 0, wx.EXPAND | wx.ALL, 10)
        sizer_menu.Add(boton_reportes, 0, wx.EXPAND | wx.ALL, 10)

        self.panel_menu.SetSizer(sizer_menu)

        #Eventos para los botones
        boton_inicio.Bind(wx.EVT_BUTTON, self.mostrar_inicio)
        boton_categorias.Bind(wx.EVT_BUTTON, self.mostrar_categorias)
        boton_productos.Bind(wx.EVT_BUTTON, self.mostrar_productos)
        boton_stock.Bind(wx.EVT_BUTTON, self.mostrar_stock)
        boton_reportes.Bind(wx.EVT_BUTTON, self.mostrar_reportes)

    def cambiar_panel(self, constructor_panel):
        #Eliminar el panel actual
        for child in self.panel_contenido.GetChildren():
            child.Destroy()

        sizer_actual = self.panel_contenido.GetSizer()

        if sizer_actual:
            sizer_actual.Clear(True)
        
        nuevo_panel = constructor_panel(self.panel_contenido)

        if not sizer_actual:
            sizer_actual = wx.BoxSizer(wx.VERTICAL)
            self.panel_contenido.SetSizer(sizer_actual)
        
        sizer_actual.Add(nuevo_panel, 1, wx.EXPAND)
        self.panel_contenido.Layout()

    def mostrar_inicio(self, event):
        self.cambiar_panel(PanelInicio)
    
    def mostrar_categorias(self, event):
        self.cambiar_panel(lambda parent: PanelCategorias(parent, self.sistema))
    
    def mostrar_productos(self, event):
        self.cambiar_panel(lambda parent: PanelProductos(parent, self.sistema))
    
    def mostrar_stock(self, event):
        self.cambiar_panel(lambda parent: PanelStock(parent, self.sistema))

    def mostrar_reportes(self, event):
        self.cambiar_panel(lambda parent: PanelReportes(parent, self.sistema))