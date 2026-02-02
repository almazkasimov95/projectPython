# tests/test_user_utils.py
from user_utils import check_age

def test_check_age_under_18():
    assert check_age(17) == "Вы ещё несовершеннолетний"

def test_check_age_18():
    assert check_age(18) == "Вам больше 18 лет"

def test_check_age_over_18():
    assert check_age(25) == "Вам больше 18 лет"