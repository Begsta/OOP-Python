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

    def __mul__(self, other) -> any:
        if isinstance(other, RatNum):
            
