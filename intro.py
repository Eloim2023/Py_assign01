print("Hello from Python")
#
name = "Eloim"
last_name = "Arreola"
age = 42
found = False

#if / else statements
if age < 100:
    print ("don't worry, you're still young")
elif age == 100:
    print("Congrats you're a century old")
else:
    print("Sorry, you're getting old")

print ("Im outside")

#function

def say_hello():
    print ("Hello there from the first kind of functions!")

def say_goodbye(name):
    print ("Goodbye" + name)

say_hello()
say_goodbye("Eloim")

#math

print(1+3)
print(1-2)
print(12*2)
print(20/4)

#concatenate

print("Hello my name is " + name + " and my age is " + str (age))

