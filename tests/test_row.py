import pytest

from reports.base import Row


def test_row_data_validation():
    test_phone = Row("iPhone 15 Pro Max", "apple", 1299, 5.0)
    assert test_phone.price == 1299.0
    assert test_phone.rating == 5.0


@pytest.mark.parametrize("rating", [-1, 5.5])
def test_row_invalid_data(rating):
    with pytest.raises(ValueError, match="Incorrect rating"):
        Row("iPhone 14", "apple", 699, rating)


def test_row_negative_price():
    with pytest.raises(ValueError, match="Price can not be negative"):
        Row("iPhone 13", "apple", -499, 4.2)
