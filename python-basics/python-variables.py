#1
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#2
x = "John"
# is the same as
x = 'John'
#3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#4
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#5
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)