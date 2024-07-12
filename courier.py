
cost1 = 0.36
cost2 = 0.25
full_insurance = 50.00
limit_insurance = 25.00
gift_cover = 15.00
no_gift = 0.00
priority_delivery = 100.00
standard_delivery = 20.00
postage_sleeve = 100.00
postage_box = 150.00


def distance():
    user = input("enter transport mode(air freight 1:  / land freight :2) ")
    if user == "1":
        return float(cost1)
    elif user == "2":
        return float(cost2)
    else:
        print("invalid option")
        return 0.0
    
def insurance():
    name = input("do you have insurance(yes/no): ")
    while name == "yes":
        x = input("full insurance 1:  or limited insurance 2: ")
        if x.isalpha():
            print("invalid")
            break
        elif not x.isnumeric():
            print("invalid")
            break
        else:
            while x:
                if x == "1":
                    return float(full_insurance)
                    
                elif x == "2":
                    return float(limit_insurance)
                    
                else:
                    print("invalid option")
                    return 0.0

    while name == "no":
        print("no insurance")
        break
    if name.isnumeric():
        print("invalid keys")
    else:
        pass

def cover():
    m = input("Do you want to add gift(yes/no)?: ")
    if m == "yes":
        return float(gift_cover)  # remember to fix
    elif m == "no":
        return 0.0

def delivery():
    h = input("delivery method(proirity delivery 1: /standard delivery 2: ")
    if h == "1":
        return float(priority_delivery)
    elif h == "2":
        return float(standard_delivery)
    else:
        return "0.0"

def package():
    f = input("would you like box or sleeve?: ")
    if f == "box":
        return float(postage_box)
    elif f == "sleeve":
        return float(postage_sleeve)
    else:
        return 0.0

def total_cost():
    distance_cost = distance()
    insurance_cost = insurance()
    cover_cost = cover()
    delivery_cost = delivery()
    package_cost = package()
    
    total = distance_cost + insurance_cost + cover_cost + delivery_cost + package_cost
    return float(total)

total = total_cost()
print("your total is: R", total)