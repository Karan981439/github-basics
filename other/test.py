#Creating a list;

car=['audi','ford','BMW','porch']
name=['reetu','PK','RAM','amit']
price=['2000','3000','233','10']

#acess the list;/mldf

print(name[0:3],"took",car[0:3],"at Price",price[0:3])

#replace/update the items from list;

car[1]= "glanza"
print(car) 

#adding item:

car.insert(4,"auto")
print("updated  list",car)

#delete 
del price[3]
print(price)

#pop
name.pop()
print(name)

print(car)
car.pop(4)
print(car)

#remove
print(name)
name.remove('PK')
print(name)

