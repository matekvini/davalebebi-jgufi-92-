 
#2 კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.

# Input არის ნებისმიერი ინფორმაცია რომელიც ადამიანს შეჰყავს და კოდი  მაგალითად. კლავიატურიდან აკრეფილი ტექსტი მაუსის დაწკაპუნება, მიკროფონით ჩაწერილი ხმა.
# Output არის ნებისმიერი ინფორმცია რომელიც გამოდის და გამოაქვს შედეგი მაგალითად. მონიტორზე გამოსახული გამოსახულება დინამიკიდან გამოსული ხმა პრინტერით ამობეჭდილი ფურცელი და ასშ.



#3 

user_input = input("enter your name: ")
input_type = type(user_input)
print("data type:", input_type)



#4  
name = "mate"          # ინახავს ტექსტს (სახელს) - str
user_age = 25          # ინახავს მომხმარებლის ასაკს - int
product_price = 12.50  # ინახავს პროდუქტის ფასს - float
car_brand = "BMW"   # ინახავს ტექსტს (ბრენდს) - str
car_year = 2022    # ინახავს მანქანის ასაკს - int




#5 
car_model = "Tesla" # ინახავს ტექსტს - str
top_speed = 250      # ინახავს მთელ რიცხვს - int
acceleration = 3.1   # ინახავს ათწილადს - float

print("string:", car_model, "| type:", type(car_model))
print("integer:", top_speed, "| type:", type(top_speed))
print("float:", acceleration, "| type:", type(acceleration))

#6 

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
print(name + " " + last_name)



#7 

num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
num3 = int(input("enter your number: "))
num4 = int(input("enter your number: "))
num5 = int(input("enter your number: "))

print((num1 + num2 + num3 + num4 + num5) / 5)

 #8 

name = input('enter your name: ')
surname = input('enter your surname: ')
age = input('enter your age: ')
height = input('enter your heigh: ')
weight = input('enter your weight: ')

print(f'{name} {surname} is {age} years old {height} cm tall and weighs {weight} kg')