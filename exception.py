#Errors and Exception
x = 5
if x < 0:
    raise Exception('x sholud be positive')

x = 5
assert (x>=0), "x is not positive"

try:
    a = 5 / 0
except:
    print('an error happened')

try:
    a = 5 / 0
except Exception as e:
    print(e)

try:
    a = 5 / 0
    b = a + '10'
except ZeroDivisionError as r:
    print(r)
except TypeError as r :
    print(r)
else:
    print("everthing is fine")


try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as r:
    print(r)
except TypeError as r :
    print(r)
else:
    print("everthing is fine")
finally:
    print("cleaning up...")



class valueTooHighError(Exception):
    pass

class valuetoosmallerror(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise valueTooHighError("value is too high:")
    if x < 5:
        raise valuetoosmallerror("value is too small:",x)
    
    
try:
    test_value(6)
except valueTooHighError as r:
    print(r)
except valuetoosmallerror as r:
    print(r.message, r.value)




