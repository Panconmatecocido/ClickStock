class Producto:

    def __init__(self, nombre, precio, categoria):

        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

        self.stock = 0

    def __str__(self):

        return self.nombre
    
    def ingresar_stock(self, cantidad):

        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False