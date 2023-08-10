from django.contrib import admin

from users.models import User


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'tg_login', 'chat_id', 'is_superuser', 'first_name')
    search_fields = ('email',)
