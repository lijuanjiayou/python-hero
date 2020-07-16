#集合：可变的数据类型，集合中的元素是不可变数据类型，不可重复，无序的
#集合特点：1.可以进行增add,update,删pop,remove,clear,del,查for i in set，
#         2.求交集，并集，反交集，差集，子集，超集

#增
#add
set1=({1,2,3,4,5})
set1.add(6)
print(set1)

#update
set1=({1,2,3,4,5,6})
set1.update("kay")
print(set1)

#删除
#pop
set1=({1,2,3,4})
print(set1.pop())
print(set1)

#remove
set1=({1,2,3,4})
set1.remove(1)
print(set1)

#clear
set1=({1,2,3,4})
set1.clear()
print(set1)

#del
# set1=({1,2,3,4})
# del set1
# print(set1)

#查
set1=({1,2,3,4,5})
for i in set1:
    print(i)

#交集
set1=({1,2,3,4,5})
set2=({4,5,6,7,8})
set3=set1&set2
print(set3)
print(set1.intersection(set2))

#并集
set1=({1,2,3,4,5})
set2=({4,5,6,7,8})
set3=set1 | set2
print(set3)
print(set1.union(set2))

#反交集
set1=({1,2,3,4,5})
set2=({4,5,6,7,8})
set3=set1 ^ set2
print(set3)
print(set1.symmetric_difference(set2))

#差集
set1=({1,2,3,4,5})
set2=({4,5,6,7,8})
set3=set1-set2
print(set3)
print(set1.difference(set2))

#子集
set1=({4,5})
set2=({4,5,6,7,8})
print(set1<set2)
print(set1.issubset(set2))

#超集
set1=({4,5})
set2=({4,5,6,7,8})
print(set2>set1)
print(set2.issuperset(set1))

#去重
li=[1,2,3,4,5,4,5,6]
set1=set(li)
li=list(set1)
print(li)

#frozenset
set1=frozenset({1,2,3,4})
print(set1)
for i in set1:
    print(i)
