
# Assignment 1 - Tip Calculator by Linda Liu

# Instructions: code a “tip calculator” program that calculates the price per person for a meal

# Variables List
tip_amount = 0

# INPUT: number of diners
num_diners = int(input("How many people are dining? "))

# INPUT: price of meal before tax, and validating it's a float
def meal_cost(meal_cost_question):
    while True:
        try:
            pre_tax_price = float(input(meal_cost_question))
        except ValueError:
            print("Not a valid meal cost!")
            continue
        else:
            return meal_cost

pre_tax_price = meal_cost("What is the cost of the meal before tax? ")

#INPUT: tip percentage selection

while True:
    tip = input("How much do you wish to tip? Type the letter associated with the tip amount. \n A. 20% \n B. 15% \n C. 10% \n D. 0% \n \n")
    tip = tip.upper()
    if tip == "A":
        tip_amount = 0.2
        break
    if tip == "B":
        tip_amount = 0.15
        break
    if tip == "C":
        tip_amount = 0.1
        break
    if tip == "D":
        tip_amount = 0
        break
    print("Not a valid selection!")

# Output 1. The number of diners
# print("The number of diners is " + str(num_diners))

# Output 2. The price of the meal before tax
# print("The cost of the meal before tax is $" + str(pre_tax_price))

# Output 3. The Quebec tax added (Federal)


# Output 4. The Quebec tax added (Provincial)
# Output 5. The total including tax
# Output 6. The tip amount (based on the price before tax)
# Output 7. The grand total including tax
# Output 8. The amount owed per person

