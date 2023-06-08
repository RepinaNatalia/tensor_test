# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты
import inspect
import sys
import pytest
def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
@pytest.mark.smoke
def test1():
    assert all_division(-80, 10) == -8

def test2():
    assert all_division(120, 6) == 20

@pytest.mark.smoke
def test3():
    assert all_division(1, 2) == 0.5

def test4():
    assert all_division(1, 3) == 0.3333333333333333

def test11():
        with pytest.raises(ZeroDivisionError):
            all_division(12, 0)