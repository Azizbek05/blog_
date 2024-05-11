from django.contrib import admin
from .models import CustomUser, Reactions, Comments, CodeConfirmation
# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


@admin.register(Reactions)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'like', 'diss_like']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment']


@admin.register(CodeConfirmation)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'code']
