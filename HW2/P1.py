
print("\nSDET101-102 HW2 Part 1, Ricardo DaSilveira, UCID:212-05-998, rcd4@njit.edu\n")


#######=======================#####
#######       Question 1      #####
#######=======================#####
print("SDET101-102, rcd4 - 212-05-998")
print("\nQuestion 1")
print("a. Calculate and print the number of days with temperatures above 24°C.")
print("b. Identify and print the highest and lowest temperatures of the month.\n")

temperatures = [18, 22, 19, 25, 17, 21, 23, 20, 26, 24, 19, 22, 27, 21, 23, 18, 24, 25, 19, 20, 22, 26, 23, 21, 19, 24, 22, 20, 18, 23]
maxTemp = 24
peakTemp = 0
lowestTemp = 100
i=0

for t in temperatures:
    if t > maxTemp:
        i +=1
    if t > peakTemp:
        peakTemp = t
    if t < lowestTemp:
        lowestTemp = t
print(f"Number of hot days (above {maxTemp}\N{DEGREE SIGN}C): {i}")
print(f"Highet Temperature: {peakTemp}\N{DEGREE SIGN}C")
print(f"Lowest Temperature: {lowestTemp}\N{DEGREE SIGN}C\n")

#######=======================#####
#######       Question 2      #####
#######=======================#####
print("\nQuestion 2")
print("a. Calculate and print the average score.")
print("b. Determine the number of students who passed and failed. (Assume a passing score is 70 or above.)")
print("c. Print a message for each student indicating 'Pass' or 'Fail'.\n")

scores = [88, 76, 90, 85, 92, 67, 73, 81, 95, 78]
print("Average score:" + str(sum(scores)/len(scores)))
passGrade = 70
passStudents = len([g for g in scores if g >= passGrade])
failStudents = len(scores) - passStudents
print(f"number of students who passed:{passStudents}" )
print(f"number of students who failed:{failStudents}" )
i=0
for s in scores:
    i+=1
    if s >= passGrade:
        result ="Pass"    
    else:
        result="Fail"
    print(f"Student {i:02}: {result}")

#######=======================#####
#######       Question 3      #####
#######=======================#####
print("\nQuestion 3")
print("a. Identify items that need restocking (quantity less than 20).")
print("b. Calculate the total value of the current inventory.")
print("c. Increase the price of items with quantity less than 15 by 10%.\n")
inventory = [
    {'item': 'Apple', 'quantity': 50, 'price': 0.5},
    {'item': 'Banana', 'quantity': 20, 'price': 0.3},
    {'item': 'Orange', 'quantity': 30, 'price': 0.7},
    {'item': 'Grapes', 'quantity': 15, 'price': 1.5},
    {'item': 'Mango', 'quantity': 10, 'price': 2.0},
]

r = [item['item'] for item in inventory if item['quantity'] < 20]
print("Items to restock: " + ', ' .join(r)) #print all items in one line
total = sum(item['quantity'] * item['price'] for item in inventory)
print(f"Total inventory value: ${total}")
print("Updated Inventory Prices:")        
t = [item for item in inventory if item['quantity'] < 15]
print(f"{t[0]['item']}: ${t[0]['price']*1.1} (Old price: ${t[0]['price']})")


