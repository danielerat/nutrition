from django.contrib import admin

from authentication.models import User, Address, UserToken, Reset
# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(UserToken)
admin.site.register(Reset)
