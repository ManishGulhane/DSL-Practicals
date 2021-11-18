balance = 0
a=input("d-deopist, w-withdraw, Enter your operation: ")
if a == "d":
  d=int(input("Enter amount to Deposit: "))
  balance +=d
  print (f" Account balance after depositing is {d}={balance}")
elif a == "w":
  w=int(input("Enter amount to Withdraw: "))
  if w>=balance:
    balance-=w
  print(f" Account balance after withdrawing is {w}={balance}")
else:
  print("Error: Enter Valid Operator! (d or w)")
