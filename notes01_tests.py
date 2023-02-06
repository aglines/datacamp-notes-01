# test notes

# math
x = 5
y = "jag kan kör"
z = 'now we drive'
a_float = 3.3

y_more = y + y
print(y_more)

print(type(z))

###### types

x = 5.5
type(x)

str(x)

print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

pi_float = float(pi_string)

###### CONVERT TYPES

x = 6
str(x)

y = 4.4
int(y)

z = True
str(z)
# can you FLOAT a boolean?
    # yes it goes to 0.0 or 1.0


##################################  LISTS

listABC = ["a", "b", "c"]

list2 = ["listhere", 37, False, ["another", "list"] ]

############## SUBSETS OF LISTS

fam = [ "personA", 5, "person_andra", 10, "BarnAgain", 15 ]
fam_subset = fam[0:2]

x = ["null", "one", "two", "three"] ; print(x)
#   ['null', 'one', 'two', 'three']
print (x[0:2])
#   ['null', 'one']
print (x[0:])
#   ['null', 'one', 'two', 'three']
print (x[1:])
#   ['one', 'two', 'three']
print (x[1:-1])
#   ['one', 'two']


####### list slice practice
x = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(x[2][1])
print(x[2][:2])



