#itertools: product,permutation,combination,accumulate,groupby,and infinite iterators
from itertools import product
a=[1,2]
b=[3]
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations
a=[1,2,3]
perm = permutations(a,2)
print(list(perm))


from itertools import combinations
a=[1,2,3,4]
comb = combinations(a,2) #2nd argument is mandatory
print(list(comb))



from itertools import combinations, combinations_with_replacement
a=[1,2,3,4]
comb = combinations(a,2) #2nd argument is mandatory
print(list(comb))
comb_wr=combinations_with_replacement(a,2) #argument is necessary
print(list(comb_wr))




from itertools import accumulate
a=[1,2,3,4]
acc= accumulate(a)
print(a)
print(list(acc))

from itertools import accumulate
import operator
a=[1,2,5,3,4]
# acc= accumulate(a, func=operator.mul)
acc = accumulate(a,func=max)
print(a)
print(list(acc))


from itertools import groupby
def smaller_than_3(x):
    return x < 3
a=[1,2,3,4]
group1=groupby(a, key=smaller_than_3)
# group1=groupby(a, key=lambda x: x<3)

for key, value in group1:
    print(key, list(value))




from itertools import groupby
persons=[{"name":"tim",'age':19,},{"name":"john",'age':40,}
         ,{"name":"brad",'age':25,},{"name":"raj",'age':35,}]

group2 = groupby(persons,key=lambda x: x['age'])
for key, value in group2:
    print(key,list(value))

from itertools import count, cycle, repeat
a = [1,2,3]
for i in count(10):
    if i==15:
        break
    print(i)


from itertools import count, cycle, repeat
a = [1,2,3]
for i in cycle(a):
    print(i)



from itertools import count, cycle, repeat
a = [1,2,3]
for i in repeat(1 , 4):
    print(i)











