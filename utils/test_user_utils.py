# tests/test_user_utils.py
import pytest
from user_utils import check_age

@pytest.mark.parametrize("age, expected", [
    (17, "Вы ещё несовершеннолетний"),
    (18, "Вам больше 18 лет"),
    (25, "Вам больше 18 лет"),
    (0, "Вы ещё несовершеннолетний"),
    (100, "Вам больше 18 лет"),
])
def test_check_age(age, expected):
    assert check_age(age) == expected