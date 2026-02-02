# user_utils.py

def check_age(age: int) -> str:
    """Возвращает сообщение в зависимости от возраста."""
    if age < 18:
        return "Вы ещё несовершеннолетний"
    else:
        return "Вам больше 18 лет"