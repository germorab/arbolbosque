from django.db import models


class Imagen(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
#    elemento = models.FileField('/medios/')
    
    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.descripcion)


class Texto(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    
    def __unicode__(self):
        return u'%s %s' % (self.titulo, self.contenido)


class Revision(models.Model):
    fecha = models.DateField()
    comentarios = models.TextField()
    
    def __unicode__(self):
        return u'%s %s' % (self.fecha, self.comentarios)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.descripcion)

class CategoriaLink(models.Model):
    texto = models.ForeignKey(Texto)
    categoria = models.ForeignKey(Categoria)
    
    def __unicode__(self):
        return u'%s %s' % (self.texto, self.categoria)


#class Resumen(models.Model):
#    resumen = models.TextField()


class Pagina(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.ForeignKey(Texto)
    revision = models.ForeignKey(Revision)
    imagen = models.ForeignKey(Imagen)
    #resumen = models.ForeignKey(Resumen)
    
    def __unicode__(self):
        return self.titulo


class IndiceDeBusqueda(models.Model):
    titulo = models.CharField(max_length=50)
    metadatos = models.TextField()
    pagina = models.ForeignKey(Pagina)
    
    def __unicode__(self):
        return u'%s %s' % (self.titulo, self.metadatos)
