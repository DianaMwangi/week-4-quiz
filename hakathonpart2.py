n = int(input("your number: "))

my_list=[0,1]

while len(my_list)< n:
    next_term = my_list[-1] + my_list[-2]
    my_list.append(next_term)

    print("list", n,":", my_list[:n])