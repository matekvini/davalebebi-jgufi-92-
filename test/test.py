# 1 დავალება 1: ასაკის შემოწმება
# წესის მიხედვით, თუ მომხმარებლის ასაკი 18 წელზე მეტია ან 18 წლისაა (if age >= 18), სისტემა უშვებს მას საიტზე.
age = 18
if   age >= 18:
    print("u can go in ")
else :
    print("u cant go in")
2
# დავალება 1: შუქნიშნის ფერებიგვაქვს შუქნიშნის წესი:if ფერი არის "წითელი" $\rightarrow$ დაიბეჭდოს: "გაჩერდი"elif ფერი არის "ყვითელი" $\rightarrow$ დაიბეჭდოს: "მოემზადე"else $\rightarrow$ დაიბეჭდოს: "წადი"

color = "red"

if color == "red":
    print("stop")
elif color == "yellow":
    print("get ready")
else:
    print("go")

# 3

temp = 20

if temp > 30:
    print("its hot")
elif temp > 15:
    print("its warm")
else:
    print("its cold")

# elif წესის მიხედვით:if შეყვანილი პაროლი არის "1234" $\rightarrow$ დაიბეჭდოს: "შესვლა წარმატებულია"else (ნებისმიერი სხვა პაროლის შემთხვევაში) $\rightarrow$ დაიბეჭდოს: "არასწორი პაროლი"
pas = "1234"
if pas == "1234":
    print("login sucsess")
else:
    print("incorrect password")

# კითხვა:

# რა დაიბეჭდება ეკრანზე, თუ მომხმარებელი შეიყვანს პაროლს "7777"? (ამოქმედდება if თუ else?)
# ამოქმედდება else
# რა დაიბეჭდება, თუ შეიყვანს "1234"-ს?
# გამოიტანს წარმატებით  შესვლა

#  index
# გვაქვს სიტყვა: "PYTHON"შეახსენეთ თავს, რომ ინდექსაცია იწყება 0-იდან:[0] = 'P'[1] = 'Y'[2] = 'T'[3] = 'H'[4] = 'O'[5] = 'N':რომელი ასო იმყოფება index 3-ზე?   რა არის ასო 'P'-ს ინდექსი (რიგითი ნომერი)?
# 3 მე ინდექსზე არის H
# p intex aris 0

# რა სიტყვა გამოვა "nika"-სგან?
#  akin 
# რა გამოვა "GEORGIA"-სგან?
# aigroeg
cookie = 2.5
mikl = 1.5
print(cookie+mikl)