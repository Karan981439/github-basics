#taking input form user:

n=str (input("Enter your name: "))
q=int (input("\n what you want today:"))
print("no1.addition\n no2.percentage\n")

while q == 1:

    x= int (input("enter first no:"))
    y= int (input("enter second no:"))
    
    z=x+y 
print("answer is:",z)

if q == 2:

e=float (input("Enter marks for english: \n"))
h=float (input("Enter marks for hindi: \n"))
p=float (input("Enter marks for  punjabi: \n"))
m=float (input("Enter marks for maths:\n"))
s=float (input("Enter marks for science: \n"))

total=float(e+h+p+m+s)

#print(total);

per=float(total/500*100)
print("Percentage is: ",per)    

