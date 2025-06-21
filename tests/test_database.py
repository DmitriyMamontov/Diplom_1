import pytest
from database import Database

class TestDatabase:
    def test_database_initialization(self):
        db = Database()
        assert isinstance(db.buns, list)
        assert isinstance(db.ingredients, list)


    def test_available_buns(self, mock_bun):
        db = Database()
        db.buns = [mock_bun]
        buns = db.available_buns()
        assert buns == [mock_bun]


    def test_available_ingredients(self, mock_ingredient):
        db = Database()
        db.ingredients = [mock_ingredient]
        ingredients = db.available_ingredients()
        assert ingredients == [mock_ingredient]