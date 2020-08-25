"""
Final look
Number of items: 3  
Price of item: 100  
Price of item: 35.56  
Price of item: 3.24  
Total price for 3 items is $124.92  
"""
num_items_question = int(input("How many items: "))
num_items = 0
cost = 0
while num_items_question < 0:
    print("Invalid number of items")
    num_items_question = int(input("How many items: "))
else:
    while num_items != num_items_question:
        cost_of_item = float(input("Cost of item: $"))
        num_items += 1
        cost += cost_of_item
    else:
        print(f"The total cost of {num_items} items is ${cost}")
    if cost > 100:
        print("As you have spent over $100 a 10% discount has been applied")
        print(f"Final Cost ${cost * 0.9} \n You have saved ${cost * 0.1}")
