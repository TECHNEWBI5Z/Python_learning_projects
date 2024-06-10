# Welcome message for the tip calculator
print("Welcome to the tip calculator!")

# Get the total bill amount from the user
total_bill_amount = input("What is your total bill amount?\n")

# Get the tip percentage the user wants to give
tip_percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15?\n")

# Get the number of people to split the bill
total_shareholders = input("How many people will split the bill?\n")

# Convert the inputs to float for calculation
total_bill_amount_as_float = float(total_bill_amount)
tip_percentage_as_float = float(tip_percentage)
total_shareholders_as_float = float(total_shareholders)

# Calculate the tip amount
tip_amount = total_bill_amount_as_float * tip_percentage_as_float / 100

# Print the calculated tip amount (for debugging purposes)
print(f"Tip amount: {tip_amount}")

# Calculate the total bill amount including the tip
total_bill_amount_with_tip = total_bill_amount_as_float + tip_amount

# Print the total bill amount with the tip (for debugging purposes)
print(f"Total bill amount with tip: {total_bill_amount_with_tip}")

# Calculate the amount each person has to pay
total_amount_to_be_paid_by_person = total_bill_amount_with_tip / total_shareholders_as_float

# Round the final amount to 2 decimal places for currency formatting
final_amount = round(total_amount_to_be_paid_by_person, 2)

# Print the type of final_amount (for debugging purposes)
print(type(final_amount))

# Print the final amount each person has to pay
print(f"Each person has to pay around ${final_amount} USD.")
