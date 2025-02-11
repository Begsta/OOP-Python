from math import gcd
from random import randint


class RatNum:
    # Функция создания элемнета класса
    # Принимает параметыр num(целое число) - числитель
    #                     den(целое число) - знаменатель
    def __init__(self, num:int, den : int) -> any:
        if num != 0 and den != 0:
            k = gcd(num, den) # Насходит общий делитель для числел
                              # Чтобы можно было записать число в виде дроби
            self.num = num // k
            self.den = den // k
        else:
            raise ValueError
    # Функция генерации случайного элемена класса
    # Принимает параметры min и max num(целые числа) - диапазон случайного числителя
    #                     min и max den(целые числа) - диапазон случайного знаменателя
    @staticmethod
    def generate(min_num : int, max_num : int, min_den : int, max_den : int) -> any:    
        return RatNum(randint(min_num, max_num), randint(min_den, max_den))
    
    # Функция вывода элмента класса
    # Принимает лишь сам объект класса
    def __str__(self) -> str:
        return  f"{self.num}/{self.den}"
    
    # Функция умножения элемента на число или на элемент класса
    # Принимает параметры self - объект класса RatNum
    #                     other - целое число или объект класса RatNum
    def __mul__(self, other) -> any:
        if isinstance(other, RatNum):
            return RatNum(self.num * other.num, self.den*other.den)
        elif isinstance(other, int):
            return RatNum(self.num * other, self.den)
        raise TypeError
    
    # Функция деления элемента на число или на элемент класса
    # Принимает параметры self - объект класса RatNum
    #                     other - целое число или объект класса RatNum
    def __truediv__(self, other) -> any:
        if isinstance(other, RatNum):
            return RatNum(self.num * other.den, self.den*other.num)
        elif isinstance(other, int):
            return RatNum(self.num, self.den* other)
        raise TypeError
    
# Тесты:

a = [RatNum.generate(1, 20, 1, 20) for _ in range(5)]

for i in a:
    b = RatNum.generate(1, 20, 1, 20)
    cm, cd = i*b, i/b
    print(f"{i} / {b} = {cm}")
    print(f"{i} * {b} = {cd}")
    cm, cd = i*2, i/2
    print(f"{i} / {b} = {cm}")
    print(f"{i} * {b} = {cd}")