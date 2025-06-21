import pytest
from ingredient import Ingredient
from data import *

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", ingredient_data)
    def test_ingredient_get_type_with_data(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type


    @pytest.mark.parametrize("ingredient_type, name, price", ingredient_data)
    def test_ingredient_get_name_with_data(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name


    @pytest.mark.parametrize("ingredient_type, name, price", ingredient_data)
    def test_ingredient_get_price_with_data(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price