# from timeit import default_timer as timer
# list3 = ['r'] * 1000000
# # print(list3)

# #bad
# start = timer()
# mylist = ""
# for i in list3:
#     mylist += i
# stop = timer()
# print(stop-start)

# #good and Faster
# start = timer()
# mylist="".join(list3)
# stop = timer()
# print(stop-start)

#format{} f-strings
rk="tom"
string="the var is %s" % rk
print(string)

rk=3.0789
string="the var is %d" % rk
print(string)
rk=3.0789
string="the var is %f" % rk
print(string)

rk=3.0789
string="the var is %.2f" % rk
print(string)

rk=3.0789
rk2=6
string="the var is {:.2f} and {}".format(rk,rk2)
print(string)

rk=3.0789
rk2=6
string=f"the var is {rk} and {rk2}".format(rk,rk2)
print(string)

rk=3.0789
rk2=6
string=f"the var is {rk*2} and {rk2}".format(rk,rk2)
print(string)