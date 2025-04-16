import random
bal = 10000
b_o = 0
week = 1
menu = True
print("Hello. Welcome to Margin of Fate.\n")
name = input("What is your name\n")
print("\nUnfortunately, I have bad news", name,".Your mom has cancer."
" Her treatment requires 200k dollars\n")
while (True):
    f = input("Would you like to save your mom? \n1.Yes \n2.No\n")
    if f in ["1","2"]:
        alive = True
        break
    else:
        print ("Enter the choice 1 or 2.\n")
while (True):
    job = input("\nLet's choose the field you will use your knowledge at to accomplish your "
    "goal in 200k dollars \n1.Crypto (more work, bigger interest rate, bigger risk)\n"
    "2.Stock market trading (less work, less interest rate, less risk)\n")
    if job in ["1", "2"]:
        print("It's a smart choice. \nLet's begin our journey\n")
        break
    else:
        print ("Enter the choice 1 or 2.\n")
while alive:
    while menu:
        bal = round(bal, 2)
        b_o = round(b_o, 2)
        print(name,", this is week",week,".Let's continue")
        print("What's your next move?")
        while (True):
            choice = input("\n1.Check stats\n2.How many hours per day you will work?"
            "\n3.Manage the time spent with your family or friends?" 
            "\n4.Week budget to treat yourself? \n6.I'm ready for the next week \n9.Exit\n")
            if choice in ["1", "2", "3", "4", "5", "6", "9"]:
                break
            else:
                print ("\nEnter the value related to your choice")
        if choice == "2":
            while (True):
                work = input("\nEnter how many hours you'd like to work this week? \nPress h for advice\n")
                if work == "h":
                    print("\nConsidering time for sleep, the limit is 16 hours per day.")
                else:
                    try:
                        work = float(work)
                        if 0 <= work <= 24:
                            break
                        else:
                            print ("\nSince there is 24 hours in a day, you need to choose a number between 0 and 24")
                    except:
                        print("Enter a valid number or 'h' for help")
        if choice == "1":
            print("Your balance =",bal,"\nYour burnout level =",b_o,"%\nThis is week",week,)
        if choice == "3":
            while (True):
                friend = input("\nWould you like to spend this weekend with your close ones?\n1.Yes\n2.No\n")
                if friend in ["1","2"]:
                    break
                else:
                    print ("\nEnter the value related to your choice")
        if choice == "4":
            while (True):
                treat = input("As a normal human you need to meet your own needs and treat yourself."
                "\nEnter the amount of money you want to assign for your leisure\n")
                try:
                    treat = float(treat)
                    if 0 <= treat <= bal:
                        break
                    else:
                        print("This amount can't be greater than you balance.")
                except:
                    print("If you don't want to assign any money, just enter 0")
        if choice == "6":
            if friend == "1":
                print ("You chose to:\nWork for",work,"hours\nTo spend a weekend with your close ones" \
                "\nAssigned",treat,"$ to treat yourself")
            if friend == "2":
                print ("You chose to:\nWork for",work,"hours\nNot to spend a weekend with your close ones" \
                "\nAssign",treat,"$ to treat yourself")
            ready = input("Are you sure you've completed your planning? \n1.Yes \n2.Return\n")
            if ready == "1":
                try:
                    work = float(work)
                    treat = float(treat)
                    menu = False
                    break
                except:
                    print("Values have to be numbers")
                    continue
        if choice == "9":
            alive = False
    if work<12:
        b_o = ((work+2)**1.3)-8
    else:
        b_o = ((work-6.5)**2)-7.5
    if friend == "1":
        b_o = b_o/1.2
    if treat>0:
        b_o = b_o*(1-(treat/bal)**2)
        bal = bal-treat
    int_rat = 0.25*work-1
    int_rat = int_rat*(1-(b_o/100))
    w_alt = (int_rat+1)/0.25
    m = random.uniform(w_alt-1,w_alt+1)
    int_rat = 0.25*m-1
    bal = bal*(1+int_rat)
    if bal ==200000:
        print("Congatulations! You did an awesome job")
    week = week+1
    if week==17:
        print("Your mom's surgery is tomorrow. Let's see if we have enough money")
    if bal>=200000:
        print("Congratulations! You saved your mom")
    else:alive=False
    menu = True