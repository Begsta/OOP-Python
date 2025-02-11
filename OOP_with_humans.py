from random import randint

class Sholnik:
    def __init__(self, name : str, klass : int, buk : str, progress : list) -> any:
        self.name = name; self.klass = klass; self.buk = buk; self.progress = progress

    def __str__(self) -> str:
        return f"Школьник под именем {self.name},\nучится в {self.klass} классе по буквой {self.buk}\nОценки:\n{ ", ".join(map(str, self.progress)) }"





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
