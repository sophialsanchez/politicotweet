from django.contrib import admin

# Register your models here.
from .models import Result

class ResultAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')
	
# Register your models here.
admin.site.register(Result, ResultAdmin)