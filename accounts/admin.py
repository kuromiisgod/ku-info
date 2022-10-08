from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from kublog.models import Contact, PostOne
from guardian.admin import GuardedModelAdmin

@admin.register(PostOne)
class PostOneAdmin(GuardedModelAdmin):
    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿'

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

