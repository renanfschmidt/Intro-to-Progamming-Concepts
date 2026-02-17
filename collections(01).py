name_1=(input("Give me the first name:\n"))
Gradelist_1=[]
Gradelist_1.append(int(input("Give me the first grade:\n")))
Gradelist_1.append(int(input("Give me the second grade:\n")))
Gradelist_1.append(int(input("Give me the third grade:\n")))
Gradelist_1.append(int(input("Give me the fourth grade:\n")))
Gradelist_1.append(int(input("Give me the fifth grade:\n")))
print("-"*50)
print(name_1)
def gradename():
 averagegrade = (Gradelist_1[0] + Gradelist_1[1] + Gradelist_1[2] + Gradelist_1[3] + Gradelist_1[4]) / len(Gradelist_1)
 return averagegrade
print("The average grade is ", gradename())
if gradename()>=90:
  print("You got an A")
elif gradename()>=80:
  print("You got a B")
elif gradename()>=70:
  print("You got a C")
elif gradename()>=60:
  print("You got a D")
else:
  print("You got an F")
