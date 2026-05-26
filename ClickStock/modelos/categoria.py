class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def buscar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None