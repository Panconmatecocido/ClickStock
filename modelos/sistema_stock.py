import sqlite3

from modelos.categoria import Categoria
from modelos.producto import Producto

class SistemaStock:
    def __init__(self):
        self.categorias = []
        self.productos = []

        #Configuramos la base de datos y carga de informacion
        self.crear_base()
        self.cargar_categorias()
        self.cargar_productos()
    
    def crear_base(self):
        #Creamos el archivo de la base de datos
        conexion = sqlite3.connect("datos/stock.db")
        cursor = conexion.cursor()

        #Creamos la tabla de categorias si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE NOT NULL
            )
        """)

        #Creamos la tabla de productos si no existe
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE NOT NULL,
                    precio REAL,
                    categoria TEXT,
                    stock INTEGER
                )
            """)


        #Agrega una categoria a la lista si su nombre no está registrado
    def agregar_categoria(self, categoria):
        for c in self.categorias:
            if c.nombre == categoria.nombre:
                return False
        self.categorias.append(categoria)
        return True

        #Devuelve la lista actual de categorías en memoria
    def obtener_categorias(self):
        return self.categorias

        #Elimina una categoría de la lista según su indice
    def eliminar_categoria(self, indice):
        del self.categorias[indice]
        
        #Agrega un producto a la lista si su nombre no está registrado
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                return False
        self.productos.append(producto)
        return True

        #Devuelve la lista actual de productos en memoria
    def obtener_productos(self):
        return self.productos

        #Elimina un producto de la lista según su indice
    def eliminar_producto(self, indice):
        del self.productos[indice]

        #Sincroniza y vuelca las categorías de la memoria en la base de datos
    def guardar_categorias(self):
        conexion = sqlite3.connect("datos/stock.db")
        cursor = conexion.cursor()
        #Limpia la tabla para evitar duplicaciones antes de reescribir
        cursor.execute("DELETE FROM categorias")
        
        #Inserta cada categoría activa de la lista
        for categoria in self.categorias:
            cursor.execute(
                "INSERT INTO categorias(nombre) VALUES(?)",
                (categoria.nombre,)
            )
        conexion.commit()
        conexion.close()

        #Trae las categorias desde la base de datos y las levanta en memoria
    def cargar_categorias(self):
        conexion = sqlite3.connect("datos/stock.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre FROM categorias")
        datos = cursor.fetchall()
        
        #Vaciamos la lista antes de la carga
        self.categorias.clear()

        #Armamos los objetos Categoria con lo que vino de la base de datos
        for nombre, in datos:
            categoria = Categoria(nombre)
            self.categorias.append(categoria)
        conexion.close()

        #Pasa los productos de la memoria a la base de datos
    def guardar_productos(self):
        conexion = sqlite3.connect("datos/stock.db")
        cursor = conexion.cursor()
        #Limpiamos la tabla para arrancar de cero antes de guardar
        cursor.execute("DELETE FROM productos")
        
        #Guardamos cada producto relacionándolo con el nombre de su categoría
        for producto in self.productos:
            cursor.execute("""
                INSERT INTO productos
                (nombre, precio, categoria, stock)
                VALUES(?,?,?,?)
            """, (

                producto.nombre,
                producto.precio,
                producto.categoria.nombre,
                producto.stock

            ))

        conexion.commit()
        conexion.close()

        #Trae los productos de la base y los engancha con su categoría correspondiente
    def cargar_productos(self):
        conexion = sqlite3.connect("datos/stock.db")
        cursor = conexion.cursor()
        cursor.execute("""

            SELECT
                nombre,
                precio,
                categoria,
                stock

            FROM productos

        """)
        datos = cursor.fetchall()
        self.productos.clear()

        for nombre, precio, categoria_nombre, stock in datos:
            #Buscamos si la categoría del producto existe en nuestra lista de categorías
            categoria = next(
                (
                    c for c in self.categorias
                    if c.nombre == categoria_nombre
                ),
                None
            )
            #Si la encontramos, armamos el objeto Producto y lo metemos a la lista
            if categoria:
                producto = Producto(
                    nombre,
                    precio,
                    categoria
                )
                producto.stock = stock
                self.productos.append(producto)
        conexion.close()

        #Busca un producto en memoria usando el nombre exacto
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None