import random
bal = 10000
b_o1 = 0
week = 1
menu = True
print("Welcome to *Margin of Fate*, a journey where time, money, and heart collide.\n")
name = input("What is your name?\n")
print("\nUnfortunately, I have terrible news", name,". Your mother has been diagnosed with cancer.")
print("Her only hope is a treatment that costs $200,000.\n")
while (True):
    f = input("Will you fight to save your mom's life?\n1. Yes, I’ll do whatever it takes.\n2. No, it’s too much.\n")
    if f in ["1","2"]:
        alive = True
        break
    else:
        print ("Enter the choice 1 or 2.\n")
while (True):
    job = input("\nChoose your financial battlefield to earn the $200,000 needed:\n"
    "1. Crypto – High stakes, higher risks, and wild rewards.\n"
    "2. Stock Market – A steadier path with smaller gains and safer steps.\n")
    if job in ["1", "2"]:
        print("It's a smart choice. \nLet's begin our journey\n")
        break
    else:
        print ("Enter the choice 1 or 2.\n")
while alive:
    bal = round(bal, 2)
    b_o1 = round(b_o1, 2)
    print("Week",week,"begins,",name,". Another chance to rise—or fall. Let’s make it count.\n")
    remain = 200000-bal
    print("You are now at",bal,"$\nYou are",b_o1,"%" "burnt out.\nYou have",remain,"$ yet to earn")
    while menu:
        print("Menu:")
        while (True):
            choice = input("\n1.Check stats\n2.How many hours per day you will work?"
            "\n3.Manage the time spent with your family or friends?" 
            "\n4.Week budget to treat yourself? \n6.I'm ready for the next week \n9.Exit\n")
            if choice in ["1", "2", "3", "4", "5", "6", "9"]:
                break
            else:
                print ("\nEnter the number related to your choice")
        if choice == "2":
            while (True):
                work = input("\nEnter how many hours you'd like to work this week? \nPress h for advice\n")
                if work == "h":
                    print("\nConsidering time for sleep, the limit is 16 hours per day.")
                else:
                    try:
                        work = float(work)
                        if 0 <= work <= 16:
                            break
                        else:
                            print ("\nSince you can't work while sleeping, you need to choose a number between 0 and 16")
                    except:
                        print("\nEnter a valid number or 'h' for help")
        if choice == "1":
            print("Your balance =",bal,"\nYour burnout level =",b_o1,"%\nThis is week",week,)
        if choice == "3":
            while (True):
                friend = input("\nWould you like to spend this weekend with your close ones?\n1.Yes\n2.No\n")
                if friend in ["1","2"]:
                    break
                else:
                    print ("\nEnter a number related to your choice")
        if choice == "4":
            while (True):
                treat = input("\nAs a normal human you need to meet your own needs and treat yourself."
                "\nEnter the amount of money you want to assign for your leisure\n")
                try:
                    treat = float(treat)
                    if 0 <= treat <= bal:
                        break
                    else:
                        print("\nThis amount can't be greater than you balance.")
                except:
                    print("\nIf you don't want to assign any money, just enter 0")
        if choice == "6":
            if friend == "1":
                print ("You chose to:\nWork for",work,"hours\nTo spend a weekend with your close ones" \
                "\nAssigned",treat,"$ to treat yourself")
            if friend == "2":
                print ("You chose to:\nWork for",work,"hours\nNot to spend a weekend with your close ones" \
                "\nAssign",treat,"$ to treat yourself")
            while (True):
                ready = input("Are you confident in your plan for this week?\n1. Yes, I'm ready.\n2. No, I want to adjust something.\n")
                if ready == "1":
                    menu = False
                    break
                if ready == "2":
                    break
                else:
                    print ("Enter the number related to your choice")
        if choice == "9":
            alive = False
    if work<12:
        b_o = ((work+2)**1.3)-8
    else:
        b_o = ((work-6.5)**2)-7.5
    b_o1 = b_o1/1.3
    b_o1 = b_o+b_o1
    if friend == "1":
        b_o1 = b_o1/1.2
        work = (5*work)/7
    if treat>0:
        b_o1 = b_o1*(1-(treat/bal)**2)
    int_rat = 0.25*work-1
    int_rat = int_rat*(1-(b_o1/100))
    w_alt = (int_rat+1)/0.25
    m = random.uniform(w_alt-1,w_alt+1)
    int_rat = 0.25*m-1
    bal = bal-treat
    bal = bal*(1+int_rat)
    week = week+1 
    if week==17:
        print("Your mom's surgery is tomorrow. Let's see if we have enough money")
        if bal>=200000:
            print("Congratulations! You saved your mom")
        else:alive=False
    menu = True