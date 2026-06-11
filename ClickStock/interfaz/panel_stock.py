import wx

class PanelStock(wx.Panel):
    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema
        self.combo_producto = wx.ComboBox(self, style=wx.CB_READONLY) 
        self.input_cantidad = wx.TextCtrl(self)
        self.lista_stock = wx.ListBox(self)
        self.cargar_productos()
        self.actualizar_lista()


        boton_entrada = wx.Button(self, label = "Entrada")
        boton_salida = wx.Button(self, label = "Salida")

        texto_producto = wx.StaticText(self, label="Producto")
        texto_cantidad = wx.StaticText(self, label="Cantidad")

        boton_entrada.Bind(wx.EVT_BUTTON, self.registrar_entrada)
        boton_salida.Bind(wx.EVT_BUTTON, self.registrar_salida)

        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        sizer_principal.Add(texto_producto, 0, wx.ALL, 5)
        sizer_principal.Add(self.combo_producto, 0, wx.EXPAND | wx.ALL, 5)
        sizer_principal.Add(texto_cantidad, 0, wx.ALL, 5)
        sizer_principal.Add(self.input_cantidad, 0, wx.EXPAND | wx.ALL, 5)

        sizer_botones = wx.BoxSizer(wx.HORIZONTAL)
        sizer_botones.Add(boton_entrada, 0, wx.EXPAND | wx.ALL, 5)
        sizer_botones.Add(boton_salida, 0, wx.EXPAND | wx.ALL, 5)
        sizer_principal.Add(sizer_botones, 0, wx.ALL, 5)
        sizer_principal.Add(self.lista_stock, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer_principal)

    def cargar_productos(self):
        self.combo_producto.Clear()
        for producto in self.sistema.obtener_productos():
            self.combo_producto.Append(producto.nombre)
    
    def actualizar_lista(self):
        self.lista_stock.Clear()
        for producto in self.sistema.obtener_productos():
            texto = (
            f"{producto.nombre} | "
            f"{producto.stock}")
            self.lista_stock.Append(texto)

    def registrar_entrada(self, event):
        indice = self.combo_producto.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        try:
            cantidad = int(self.input_cantidad.GetValue())
        except ValueError:
            return

        producto = self.sistema.obtener_productos()[indice]
        producto.stock += cantidad
        self.actualizar_lista()

    def registrar_salida(self, event):
        indice = self.combo_producto.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        try:
            cantidad = int(self.input_cantidad.GetValue())
        except ValueError:
            return

        producto = self.sistema.obtener_productos()[indice]
        if producto.stock >= cantidad:
            producto.stock -= cantidad
        self.actualizar_lista()