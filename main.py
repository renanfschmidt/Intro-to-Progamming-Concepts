print("Hello World")
#using the hashtag symbol is a way to make comments
print("Hello hows it going")

name="scooby"#variables unlike other languages dont have a type
#int(whole number), double(double the float) ,float(decimal number), char( characters ),string (words), boolean(true or false)
# == this is the value for equals
age = 23
temperature = 98.7
print("I am {} years old ,and the temparature is {} degrees".format(age,temperature))
#input
friendName = input("Whats your name?\n ")
print(friendName)
fage = int(input("Whats your friends age?\n "))
print(fage)
total = 56+78
print(total)
agesTotal = fage+age
print(agesTotal)
modulusTotal= 5 % 2
print(modulusTotal)

money= int(input("Whats your money?\n"))
movie_cost=14
if money>movie_cost:
    print("You can see the movie")
else:
    print("we cannot see the movie")
print("end program")
#! not equal to
#== equal to
#= assings to
lang="Python"
grade=85
match lang:
    case'Java':
        print("Java is working")
    case 'Python':
        print("Python is working")
    case 'C++':
        print("C++ is working")
    case 'C#':
        print("C# is working")
if (grade >=90):
    print("you got an A")
elif(grade>=80):
    print("you got an B")
elif(grade>=70):
    print("you got an C")
else:print("you failed")
print("end program")

#FUNCTIONS
#def printMessage():
    #print("I dont return a value")

#def sum(value1,value2):#parameters
    #answer=value1+value2
    #return answer
#num1=int(input("Give me the first number:"))
#num2=int(input("Give me the second number:"))
#answer= sum(num1,num2)
#arguments
#(MIDTERM QUESTION : WHATS THE PARAMETER AND WHATS THE ARGUMENTS)
#You define a function with parameters ,and call the function with the arguments
#The function can be called 0 to infinite times

#print(answer)

def convert(value1):
 converted_number=value1*2+3
 return converted_number
MyAnswer=convert(int(input("Give me the number:")))
print("The answer is ",MyAnswer)