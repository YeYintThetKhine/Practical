tsc = 15
ccc = 5
hdc = 100
shc = 3

def totalCost(ts, cc, hd, shc):
    total = (ts * tsc)+(cc * ccc)+(hd * hdc)
    totalQty = ts + cc + hd
    print("Total Cost--->", total)
    if total > 100:
        discount = total * 0.1
        print("Total Shipping Cost:$", total)
    else:
        print("Shipping to fees will be applied. Grand total is", total + (totalQty * shc))

def getQty(message):
    qty = int(input(message))
    while qty < 0:
        print("Invalid number of items")
        qty = int(input(message))
    return qty

def main():
    ts = getQty("How many T-Shirts do you want?")
    cc = getQty("How many Coffee Cups do you want?")
    hd = getQty("How many portable Hard drives do you want?")
    print("Number of T-Shirts--->", ts)
    print("Number of Coffee Cups--->", cc)
    print("Numer of Portable Hard Drives--->", hd)
    totalCost(ts, cc, hd, shc)

main()