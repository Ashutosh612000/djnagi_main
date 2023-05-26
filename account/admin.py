from django.contrib import admin
from account.models import User       

class Account_admin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'mobile','password']
# Register your models here.
admin.site.register(User,Account_admin)