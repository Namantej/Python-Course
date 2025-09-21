def age_calc():
    age = int(input("How old are you: "))
    decades = age // 10   # // means Modulus(MOD)
    remaining = age % 10
    print("You are", str(decades), "decades", "and", str(remaining),"year(s) old")

age_calc()
