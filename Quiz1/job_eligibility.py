age=int(input("enter age: "))
catg=input("enter the category: ")
exp=int(input("enter work experience: "))
if(age>=18):
    if(catg=="Data Analyst"):
        if(exp>=2):
            print("eligible")
elif(age>=18):
    if(catg=="Data Scientist"):
        if(exp>=5):
            print("eligible")
elif(age>=18):
    if(catg=="Data Engineer"):
        if(exp>=3):
            print("eligible")
else:
    print("not eligible")