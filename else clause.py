try:
    num=int(input("enter a number:"))
    result=10/num
except valueerror:
    print("error:invalid input!please enter a valid number")
except Zerodivisionerror:
    print("error:division by zero!")
else:
    print("result:",result)
