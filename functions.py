def greet_user():
    print("hii")
    print("welcome")
print("start")
greet_user()
print("finish")

def greet_user(name):
    print(f"hii,{name}!")
    print("welcome")
print("start")
greet_user("keerthana")
greet_user("mary")
print("finish")

def greet_user(first_name,last_name):
    print(f"hii,{first_name} {last_name}!")
    print("welcome")
print("start")
greet_user("keerthana","keerthi")
greet_user("mary","keerthi")
print("finish")

def greet_user(first_name,last_name):
    print(f"hii,{first_name} {last_name}!")
    print("welcome")
print("start")
greet_user("keerthana","keerthi")
print("finish")

def square(number):
    return number*number

result = square(3)
print(result)