from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Property , PropertyBook, PropertyImages, PropertyReview, Category, Place
# Register your models here.

class SummernoteAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'price' , 'get_avg_rating', 'check_availability']

admin.site.register(Property,SummernoteAdmin)

class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property','in_progress']

admin.site.register(PropertyBook,PropertyBookAdmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
admin.site.register(Place)
