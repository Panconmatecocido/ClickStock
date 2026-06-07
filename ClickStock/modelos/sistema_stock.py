class SistemaStock:
    def __init__(self):
        self.categorias = []
        self.productos = []
    
    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def obtener_categorias(self):
        return self.categorias
    
    def eliminar_categoria(self, indice):
        del self.categorias[indice]

    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def obtener_productos(self):
        return self.productos
    
    def eliminar_producto(self, indice):
        del self.productos[indice]