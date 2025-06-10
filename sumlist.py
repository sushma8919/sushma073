l=eval(input("enter some list elements:"))
ls=[]
for x in l:
     if x not in ls:
         ls.append(x)
print("before removing duplicate objects:",l)
print("after removing duplicate objects:",ls)
 
