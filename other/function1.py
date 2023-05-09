#function

def test(name):
	print("hello "+name+"! welcome to python class")
	
#normal function calling
"""
test(".")
test("reetu")
test("PK")
test("ram")"""

#using for loop calling fucntion and taking input

for i in range(1,5):
        test(input("Enter you name:"))