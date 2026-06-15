import wx

from modelos.producto import Producto

class PanelProductos(wx.Panel):

    def __init__(self, parent, sistema):

        super().__init__(parent)

        self.sistema = sistema
    
        texto_nombre = wx.StaticText(self, label="Nombre producto")
        self.input_nombre = wx.TextCtrl(self)

        texto_precio = wx.StaticText(self, label="Precio")
        self.input_precio = wx.TextCtrl(self)

        texto_categoria = wx.StaticText(self, label="Categoría")
        self.combo_categoria = wx.ComboBox(self, style=wx.CB_READONLY)
        self.lista_productos = wx.ListBox(self)

        self.cargar_categorias()
        self.actualizar_lista()

        boton_agregar = wx.Button(self, label="Agregar")
        boton_eliminar = wx.Button(self, label="Eliminar")
        boton_editar = wx.Button(self, label="Editar")

        boton_agregar.Bind(wx.EVT_BUTTON, self.agregar_producto)
        boton_eliminar.Bind(wx.EVT_BUTTON, self.eliminar_producto)
        boton_editar.Bind(wx.EVT_BUTTON, self.editar_producto)
        self.lista_productos.Bind(wx.EVT_LISTBOX, self.seleccionar_producto)

        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        sizer_principal.Add(texto_nombre, 0, wx.ALL, 5)
        sizer_principal.Add(self.input_nombre, 0, wx.EXPAND | wx.ALL, 5)
        sizer_principal.Add(texto_precio, 0, wx.ALL, 5)
        sizer_principal.Add(self.input_precio, 0, wx.EXPAND | wx.ALL, 5)
        sizer_principal.Add(texto_categoria, 0, wx.ALL, 5)
        sizer_principal.Add(self.combo_categoria, 0, wx.EXPAND | wx.ALL, 5)
        sizer_principal.Add(boton_agregar, 0, wx.ALL, 5)
        sizer_principal.Add(boton_eliminar, 0, wx.ALL, 5)
        sizer_principal.Add(boton_editar, 0, wx.ALL, 5)
        sizer_principal.Add(self.lista_productos, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer_principal)

        self.actualizar_lista()


    def cargar_categorias(self):

        if self.combo_categoria.GetCount() > 0:
            wx.MessageBox("No hay categorias cargadas.\nDebe crear una categoría primero.", "Información", wx.OK | wx.ICON_INFORMATION)

        self.combo_categoria.Clear()

        for categoria in self.sistema.obtener_categorias():

            self.combo_categoria.Append(categoria.nombre)
        
        if self.combo_categoria.GetCount() > 0:
            self.combo_categoria.SetSelection(0)

    def agregar_producto(self, event):

        if len(self.sistema.obtener_categorias()) == 0:
            wx.MessageBox("Debe agregar una categoría antes de agregar productos", "Error", wx.OK | wx.ICON_ERROR)
            return

        nombre = self.input_nombre.GetValue().strip()
        precio_texto = self.input_precio.GetValue().strip()
        categoria_indice = self.combo_categoria.GetSelection()

        if nombre == "":
            return

        if precio_texto == "":
            return

        if categoria_indice == wx.NOT_FOUND:
            return

        precio = float(precio_texto)
        try:
            precio = float(precio_texto)
        except ValueError:
            wx.MessageBox("El precio debe ser un número válido", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        if precio < 0:
            wx.MessageBox("El precio no puede ser negativo", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        categoria = self.sistema.obtener_categorias()[categoria_indice]
        
        producto = Producto(nombre, precio, categoria)
       
        resultado = self.sistema.agregar_producto(producto)
        if not resultado:
            wx.MessageBox("El producto ya existe", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.actualizar_lista()
        self.limpiar_campos()
        self.sistema.guardar_productos()
    
    def eliminar_producto(self, event):
        indice = self.lista_productos.GetSelection()

        if indice == wx.NOT_FOUND:
            return

        self.sistema.eliminar_producto(indice)
        self.actualizar_lista()
        self.sistema.guardar_productos()

    def editar_producto(self, event):
        indice = self.lista_productos.GetSelection()

        if indice == wx.NOT_FOUND:
            return

        nombre = self.input_nombre.GetValue().strip()
        precio_texto = self.input_precio.GetValue().strip()
        categoria_indice = self.combo_categoria.GetSelection()

        if nombre == "":
            return

        if precio_texto == "":
            return

        if categoria_indice == wx.NOT_FOUND:
            return

        precio = float(precio_texto)
        categoria = self.sistema.obtener_categorias()[categoria_indice]
        producto = self.sistema.obtener_productos()[indice]
        producto.nombre = nombre
        producto.precio = precio
        producto.categoria = categoria

        self.actualizar_lista()
        self.limpiar_campos()
        self.sistema.guardar_productos()

    def actualizar_lista(self):

        self.lista_productos.Clear()

        for producto in self.sistema.obtener_productos():

            texto = (
            f"{producto.nombre} | "
            f"${producto.precio:.2f} | "
            f"{producto.categoria.nombre} | "
            f"stock: {producto.stock}" ) 

            self.lista_productos.Append(texto)
    
    def limpiar_campos(self):

        self.input_nombre.SetValue("")
        self.input_precio.SetValue("")
        self.combo_categoria.SetSelection(wx.NOT_FOUND)
    
    def seleccionar_producto(self, event):

        indice = self.lista_productos.GetSelection()

        if indice == wx.NOT_FOUND:
            return

        producto = self.sistema.obtener_productos()[indice]

        self.input_nombre.SetValue(producto.nombre)
        self.input_precio.SetValue(str(producto.precio))

        categoria = self.sistema.obtener_categorias()

        indice_categoria = categoria.index(producto.categoria)

        self.combo_categoria.SetSelection(indice_categoria)