# 1) შექმენით ფუნქცია სახელად greet, რომელიც დაბეჭდავს მისალმების ტექსტებს. "Hello World!" და "Hello {name}def greet(name="World"):

def greet(name):
    print("Hello World!")
    print(f"Hello {name}")
greet("mate")
# 2) შექმენი ფუნქცია double, რომელიც მიიღებს პარამეტრად 1 ცალ რიცხვს და თქვენი დავალებაა დააბრუნებინოთ ამ ფუნქციას აკვადრატებული რიცხვი.

def double(num):
    return num * num
print(double(5))

# 3) შექმენი ფუნქცია checkOdd, რომელიც მიიღებს პარამეტრად 1 ცალ რიცხვს და თქვენი დავალებაა დააბრუნებინოთ ფუნქიას "ლუწი" თუ რიცხვი ლუწია, და "კენტი" თუ კენტია.
def checkOdd(num):
    if num % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

print(checkOdd(4))
print(checkOdd(7))

# 4) შექმენი ფუნქცია BMI, რომელიც პარამეტრად მიიღებს 2 ცალ რიცხვს (height, weight), თქვენი დავალებაა დააბრუნოთ ამ ადამიანის BMI --> formula: weight / (height * height)


def BMI(height, weight):
    return weight / height**2


print(BMI(1.75, 70))

# 5) შექმენი ფუნქცია getNameByUpper, რომელიც პარამეტრად მიიღებს მომხმარებლის სახელს. თქვენი დავალებაა ფუნქციაში დააბრუნოთ მომხმარებლის საწყისი სახელი მაღალ რეგისტრში (upperCase). ფუნქციას არგუმენტად გამოძახებისას გადაეცით input-ის მეშვეობით შემოტანილი მომხმარებლის სახელი.

def getNameByUpper(name):
    return name.upper()

user_name = input("type name: ")
print(getNameByUpper(user_name))