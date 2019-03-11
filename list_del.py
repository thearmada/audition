def func1():
    l1 = [1, 3, 4, 5, 4, 4, 5, 6, 8, 7]
    l2 = list(set(l1))
    print(l2)

def func2():
    l1 = ['c', 'b', 'z', 'a', 'b', 'a']
    l2 = list(set(l1))
    l2.sort(key=l1.index)
    print(l2)

def func3():
    l1 = ['c', 'b', 'a', 'e', 'c', 'a', 'x']
    l2 = []
    for i in l1:
        if not i in l2:
            l2.append(i)
    print(l2)

if __name__ == '__main__':
    func1()
    func2()
    func3()