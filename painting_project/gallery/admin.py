from django.contrib import admin
from .models import Artist, Painting, Gallery
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'creation_date')
    list_filter = ('creation_date', 'artist')
    search_fields = ('title',)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Painting, PaintingAdmin)
admin.site.register(Gallery, GalleryAdmin)
