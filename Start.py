print(14)
#print("Internship is here! "+ str(2+3+6) + "  Minutes" ) 
print(f"Internship is here! {5+6} Minutes" ) 
print(2+3+6) 

name="Flaxem"
def location(weeks):
    print(f"{weeks} Have loved this place "+ name)

location(8)
location(82)
location(2)
location(58)


today="Monday"

def takein(pizza):
    return f"{pizza} is ate on {today}"

take=takein("peas")
print(take)

semester="Finalists"
def report(date):
    print(f"{date} will be for champions {semester}")

report("August")


def vain(variable):
    print(variable<=15)
    if variable<15:
        print("Underage")  
    elif varible == 15:
        print("Normal")  
    else:
        print("Overage")

rest=vain(13)
print(rest)

count=0
while (count < 3):
    print("Kisasi")
    count=count+1
else:
     print("Shut down")

n=5
for m in range(2,n):
    print(m)
   
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
  
min=["Kin","Fred","Lubo"]
J=["Trace","Frank", "sugar"]
min.append(J)
for minu in min:
    print(minu)



""""
value1=input("Please enter the numebr \n")
value2=input("Please enter the numebr \n")

def result():
    print(int(value1) + int(value2))
res=result()
print(f"The final statement of the value {res}")
"""""
