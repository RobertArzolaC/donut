from django.contrib import admin
from .models import WorkSpace, Entity, Relationship, Association


class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ( "name", "description", )

admin.site.register(WorkSpace, WorkSpaceAdmin)


class EntityAdmin(admin.ModelAdmin):
    list_display = ( "name", "description", "workspace", )

admin.site.register(Entity, EntityAdmin)


class RelationshipAdmin(admin.ModelAdmin):
    list_display = ( "name", "description", )

admin.site.register(Relationship, RelationshipAdmin)


class AssociationAdmin(admin.ModelAdmin):
    list_display = ( "entity_1", "relationship", "entity_2", "workspace", )

admin.site.register(Association, AssociationAdmin)
