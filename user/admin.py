from django.contrib import admin
from .models import*

class ProfilAdmin(admin.ModelAdmin):
    list_display =('isim','olusturan','slug','id')
    list_display_links=('isim','olusturan',)
    list_filter = ('olusturan',)
    search_fields=('isim',)
    # list_editable = ('slug',)
    readonly_fields= ('slug',)
# Register your models here.
admin.site.register(Profil,ProfilAdmin)
admin.site.register(Hesap)