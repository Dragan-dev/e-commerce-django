from django.forms import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient
# Create your tests here.


User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('laki', password='laki1234')

    def test_user_pw(self):
        checked = self.user_a.check_password('laki1234')
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('laki', password='laki1234')

        self.recipe_a = Recipe.objects.create(
            name='Grilled beef',
            user=self.user_a
        )

        self.recipe_b = Recipe.objects.create(
            name='Grilled beef steak',
            user=self.user_a
        )

        self.recipe_ingredients_a = RecipeIngredient.objects.create(

            recipe=self.recipe_a,
            name='Beef',
            quantity='0.75',
            unit='grams'

        )

    def test_user(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredients_reverse_count(self):
        recipe = self.recipe_a
        # >recipeingredient< must be the same as model name RecipeIngredient but lowercase
        qs = recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(), 1)

    def test_recipe_ingredientcount(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        recipeingredient_ids = list(user.recipe_set.all(
        ).values_list('recipeingredient__id', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=recipeingredient_ids)
        self.assertEqual(qs.count(), 1)


    def test_unit_measure_validation(self):
        invalid_unit = 'ounce'
        ingredient = RecipeIngredient(
            name='New',
            quantity=10,
            recipe=self.recipe_a,
            unit=invalid_unit
        )
        ingredient.full_clean()  # same as form.is_valid()



    def test_unit_measure_validation_error(self):
        invalid_units = ['falseUnit','anotherUnit']
        with self.assertRaises(ValidationError):
            for unit in invalid_units:
                ingredient = RecipeIngredient(
                name='New',
                quantity=10,
                recipe=self.recipe_a,
                unit=unit
        )   
        ingredient.full_clean()  
