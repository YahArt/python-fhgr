# 5.4 a, b, c

total_sum = 0.0
quit = 'x'
price_reduction = False

# Allow entering prices until the user inputs a 'x'
result = input("Enter your price enter 'x' when your are finished: ")
while result != quit:
    total_sum += float(result)

    # Keep the loop going...
    result = input("Enter your price enter 'x' when your are finished: ")

# Check for price reduction
if total_sum > 100.0:
    print("You have a total sum of over 100 so you get a 5% discount...")
    total_sum = total_sum * 0.95

# Calculate prices in CHF and EUROS
price_chf = total_sum
price_eur = price_chf * 0.91 # Go online and see the exchange rate
print("The total price in CHF:", price_chf)
print("The total price in EUR:", price_eur)
