from django.contrib import admin

# Register your models here.
from chu2pa.models import UserStatus, Calendar

admin.site.register(UserStatus)
admin.site.register(Calendar)