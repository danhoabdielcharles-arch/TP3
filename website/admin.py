from django.contrib import admin # type: ignore
from .models import slider, banner3, About, banner, Services , ServiceHeader,ServiceImage
from .models import FeatureHeader, FeatureItem

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 5   # 5 images supplémentaires 

class ServicesAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]







# Register your models here.
admin.site.register(slider)
admin.site.register(banner3)
admin.site.register(About)
admin.site.register(banner)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServiceHeader)
admin.site.register(ServiceImage)


class FeatureItemInline(admin.TabularInline):
    model = FeatureItem
    extra = 1 


    
@admin.register(FeatureHeader)
class FeatureHeaderAdmin(admin.ModelAdmin):
    list_display = ('page', 'small_title', 'big_title')
    inlines = [FeatureItemInline]   # <-- demandé : inline ajouté ici

# --- ADMIN DES ITEMS (optionnel mais utile pour la recherche) ---
@admin.register(FeatureItem)
class FeatureItemAdmin(admin.ModelAdmin):
    list_display = ('titre', 'feature_header', 'ordre')
    list_filter = ('feature_header__page',)
    search_fields = ('titre', 'description')