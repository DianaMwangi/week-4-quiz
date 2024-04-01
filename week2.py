my_list=[]

print(type(my_list))
#append can only add one variable. Extend  expects a single iterable
my_list.extend([10,20,30,40])

my_list.insert(1, 13)

my_list2=[50,60,70]

#my_list.append(my_list2)

#my_list=[40,30,20,10]
del my_list[4]

my_list.sort()

print(my_list[3])