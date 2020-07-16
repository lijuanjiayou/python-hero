import copy
#浅拷贝：不拷贝子对象的内容，只拷贝子对象的引用
#深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响原对象

def testCopy():
    a=[10,20,[50,60]]
    b=copy.copy(a)
    b.append(30)
    b[2].append((70))
    print("浅拷贝。。。")
    print("a:",a)
    print("b:",b)

def testDeepcopy():
    a=[10,20,[50,60]]
    b=copy.deepcopy(a)
    b.append(30)
    b[2].append((70))
    print("深拷贝。。。")
    print("a:",a)
    print("b:",b)
testCopy()
testDeepcopy()

