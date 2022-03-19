from django.contrib import admin
from main.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'type', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name','last_name', 'email' )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('type', 'phone')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )

admin.site.register(Slider)
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Info)
admin.site.register(Newsletters)
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(Wishlist)
