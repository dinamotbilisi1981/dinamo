print("Gamarjoba Hello world " + str(2342) + " daadeda")

x = 5
y = "mrdachi"
print (type(x))
print (x)
print (type(y))
print (y)

thislist = ["apple" , "watermalon" , "mrdachi", "banana" , "bachana" , "mrnikolozi"]
print (thislist)
print (thislist[1])
print (len(thislist))

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))

thisset = ("apple", "banana", "mr maxo")
print(thisset)

thisdict = {
    "brand" : ["Ford", "BMW"],
    "year" : 1964
}

print(thisdict["brand"][1], "-")

a = 13
b = 232
if b>a:
    print("B is big man")

arr = [123, 13123, 13231, 312312, 13221, 312312]

if 123 in arr:
    print("SHen es ar unda gcodnoda sworia")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x, end=" ")
    print(x[0], end=" ")

for x in "banana":
    print(x)

for x in fruits:
    for y in x:
        print(y, end=" ")

for x in fruits:
    print(x[0], end="")


print(123); print("test wertil mzdime ert xaze daweris uflebas gvazlvevs anu or xazis kods ertad vaertianebt")

for x in range(6):
    print(x)

for x in range(2, 30, 8):
    print (x)


#///////////////////////////////////////////////
def my_function(fname, lname="text"):
    print(fname + " " + lname)

my_function("email")


# es * aris masivi 
def myfunction1(*kids):
    print("Mr dachi " + kids[1])

myfunction1("dachi", "grdzelishvili", "me var dachovani")


