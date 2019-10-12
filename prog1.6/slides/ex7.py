# 5.4 d, e
from pprint import pprint # For pretty printing the dictionary

total_sum = 0.0
quit = 'x'
price_reduction = False

products = {
    'Apple': 1.50,
    'Banana': 2.50,
    'Meat': 4.50,
    'The food of the gods': 99999 # Also known as cinnamon buns
}

# Allow entering products until the user inputs a 'x'
pprint(products)
result = input("Enter your product enter 'x' when your are finished: ")
while result != quit:
    if products.get(result):
        ammount = input("You have choosen " + result + " how many do you want? ")
        # Well we do not do any validation here... living on the edge
        print("Alrighty then", ammount, result, "it is...")
        total_sum += products[result] * float(ammount)

    else:
        print("Sorry this product does not exist, the following products exist")
        print(products.keys())

    # Keep the loop going...
    result = input("Enter your product enter 'x' when your are finished: ")


# Check for price reduction
if total_sum > 100.0:
    print("You have a total sum of over 100 so you get a 5% discount...")
    total_sum = total_sum * 0.95

# Calculate prices in CHF and EUR
price_chf = total_sum
price_eur = price_chf * 0.91 # Go online and see the exchange rate
print("The total price in CHF:", price_chf)
print("The total price in EUR:", price_eur)
