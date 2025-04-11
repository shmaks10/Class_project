bal = 10000
b_o = 0
week = 0
int_rat = 0
menu = True
print("Hello. Welcome to Margin of Fate.")
name = input("What is your name")
print("Unfortunately, I have bad news", name,".Your mom has cancer."
" Her treatment requires 200k dollars")
f = input("Would you like to save your mom? \n1.Yes \n2.No")
if f == "1":
    job = input("Let's choose the field you will use your knowledge at, to accomplish your "
    "goal in 1 million dollars \n1.Crypto (more work, bigger interest rate, bigger risk)\n"
    "2.Stock market trading (less work, less interest rate, less risk)")
    alive = True
    print("It's a smart choice. \nLet's begin our journey")
else: alive = False
while alive:
    while menu:
        print("Good morning",name,"this is week",week,"let's continue")
        print("What are your plans for the next week?")
        choice = input("1.Check stats\n2.How many hours per day you will work?"
        "\n3.Are you going to spend this weekend with your family or friends?"
        "\n4.Would you like to treat yourself? \n9.Exit")
        if choice == "2":
            work = input("Enter how many hours you'd like to work this week? \nPress h for advice")
            if work == "h":
                print("Considering time for sleep, the limit is 16 hours per day.")
        if choice == "1":
            print("Your balance =",bal,"\nYour burnout level =",b_o,"\nThis is week",week,"\nYour interest rate =",int_rat,)
        if choice == "3":
            friend = input("Would you like to spend this weekend with your friends or working?\n1.Yes\n2.No")
        if choice == "4":
            treat = input("As a normal human you need to meet your own needs and treat yourself."
            "\nEnter the amount of money you want to assign for your leisure")
        if choice == "9":
            alive = False
        try:
            work = float(work)
            menu = False
        except:
            continue
    if work<12:
        b_o = ((work+2)^1.3)-8
    else:
        b_o = ((work-6.5)^2)-7.5
    if friend == "1":
        b_o = b_o/1.2
