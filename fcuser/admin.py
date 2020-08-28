from django.contrib import admin
from .models import Fcuser
# Register your models here.

class AdminFcuser(admin.ModelAdmin):
    list_display=('username','password','registered_date')

admin.site.register(Fcuser,AdminFcuser)