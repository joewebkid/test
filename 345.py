# a1, b1, a2, b2 = 1,10,1,5
#
# if a1 == a2 and b1 == b2:
#     print(a1, b1)
# elif (a2 > b1 and a2 > a1) or (a1 > b2 and a1 > a2):
#     print('пустое множество')
# elif a1 == a2 and b1 > b2:
#     print(a1, b2)
# elif a1 == a2 and b1 < b2:
#     print(a1, b1)
# elif b1 == b2 and a2 > a1:
#     print(a2, b2)
# elif b1 == b2 and a2 < a1:
#     print(a1, b1)
# elif a1>a2 and b1<b2:
#     print(a1, b1)
# elif b1 == a2:
#     print(a2)
# elif a1 == b2:
#     print(a1)
# elif a1<a2 and b1>b2:
#     print(a2,b2)
# elif a1<a2 and b1<b2:
#     print(a2,b1)
# elif a1>a2 and b1>b2:
#     print(a1,b2)
#
# def foo():
#     x = 10 / 0
#     #y = (float(10) ** 1000)
#     #z = -1
#     #assert z > 0
# try:
#     foo()
# except AssertionError:
#     print(type("AssertionError"))
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
import datetime



# class PositiveList(list):
#     def append(self,x):
#         if x > 0:
#             super().append(x)
#         else:
#             raise NonPositiveError
#
# class NonPositiveError(Exception):
#     pass
#
# a=PositiveList()
# a.append(1)
# print(a)

import datetime
# a = datetime.datetime.today().strftime("%Y%m%d")
# print(a)  # '20170405'

s = list(map(int, input().split()))
x = str(datetime.date(s[0], s[1], s[2]) + datetime.timedelta(days = int(input())))
#2016-05-04
x = x.split('-')
#print(*x.split('-'))
print(int(x[i]) for i in x)
