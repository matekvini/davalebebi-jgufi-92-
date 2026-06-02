# 2) ლოგიკური ოპერატორებისა და შედარების ოპერატორებზე შეადგინეთ 10 მაგალითი,5 მაგალითმა უნდა დააბრუნოს False და 5 მაგალითმა უნდა დაააბრუნოს True
#2
#true მაგალითები
num = False
print(num or True)
num = 11
print(num >10)
num = 12
print(num > 4)
num = 14
print(num > 6)
num = 15
print(num > 5)

#false მაგალითები 
x = False
print(x and True)
x = 5
print(x > 5)
x = 11
print(x > 11)
x = 12
print(x > 14)
x = 14
print(x >15)

# 3) კომენტარის სახით დაწერეთ თუ რა არის sequancing,iteration,selection აღწერე თითეული მათგანი თქვენი სიტყვებით

#sequancing არის კოდის შინაარსი რომელსაც პროგრამა მიყვება თანმიმდევრობით
#iteration არის შინაარსი რომეიც კოდს ეუბნება რომ გააგრძელოს რაღაცის კეთება სანამ პრიობა შესრულდება.
#selection არის პროგრამის უნარი მიიღოს გადაწყვეტილებები.

# 4) მოიყვანე sequencing ის მაგალითი,და კომენტარით მიუწერე რატომ არის შენს მიერ მოყვანილი მაგალითი sequence

price = 50
limit = 100
print(price < limit)  # ეს კოდი არის sequencing - ი რადგან კოდი კითხულობს ზემოდან ქვევით თანმიმდევრობით

#5 კომენტარის სახით ახსენით თუ რა არის for loop და რაში გვეხმარება ის

# for loop არის ციკლი და ის გვეხმარება რომ ერთი და იგივე კოდი არ ვწეროთ ბევრჯერ

#6) კომენტარის სახით ახსენით თუ რა გადაეცემა range() ფუნქციას და როგორ მუშაობს for loop
# range ფუნქციას ფრჩხილებში გადაეცემა არგუმენტები (რიცხვები), რომლებიც განსაზღვრავენ, თუ როგორ შეიქმნას ციფრების მიმდევრობა.
# for loop ციკლი მუშაობს მონაცემების ავტომატური „კონვეიერის მსგავსად ის იღებს ელემენტების კრებულს და ასრულებს ერთსა და იმავე მოქმედებას თითოეულ ელემენტზე, ერთმანეთის მიყოლებით, სანამ ბოლომდე არ მიაღწევს

#7 შენი დავალებაა ტერმინალში გამოიყანო საყვარელი ავტომობილის სახელი ტერმინალში გამოიყენე for loop

brand = "BMW"
for letter in brand:
    print(letter)
 
 # 8) შენი დავალებაა ტერმინალში გამოიტანო შენი გვარი 100 ჯერ

last_name = "kvinikadze"
for i in range(1, 101):
    print(last_name)

#9) შენი დავალებაა ტერმინალში გამოიტანო საყვარელი ფერი 46 ჯერ

fav_color = "black"
for i in range(46):
    print(fav_color)

#10) შენი დავალებაა ტერმინალში გამოიტანო შენი სახელის პირველი ასო 32 ჯერ
last_name = "K"
for i in range(32):
    print(last_name)


# გადამეორება

#11 
name = input("enter your name: ")
last_name = input("enter your last_name: ")
city = input("enter your city: ")

num1 = input("enter number: ")
print(name+last_name+city+num1)

# 12) შექმენი 4 ცვლადი,თითოეულში შეინახე განსხვავებული მონაცემთა ტიპები,შენი დავალებაა გაიგო ამ ცვლადებში შენახული მნიშვნელობის მონაცემთა ტიპი(გამოიყენე შესაბამისი ფუნქცია)
 
name = ("mate")
age = 23
pi = (3.14 )
adress = True

print(type(name))
print(type(age))
print(type(pi))
print(type(adress))

# 13) მომხმარებელს შემოატანინე 4 რიცხვი და ტერმინალში დააბრუნე ამ 4 რიცხვის ჯამი

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
num4 = int(input("Enter your fourth number: "))

print(num1+num2+num3+num4)