#collection : counter , nametuple,order dict,defaultdict,deque
from collections import Counter
a="aaaabbbccc"
Counter1 = Counter(a)
print(Counter1)
print(Counter1.items)
print(Counter1.keys())
print(Counter1.values())

print(Counter1.most_common(1)[0][0])
# it can shows the element repeatation
print(list(Counter1.elements()))


from collections import namedtuple
point = namedtuple("point", "x,y")
pt = point(1,-4)
print(pt)




from collections import OrderedDict
Dict= OrderedDict()
Dict["b"] = 2
Dict["c"] = 3
Dict["d"] = 4
Dict["a"] = 1
print(Dict)



from collections import defaultdict
k = defaultdict()
k['a'] = 1
k['b'] = 2
print(k['c'])




from collections import deque
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
# print(d)

# d.popleft()
# d.clear()

# d.extend([4,5,6])
d.extendleft([4,5,6])
print(d)
d.rotate(-1)
print(d)
