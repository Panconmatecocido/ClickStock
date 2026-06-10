import wx

class PanelStock(wx.Panel):
    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        self.cargar_productos()
        
        self.input_cantidad = wx.TextCtrl(self)

        self.lista_stock = wx.ListBox(self)

        boton_entrada = wx.Button(self, label = "Entrada")
        boton_salida = wx.Button(self, label = "Salida")

        boton_entrada.Bind(wx.EVT_BUTTON, self.registrar_entrada)
        boton_salida.Bind(wx.EVT_BUTTON, self.registrar_salida)

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
        
        cantindad = int (self.input_cantidad.GetValue())

        producto = self.sistema.obtener_productos()[indice]
        producto.stock += cantindad
        self.actualizar_lista()

    def registrar_salida(self, event):
        indice = self.combo_producto.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        cantidad = int (self.input_cantidad.GetValue())

        producto = self.sistema.obtener_productos()[indice]
        if producto.stock >= cantidad:
            producto.stock -= cantidad
        self.actualizar_lista()