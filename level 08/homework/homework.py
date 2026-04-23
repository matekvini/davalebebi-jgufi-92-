
# 2 კომენტარების სახით ჩამთვალეთ ყველა შედარებითი ოპერატორები და გააკეთეთ 5-5 ნაგალითი თითოეულზე.

# შედარებითი  ოპერატორები.  ტოლია თუ არა, (==) უთანაბრობა  (!= ), მეტობა, > ნაკლებობა,(<) მეტობა ან ტოლობა, ( >= )  ნაკლებობა ან ტოლობა ( <= )

# 1
score1 = 100
score2 = 200
print(score1 == score2)
# 2 
score3 = 100
score4 = 400
print(score3 == score4)
# 3 
score5 = 500
score6 = 400
print(score5 == score6)  

# 4
score7 = 600
score8 = 100
print(score7 == score8 )

#5 
score9 = 700
score10 = 700
print(score9 == 800)

# უტოლობის მაგალითები 

#1
x = 10
y = 20
print(x != y)

#2
x = 11
y = 14
print(x != y)

# 3 
x = 14
y = 22
print(x !=y)

# 4
x = 11
y = 22
print(x!=y)

# 5 
x = 12
y = 21
print(x!=y)

# ნაკლებობის მაგალითები 

# 1
score1 = 500
score2 = 1000
print(score1 < score2)

# 2
score2 = 300
score3 = 400
print(score2 < score3)

# 3

score4 = 22
score5 = 25
print(score4 < score5)

# 4
score6 = 11
score7 = 22
print(score6 < score7)

# 5 
score8 = 19
score9 = 21
print(score8 < score9)

# #მეტობის მაგალითები 

# 1 
a = 5
b = 15
print(a > b)
# 2
a = 2
b = 13
print(a > b)

# 3
a = 3
b = 11
print( a > b)

# 4
a = 4
b = 5
print(a > b)

#5
b = 6
a = 8
print(b > a)

# მეტობის ან ტოლობის მაგალითები 

# 1
a = 20
b = 15
print(a >= b) 

#2
a = 20
b = 16
print(a >= b)

#3
a = 21
b = 16
print(a >= b)

#4
a = 22
b = 11
print(a >= b)
#5
a = 22
b = 11
print(a >=b)

# ნაკლებობის ან ტოლობის მაგალითები
# 1
x = 20
y = 20
print(x <= y)
#2

# x = 20
y = 22
print(x <= y)
3
x = 21
y = 23
print(x <= y)
#4
x = 22
y = 24
print(x <= y)
#5
x = 23
y = 25
print(x <= y)

# #3 კომენტარის  სახით ახსენით რა არის logical operators  რა შედეგს გვიბრუნებს
# # -------------------------------------------------------------
# # (Logical Operators) პროგრამირებაში გამოიყენება რამდენიმე პირობის ერთმანეთთან დასაკავშირებლად. 
# #მათი დახმარებით კომპიუტერი იღებს გადაწყვეტილებას: არის თუ არა მთლიანი გამოსახულება ჭეშმარიტი (True) თუ მცდარი (False).


# მაგალითი 1:  AND 
print(10 > 5 and 20 > 15)
# მაგალითი 2: 
print(10 > 5 and 20 < 15)  

# მაგალთი 1  OR 
print(10 > 5 or 20 < 15)
# მაგალითი 2 
print(10 < 5 or 20 < 15)

# and — "ორივე ერთად" ეს ოპერატორი ძალიან "მომთხოვნია". ის მხოლოდ მაშინ გვაძლევს True-ს, თუ ყველა პირობა სწორია.
# #or  ეს ოპერატორი უფრო მეგობრულია. ის გვაძლევს True-ს, თუ ერთი პირობა მაინც შესრულდა.

#4 გააკეთეთ 3-3 მაგალითი logical operator-ებზე.

print(True and True)
print(True and False)
print(False and True)

print(True or False)
print(False or True)
print( False or False)


#5 მომხმარებელს შემოატანინეთ რიცხვი, შეინახეთ იგი ცვლადში და შეადარეთ იგი მეტია თუ არა თქვენს მიერ წინასწარ გამზადებულ რიცხვზე.
user_num = 50
user_input = int(input("type any number: "))
print(user_input > user_num)

# 6  მომხმარებელს შემოატანინეთ სახელი, შეინახეთ იგი ცვლადში და მკაცრად შეამოწმეთ უდრის თუ არა იგი თქვენს სახელს.

user_name = input("enter your name:")
print(user_name == "mate")

#7 მომხმარებელს შემოატანინეთ თავისი ასაკი, შეინახეთ იგი ცვლადში და შეამოწმეთ მეტია თუ არა იგი 18.

age = int(input("Enter your age: "))
print(age > 18) 