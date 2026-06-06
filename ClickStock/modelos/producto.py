class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def descontar(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False
    
    def reponer_stock(self, cantidad):
        self.stock += cantidad