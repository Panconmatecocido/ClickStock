from modelos.categoria import Categoria
from modelos.venta import Venta

class Sistema:
    def __init__(self):
        self.categorias = []
        self.ventas = []
        self.ganancias = 0
    
    def agregar_categoria(self, nombre):
        nueva = Categoria(nombre)
        self.categorias.append(nueva)

    def buscar_categoria(self, nombre):
        for categoria in self.categorias:
            if categoria.nombre == nombre:
                return categoria
        return None
    
    def registrar_venta(self, producto, cantidad):
        if producto.vender(cantidad):
            venta = Venta(producto, cantidad)
            self.ventas.append(venta)
            self.ganancias += venta.total
            return True
        return False