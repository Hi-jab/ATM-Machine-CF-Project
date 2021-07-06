import time
print("Please Insert Your Card: ")
time.sleep(3)
password=1234
pin=int (input("Enter Your ATM Pin: "))
balance = 5000
if pin==password:
    while True:
        print("""
          1==balance
          2==withdraw balance
          3==deposit balance
          4==exit
          """
          )
        try:
            option=int (input("Please Enter Your Choice: "))
        except:
            print("Please Enter Valid option")
            print("===========================================")
            print("===========================================")
            print("===========================================")
        if option==1:
            print("Your Current Balance is" ,balance)
            print("===========================================")
            print("===========================================")
            print("===========================================")
        if option==2:
            withdraw_amount=int(input("Please Enter withdraw_amount: "))
            balance=balance-withdraw_amount
            print("withdraw_amount is debited from your Account")
            print("===========================================")
            print("===========================================")
            print("===========================================")
            print("Your Current Balance is", balance)
            print("===========================================")
            print("===========================================")
            print("===========================================")
        if option==3:
            deposit_amount=int(input("Please Enter deposit_amount: "))
            balance=balance+deposit_amount
            print( "is credited to your account" , deposit_amount)
            print("===========================================")
            print("===========================================")
            print("===========================================")
            print("Your updated balance is" ,balance)
            print("===========================================")
            print("===========================================")
            print("===========================================")
        if option==4:
            break
else:
    print("Wrong Pin Please Try Again")
