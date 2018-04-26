PRICE = float(input("Enter cents per kWh:"))
USAGE = float(input("Enter daily use in kWh:"))
DAYS = int(input("Enter number of billing days"))

BILL= PRICE + USAGE + DAYS
print("Estimated BILL: $", BILL)


