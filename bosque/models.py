from django.db import models


class Imagen(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.FileField(upload_to = './')
    
    def __unicode__(self):
        return u'%s - %s' % (self.nombre, str(self.imagen))


class Revision(models.Model):
    fecha = models.DateField()
    comentarios = models.TextField()
    
    def __unicode__(self):
        return u'%s - %s' % (self.fecha, self.comentarios)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.descripcion)


class IndiceDeBusqueda(models.Model):
    palabrasclave = models.TextField()
    
    def __unicode__(self):
        return u'%s' % (self.palabrasclave)


class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    revision = models.ForeignKey(Revision, null=True, blank=True)
    imagen = models.ForeignKey(Imagen, null=True, blank=True )
    
    def __unicode__(self):
        return u'%s - %s' % (self.titulo, self.contenido)


class IndiceBusquedaArticulo(models.Model):
    articulo = models.ForeignKey(Articulo)
    indicebusqueda = models.ForeignKey(IndiceDeBusqueda)
    
    def __unicode__(self):
        return u'%s - %s' % (self.articulo, self.indicebusqueda)


class CategoriaLink(models.Model):
    articulo = models.ForeignKey(Articulo)
    categoria = models.ForeignKey(Categoria)
    
    def __unicode__(self):
        return u'%s - %s' % (self.articulo, self.categoria)
