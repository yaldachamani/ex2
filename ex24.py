a=[]
while True:
    n=int(input("please enter a number: "))
    a.append(n)
    
    i=input("if you want to exit please enter exit  ")
    if i=="exit":
        break
    
        
Sum=sum(a)
print("sum = ",Sum)  