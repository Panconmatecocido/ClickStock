import wx
from modelos.categoria import Categoria

class PanelCategorias(wx.Panel):
    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        texto = wx.StaticText(self, label="Nombre categoría")

        self.input_categoria = wx.TextCtrl(self)

        boton_agregar = wx.Button(self, label="Agregar")
        boton_eliminar = wx.Button(self, label="Eliminar")
        boton_editar = wx.Button(self, label="Editar")

        self.lista_categorias = wx.ListBox(self)

        boton_agregar.Bind(wx.EVT_BUTTON, self.agregar_categoria)
        boton_eliminar.Bind(wx.EVT_BUTTON, self.eliminar_categoria)
        boton_editar.Bind(wx.EVT_BUTTON, self.editar_categoria)
        self.lista_categorias.Bind(wx.EVT_LISTBOX, self.seleccionar_categoria)

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(texto, 0, wx.ALL, 10)
        sizer.Add(self.input_categoria, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.lista_categorias, 1, wx.EXPAND | wx.ALL, 10)
        
        sizer_botones = wx.BoxSizer(wx.HORIZONTAL)
        sizer_botones.Add(boton_agregar, 0, wx.EXPAND | wx.ALL, 5)
        sizer_botones.Add(boton_eliminar, 0, wx.EXPAND | wx.ALL, 5)
        sizer_botones.Add(boton_editar, 0, wx.ALL, 5)
        sizer.Add(sizer_botones, 0, wx.ALL, 5)

        self.SetSizer(sizer)

        self.actualizar_lista()

    def agregar_categoria(self, event):
        nombre = self.input_categoria.GetValue()
        if nombre == "":
             return
            
        categoria = Categoria(nombre)
        self.sistema.agregar_categoria(categoria)
        self.sistema.guardar_categorias()
        self.actualizar_lista()
        self.input_categoria.SetValue("")
    
    def eliminar_categoria(self, event):
        indice = self.lista_categorias.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        self.sistema.eliminar_categoria(indice)
        self.sistema.guardar_categorias()
        self.actualizar_lista()
    
    def actualizar_lista(self):
        self.lista_categorias.Clear()
        for categoria in self.sistema.obtener_categorias():
            self.lista_categorias.Append(categoria.nombre)

    def seleccionar_categoria(self, event):
        indice = self.lista_categorias.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        categoria = self.sistema.obtener_categorias()[indice]
        self.input_categoria.SetValue(categoria.nombre)

    def editar_categoria(self, event):
        indice = self.lista_categorias.GetSelection()
        if indice == wx.NOT_FOUND:
            return
        
        nuevo_nombre = self.input_categoria.GetValue()
        if nuevo_nombre == "":
            return
        
        categoria = self.sistema.obtener_categorias()[indice]
        categoria.nombre = nuevo_nombre
        self.sistema.guardar_categorias()
        self.actualizar_lista()