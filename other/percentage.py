#taking input form user:

n = str(input("Enter your name: "))
q = int(input("\nWhat do you want to do today?\n1. Addition\n2. Percentage\n"))

if q == 1:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    z = x + y
    print("The sum of", x, "and", y, "is", z)
elif q == 2:
    e = float(input("Enter marks for English: "))
    h = float(input("Enter marks for Hindi: "))
    p = float(input("Enter marks for Punjabi: "))
    m = float(input("Enter marks for Maths: "))
    s = float(input("Enter marks for Science: "))
    total = e + h + p + m + s
    per = float(total/500*100)
    print("The percentage is:", per)
else:
    print("Invalid input! Please enter either 1 or 2.")
 


"""
#how to check percentage,

print("Hello Students:\n")
print("please enter your marks as per below:\n")
e=float (input("Enter marks for english: \n"))
h=float (input("Enter marks for hindi: \n"))
p=float (input("Enter marks for  punjabi: \n"))
m=float (input("Enter marks for maths:\n"))
s=float (input("Enter marks for science: \n"))

total=float(e+h+p+m+s);

#print(total);

per=float(total/500*100)
print("Percentage is: ",per)

#practice program

a=int(input("\n enter value for a:"))
b=int(input("\n enter value for b:"))

total=int(a+b);

print(total);"""