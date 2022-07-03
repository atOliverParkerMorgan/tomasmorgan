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


class SongsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


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

    # def has_add_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     search_fields = ['name']
#
#
# class ActorAdmin(admin.ModelAdmin):
#     list_display = ['name', 'birthdate', 'sex']
#     search_fields = ['name']
#     list_filter = ['sex']
#     list_editable = ['birthdate', 'sex']
#     date_hierarchy = "birthdate"


# Register your models here.
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Songs)
admin.site.register(Contact)
admin.site.register(BackgroundImages, BackgroundImagesAdmin)
