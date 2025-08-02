#sets: unordered, mutable, no duplicates
odds={1,3,5,7,9}
evens={2,4,6,8,12}
primes={2,3,5,7}

a=odds.union(evens)
print(a)

p=odds.intersection(primes)
print(p)

seta={1,2,3,4,5,6}
setb={1,2}
setc={7,8}

#shows the difference
let=seta.difference(setb)
print(let)

#shows difference in both set
let=setb.symmetric_difference(seta)
print(let)

#shows same numbers in set
seta.intersection_update(setb)
print(seta)

#show only different number not same
seta.difference_update(setb)
print(seta)

#don't show the same number
seta.symmetric_difference_update(setb)
print(seta)

#every elements in another set
print(setb.issubset(seta))

#every elements in the every set
print(seta.issuperset(setb))

#two sets have a null intersection
print(seta.isdisjoint(setc))


# copying two sets
setb = set(seta)
setb = seta.copy()
setb.add(9)
print(seta)
print(setb)

#frozen set method
a=frozenset([1,2,3,4])
a.remove(2)
print(a)



