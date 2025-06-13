f=open("D:\\24FFMCA077\\python lab\\demo.txt",'r')
print("The file pointer is at byte:",f.tell())
content=f.read()
print("After reading,the file pointer is at:",f.tell())
