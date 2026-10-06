import random
import time
money = 500
day = 1
hour = 9
minute = 0
computers = [
    {"id": 1, "working": True},
    {"id": 2, "working": True},
    {"id": 3, "working": True},
    {"id": 4, "working": True},
    {"id": 5, "working": True}
]
customers = [
    {
        "name": "Ahmed",
        "type": "student",
        "need": "research",
        "patience": 5,
        "spending": 20
    },
    {
        "name": "Sara",
        "type": "student",
        "need": "email",
        "patience": 4,
        "spending": 15
    },
    {
        "name": "Bilal",
        "type": "gamer",
        "need": "gaming",
        "patience": 3,
        "spending": 30
    },
    {
        "name": "Mr. Khan",
        "type": "office worker",
        "need": "work",
        "patience": 6,
        "spending": 40
    },
    {
        "name": "Ayesha",
        "type": "email user",
        "need": "email",
        "patience": 5,
        "spending": 20
    }
]
def show_time():
    period = "AM"
    display_hour = hour
    if hour >= 12:
        period = "PM"
    if hour > 12:
        display_hour = hour - 12
    if display_hour == 0:
        display_hour = 12
    return f"{display_hour}:{minute:02d} {period}"
def advance_time(minutes):
    global hour
    global minute
    minute += minutes
    while minute >= 60:
        minute -= 60
        hour += 1
def show_status():
    print("\n==============================")
    print("      INTERNET CAFÉ 2007")
    print("==============================")
    print(f"Day: {day}")
    print(f"Time: {show_time()}")
    print(f"Money: ${money}")
    working = 0
    for computer in computers:
        if computer["working"]:
            working += 1
    print(f"Computers working: {working}/{len(computers)}")
    print("==============================\n")
def show_computers():
    print("\nCOMPUTERS")
    for computer in computers:
        if computer["working"]:
            status = "WORKING"
        else:
            status = "BROKEN"
        print(f"Computer {computer['id']}: {status}")
def get_customer():
    customer = random.choice(customers)
    print("\nA customer walks into the café...")
    time.sleep(1)
    print(f"\nName: {customer['name']}")
    print(f"Type: {customer['type']}")
    print(f"They need: {customer['need']}")
    print(f"Patience: {customer['patience']}")
    return customer
def serve_customer():
    global money
    working_computers = []
    for computer in computers:
        if computer["working"]:
            working_computers.append(computer)
    if len(working_computers) == 0:
        print("\nThere are no working computers!")
        print("The customer leaves angry.")
        return
    customer = get_customer()
    computer = random.choice(working_computers)
    print(f"\n{customer['name']} uses Computer {computer['id']}.")
    print(f"They are here to {customer['need']}.")
    session_time = random.randint(10, 45)
    print(f"They stay for {session_time} minutes.")
    time.sleep(2)
    advance_time(session_time)
    earnings = random.randint(
        5,
        customer["spending"]
    )
    money += earnings
    print(f"\n{customer['name']} pays ${earnings}.")
    print(f"You now have ${money}.")
def random_event():
    global money
    event = random.randint(1, 10)
    if event == 1:
        broken = random.choice(computers)
        if broken["working"]:
            broken["working"] = False
            print("\n⚠️ OH NO!")
            print(
                f"Computer {broken['id']} has broken!"
            )
    elif event == 2:
        print("\nThe electricity flickers...")
        print("Luckily, it comes back.")
    elif event == 3:
        print("\nSomeone calls the café.")
        print("They ask about your internet prices.")
    elif event == 4:
        print("\nYou find a forgotten drink.")
        print("You decide to keep it.")
    else:
        print("\nNothing unusual happens.")
def game():
    global day
    global hour
    global minute
    print("\n================================")
    print("       INTERNET CAFÉ 2007")
    print("================================")
    print("\nYou have just opened your own")
    print("tiny internet café.")
    print("Your goal:")
    print("SURVIVE AND MAKE MONEY.\n")
    while True:
        if hour >= 22:
            print("\nIt is 10 PM.")
            print("The café is closing.")
            day += 1
            hour = 9
            minute = 0
            print(
                f"\nDay {day} begins at 9:00 AM."
            )
            continue
        show_status()
        print("What do you want to do?")
        print("1. Serve a customer")
        print("2. Check computers")
        print("3. End the day")
        print("4. Quit")
        choice = input("\n> ")
        if choice == "1":
            serve_customer()
            random_event()
        elif choice == "2":
            show_computers()
        elif choice == "3":
            print("\nYou close the café for the night.")
            day += 1
            hour = 9
            minute = 0
            print(
                f"\nDay {day} begins tomorrow."
            )
        elif choice == "4":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice.")
game()