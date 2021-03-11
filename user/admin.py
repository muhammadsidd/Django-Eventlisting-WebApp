from django.contrib import admin
from user.models import UserManagement,Role
# Register your models here.

admin.site.register(Role)
admin.site.register(UserManagement)