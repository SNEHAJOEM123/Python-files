command=""
started=False
while True:
    command=input("> ").lower()

    if command=="start":
        if started:
            print("Car is already started")
        else:    
            print("Car started...")
            started=True


    elif command=="stop":
        if not started:
            print("Car had already stopped")
        else:    
            print("Car stopped...")
            started=False

    elif command=="help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit""")
    elif command=="quit":
        break
    else:
        print("Sorry,I don't understand that!")

