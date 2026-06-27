import wx
from modelos.categoria import Categoria

class PanelCategorias(wx.Panel):
    def __init__(self, parent, sistema):
        super().__init__(parent)
        self.sistema = sistema

        texto = wx.StaticText(self, label="Agregar Categorías")
        fuente = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        texto.SetFont(fuente)

        self.input_categoria = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.input_categoria.SetHint("Ingrese nueva categoría")

        boton_agregar = wx.Button(self, label="Agregar")
        boton_eliminar = wx.Button(self, label="Eliminar")
        boton_editar = wx.Button(self, label="Editar")

        self.lista_categorias = wx.ListBox(self)

        boton_agregar.Bind(wx.EVT_BUTTON, self.agregar_categoria)
        boton_eliminar.Bind(wx.EVT_BUTTON, self.eliminar_categoria)
        boton_editar.Bind(wx.EVT_BUTTON, self.editar_categoria)
        self.lista_categorias.Bind(wx.EVT_LISTBOX, self.seleccionar_categoria)
       
        #Fila Superior
        sizer_superior = wx.BoxSizer(wx.HORIZONTAL)
        sizer_superior.Add(self.input_categoria, 1, wx.EXPAND | wx.RIGHT, 10)
        sizer_superior.Add(boton_agregar, 0, wx.ALIGN_CENTER_VERTICAL)

        #Bloque de Botones Derechos
        sizer_botones_derechos = wx.BoxSizer(wx.VERTICAL)
        sizer_botones_derechos.Add(boton_editar, 0, wx.EXPAND | wx.BOTTOM, 10)
        sizer_botones_derechos.Add(boton_eliminar, 0, wx.EXPAND)

        #Fila Inferior
        sizer_inferior = wx.BoxSizer(wx.HORIZONTAL)
        sizer_inferior.Add(self.lista_categorias, 1, wx.EXPAND | wx.RIGHT, 10)
        sizer_inferior.Add(sizer_botones_derechos, 0, wx.ALIGN_TOP) # Alineados arriba al lado de la lista

        #Sizer Principal
        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        sizer_principal.Add(texto, 0, wx.TOP | wx.LEFT | wx.RIGHT, 15)
        sizer_principal.Add(sizer_superior, 0, wx.EXPAND | wx.ALL, 15)
        sizer_principal.Add(sizer_inferior, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 15)

        self.SetSizer(sizer_principal)

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