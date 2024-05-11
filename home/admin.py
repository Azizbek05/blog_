from django.contrib import admin
from .models import Maqola

#
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'is_active']
#     class Meta:
#         model = Author

@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'description', 'created_at', 'user_name']

    class Meta:
        model = Maqola
