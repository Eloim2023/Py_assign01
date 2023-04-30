#list
color = ["yellow", "black", "blue", "green", "yellow"]

#add 
#color.append("pink")

#color.remove("pink")
#get any elements

print(color)

#travel the list of elements 
# for(i=0;i<list;i++)
#     let temp = list[i];
#     console.log(temp)
for travel in color:
    print(travel)
    
#dictionary 
me ={
    "first_name":"Adrian",
    "last_name":"Rodriguez",
    "age":"36"
}
print(me)
print(me["first_name"])
#modify the dictionary
me["age"] = 50
print(me)

# add 
me["color"]= "blue"
print(me)
print("hello from python")
#
name = "Eloim"
last_name = "Arreola"
age = 101
found = False

#if /else statements
if age < 100:
    print("don't worry, youre still young")
elif age == 100:
    print("Crongrats youre a century old")
else:
    print(" Sorry, youre getting old")
    
print("Im outside")

#function
def say_hello():
    print("Hello there from the first kind of functions!")
    
def say_goodbye(name):
    print("Goodbye" + name)
    
say_hello()
say_hello()
say_goodbye("Jorge")

# math
print(1+3)
print(1-2)
print(12*2)
print(100/2)

#concatenate
print("Hello my name is " + name +"and my age is " + str(age))