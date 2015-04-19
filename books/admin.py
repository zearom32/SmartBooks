from django.contrib import admin
from books.models import *

# Register your models here.


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
  list_display=('title','isbn','price')
class GoodInfoAdmin(admin.ModelAdmin):
  list_display=('seller','book','price')

admin.site.register(UserInfo)
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(GoodsInfo,GoodInfoAdmin)


