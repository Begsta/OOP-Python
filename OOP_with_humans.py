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
    

class Mgister:
    def __init__(self, name:str, group:int, form:bool, staty:int, progress:list) -> any:
        self.name = name; self.group = group; self.form = form; self.progress = progress; self.staty = staty
    def __str__(self)->str:
        return (f"Студент под именем {self.name}\nучится в группе {self.group}\nна {"очке" if self.form else "заочке"}\nс оценками: { ", ".join(map(str, self.progress)) }\n"
            f"имеет статей {self.staty}")


class Aspirant:
    def __init__(self, name:str, group:int, form:bool, staty:int, progress:list, name_ruk:str)->any:
        self.name = name; self.group = group; self.form = form; self.progress = progress; self.staty = staty; self.name_ruk =name_ruk
    def __str__(self):
        return (f"Студент под именем {self.name}\nучится в группе {self.group}\nна {"очке" if self.form else "заочке"}\nс оценками: { ", ".join(map(str, self.progress)) }\n"
            f"имеет статей {self.staty},\nимя руководителя {self.name_ruk}")
    



#------------------------------------------------------------------------------------------------------------------------------------------------------
size_t = 10

arrayNames = ['Влад', "Настя", "Глеб", "Саня",  "Рома", "Егор" ]
arrayKlass = [11, 8, 9, 2, 5, 6]
arrayBuk = ["A", "B", "E", "C" ]
arraySh = [Sholnik(arrayNames[randint(0, 5)], arrayKlass[randint(0, 5)], arrayBuk[randint(0, 3)], [randint(2, 5) for _ in range(5)]) for i in range(size_t)]
#------------------------------------------------------------------------------------------------------------------------------------------------------
print("Школьни:")
for i in arraySh:
    print(i)

arraySh = sorted(arraySh, key=lambda a: a.name)

print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Школьни:")
for i in arraySh:
    print(i)
print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Плохие студенты")
n=0
for st in arraySh:
    for j in st.progress:
        if j < 3:
            print(st)
            n+=1
            break
if n ==0:
    print("Таких нет")
