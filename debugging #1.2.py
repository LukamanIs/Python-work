#This code is able about a store giving a discount
#base on the number of items in the cart
#for 4 and under you get no discount
#for 5-7 you get 20% off
#for 8-10 you get 30% off
#and for  and over you get 40% off

total_price = float()
discount = float()
discount_total = float()
discount_off = float()
counter = 0

item = float(input("how much items in the cart: "))

if item >= 5:
    discount = .20
    while counter < 7:
        item = float(input("Enter the price of item:"))
        counter = counter + 1
        total_price = total_price + item    
    discount_off = total_price * discount
    discount_total = total_price - discount_off
    print("the total is:",discount_total)
elif item >= 8:
    discount = .30
    while counter < 10:
        item = float(input("Enter the price of item:"))
        counter = counter + 1
        total_price = total_price + item 
    discount_off = total_price * discount
    discount_total = total_price - discount_off
    print(discount_total)
elif item >= 11:
    discount = .40
    while counter < 20:
        item = float(input("Enter the price of item:"))
        counter = counter + 1
        total_price = total_price + item 
    discount_off = total_price * discount
    discount_total = total_price - discount_off
    print(discount_total)
else:
    while counter < 4:
        item = float(input("Enter the price of item:"))
        counter = counter + 1
        total_price = total_price + item 
    print(total_price)
    
