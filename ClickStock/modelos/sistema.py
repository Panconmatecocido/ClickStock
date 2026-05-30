from modelos.categoria import Categoria
class Sistema:
    def __init__(self):
        self.categorias = []
        self.ganancias = 0
    
    def agregar_categoria(self, nombre):
        nueva = Categoria(nombre)
        self.categorias.append(nueva)

    def buscar_categoria(self, nombre):
        for categoria in self.categorias:
            if categoria.nombre == nombre:
                return categoria
        return None
    