print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

result = ((float(tip_percentage) / 100 + 1) * float(total_bill)) / int(people)

print(f"Each person should pay: ${round(result, 2)}")
