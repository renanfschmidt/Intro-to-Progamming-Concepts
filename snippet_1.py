with open("output.txt", "a") as db:
    a = "Hello" + str(1)
    b = "How do you do?"
    db.write(a + ", " + b + "\n")

def findTotal(a):
 for i in a:
  print(sum(i)*2)
findTotal([[5,10],[10,30]])

Hello1, How do you do?
