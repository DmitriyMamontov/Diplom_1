import pytest
from database import Database


def test_database_initialization(database):
    assert isinstance(database.buns, list)
    assert isinstance(database.ingredients, list)


def test_available_buns(database, mock_bun):
    database.buns = [mock_bun]
    buns = database.available_buns()
    assert buns == [mock_bun]


def test_available_ingredients(database, mock_ingredient):
    database.ingredients = [mock_ingredient]
    ingredients = database.available_ingredients()
    assert ingredients == [mock_ingredient]