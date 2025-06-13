f=open("D:\\24FFMCA077\\python lab\\demo.txt",'r')
print("The filepointer is at byte:",f.tell())
f.seek(10)
print("After reading,the filepointer is at:",f.tell())
