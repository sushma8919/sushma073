try:
    x=int(input("enter a number upto 100:"))
    if x>100:
        raise valueerror(x)
except valueerror:
    print(x,"is out of allowed range")
else:
    print(x,"is within the allowed range")
