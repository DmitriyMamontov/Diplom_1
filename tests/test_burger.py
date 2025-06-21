import pytest
from unittest.mock import Mock
from data import *
from burger import Burger

class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []


    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient


    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = INGREDIENT_FILLING_1
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient


    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250  # 2*100 + 50
        mock_bun.get_price.assert_called_once()
        mock_ingredient.get_price.assert_called_once()


    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        assert BUN_NAME in receipt
        assert INGREDIENT_SOUSE_1 in receipt
        assert "250" in receipt
        assert mock_bun.get_name.call_count == 2
        assert mock_ingredient.get_name.call_count == 1