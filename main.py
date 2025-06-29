

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

# def getOutput():
#     a = int(input("Enter first number."))
#     b = int(input("Enter Second number."))
#     ot = int(input('Choose an options 1:ADD,2:SUBSTRACT,3:MULTIPLY,4:DIVIDE :'))

#     if ot == 1:
#         print( a+b)
#     elif ot ==2:
#         print( a-b)
#     elif ot ==3:
#         print( a*b)
#     elif ot ==4:
#         if(b != 0):
#             print( a/b)
#         else:
#             print('Cannot divide bt zero')
#     else:
#         print('Invalid option selected')
    
# getOutput()

# def getOutput(a,b):
#     c= int(input('Enter a number'))
#     d= int(input('Enter a number'))
#     def add(c,d):
#         z = a+b+c+d
#         return z
#     return add(c,d)
# print(getOutput(2,2)) 

# Day 22---------------------------------------------------



# if 7 in marks:
#     print("yes")
# else:
#     print("no")
# marks = [3,5,6,8,9,"bibek",True]

# # print(marks)
# # print(type(marks))
# # print(marks[len(marks)-1]) 
# # print(marks[1:4:2])

# lst = [i for i in range(20) if i%2 == 0]
# print(lst)
    
#append,sort,reverse,copy


# l = [1,2,3,4,6,11,34];

# # l.insert(1,899)
# m = [200,500,700]

# k = l+m

# print(k)

# names = ("hary","shyam","sonu","ram")
# number = (1,3,5)

# print(names)

# countries = ("Spain","Italy","Nepal","Australia")
# names1 = names[1:4]
# print(names1)
# temp = list(countries)
# temp.append("Russia")
# temp.append("bibek")
# temp.pop()
# temp[2] = 'Finland'
# countries = tuple(temp)



# print (countries)

# import time



# name = input("Enter your name : ")
# t = time.strftime('%H%M%S')
# hour = int(time.strftime('%H'))

# if(0<=hour<12):
#     print("Good Morning",name)
# elif(12 <= hour <17):
#     print("Good afternoon", name)
# elif(17<hour <24):
#     print("Good night", name)


# print (hour)
# name = input("Enter your Name: ")
# print("Welcome " + name + " to crore Pati Show.You can will multiple prizes and $$$")
# print("Here is your first Question....")
# print('1. How many eye does lion have?  \n1 = 4\n2 = 2\n3 = 5\n4 = 10')
# first_answer = int(input("Choose the correct answer : "))
# if(first_answer == 2):
#     print("You are correct. ✅")
#     print("Lets go to next question")
# else:
#     print("Plese try again later")
#     exit()





# questions = [
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",2],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",3],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",2],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#     ["What is the capital state of Australia","NSW","ACT","QLT","DARWIN",4],
#             ]

# levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]



# name = input("Enter your name ? ")
# print(f"Welcome to the quiz {name}. Here are your questions")

# for i in range(0,len(questions)):
#     question = questions[i]
#     print(f"Question for price of {levels[i]}")
#     print(question[0])
#     print(f"a.{question[1]}          b.{question[2]}")
#     print(f"c.{question[3]}          d.{question[4]}")
#     reply = int(input("Choose the correct answer (1-4)."))
#     if(reply == question[-1]):
#         print("Correct answer")
#     else:
#         print("Wrong answer")
#         break
    

# numbers = [1,23,4,5,6,7,6,543,2,34,56,543,2,345,65,432,3,456,543,2,34]

# fruits 

# for i in fruits:
#     print(i)


# shopping lists:

# shopping_list = [];

# for i in range(10):
#     print("\nOptions: 1. Add item  2. Show list  3. Remove item  4. Quit")
#     reply = int(input("choose options :"))
#     if(reply == 1):
#         item = input("Enter item to add: ")
#         shopping_list.append(item)
#     elif(reply == 2):
#         print(f"\n {shopping_list}"  )
#         for i,item in enumerate(shopping_list):
#             print(f"{i+1}. {item}")
#     elif(reply == 3):
#         item = input("Enter a item")
#         if item in shopping_list:
#             shopping_list.remove(item)
#             print(f"{item} is removed")
        
#     else:
#         print("Invalid Choice")
#         break
# print(shopping_list)
    

# def square(n):
#     '''
#     Takes in a number n, return the square of n
#     '''
#     print(n**2)
# square(5)
# print(square.__doc__)




# factorial

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(4))




















# shopping

# shopping_list = []

# print("Here are the shopping list you can choose to do!!")
# for i in range(2):
#     print("Choose an option")
#     print("add = 1, show-list = 2, delete = 3 ,exit = 4")
#     reply = int(input("Choose an option: "))
    
#     if(reply == 1):
#         list = input("Add an item : ")
#         shopping_list.append(list)
# print(shopping_list) 
    # 
    
    
    # Dictionaries 
# student = {
#         "name":"Bibek",
#         "age":25,
#         "course":"Python"
#     }

# car = {
#     "brand": "Toyota",
#     "model":"Corolla",
#     "year":2020
# }
# car["year"] = 2025
# car["owner"] = "Bibek"
# car["color"] = "red"

# if "model" in car:
#     print("Yes, model is one of the ky")
    
# else:
#     print("Donto print")

# print(car)
# print(car.values())

# students = {
#     "student1":{"name":"Bibek","age":25},
#     "student2":{"name":"Hira","age":15},
#     "student3":{"name":"Maan","age":35},
# }
# print(students['student1']["age"])

# person = {
#     "name":"Alex",
#     "city":"Canberra",
#     "age":22
# }
# person["age"] = 31
# person["job"] = 'chef'



# person.pop("city")
# for keys,value in person.items():
#     print(f"{keys} : {value}")
# # print(person)
# del person['name']
# print(person)

# For else loop---------------------------------

# for item in python:
#     # do somethings
#     if conditons:
#         break
# else:
#     # only run if loop donot break








# numbers = [1,2,3,4,6,7,8]

# for num in numbers:
#     if num == 5:
#         print('Found 5!')
#         break
# else:
#     print("5 not found")


# num = 110
# for i in range(2,num):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")


# items = [2,4,6,8]

# for i in items:
#     if i %2 != 0:
#         print(i)
#         break
# else:
#     print("All numbers are eve
names = ["Alice", "bob","Charlie","Alice"]
for i in range(len(names)):
    if names[i] in names[:i]:
        print(f'Duplicate found : {names[i]}')
        break
else:
    print("No duplicate found")