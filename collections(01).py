name_1=(input("Give me the first name:\n"))
Gradelist_1=[]
Gradelist_1.append(int(input("Give me the first grade:\n")))
Gradelist_1.append(int(input("Give me the second grade:\n")))
Gradelist_1.append(int(input("Give me the third grade:\n")))
Gradelist_1.append(int(input("Give me the fourth grade:\n")))
Gradelist_1.append(int(input("Give me the fifth grade:\n")))
averagegrade=(Gradelist_1[0]+Gradelist_1[1]+Gradelist_1[2]+Gradelist_1[3]+Gradelist_1[4])/len(Gradelist_1)
print("-"*50)
print(name_1)
print("The average grade is ",averagegrade)
if averagegrade>=90:
 print("You got an A")
elif averagegrade>=80:
 print("You got a B")
elif averagegrade>=70:
 print("You got a C")
elif averagegrade>=60:
 print("You got a D")
else:
 print("You got an F")