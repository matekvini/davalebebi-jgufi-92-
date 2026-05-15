# 2 შექმენით ცვლადი სადაც შეინახავთ integer ტიპის მონაცემს, შემდეგ შეამოწმეთ თუ ეს რიცხვი რომელიც ცვლადში გაქვთ შენახული მეტია 10 ზე დაპრინტეთ "more than 10" სხვა შემთხვებაში დაპრინტეთ "less than 10"
x = 15
if x > 10: 
   print("number is more than 10 ")
else:
    print("less than10")

# 3 მომხმარებელს შემოაყვანინეთ რიცხვი, შემდეგ შეამოწმეთ თუ ეს რიცხვი უდრის 15 ს დაუპრინტეთ "equal to 15" სხვა შემთხვევაში დაუპრინტეთ "not equal to 15"

number = int(input("Enter a number: "))

if number == 15:
    print("equal to 15")
else:
    print("not equal to 15")

#   4 მომხმარებელს შემოატანეთ სტრინგი. შენი დავალებაა შეამოწმო, თუ მომხამრებლის მიერ შემოყვანილი სტრინგი არის group92 დაუპრინტეთ 'you are correct" სხვა შემთხვევაში დაუპრინტეთ "you are wrong"
user_input = input("Enter the group name: ")

if user_input == "group92":
    print("you are correct")
else:
    print("you are wrong")
# 5) დაატრიალეთ for ციკლი 50 დან 100 მდე 5 ის გამოტოვებით

for i in range(50, 101, 5):
    print(i)

# 6) for ციკლის დახმარებით გამოიტანეთ ტერმინალში თქვენი სახელი და გვარი

for i in range(10):
    print("mate kvinikadze")

# 7) while loop ის დახმარებით ტერმინალში გამოიტანეთ რიცხვები 20 დან 50 მდე

number = 20
while number <= 50:
    print(number)
    number = number + 1

# 8) დაბეჭდეთ 0-დან 100-მდე ყველა რიცხვი. (for-თაც და while-თაც)
for i in range(101):
    print(i)

i = 0  
while i <= 100:  
    print(i)
    i += 1  

# 9) დაბეჭდეთ 0-დან 100-ის ჩათვლით ყველა რიცხვი. (for-თაც და while-თაც)

for i in range(101):
    print(i)

i = 0
while i <= 100:
    print(i)
    i += 1

# 10) დაბეჭდეთ 10-დან 20-მდე ყველე რიცხვი (for-თაც და while-თაც)

for i in range(10, 21):
    print(i)

i = 10
while i <= 20:
    print(i)
    i += 1 

# 11) დაბეჭდეთ 100-დან 200-ის ჩათვლით ყოველი მე-5 რიცხვი (for-თაც და while-თაც)

for i in range(100,201,5):
    print(i)

i = 100
while i <= 200:
    print(i)
    i+=5

# 12) დაბეჭდეთ 10-დან 0-ის ჩათვლით ყველა რიცხვი (for-თაც და while-თაც)

for i in range(10,-1,-1):
    print(i)

i = 10
while i >= 0:
    print(i) 
    i-=1

# 13 მომხმარებელს შემოაყვანიეთ რაიმე რიცხვი(მთელი/ათწილადი); შეამოწმეთ ეს რიცხვი - 
  
number = int(input("Enter a whole number: "))

if number > 0:
    print("this number is positive")
elif number < 0:
    print("this number is negative ")
else:
    print("this number is 0 ")


# 14) მომხმარებელს შემოაყვანიეთ თავისი ასაკი:
# 0–12 წლის ასაკი --> დაპრინტეთ 'ბავშვი ხარ'
# 13-19 წლის ასაკი --> დაპრინტეთ 'მოზარდი/თინეიჯერი ხარ'
# 20-64 წლის ასაკი --> დაპრინტეთ 'ზრდასრული ხართ'
# 65-120 წლის ასაკი --> დაპრინტეთ 'ხანში შესული ხართ'
# 120 და ზემოთ --> დაპრინტეთ 'გურუ ან ჯადოქარი'
# თუ შემოყვანილი ასაკი უარყოფითია --> დაპრინტეთ 'არასწორი ინფო'


age = int(input("Enter your age: "))

if age < 0:
    print('Invalid info')
elif age <= 12:
    print('You are a child')
elif age <= 19:
    print('You are a teenager')
elif age <= 64:
    print('You are an adult')
elif age <= 120:
    print('You are a senior')
else:
    print('Guru or Wizard')


# 15) მომხმარებელს შემოატანიეთ სამი რიცხვი(მთელი/ათწილადი) და ამ სამი რიცხვთაგან დაბეჭდეთ უდიდესი

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# 16) შემოატანიეთ მომხმარებელს რიცხვი 1-დან 7-ჩათვლით
# თუ 1 --> დაპრინტეთ 'ორშაბათი'
# თუ 2 --> დაპრინტეთ 'სამშაბათი'
# თუ 3 --> დაპრინტეთ 'ოთხშაბათი'
# თუ 4 --> დაპრინტეთ 'ხუთშაბათი'
# თუ 5 --> დაპრინტეთ 'პარასკევი' 
# თუ 6 --> დაპრინტეთ 'შაბათი'
# თუ 7 --> დაპრინტეთ 'კვირა' 


day = int(input("Enter a number (1-7): "))

if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')

# 17) მომხმარებელს შემოატანინეთ რიცხვი, თუ ის მეტია 50-ზე დაბეჭდეთ ეს რიცხვი გამრავლებული 5-ზე, სხვა შემთხვევაში დაბეჭდეთ ეს რიცხვი კვადრატში.

number = float(input("Enter a number: ")) 

if number > 50:
    print(number * 5)
else:
    print(number ** 2)

# 18) მომხმარებელს შემოატანინეთ პაროლი თუ ის უდრის მაგალითად "goa123"-ს დაბეჭდეთ "Password is correct!", სხვა შემთხვევაში დაბეჭდეთ "Incorrect password!"


password = input("Enter your password: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")

# 19) მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ 1-დან შემოტანილის ჩათვლით ყველა რიცხვის ჯამი.

number = int(input("Enter a number: "))

total = 0
for i in range(1, number + 1):
    total = total + i  

print(total)
