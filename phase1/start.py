# This is a simple Python script to demonstrate basic data types and operations.
#Variables, lists, and basic operations are covered.
int = 3
print(int)

myfloat = 7.0
print(myfloat)
myfloat = float(8)
print(myfloat)

mystring = "Hello, World!"
print(mystring)

print("This is a string with a number: " + str(int))

print(int, mystring)

mylist = []
mylist.append(int)
mylist.append(myfloat)
mylist.append(mystring)

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print(second_name)
print("The second name on the names list is: " + second_name)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

    data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("You have successfully completed the exercise!")
else:
    print("There is still something wrong with your code. Please try again.")

prime = [2, 3, 5, 7]
for prim in prime:
    print(prim)
    
    #Dictionary example
    
    phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)