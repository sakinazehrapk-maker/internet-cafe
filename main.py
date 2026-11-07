import random
import time
money = 500
day = 1
hour = 9
minute = 0
electricity = True
ups_owned = False
outage_count = 0
computers = [
    {
        "id": 1,
        "working": True,
        "condition": 95,
        "speed": 3,
        "price": 15,
        "customer": None
    },
    {
        "id": 2,
        "working": True,
        "condition": 80,
        "speed": 2,
        "price": 12,
        "customer": None
    },
    {
        "id": 3,
        "working": True,
        "condition": 65,
        "speed": 1,
        "price": 10,
        "customer": None
    },
    {
        "id": 4,
        "working": True,
        "condition": 90,
        "speed": 3,
        "price": 15,
        "customer": None
    },
    {
        "id": 5,
        "working": True,
        "condition": 50,
        "speed": 1,
        "price": 8,
        "customer": None
    }
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
    if electricity:
        print("Electricity: ON")
    else:
        print("Electricity: OFF")
    if ups_owned:
            print("UPS: Installed")
    else:
            print("UPS: Not installed")
    working = 0
    for computer in computers:
        if computer["working"]:
            working += 1
    print(f"Computers working: {working}/{len(computers)}")
    print("==============================\n")
def show_computers():
    print("\n========== COMPUTERS ==========")
    for computer in computers:
        if computer["working"]:
            status = "WORKING"
        else:
            status = "BROKEN"
        print(
            f"\nComputer {computer['id']}"
        )
        print(
            f"Status: {status}"
        )
        print(
            f"Condition: {computer['condition']}%"
        )
        print(
            f"Speed: {computer['speed']}/3"
        )
        print(
            f"Price: ${computer['price']}"
        )
        if computer["customer"] is not None:
            print(
                f"Customer: {computer['customer']}"
            )
        else:
            print("Customer: Empty")
def repair_computer():
    global money
    show_computers()
    print("\nWhich computer do you want to repair?")
    print("Enter the computer number.")
    print("Enter 0 to cancel.")
    choice = input("\n> ")
    if choice == "0":
        return
    if not choice.isdigit():
        print("\nPlease enter a number.")
        return
    computer_id = int(choice)
    computer = None
    for pc in computers:
        if pc["id"] == computer_id:
            computer = pc
            break
    if computer is None:
        print("\nThat computer doesn't exist.")
        return
    if computer["condition"] >= 100:
        print("\nThat computer doesn't need repairs.")
        return
    repair_amount = 100 - computer["condition"]
    repair_cost = repair_amount // 2
    if repair_cost < 5:
        repair_cost = 5
    print(
        f"\nRepairing Computer {computer['id']} "
        f"will cost ${repair_cost}."
    )
    confirm = input("Repair it? (y/n): ").lower()
    if confirm != "y":
        print("\nRepair cancelled.")
        return
    if money < repair_cost:
        print("\nYou don't have enough money!")
        return
    money -= repair_cost
    computer["condition"] = 100
    computer["working"] = True
    print(
        f"\nComputer {computer['id']} "
        "has been completely repaired!"
    )
    print(f"You spent ${repair_cost}.")
    print(f"You now have ${money}.")
    advance_time(15)
    print("Repair took 15 minutes.")
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
    if not electricity:
        print("\nThe electricity is out!")
        print("You cannot serve customers right now.")
        return
    if len(working_computers) == 0:
        print("\nThere are no working computers!")
        print("The customer leaves angry.")
        return
    customer = get_customer()
    computer = random.choice(working_computers)
    if customer["need"] == "gaming":
        fast_computers = []
    for pc in working_computers:
        if pc["speed"] >= 2:
            fast_computers.append(pc)
    if len(fast_computers) > 0:
        computer = random.choice(fast_computers)
        computer["customer"] = customer["name"]
    print(f"\n{customer['name']} uses Computer {computer['id']}.")
    print(f"They are here to {customer['need']}.")
    session_time = random.randint(10, 45)
    print(f"They stay for {session_time} minutes.")
    time.sleep(2)
    advance_time(session_time)
    wear = random.randint(1, 5)
    computer["condition"] -= wear
    if computer["condition"] < 0:
        computer["condition"] = 0
        print(
            f"Computer {computer['id']} loses "
            f"{wear}% condition."
            )
    earnings = random.randint(
        5,
        customer["spending"]
    )
    money += earnings
    print(f"\n{customer['name']} pays ${earnings}.")
    print(f"You now have ${money}.")
    computer["customer"] = None
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
        electricity_outage()
    elif event == 3:
        print("\nSomeone calls the café.")
        print("They ask about your internet prices.")
    elif event == 4:
        print("\nYou find a forgotten drink.")
        print("You decide to keep it.")
    else:
        print("\nNothing unusual happens.")
def electricity_outage():
    global electricity
    global outage_count
    global money
    print("\n" + "=" * 35)
    print("ELECTRICITY OUTAGE!")
    print("=" * 35)
    electricity = False
    outage_count += 1
    print("\nThe entire café goes dark!")
    if ups_owned:
        print("\nYour UPS activates!")
        print("The computers are still running.")
        outage_duration = random.randint(10, 30)
        print(
            f"Electricity will return in "
            f"{outage_duration} minutes."
        )
        advance_time(outage_duration)
        electricity = True
        print("\nElectricity is back!")
        return
    print("\nYou don't have a UPS!")
    print("All computers shut down.")
    outage_duration = random.randint(20, 60)
    print(
        f"\nThe outage lasts {outage_duration} minutes."
    )
    for computer in computers:
        if computer["customer"] is not None:
            print(
                f"\n{computer['customer']} "
                "leaves without paying!"
            )
            computer["customer"] = None
            computer["condition"] -= 5
            if computer["condition"] < 0:
                computer["condition"] = 0
    advance_time(outage_duration)
    electricity = True
    print("\nElectricity has returned!")
    print("You can reopen the café.")
def buy_ups():
    global money
    global ups_owned
    if ups_owned:
        print("\nYou already own a UPS!")
        return
    ups_price = 200
    print("\n========== UPS SYSTEM ==========")
    print("A UPS provides backup electricity.")
    print(f"Price: ${ups_price}")
    print("Protects your computers during outages.")
    print("================================")
    choice = input("\nBuy UPS? (y/n): ").lower()
    if choice != "y":
        print("\nPurchase cancelled.")
        return
    if money < ups_price:
        print("\nYou don't have enough money!")
        return
    money -= ups_price
    ups_owned = True
    print("\nCongratulations!")
    print("You purchased a UPS!")
    print(f"Remaining money: ${money}")
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
        print("3. Repair a computer")
        print("4. Buy UPS")
        print("5. End the day")
        print("6. Quit")
        choice = input("\n> ")
        if choice == "1":
            serve_customer()
            random_event()
        elif choice == "2":
            show_computers()
        elif choice == "3":
            repair_computer()
        elif choice == "4":
            buy_ups()
        elif choice == "5":
            print("\nYou close the café for the night.")
            day += 1
            hour = 9
            minute = 0
            print(
                f"\nDay {day} begins tomorrow."
            )
        elif choice == "6":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice.")
game()