def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        return True
    print(price)

        
price=int(input("price:"))
discount_percentage=int(input("dicount:"))

print (calculate_discount(price,discount_percentage))
    