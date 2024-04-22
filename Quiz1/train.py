coachtype=input("enter coach type: ")
journeytype=input("enter jorney type: ")

if(coachtype=="1AC"):
    cost=400
elif(coachtype=="2AC"):
    cost=300
elif(coachtype=="3AC"):
    cost=200
elif(coachtype=="sleeper"):
    cost=100
else:
    print("invalid number")
if(journeytype=="monthly"):
    cost=(cost*30)
    print(cost)
else:
    cost=cost*1
    print(cost)
    



