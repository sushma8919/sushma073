try:
  num=int(input("enter a number:"))
  result=10/num
  print("result:",result)
except valueerror:
  print("Error:Invalid input!please enter a valid number")
except ZeroDivisionerror:
  print("Error:Division by zero!")
    
