import sqlite3

from modelos.categoria import Categoria
from modelos.producto import Producto

class SistemaStock:
    def __init__(self):
        self.categorias = []
        self.productos = []

        self.crear_base()

        self.cargar_categorias()
        self.cargar_productos()
    
    def crear_base(self):
        conexion = sqlite3.connect("ClickStock/datos/stock.db")
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE NOT NULL
            )
        """)
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE NOT NULL,
                    precio REAL,
                    categoria TEXT,
                    stock INTEGER
                )
            """)



    def agregar_categoria(self, categoria):
        for c in self.categorias:
            if c.nombre == categoria.nombre:
                return False
        self.categorias.append(categoria)
        return True

    def obtener_categorias(self):
        return self.categorias
    
    def eliminar_categoria(self, indice):
        del self.categorias[indice]

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                return False
        self.productos.append(producto)
        return True

    def obtener_productos(self):
        return self.productos
    
    def eliminar_producto(self, indice):
        del self.productos[indice]

    def guardar_categorias(self):
        conexion = sqlite3.connect("ClickStock/datos/stock.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM categorias")
        
        for categoria in self.categorias:
            cursor.execute(
                "INSERT INTO categorias(nombre) VALUES(?)",
                (categoria.nombre,)
            )
        conexion.commit()
        conexion.close()

    def cargar_categorias(self):
        conexion = sqlite3.connect("ClickStock/datos/stock.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre FROM categorias")
        datos = cursor.fetchall()
        self.categorias.clear()

        for nombre, in datos:
            categoria = Categoria(nombre)
            self.categorias.append(categoria)
        conexion.close()
    
    def guardar_productos(self):
        conexion = sqlite3.connect("ClickStock/datos/stock.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos")
        
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

    def cargar_productos(self):
        conexion = sqlite3.connect("ClickStock/datos/stock.db")
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
            categoria = next(
                (
                    c for c in self.categorias
                    if c.nombre == categoria_nombre
                ),
                None
            )

            if categoria:
                producto = Producto(
                    nombre,
                    precio,
                    categoria
                )
                producto.stock = stock
                self.productos.append(producto)
        conexion.close()
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None