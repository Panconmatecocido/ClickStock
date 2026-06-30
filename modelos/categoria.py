class Categoria:
    def __init__(self, nombre):
        #Inicializa la categoría guardando su nombre
        self.nombre = nombre

    def __str__(self):
        #Al imprimir el objeto se lee directo el nombre de la categoría
        return self.nombre