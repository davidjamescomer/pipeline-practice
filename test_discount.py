import random
from discount import apply_discount


def test_full_price_with_no_discount():
    assert apply_discount(100, 0) == 100

def test_twenty_percent_off():
    assert apply_discount(100, 20) == 80

def test_discount_reduces_price():
    percent = random.randint(0, 4)
    assert apply_discount(100, percent) < 100
