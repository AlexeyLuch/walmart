from django.contrib import admin
from .models import Product,Task
from django.utils.safestring import mark_safe


admin.site.register(Task)

admin.site.site_header = "My admin panel"

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title","price","rating_reviews","in_stock","amount","button")

    def button(self, obj):
        return mark_safe(f'<a class="button" href="{ obj.url }" >Кнопка</a>')


admin.site.register(Product,ProductAdmin)