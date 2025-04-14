import random
bal = 10000
b_o = 0
week = 1
menu = True
print("Hello. Welcome to Margin of Fate.")
name = input("What is your name")
print("Unfortunately, I have bad news", name,".Your mom has cancer."
" Her treatment requires 200k dollars")
f = input("Would you like to save your mom? \n1.Yes \n2.No")
if f == "1":
    job = input("Let's choose the field you will use your knowledge at to accomplish your "
    "goal in 200k dollars \n1.Crypto (more work, bigger interest rate, bigger risk)\n"
    "2.Stock market trading (less work, less interest rate, less risk)")
    alive = True
    print("It's a smart choice. \nLet's begin our journey")
else: alive = False
while alive:
    while menu:
        bal = round(bal, 2)
        b_o = round(b_o, 2)
        print("Good morning,",name,".This is week.",week,"Let's continue")
        print("What's your next move?")
        choice = input("1.Check stats\n2.How many hours per day you will work?"
        "\n3.Manage the time spent with your family or friends?" 
        "\n4.Week budget to treat yourself? \n6.I'm ready for the next week \n9.Exit")
        if choice == "2":
            work = input("Enter how many hours you'd like to work this week? \nPress h for advice")
            if work == "h":
                print("Considering time for sleep, the limit is 16 hours per day.")
        if choice == "1":
            print("Your balance =",bal,"\nYour burnout level =",b_o,"\nThis is week",week,)
        if choice == "3":
            friend = input("Would you like to spend this weekend with your close ones?\n1.Yes\n2.No")
        if choice == "4":
            treat = input("As a normal human you need to meet your own needs and treat yourself."
            "\nEnter the amount of money you want to assign for your leisure")
        if choice == "6":
            ready = input("Are you sure you've completed your planning? \n1.Yes \n2.Return")
            if ready == "1":
                work = float(work)
                treat = float(treat)
                menu = False
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
    week = week+1
    if week==17:
        print("Your mom's surgery is tomorrow. Let's see if we have enough money")
        if bal==200000:
            print("Congratulations! You ssaved your mom")
        else:alive=False
    menu = True