command =""
started = False
while True:
    command=input(">").lower()
    if command =="start":
        if started:
            print("caris started...")
        else:
            started=True
        print("car started...")
    elif command =="stop":
        if not started:
            print("car is already stopped..")
        print("car stopped...")
    elif command =="help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to quit")
    elif command =="quit":
        break
    else:
        print("sorry, I don't understand that...")