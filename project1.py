bal = 10000
b_o = 0
week = 0
int_rat = 0
menu = True
print("Hello. Welcome to Margin of Fate.")
name = input("What is your name")
print("Unfortunately, I have bad news", name,".Your mom has cancer."
" Her treatment requires 1 million dollars")
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
        menu = input("What's your next step? \n1.Continue to grind \n2.Check stats \n9.Exit")
        if menu == "1":
            work = input("Enter how many hours you'd like to work this week? \nPress h for advice")
            if work == "h":
                print("Considering time for sleep, the limit is 112 hours a week. We recommend to work for 70 hours "
            "a week to mitigate the burnout level.")
        if menu == "2":
            print("Your balance =",bal,"\nYour burnout level =",b_o,"\nThis is week",week,"\nYour interest rate =",int_rat,)
        if menu == "9":
            alive = False
        try:
            work = int(work)
            menu = False
        except:
            continue
