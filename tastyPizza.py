import time

pizzas = {1: "vegetarian", 2: "meaty", 3: "pepperoni",
          4: "hawaiian", 5: "BBQ-spicedchicken"}
pizzaSize = {'vegetarian': {'small': 8, 'medium': 17, 'large': 22},
             'meaty': {'small': 15, 'medium': 25, 'large': 30},
             'pepperoni': {'small': 7, 'medium': 15, 'large': 20},
             'hawaiian': {'small': 18, 'medium': 35, 'large': 40},
             'BBQ-spicedchicken': {'small': 15, 'medium': 28, 'large': 34}}

custOrder = 'yes'
yes = ('Yes', 'yes', 'y')
no = ('No', 'no', 'n')
id = 0
total_bill = 0
bill = 0
pizza_list = []
checkout = True
ready = 'yes'

custName = ""


def order():
    #    bill = 0
    global pizChoice
    global sizeChoice
    global checkout
    while checkout:

        print("Which pizza would you like? ")
        for pizza in pizzas:
            print(pizza, '->', pizzas[pizza])
        choice = int(input("Enter the number of your choice? "))
        print("You have selected", pizzas[choice])
        pizChoice = pizzas[choice]
        sizeChoice = input(
            "What size do you want? small, medium, or large\n-> ")
        global bill
        topizza = (pizzaSize[pizChoice][sizeChoice])
        print(f"That is $", topizza)
        if sizeChoice == 'small' or 'medium' or 'large':
            bill = topizza

        else:
            print("check your input")

        return custName, bill, pizChoice, sizeChoice


for word in "Welcome to TaStY Pizza".split():
    print(f'{word.capitalize():=^65}')
print("\n")
time.sleep(0.5)
print('We make the best pizza you would expect,\n')
time.sleep(1.0)
print('very tasty and satisfying.\n')
time.sleep(1.3)


custName = input("Can I have your name please? ")
for char in custName:
    if char.isalpha():
        custName == char
    else:
        print("Your name has to be written using alphabets")

while custOrder in yes:
    pizOrder = 'yes'

    pizOrder = input("Would you like to add a pizza? (Yes/No)  ")
    if pizOrder in yes:
        id += 1
        print(id)
        order()

        pizza_list.append(id)
        pizza_list.append(pizChoice)
        pizza_list.append(sizeChoice)
        total_bill += bill
        ready = input("Are you done with your order? Yes or No  ")
        if ready in yes:
            break
    else:
        print("Thanks for coming around, Have a good day")
        break

print("Thanks {} , your total cost is: ${:.2f} and your orders are as below:".format(
    custName, total_bill))

# making the Pizza_list in form of a list to the customer
z = 0
zz = 0
while z < len(pizza_list)/3:
    print(pizza_list[zz], pizza_list[zz+1], pizza_list[zz+2])
    z += 1
    zz += 3


with open('pizzaOrder.txt', 'w') as file:
    # file.write(pizChoice)
    file.write(str(total_bill))

with open('pizzaOrder.txt', 'r') as file:
    text = file.read()
    print('\nContents of file are the Total bill that is: $', text)
