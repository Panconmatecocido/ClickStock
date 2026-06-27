import wx

class PanelStock(wx.Panel):
    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        titulo = wx.StaticText(self, label="Agregar Stock")
        fuente_titulo = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        titulo.SetFont(fuente_titulo)

        texto_producto = wx.StaticText(self, label="Producto")
        self.combo_producto = wx.ComboBox(self, style=wx.CB_READONLY) 

        self.input_cantidad = wx.TextCtrl(self)
        self.input_cantidad.SetHint("Cantidad")
        
        self.lista_stock = wx.ListBox(self)
        self.cargar_productos()
        self.actualizar_lista()

        boton_entrada = wx.Button(self, label="Agregar")
        boton_salida = wx.Button(self, label="Sacar")

        boton_entrada.Bind(wx.EVT_BUTTON, self.registrar_entrada)
        boton_salida.Bind(wx.EVT_BUTTON, self.registrar_salida)

        sizer_botones = wx.BoxSizer(wx.HORIZONTAL)
        sizer_botones.Add(boton_entrada, 0, wx.RIGHT, 5)
        sizer_botones.Add(boton_salida, 0, wx.RIGHT, 5)

        sizer_principal = wx.BoxSizer(wx.VERTICAL)

        sizer_principal.Add(titulo, 0, wx.ALL, 10)

        sizer_principal.Add(texto_producto, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        sizer_principal.Add(self.combo_producto, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        sizer_principal.Add(self.input_cantidad, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        sizer_principal.Add(sizer_botones, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        sizer_principal.Add(self.lista_stock, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        
        self.SetSizer(sizer_principal)

    def cargar_productos(self):
        self.combo_producto.Clear()
        for producto in self.sistema.obtener_productos():
            self.combo_producto.Append(producto.nombre)

        if self.combo_producto.GetCount() > 0:
            self.combo_producto.SetSelection(0)

    
    def actualizar_lista(self):
        self.lista_stock.Clear()
        for producto in self.sistema.obtener_productos():
            texto = (
                f"{producto.nombre} | Stock: {producto.stock}"
            )
            self.lista_stock.Append(texto)

    def registrar_entrada(self, event):
        indice = self.combo_producto.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        try:
            cantidad = int(self.input_cantidad.GetValue())
        except ValueError:
            return
        
        if cantidad <= 0:
            wx.MessageBox("La cantidad debe ser mayor a cero", "Error", wx.OK | wx.ICON_ERROR)
            return

        producto = self.sistema.obtener_productos()[indice]
        producto.ingresar_stock(cantidad)
        self.sistema.guardar_productos()
        self.actualizar_lista()
        self.input_cantidad.SetValue("")

    def registrar_salida(self, event):
        indice = self.combo_producto.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        try:
            cantidad = int(self.input_cantidad.GetValue())
        except ValueError:
            return
        
        if cantidad <= 0:
            wx.MessageBox("La cantidad debe ser mayor a cero", "Error", wx.OK | wx.ICON_ERROR)
            return

        producto = self.sistema.obtener_productos()[indice]
        if producto.stock >= cantidad:
            producto.retirar_stock(cantidad)
        else:
            wx.MessageBox("Stock insuficiente", "Error", wx.OK | wx.ICON_ERROR)
        self.sistema.guardar_productos()
        self.actualizar_lista()
        self.input_cantidad.SetValue("")