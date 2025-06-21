import pytest
from bun import Bun
from data import *
class TestBun:

    @pytest.mark.parametrize("expected_name, expected_price", bun_data)
    def test_bun_get_name(self, expected_name, expected_price):
        bun = Bun(expected_name, expected_price)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("expected_name, expected_price", bun_data)
    def test_bun_get_price(self, expected_name, expected_price):
        bun = Bun(expected_name, expected_price)
        assert bun.get_price() == expected_price