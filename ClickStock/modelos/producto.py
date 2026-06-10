class Producto:

    def __init__(self, nombre, precio, categoria):

        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

        self.stock = 0

    def __str__(self):

        return self.nombre