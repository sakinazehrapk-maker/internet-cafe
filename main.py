import random
import time
money = 500
day = 1
computers = [
    {"id": 1, "working": True},
    {"id": 2, "working": True},
    {"id": 3, "working": True},
    {"id": 4, "working": True},
    {"id": 5, "working": True}
]
customers = [
    "student",
    "office worker",
    "gamer",
    "email user",
    "random customer"
]
def show_status():
    print("\n==============================")
    print("      INTERNET CAFÉ 2007")
    print("==============================")
    print(f"Day: ${day}")
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
    print(f"They are a {customer}.")
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
    print(f"\nCustomer uses Computer {computer['id']}.")
    print("They use the internet...")
    time.sleep(2)
    earnings = random.randint(10, 30)
    money += earnings
    print(f"\nCustomer pays ${earnings}.")
    print(f"You now have ${money}.")
def random_event():
    global money
    event = random.randint(1, 10)
    if event == 1:
        broken = random.choice(computers)
        if broken["working"]:
            broken["working"] = False
            print("\n⚠️ OH NO!")
            print(f"Computer {broken['id']} has broken!")
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
    print("\n================================")
    print("       INTERNET CAFÉ 2007")
    print("================================")
    print("\nYou have just opened your own")
    print("tiny internet café.")
    print("Your goal:")
    print("SURVIVE AND MAKE MONEY.\n")
    while True:
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
            print(f"\n🌙 Day {day} begins tomorrow.")
        elif choice == "4":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice.")
game()