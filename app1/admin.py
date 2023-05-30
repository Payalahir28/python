from django.contrib import admin
from app1.models import Blog,Author,Entry,Category

# Register your models here.

class blogregister(admin.ModelAdmin):
    list_display = ['name','tagline']
    # list_display = ['name','email']
    search_fields = ['name','tagline']

class entryregister(admin.ModelAdmin):
    list_display = ['blog','body_text','rating']
    list_filter =['blog','body_text','rating']                            
    

admin.site.register(Blog,blogregister)
admin.site.register(Author)
admin.site.register(Entry,entryregister)
admin.site.register(Category)


