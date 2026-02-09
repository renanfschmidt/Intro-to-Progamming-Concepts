import math
def area_circle(radius):
 area=math.pi*radius**2
 return round(area,2)
Answer=area_circle(int(input("Give me the radius of the circle:\n")))
print("The area for the circle is: ",Answer)

print(str("-"*50))

def tax_rate(money,tax):
 taxes = (money * tax/ 100)
 return money+taxes
money = int(input("How much money for the conversion:\n"))
tax = int(input("Whats the Tax percentage:\n"))
Answer_2= round(tax_rate(money,tax),2)
if money<=0:
 print("The money its not enough.")
else:
 print("The tax rate is ",Answer_2)

print(str("-"*50))

def fahrenheit_to_celsius(fahrenheit):
 celsius = (fahrenheit - 32) * (5/9)
 return celsius
Answer_3=round(fahrenheit_to_celsius(int(input("What is the temperature in fahrenheit:\n"))),5)
print("The temperature is ",Answer_3,"in celsius")