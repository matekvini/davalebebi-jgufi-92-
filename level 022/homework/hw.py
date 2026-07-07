# 2) კომენტარების სახით ახსენით თუ რა დანიშნულება აქვთ .append(); .insert() და .pop() ფუნქციებს.
# append ფუნქციის დანიშნულება არის ის რომ სიის ბოლოში ჩავამატოთ ახალი ელემენტი
# insert ფუნქციის დანიშნულებაა არის რომ კონკრეტულ ინტექსზე ჩავამატოთ ელემენტი
# pop ფუნქციის დანიშნულება არის ის რომ გარკვეული ელემენტი ამოვიღოთ ინდექსიდან

#  3) შექმენით რამდენიმე ელენტისგან შემდგარი სია, თქვენი დავალებაა დაბეჭდოთ ამ სიის სიგრძე, ანუ სიაში არსებული ელემენტების რაოდენობა.
arr = ["mate","nato","mariam","lia"]
count = len(arr)
print(count)

# 4) შექმენით ცარიელი სია სადაც მომხმარებელს 5-ჯერ შემოატანინენებთ რიცხვს, შემდეგ კი დაამატებთ მას სიის ბოლოში append() ფუნქციით.
numbers = []
for i in range(5):
    user_num = int(input("type number: "))
    numbers.append(user_num)
print("numbers", numbers)

# 5) მოცემულია სია:
# colors = ["red", "green", "blue", "yellow", "purple"]
# თქვენი დავალებაა სიიდან წაშალოთ ბოლო ელემენტი .pop() მეთოდის დახმარებით, შემდეგ კი დაბეჭდოთ განახლებული სია.
colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()
print(colors)

# 6) მოცემულია სია:
# animals = ["dog", "cat", "elephant", "lion"]
# თქვენი დავალებაა insert() მეთოდით ჩასვათ სიტყვა "monkey" სიაში მეორე პოზიციაზე, რის შემდეგაც დაბეჭდავთ განახლებულ სიას.

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1, "monkey")
print(animals)

# 7) შემქნით ცარიელი სია, სადაც 3-ჯერ input-ის სახით მომხმარებელს შეაყვანინებთ სამი სტუდენტის სახელს და დაამატებთ სიაში append() ფუნქციით. შემდეგ კი ჩასვით "Teacher" სიის თავში, წაშალეთ ბოლო სტუდენტი და დაბეჭდეთ სიის სიგრძე, ასვეე საბოლოო სია.

students = []

for i in range(3):
    name = input("Enter student name: ")
    students.append(name)

students.insert(0, "Teacher")

students.pop()
print(len(students))
print("Result:", students)
