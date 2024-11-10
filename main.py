"""
Array.diff

Ваша задача в этом задании — реализовать функцию разности,
которая вычитает один список из другого и возвращает результат.
Он должен удалить все значения из списка a, которые присутствуют
в списке b, сохранив их порядок.

array_diff([1,2],[1]) == [2]

Если значение присутствует в b, все его вхождения должны быть
удалены из другого значения:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""

#def array_diff(a,b)

a = [[1,2,3], [1,3], [1,2], [3,2,1]]
b = [1,2]

c = []
cc = []
aa = []
aaa = []
bb = []
bbb = 0
new_a = []

#print(len(a))
for i in range(0, len(a), 1):
    aa = a[i]
    for j in range(0, len(aa), 1):
        aaa = aa[j]
        for k in range(0, len(b), 1):
            print(i,j,k)
            #bbb = len(b[k])

            if len(bb) != 0:
                if aaa[j] == b[k]:
                    aaa.pop(j)
                cc.append(aaa[j])
print(c)


"""
a = [[1,2,3], [1]]
b = [1]

c = []
new_a = []
#print(len(a))
for i in range(0, len(a), 1):
    new_a = a[i]
    for j in range(len(a[i])-1, 0, -1):
        if len(b) != 0:
            if new_a[j] == b[0]:
                new_a.pop(j)
                #print(i,j,new_a)
    c.append(new_a)
print(c)
"""

#return c