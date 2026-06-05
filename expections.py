try:
    age= int(input("age:"))
    invome=20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0.")
except valueError:
    print("Invalid value")
