
# Assignment 1 - Tip Calculator by Linda Liu

# Instructions: code a “tip calculator” program that calculates the price per person for a meal

# Variable initialization
tip_amount = 0

# INPUT: number of diners
num_diners = int(input("How many people are dining? "))

# INPUT: price of meal before tax, and validating it's a float
def meal_cost_fc(meal_cost_question):
    while True:
        try:
             meal_cost = float(input(meal_cost_question))
        except ValueError:
            print("Not a valid meal cost!")
            continue
        else:
            return meal_cost
            break

pre_tax_price = meal_cost_fc("What is the cost of the meal before tax? ")

#INPUT: tip percentage selection

while True:
    tip = input("How much do you wish to tip? Type the letter associated with the tip percentage. \n A. 20% \n B. 15% \n C. 10% \n D. 0% \n \n")
    tip = tip.upper()
    if tip == "A":
        tip_percentage = 0.2
        break
    if tip == "B":
        tip_percentage = 0.15
        break
    if tip == "C":
        tip_percentage = 0.1
        break
    if tip == "D":
        tip_percentage = 0
        break
    print("Not a valid selection!")

# OUTPUT: calculating outputs 3 to 8
GST = 0.05
QST = 0.09975

meal_GST = pre_tax_price * GST
meal_QST = pre_tax_price * QST
grand_total = pre_tax_price + meal_GST + meal_QST + (pre_tax_price * tip_percentage)
cost_per_person = grand_total / num_diners

receipt = {'Price':pre_tax_price, 'GST':meal_GST, 'QST':meal_QST,
           'Price incl. tax':pre_tax_price + meal_GST + meal_QST,
           'Tip':pre_tax_price * tip_percentage, 'Grand Total':grand_total}

# OUTPUT: printing the results of the output into a receipt (for 1 diner) format
print("\nRECEIPT")
print("=" * 30)
print("\n{0:20s}{1:}".format('Diners', num_diners))

for i, j in receipt.items():
    print("{0:20s}${1:.2f}".format(i,j))

print("-" * 30)
print("{0:20s}${1:.2f}".format('You pay:', cost_per_person))