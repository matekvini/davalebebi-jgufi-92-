
#2 მომხმარებელს შეაყვანიე 3 რიცხვი, ხოლო პროგრამამ დაბეჭდოს მათი საშუალო არითმეტიკული

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
avg = (num1 + num2 + num3) / 3
print("Average:", avg)

#3  მომხმარებელს შემოატანინე ორი რიცხვი და დაბეჭდე მათი ჯამი.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

# 4  input ფუნქციის საშუალებით შემოიყვანეთ თქვენი და თქვენი ოჯახის წევრების სახელები და დაპრინტეთ ერთი დიდი წინადადება კონკატენაციის სახით.
my_name = input("Enter my name: ")
mother_name = input("Enter mother name: ")
fathers_name = input("Enter father name: ")
print("my name is " + my_name +" my mother name is " + mother_name +" my father name is " + fathers_name )




#5  მომხმარებელს შემოატანინეთ მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ ინფორმაცია

city = input("Enter your city name: ")
district = input("Enter your discrict name: ")
building = input("Enter your building name: ") 
floor = input("Enter your floor name: ")
full_address = f"Address: {city}, {district}, Building {building}, Floor {floor}"
print(full_address)

#6  მომხმარებელს შემოატანინეთ ასაკი და ამოყენებითმსგავსი ფორმატის წინადადება დაბეჭდეთ "თქვენ ხართ [ასაკი] წლის"

age = int(input("Enter your age: "))
print(f"You are {age} years old.")