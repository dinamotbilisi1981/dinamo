#////////////////////
print("hello world")

#//////////////////////////////////////

x = 5
y = "Hello"
z = 3.14
is_active = True
print(type(x))

#//////////////////////////////////////

#//////////////// listebi ordered mutable allows duplicates

fruits = ["apple", "banana", "cherry"]
print(fruits[1]) 
fruits.append("orange")
fruits[0] = "kiwi"
fruits.remove("banana")

#//////////////////////////////////////

for fruit in fruits:
    print(fruit)

#//////////////////////////////////////

squares = [x**2 for x in range(10)]

#//////////////////////////////////////

#///// ordered immutable allows duplicates

mytuple = ("apple", "banana", "cherry")
print(mytuple[1])

#////////////////////////////////////////
##////// unordered no duplicates
myset = {"apple", "banana", "cherry"}
myset.add("orange")
myset.remove("banana")

#////////////////////////////////////////
#/key-value pairs

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person["name"])