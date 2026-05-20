command =""
while True:
    command=input(">").lower()
    if command =="start":
        print("car started...")
    elif command =="stop":
        print("car stopped...")
    elif command =="help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to quit")
    elif command =="quit":
        break
    else:
        print("sorry, I don't understand that...")