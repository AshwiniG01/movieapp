from django.contrib import admin
from bookmyshowapp import MovieTable
# Register your models here.
class MovieTableAdmin(admin.ModelAdmin):

	list_display=['movie_name','release_date','hero_name','heroin_name','language']


admin.site.register(MovieTable,MovieTableAdmin)
