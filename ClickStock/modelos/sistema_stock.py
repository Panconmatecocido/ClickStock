import json

from modelos.categoria import Categoria
from modelos.producto import Producto

class SistemaStock:
    def __init__(self):
        self.categorias = []
        self.productos = []

        self.cargar_categorias()
        self.cargar_productos()
    
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

    def guardar_categorias(self):
        datos = []
        
        for categoria in self.categorias:
            datos.append({"nombre": categoria.nombre})
       
        with open("datos/categorias.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_categorias(self):
        try:
            with open("datos/categorias.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

                for item in datos:
                    categoria = Categoria(item["nombre"])
                    self.categorias.append(categoria)
        except FileNotFoundError:
            pass
    
    def guardar_productos(self):
        datos = []

        for producto in self.productos:
            datos.append({
                "nombre": producto.nombre,
                "precio": producto.precio,
                "categoria": producto.categoria.nombre,
                "stock": producto.stock
            })
        
        with open("datos/productos.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_productos(self):

        try:

            with open(
                "datos/productos.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                for item in datos:

                    categoria = next(

                        c for c in self.categorias

                        if c.nombre ==
                        item["categoria"]
                    )

                    producto = Producto(

                        item["nombre"],

                        item["precio"],

                        categoria
                    )

                    producto.stock = item["stock"]

                    self.productos.append(
                        producto
                    )

        except FileNotFoundError:

            pass