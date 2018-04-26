
sales = 1
sales = float(input("Enter sales: $"))
while sales > -1:
    if -1 < sales < 1000:
        sales *= .1
    elif sales >= 1000:
        sales *= .15
    else:
        break
print("$" + "{:.2f}".format(sales))