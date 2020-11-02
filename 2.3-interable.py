# import simplecrypt
#
# with open('C:\Python\maya\encrypted.bin', 'rb') as fo:
#     ciphertext = fo.read()
#     with open('C:\Python\maya\passwords.txt') as fin:
#         for line in fin:
#             line = line.replace('\n', '')
#             try:
#                 dec = simplecrypt.decrypt(line, ciphertext)
#             except simplecrypt.DecryptionException:
#                 pass
#             else:
#                 print(line, dec)
#                 with open('C:\Python\maya\crypted.bin', 'wb') as fo:
#                     fo.write(dec)
#             # print("decrypted text: %s" % dec)
# #---------------------------------
# import requests
# from simplecrypt import decrypt, DecryptionException
#
# code = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
# passes = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').content
#
# for p in passes.split():
#     try:
#         s = decrypt(p, code)
#     except DecryptionException:
#         pass
#     else:
#         print(p, s)
#====================================================

class multifilter:
    def judge_half(pos, neg):
        return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        pass
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return 1
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        pass
        self.interable = iterable
        self.funcs = funcs # будет картежем из функций: (mul2, mul3, mul5)
        self.judge = judge
        self.i = 0

        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        return self
        '''поэтому в функции def __iter__ сначала делаю цикл для у из self.iterable, а внутри него создается цикл for x in self.funcs: 
         команда x(y) - это команда на выполнение функции х(mul1 или mui5, или еще какие добавятся) с параметром у (оказывается так можно!) ,
          после ее выполнения узнаем что из pos или neg увеличивается на 1, и если self.judge(pos,neg) верно, то yield у.
           (yield присутствует только в функции __iter__)
           
           Существует конструкция yield from, которая немного упрощает код
           yield from g равноценно for v in g: yield v
           
           В указанной структуре класса multifilter нет __next__ Поэтому реализовала через __iter__  и yield. На самом деле в "Решениях" преподавателем 
           класс реализован через __next__. Если оставите __next__, тоже примет. Только в __init__ определите self.iterator = iter(iterable)
                 '''

        # возвращает итератор по результирующей последовательности
    def __next__(self):
        if self.i < len(self.interable):
            self.i += 1
            return self.interable[self.i - 1]
        else:
            raise StopIteration

def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0
a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]


# просто пример для размышления
# class iterable:
#     def __init__(self):
#         self.x = 1
#
#     def __next__(self):
#         self.x += 1
#         if self.x >= 11:
#             raise StopIteration
#         return self.x
#
#     def __iter__(self):
#         return self
#
# it = iterable()
# print(list(it))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
