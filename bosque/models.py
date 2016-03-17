from django.core.urlresolvers import reverse
from django.db import models

from bosque.utils import make_absolute_url


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


class Tematica(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.descripcion)

    # API REST methods

    def get_categories_api_url(self):

        reverse_url = reverse(
            'forest:v1:thematic_categories', args=[self.pk]
        )

        return make_absolute_url(reverse_url)

    # End API REST methods


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    tematica = models.ForeignKey(Tematica)
    
    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.descripcion)

    # API REST methods

    def get_thematic_api_url(self):

        reverse_url = reverse(
            'forest:v1:category_thematic', args=[self.pk]
        )

        return make_absolute_url(reverse_url)

    def get_articles_api_url(self):

        reverse_url = reverse(
            'forest:v1:category_articles', args=[self.pk]
        )

        return make_absolute_url(reverse_url)

    # End API REST methods


class IndiceDeBusqueda(models.Model):
    palabrasclave = models.TextField()
    
    def __unicode__(self):
        return u'%s' % (self.palabrasclave)


class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    revision = models.ForeignKey(Revision, null=True, blank=True)
    imagen = models.ForeignKey(Imagen, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria)
    
    def __unicode__(self):
        return u'%s - %s' % (self.titulo, self.contenido)

    # API REST methods

    def get_categories_api_url(self):

        reverse_url = reverse(
            'forest:v1:article_categories', args=[self.pk]
        )

        return make_absolute_url(reverse_url)

    # End API REST methods


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
