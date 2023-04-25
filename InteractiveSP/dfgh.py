# class E:
#     def __init__(self):
#         self.name=input("Nsame")
#         self.empid=input("EMPID:")
#         self.sal=input("Salary:")


#     def show(self):
#         print("NAme:",self.name)
#         print("id:",self.empid)
#         print("sal=",self.sal)
#         print("LN:",self.last)   

# class D(E):
#     def __init__(self):
#         self.last=input("Last name")   
#         self.name=input("Nsame")
#         self.empid=input("EMPID:")
#         self.sal=input("Salary:")
         


# c=D()
# c.show()
 

# try:
#     f=open("f1.txt",'z')
#     print("Done")
# except ValueError:
#     print("VE")

try:
    f=open("none.txt",'w')
    print("Done")
except FileNotFoundError:
    print("FNFE")   

try:
    f=open("") 

      