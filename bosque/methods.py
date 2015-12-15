from models import *
import traceback

def consultarCategorias ():
    try:
        catslist = []
        cats = Categoria.objects.all()
        print cats
        for one in cats:
             catslist.append ([one.id, one.nombre])
        return catslist
    except:
        print "except - consultarCategorias"
        cats = []
    return cats


def guardarTextoNuevo (titulo, contenido, categoria):

    nt = Texto(titulo = titulo, contenido = contenido)
    nt.save()
    
    for i in categoria:
        categoriai = Categoria.objects.get(id = int(i))
        ctl = CategoriaLink (categoria = categoriai, texto = nt)
        ctl.save()


def guardarCategoriaNueva (nombre, descripcion):
    nc = Categoria(nombre = nombre, descripcion = descripcion)
    nc.save()


def consultarPagina (titulo):
    
    pag = {}
    
    try:
        pagob = Pagina.objects.get (titulo = titulo)
        pag['titulo'] = titulo
        pag['texto'] = Texto.objects.get(id = pagob.texto_id).contenido
        cates = []
        categ = CategoriaLink.objects.get(texto =  pagob.texto_id)
        cates.append(categ.categoria.nombre)
        pag['categorias'] = cates
        
    except:
        print "except - consultarPagina"
        print traceback.format_exc()
        pag = None
        
    return pag
    
    #armar lista 
