from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient


User = get_user_model()
admin.site.unregister(User)


class RecipeInLine(admin.StackedInline):
    model = Recipe
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [RecipeInLine]
    list_display = ['username']


admin.site.register(User, UserAdmin)


class RecipeIngredientInLine(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ['quantity_as_float','as_mks','as_imperial']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Recipe, RecipeAdmin)
