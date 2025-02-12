from random import randint

class Sholnik:
    def __init__(self, name : str, klass : int, buk : str, progress : list) -> any:
        self.name = name; self.klass = klass; self.buk = buk; self.progress = progress

    def __str__(self) -> str:
        return f"Школьник под именем {self.name},\nучится в {self.klass} классе по буквой {self.buk}\nОценки:\n{ ", ".join(map(str, self.progress)) }"

class Student:
    def __init__(self, name:str, group:int, form:bool, progress:list) -> any:
        self.name = name; self.group = group; self.form = form; self.progress = progress

    def __str__(self) -> str:
        return f"Студент под именем {self.name}\nучится в группе {self.group}\nна {"бакалавр" if self.form else "специалиет"}\nс оценками: { ", ".join(map(str, self.progress)) }"
    

class Magister:
    def __init__(self, name:str, group:int, form:bool, staty:int, progress:list) -> any:
        self.name = name; self.group = group; self.form = form; self.progress = progress; self.staty = staty
    def __str__(self)->str:
        return (f"Магистр под именем {self.name}\nучится в группе {self.group}\nна {"очке" if self.form else "заочке"}\nс оценками: { ", ".join(map(str, self.progress)) }\n"
            f"имеет статей {self.staty}")


class Aspirant:
    def __init__(self, name:str, group:int, form:bool, staty:int, progress:list, name_ruk:str)->any:
        self.name = name; self.group = group; self.form = form; self.progress = progress; self.staty = staty; self.name_ruk =name_ruk
    def __str__(self) -> str:
        return (f"Аспирант под именем {self.name}\nучится в группе {self.group}\nна {"очке" if self.form else "заочке"}\nс оценками: { ", ".join(map(str, self.progress)) }\n"
            f"имеет статей {self.staty},\nимя руководителя {self.name_ruk}")
    
class Ruk:
    def __init__(self, name:str, ucState:bool, groups:list) -> any:
        self.name = name; self.ucState = ucState; self.groups = groups

    def __str__(self)->str:
        return f"Имя преподавателя {self.name}\nналичее учёной степения {"присутствует" if self.ucState else "остутствует"}\nгруппы которые он ведёт: {', '.join(map(str, self.groups))}"



#------------------------------------------------------------------------------------------------------------------------------------------------------
size_t = 3

arrayNames = ['Влад', "Настя", "Глеб", "Саня",  "Рома", "Егор" ]
arrayKlass = [95, 49, 86, 69, 79]
arrayBuk = ["A", "B", "E", "C" ]
arraySh = [Ruk(arrayNames[randint(0, 5)], randint(0, 1), [randint(23, 65) for _ in range(5)]) for i in range(size_t) ]
#------------------------------------------------------------------------------------------------------------------------------------------------------
print("Руководители:")
for i in arraySh:
    print(i)

arraySh = sorted(arraySh, key=lambda a: a.name)

print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Руководители:")
for i in arraySh:
    print(i)
print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Плохие Руководителей не бывает")

