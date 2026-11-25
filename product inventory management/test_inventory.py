import pytest

from inventory import apply_discount, calculate_total_price, check_stock


# Test 1: Calculate total price
def test_calculate_total_price():
    assert calculate_total_price(500, 3) == 1500


# Test 2: Calculate total with one quantity
def test_single_product_price():
    assert calculate_total_price(1000, 1) == 1000


# Test 3: Apply discount
def test_apply_discount():
    assert apply_discount(1000, 10) == 900


# Test 4: Check available stock
def test_check_stock_available():
    assert check_stock(10, 5) == True


# Test 5: Check insufficient stock
def test_check_stock_unavailable():
    assert check_stock(5, 10) == False


# Test 6: Reject negative price
def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total_price(-500, 2)


# Test 7: Reject invalid discount
def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(1000, 120)


# Test 8: Reject invalid quantity
def test_invalid_quantity():
    with pytest.raises(ValueError):
        calculate_total_price(500, 0)
