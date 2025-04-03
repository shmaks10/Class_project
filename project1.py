print("Hello. Welcome to Margin of Fate.")
name = input("What is your name")
print("Unfortunately, I have bad news", name, ". Your mom has cancer."
" Her treatment requires 1 million dollars")
c = input("Would you like to save your mom? \n1.Yes \n2.No")
if c == "1":
    job = input("Now let's choose the field you will use your knowledge at to accomplish your "
    "goal in 1 million dollars \n1.Crypto (more work, bigger interest rate, bigger risk)\n"
    "2.Stock market trading (less work, less interest rate, less risk)")
    alive = True
else: alive = False
while alive:
    print("a")