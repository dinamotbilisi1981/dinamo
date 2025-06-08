thislist = ["apple" , "watermalon" , "mrdachi", "banana" , "bachana" , "mrnikolozi" ]
print (thislist)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thisset = ("apple", "banana", "cherry ")
print(thisset)

thisdic = {"apple", "banana", "cherry"}
print(thisdic)

#//////////////////////////////////////////////

list1 = ["cherry", "apple", "banana"]
list2 = ["cherry 1", "apple 1", "banana 1"]

pliusoperatori = list1 + list2
print (pliusoperatori)

list1.extend(list2)
print (list1)


#///////////////////////////////////////////////////////////////

def find_min_max(ricxvi):
    
    return (min(ricxvi), max(ricxvi))

tuple1 = find_min_max((111, 3232, 123))
tuple2 = find_min_max((10, 3, 9))
tuple3 = find_min_max((13, 12, 21))

print("pirveli", tuple1)
print("meore", tuple2)
print("mesame", tuple3)


#/////////////////////////////////////////////////////////////

def find_longest_word(words):
    
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

thislist12 = find_longest_word(["apple", "banana", "cherry", "blueberry"])

print(thislist12)

#///////////////////////////////////////////////////////////////
def find_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


luwi = find_even_numbers(1,12,23,2,3,23,23,23,12)

print(luwi) 