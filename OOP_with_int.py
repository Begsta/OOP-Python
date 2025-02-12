from math import gcd, sqrt
from random import randint


class RatNum:
    # Функция создания элемнета класса
    # Принимает параметыр num(целое число) - числитель
    #                     den(целое число) - знаменатель
    def __init__(self, num:int, den : int) -> any:
        if num * den != 0:
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
    

class IrNum:
    def __init__(self, num : int, den : int, see : int):
        if num * den != 0:
            if num != 1:
                self.num = sqrt(num)
                self.den = den
                self.switch = True # Для понимания числитель ирроцианальный
                                   # Или знаменатель
            elif den != 1:
                self.num = num
                self.den = sqrt(den)
                self.switch = False
        else:
            raise ValueError
        self.see = see
    
    # Функция генерации случайного элемена класса
    # Принимает параметры min и max num(целые числа) - диапазон случайного числителя
    #                     min и max den(целые числа) - диапазон случайного знаменателя
    @staticmethod
    def generate(min_num : int, max_num : int, min_den : int, max_den : int) -> any:    
        return IrNum(randint(min_num, max_num), randint(min_den, max_den), randint(4, 6))
    
    # Функция вывода элмента класса
    # Принимает лишь сам объект класса
    def __str__(self) -> str:
        if self.switch:
            return  f"{round(self.num, self.see)}/{self.den}"
        return f"{self.num}/{round(self.den, self.see)}"
    
    # Функция умножения элемента на число или на элемент класса
    # Принимает параметры self - объект класса IrNum
    #                     other - целое число или объект класса RatNum
    def __mul__(self, other) -> any:
        if isinstance(other, IrNum):
            return IrNum(self.num * other.num, self.den*other.den, self.see)
        elif isinstance(other, int):
            return IrNum(self.num * other, self.den, self.see)
        raise TypeError
    
    # Функция деления элемента на число или на элемент класса
    # Принимает параметры self - объект класса IrNum
    #                     other - целое число или объект класса RatNum
    def __truediv__(self, other) -> any:
        if isinstance(other, IrNum):
            return IrNum(self.num * other.den, self.den*other.num, self.see)
        elif isinstance(other, int):
            return IrNum(self.num, self.den* other, self.see)
        raise TypeError


class DrobFib:
    def __init__(self, num1 : int, den1 : int, 
                num2 : int, den2 : int,
                times : int ) -> any:
        if times > 0:
            for _ in range(times):
                num, den = num1*den2+num2*den1, den1*den2
                k = gcd(num, den)
                num, den = num // k, den // k
                num1, num2, den1, den2 = num2, num, den2, den
            self.num = num
            self.den = den
        elif times == 0:
            k = gcd(num2, den2)
            self.num, self.den = num2 // k, den2 // k
        else:
            raise ValueError
        
    # Генерация случайного элемента класса
    @staticmethod
    def generate(min_num : int, max_num : int, min_den : int, max_den : int, min : int, max : int) -> any:
        return DrobFib(randint(min_num, max_num), randint(min_den, max_den), 
                       randint(min_num, max_num), randint(min_den, max_den), 
                       randint(min, max))
    
    def __str__(self) -> str:
        return f"{self.num}/{self.den}"
    
    def __mul__(self, other) -> any:
        if isinstance(other, DrobFib):
            return DrobFib(0,0, self.num * other.num, self.den * other.den, 0)
        elif isinstance(other, int):
            return DrobFib(0,0, self.num * other, self.den, 0)
        else:
            raise TypeError
    
    def __truediv__(self, other) -> any:
        if isinstance(other, DrobFib):
            return DrobFib(0,0, self.num * other.den, self.den * other.num, 0)
        elif isinstance(other , int):
            return DrobFib(0,0, self.num, self.den*other, 0)
        else:
            raise TypeError
       

# Тесты:

a = [DrobFib.generate(1, 20, 1, 20, 1, 5) for _ in range(5)]

for i in a:
    b = DrobFib.generate(1, 20, 1, 20, 1, 5)
    cm, cd = i*b, i/b
    print(f"{i} / {b} = {cm}")
    print(f"{i} * {b} = {cd}")
    cm, cd = i*2, i/2
    print(f"{i} / {b} = {cm}")
    print(f"{i} * {b} = {cd}")