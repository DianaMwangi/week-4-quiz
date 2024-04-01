def my_function(base,expotent):
    result = base**expotent
    return result > 5000


base_number = int(input("write number here: "))
expotent_number = int(input("write number here: "))

print(my_function (base_number, expotent_number))