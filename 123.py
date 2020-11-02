# x={}
# for i in range(2):
#     a=list(input().split(' : '))
#     print(a, len(a))
#     x[a[0]] = a[1].split() if len(a) > 1 else []
# print (x)
#
# if c[1] in x.values():

# for i in range(2):
#     c = list(input().split())
#     c[1]
def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0

class MyList:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, lst, *func, judge=judge_half):
        self.iterable = lst
        self.func = func
        self.judge = judge

    #def judge_1(self, num):
    #    return "element = " + str(num)

    def __iter__(self):
        a1=[]
        for i in self.iterable:
            n,p=0,0
            for y in self.func:
                if y(i):
                    p += 1
                else:
                    n += 1
            if self.judge(p,n):
                a1.append(i)
        yield a1

def f2(n):
    return n / 2
a = [i for i in range(31)] # [0, 1, 2, ... , 30]
l = MyList(a, mul2, mul3, mul5,judge=MyList.judge_any)
for i in l:
    print(i)
#--------------------------------------------
#x = 10 if y == 0 else 5


a = [i for i in range(31)] # [0, 1, 2, ... , 30]
#print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]