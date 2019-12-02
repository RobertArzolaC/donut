import uuid
from django.db import models
from .utils import graph


class WorkSpace(models.Model):
    name = models.CharField("Espacio de trabajo", max_length=250,
                            unique=True, null=True)
    description = models.TextField("Descripción", blank=True, null=True)

    class Meta:
        verbose_name = "Espacio de trabajo"
        verbose_name_plural = "Espacios de trabajo"

    def __str__(self):
        return self.name


class Entity(models.Model):
    name = models.CharField("Nombre", max_length=250, unique=True)
    description = models.TextField("Descripción", blank=True, null=True)
    workspace = models.ForeignKey(
        WorkSpace, on_delete=models.PROTECT, related_name='entities',
        verbose_name='Espacio de trabajo', null=True
    )

    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"

    def __str__(self):
        return self.name


class Relationship(models.Model):
    name = models.CharField("Nombre", max_length=250, unique=True)
    description = models.TextField("Descripción", blank=True, null=True)

    class Meta:
        verbose_name = "Relación"
        verbose_name_plural = "Relaciones"

    def __str__(self):
        return self.name


class Association(models.Model):
    entity_1 = models.ForeignKey(
        Entity, on_delete=models.CASCADE, related_name='associations_1',
        verbose_name='Entidad 1')
    entity_2 = models.ForeignKey(
        Entity, on_delete=models.CASCADE, related_name='associations_2',
        verbose_name='Entidad 2')
    relationship = models.ForeignKey(
        Relationship, on_delete=models.PROTECT, related_name='associations', 
        verbose_name='Relación')
    workspace = models.ForeignKey(
        WorkSpace, on_delete=models.PROTECT, related_name='associations',
        verbose_name='Espacio de trabajo'
    )

    class Meta:
        verbose_name = "Asociación"
        verbose_name_plural = "Asociaciones"

    def __str__(self):
        return "Asociación {0}".format(self.id)
