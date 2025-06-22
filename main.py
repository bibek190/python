

# print(a+a1)
# print("The type of a is ",type(a))
# print("The type of b is ",type(b))
# print("The type of c is ",type(c))

# list1 = [8,2.3,[-4,5],["apple",'banana']]
# print(list1)

# tuple1 = (("parrot","sparrow"),("lion","tiger"))
# print(tuple)

# dict1 = {"name":"Bibek","age":20,"canVote":True}
# print(dict1)
# Day 8 ----------------------------------------------
# a= int(input('Enter first  number '));
# b= int(input('Enter second  number '));

# print("The value of ",a ,'+',b,"is ",a+b);
# print("The value of ",a ,'-',b,"is ",a-b);
# print("The value of ",a ,'%',b,"is ",a%b);
# print("The value of ",a ,'*',b,"is ",a*b);

# Day 9 ---------------------------------------------------------------------------------

# a = '1'
# b = '2'
# print(int(a)+int(b))

# name = input("Enter your name: ")
# last_name = input("Enter your last name:")
# print("Welcome to my snake world,", name + last_name)
# input("Do you want to go further?")


# def add(num1,num2):
#     return num1+num2

# result = add(2,1);

# if result == 4:
#     print("Hey you are 4")
# elif result == 10:
#     print("Hey you are 10")
# else:
#     print("Error")



# -------------------------Day2------------------------------------

# name = "Bibek"
# friend = "Rohan"
# anotherFriend = "Lovish"
# apple = '''he wants to have an apple
#             dfsdfdsfdsfsdfsdf'''

# fruit = "Mango"
# mangolen = len(fruit)
# print(mangolen)
# print(fruit[-3:-1])


# # Quiz:
# nm = "Harby"
# print(nm[-6:-5])

# -------------strings are immutable-------------
# a = '!!Bibek!!!!! !!!harry!! !!thaapa!!'

# name = a.upper()
# nameLower = a.lower()
# print(len(a))
# print(name)
# print(nameLower)
# print(a.strip("!"))
# print(a.replace("Bibek","John"))
# print(a.split(" "))

# blogHeading = "introduce to THE js"
# print(blogHeading.capitalize())

# str1 = "Welcome to the goldCoast couples"
# # print(len(str1))
# # print(len(str1.center(50)))
# print(str1.count("e"))

# name = input("Enter your name?")

# if name == "Bibek":
#     print("Welcome boss")
# elif name == "Rubisha":
#     print("Welcome boss's Wife")
# else:
#     print("Welcome to home " + name )

# a = int(input("Enter your age?"))
# print("Your age is: ", a)

# if(a>=18):
#     print("Welcome to the pub. Enjoy the day")
# elif(a<=18):
#     print("Sorry, not allowed")

# import time;

# print(time.strftime('%H:%M:%S'))

# hour = int(time.strftime('%H'))



# name = input("Enter your name?")
# print("Welcome to our country." + name)


# if(hour >12):
#     print('Have a great evening')
# elif(hour < 12 ):
#     print("Good Morning, have a good day. ")
# elif(hour == 12):
#     print("Good Evening")



# print("Hello world from ...")
# x = 2

# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("x is 4")
#     case 5:
#         print("x is 5")
#     case _ : 
#         print(x)
        
# x = int(input("Enter a number"))      
        
# match x:
#     case _ if x !=90:
#         print("x is zero")
#     case 4:
#         print("x is 4")
#     case 5:
#         print("x is 5")
#     case _ : 
#         print(x)

# x = [1,2,3,4,5,6,7,8]
# x = 'abishebk'
# for i in x :
#     print(i,end =",")
#     if(i == "b"):
#         print("This is something special")

# colors = ["red","green","blue","yellow"];
# for color in colors:
#     print(color)
#     for letters in color:
#         print(letters)
    
# count = 5
# while(count > 0):
#     print(count)
#     count = count -1
# else:
#     print("Inside else,Loop ended")

# for i in range(15):
    
#     if(i == 10):
#         print("Skip the iteration")
#         continue
#     print("5 X", i,"=", 5*i)
# print("Loop ended")
# i= 0
# while True:
#     print(i)
#     i = i+1
#     if(i%100 == 0):
#         break
#     print('Happening')

# i = 0;
# while True:
#     print(i)
#     i = i+1
#     if(i%100 == 0):
#         break
#     print("in Loop")
# print('Outta loop')


# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def isGreater(a,b):
#     if(a>b):
#         print('First number is greater')
#     else:
#         print('Second number is greater or equal')   

# def isLesser(a,b):
#     pass

# def average(a,b = 5):
#     print("The average is ", (a+b)/2)
    
# average(5)


# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     return sum/len(numbers)

# c = average(10,2,3,4)
# print(c)

# -----------------------------Start with 22 lesson-------------

def getOutput():
    a = int(input("Enter first number."))
    a = int(input("Enter Second number."))
    ot = input('Choose an options 1,2,3,4 :')

    if ot == 1:
        print( a+b)
    if ot ==2:
        print( a-b)
    if ot ==3:
        print( a*b)
    if ot ==4:
        print( a/b)
    else:
        print(ot)
    
getOutput()