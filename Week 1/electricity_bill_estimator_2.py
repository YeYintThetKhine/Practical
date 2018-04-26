print("Electricity Bill Estimator \n")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tariff? 11 or 31?"))

while tariff != 11 and tariff != 31:
    print("Invalid option")
    tariff = int(input("Which tariff? 11 or 31?"))
if tariff == 11:
    cents_per_kwh = TARIFF_11
else:
    cents_per_kwh = TARIFF_31

daily_use_kWh = float(input("Enter daily use in kWh: "))
while daily_use_kWh <=0:
    print("Invalid value")
    daily_use_kWh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
while billing_days <=0:
    print("Invalid value")
    billing_days = int(input("Enter number of billing days: "))
estimated_bill = round(cents_per_kwh * daily_use_kWh * billing_days, 2)
print("Estimated bill: ${:.2f}".format(estimated_bill))