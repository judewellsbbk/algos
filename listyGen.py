from random import randint

def listyGen(n, m):
    ls = []
    for i in range(n):
        ls.append(randint(1, m))
    print(ls)

listyGen(100, 50)