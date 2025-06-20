import pytest
from ingredient import Ingredient
from data import *

@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, INGREDIENT_SOUSE_1, 100),
    (INGREDIENT_TYPE_FILLING, INGREDIENT_FILLING_1, 200),
])
def test_ingredient_initialization(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price