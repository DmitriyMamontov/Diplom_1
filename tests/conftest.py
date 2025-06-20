import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from burger import Burger
from unittest.mock import Mock
import pytest
from bun import Bun
from ingredient import Ingredient
from database import Database
from data import *

@pytest.fixture
def bun():
    return Bun(BUN_NAME, BUN_PRICE)

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = BUN_NAME
    mock.get_price.return_value = BUN_PRICE
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_name.return_value = INGREDIENT_SOUSE_1
    mock.get_price.return_value = 50
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock
