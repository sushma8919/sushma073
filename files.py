file.path="Example.txt"
f=open("c:\example.txt","r")
with open(file_path,"w")as file:
    file.write("hello,world!")
with open(file_path,"r")as file:
    content=file.read()
    print("file content",content)
