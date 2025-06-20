import pytest
from bun import Bun
from data import *

@pytest.mark.parametrize("name, price", [
    (BUN_NAME, BUN_PRICE),
    (BUN_NAME2, BUN_PRICE2),
    (BUN_NAME3, BUN_PRICE3),
])
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price