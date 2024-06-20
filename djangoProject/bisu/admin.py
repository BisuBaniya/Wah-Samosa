from django.contrib import admin # type: ignore
from .models import SamosaVariety,SamosaReview,Store,SamosaCertificate # type: ignore

# Register your models here.

class SamosaReviewInline(admin.TabularInline):
    model = SamosaReview
    extra = 2

class SamosaVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [SamosaReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('samosa_varieties',)

class SamosaCertificateAdmin(admin.ModelAdmin):
    list_display = ('samosa', 'certificate_number')

admin.site.register(SamosaVariety,SamosaVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(SamosaCertificate,SamosaCertificateAdmin)


