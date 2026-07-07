# შექმენი სია სახელელად my_list სადაც ჩაწერ შენს საყვარელ 3 ხილს და 2 რიცხვს len() ფუნქციის დახმარებით დათვალე რამდენი ელემენტისგან შედგება შენი სია

my_list = ["banana", "peach", "cherry", 12, 2]

my_list.pop(0)
my_list.insert(1, "banana")
my_list.append("apple")

print(len(my_list))
print("Final list:", my_list)


students = ["გიორგი", "ანა", "ლუკა", "მარიამ"]


print("საწყისი სია:", students)


students.append("დავითი")
students.append("ელენე")


students.insert(0, "ქალბატონი ნინო")

students.insert(3, "ნიკოლოზი")

print("განახლებული სია:", students)




num = [15, 40.2, 15, 5, 7, 10, 23, 15]
print(num)

print(num.count(15))

num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(num[::-1])  