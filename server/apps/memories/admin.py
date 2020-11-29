from django.contrib import admin

from apps.memories.models import Memory


class MemoryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'text',
    )
    readonly_fields = (
        'longitude',
        'latitude',
        'created',
        'last_modified',
    )


admin.site.register(Memory, MemoryAdmin)
