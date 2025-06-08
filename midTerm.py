
num = 1

while num <= 50:
    if num % 3 == 0:
        print(num)
    num +=1


print("#################################")


############################################

fruits = ["Apple", "Banana", "Cherry", "WaterMelon", "Kiwi"]
fruits[1] = "Blueberry"
fruits.append("Pineapple")

for fruit in fruits:
    print(fruit)


print("#################################")

############################################

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Mr dachovani")
greet("nika", "ra kargi dgea :)")
greet("giorgi", "gaumarjos")

print("#################################")
############################################

people = {
    "dachi": 20,
    "nika": 55,
    "bachana": 107,
    "giorgi": 6,
    "mari": 19
}

def b(per):
    return [name for name, age in per.items() if age == max(per.values())][0]

print(b(people))


print("#################################")
#########################################################33

class Animal:
    def name(self):
        print("ეს ცხოველია")
    
    def sound(self):
        print("ხმა")

class Cat(Animal):
    def sound(self):
        print("Meow!")

a = Animal()
a.name()
a.sound()

c = Cat()
c.name()
c.sound()

print("#################################")
#################################################

product = lambda x, y: x * y

def datvla(pairs):
    return [product(x, y) for x, y in pairs]

number_pairs = [(2, 3), (4, 5), (6, 7)]
print(datvla(number_pairs))  

print("#################################")

###################################################


