def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0

class multifilter:
    def judge_half(pos, neg):
        return pos >= neg
    def judge_any(pos, neg):
        return pos >= 1
    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, lst, *func, judge=judge_any):
        self.iterable = lst
        self.func = func
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            n, p = 0, 0
            for y in self.func:
                if y(i):
                    p += 1
                else:
                    n += 1
            if self.judge(p, n):
                yield i

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]

#====================================================================================================================

'''
Решать задачу нужно держа в голове то, что этот урок на понимание того, как работают и как создать свой итератор - мы учимся их создавать.

Для понимания делайте по частям:
*Это не решение задачи, а шаги к пониманию*
Итератор - это отдельный класс, в котором есть функция __next__, которая возвращает по порядку элементы переданного итерируемого объекта.
Например, создайте простейший итератор - класс MyIterator, который возвращает элементы переданного ему итерируемого объекта (iterable),
и никакой логики внутри (по честному будет сказать, что в этом примере итератор ждет не просто итерируемый объект, а список, потому
что в next он использует доступ к элементам по индексу):

class MyIterator:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1]
        raise StopIteration

Теперь создайте свой класс MyList ни от чего не наследуя и просто определите внутри функцию __iter__ сделав тем 
самым объекты этого класса итерируемыми, а внутри __iter__ возвращайте свой ранее созданный итератор MyIterator
 передавая в него итерируемый объект, например список:

class MyList:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
     return MyIterator(self.lst)

А теперь создайте объект типа MyList передав в него, например, список:

l = MyList([1, 2, 3, 4, 5])


Полный код:

class MyIterator:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1]
        raise StopIteration


class MyList:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return MyIterator(self.lst)


l = MyList([1, 2, 3, 4, 5])
print(type(l))  # "l" is not a list, but MyList object

# but "l" contains elements and "l" is iterable
for i in l:
    print(i)

Теперь глядя на весь этот код должно стать понятно, что объект "l" - это НЕ список:
- l - это объект типа MyList
- он итерируемый (определен метод __iter__)
- для итерации по элементам объекта типа MyList используется итератор MyIterator
- итератор MyIterator возвращает по одному элементу переданного в него итерируемого объекта 
(в нашем случае списка, который мы задавали при создании объекта "l")

Поняв это вы легко сможете перенести функцию __next__ внутрь класса MyList, сделав тем самым класс
 MyList еще и итератором (теперь, когда объекты класса MyList являются итераторами, то функция __iter__ может 
 возвращать сам объект класса MyList, то есть "return self"). Конечно же надо позаботиться о переменных, которые
используются в __next__:

class MyList:
    def __init__(self, lst):
        self.iterable = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1]
        raise StopIteration


Ну а теперь добавьте логику в функцию next, например, каждый элемент делить на 2 перед выводом:

class MyList:
    def __init__(self, lst):
        self.iterable = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1] / 2
        raise StopIteration


l = MyList([1, 2, 3, 4, 5])

for i in l:
    print(i)

# 0.5
# 1
# 1.5
# 2
# 2.5


Добавляя сложности, дальше можно определить функцию f2 и использовать в __next__, которая будет делить
 на 2 и результат подставлять в return в __next__:

class MyList:
    def __init__(self, lst):
        self.iterable = lst
        self.index = 0

    def __iter__(self):
        return self

    def f2(self, n):
        return n / 2

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.f2(self.iterable[self.index - 1])
        raise StopIteration

l = MyList([1, 2, 3, 4, 5])

for i in l:
    print(i)


Еще сложнее, вынесем функцию f2 за класс, а внутрь класса будем передавать ее аргументом, плюс добавим внутрь 
класса еще одну функцию judge, которая будет использовать нашу f2 и тоже что-то делать (не забывайте инициализировать
 новые переменные в __init__):

class MyList:
    def __init__(self, lst, func):
        self.iterable = lst
        self.func = func
        self.index = 0

    def judge(self, num):
        return "element = " + str(num)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            self.result_of_f2 = self.func(self.iterable[self.index - 1])
            self.result_of_judge = self.judge(self.result_of_f2)
            return self.result_of_judge
        raise StopIteration


def f2(n):
    return n / 2

l = MyList([1, 2, 3, 4, 5], f2)

for i in l:
    print(i)

Продолжайте усложнять до тех пор пока не получится решить задание :)

Надеюсь кому-то помог.


!!! НО ИМЕЙТЕ В ВИДУ !!! Если класс итерируемый (__iter__) И ОН ЖЕ является итератором (__next__), то итерироваться
 по элементам объекта этого класса возможно будет только ОДИН раз. В указанном примере попробуйте заменить for i in l
  на две строки print(list(l)):

print(list(l))
print(list(l))

 Получите вывод:

['element = 0.5', 'element = 1.0', 'element = 1.5', 'element = 2.0', 'element = 2.5']
[]

А если использовать внешний итератор, то все ок.


'''