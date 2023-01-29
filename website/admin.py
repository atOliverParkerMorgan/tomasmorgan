from django.contrib import admin
from website.models import *

admin.site.site_header = 'TOMAS MORGAN - admin'


class SubtitleInline(admin.TabularInline):
    model = Subtitle
    extra = 1


class AboutMeAdmin(admin.ModelAdmin):
    inlines = [SubtitleInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class GalleryImageAdmin(admin.ModelAdmin):
    pass

class SongsInline(admin.TabularInline):
    model = Song
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongsInline]


class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class BackgroundImageInline(admin.TabularInline):
    model = BackgroundImage
    extra = 1


class BackgroundImagesAdmin(admin.ModelAdmin):
    inlines = [BackgroundImageInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(BackgroundImages, BackgroundImagesAdmin)
admin.site.register(Gallery, GalleryImageAdmin)

