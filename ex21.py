import random
pc_number=random.randint(0,20)
count=0
while True:
    user_number=int(input("enter number:  "))
    if pc_number==user_number:
        print("barande shodi")
        print("tedad hads: ",count)
        break
    if pc_number>user_number:
        print("boro balatar")
        count=count+1
    if pc_number < user_number:
        print("boro paeintar")
        count=count+1