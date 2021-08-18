import datetime
print("Welcome to the Grocery Shopping Simulator")
#display current date and time
x=datetime.datetime.now()
print("Current Date and Time: " + x.strftime("%c"))

#create shopping list 
shopping = ["Meat","Cheese"]

print("\nYou currently have " + shopping[0] + " and " + shopping[1] + " on your shopping list. Please add 3 more items.")

#gather user input for remaining items, add to list and capitalise first letter
item = input("\nFirst item to be added to list:")
shopping.append(item.title())
item = input("Second item to be added to list:")
shopping.append(item.title())
item = input("Third item to be added to list:")
shopping.append(item.title())

print("\nHere is your current shopping list:")
print(shopping)

#sort list alphabetically
print("\nHere is your list sorted:")
shopping.sort()
print(shopping)

print("\nSimulating shopping...")

#print length of current list
print("\nCurrent shopping list: " + str(len(shopping)) + " items")

#ask user which item purchased and remove from list 3 times
item = input("What item did you just buy:")
item = item.title()
print("Removing " + item + " from list...")
shopping.remove(item)

print("\nCurrent shopping list: " + str(len(shopping)) + " items")
print("You still have " + str(shopping) + " on your list.")
item = input("\nWhat item did you just buy:")
item = item.title()
print("Removing " + item + " from list...")
shopping.remove(item)

print("\nCurrent shopping list: " + str(len(shopping)) + " items")
print("You still have " + str(shopping) + " on your list.")
item = input("\nWhat item did you just buy:")
item = item.title()
print("Removing " + item + " from list...")
shopping.remove(item)

#advise store out of last product on list and get user input for replacement item. New item to be placed at start of list
print("\nCurrent shopping list: " + str(len(shopping)) + " items")
no_stock = input("You still have " + str(shopping) + " on your list. \n\nThe store has run out of " + shopping[-1] + ". \nWhat would you like instead: ")
shopping.pop(-1)
shopping.insert(0,no_stock.title())

print("\nThese items remain on your list:\n" + str(shopping) )



