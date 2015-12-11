# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articulo', models.ForeignKey(to='bosque.Articulo')),
                ('categoria', models.ForeignKey(to='bosque.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.FileField(upload_to=b'./')),
            ],
        ),
        migrations.CreateModel(
            name='IndiceBusquedaArticulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articulo', models.ForeignKey(to='bosque.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='IndiceDeBusqueda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('palabrasclave', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('comentarios', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='indicebusquedaarticulo',
            name='indicebusqueda',
            field=models.ForeignKey(to='bosque.IndiceDeBusqueda'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ForeignKey(blank=True, to='bosque.Imagen', null=True),
        ),
        migrations.AddField(
            model_name='articulo',
            name='revision',
            field=models.ForeignKey(blank=True, to='bosque.Revision', null=True),
        ),
    ]
