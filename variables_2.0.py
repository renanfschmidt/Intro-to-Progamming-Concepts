
def outputFunction(answer):
    print("The answer is",answer)
continueLoop = True
calculation=0
while continueLoop:
    var1=int(input("Give me the first number:"))
    var2=int(input("Give me the second number:"))

    if calculation==0:
        answer=var1*var2
    elif calculation==1:
        answer=var1/var2
    elif calculation==2:
        answer=var1//var2
    elif calculation==3:
        answer=var1%var2
    elif calculation==4:
        answer=var1+var2
    elif calculation==5:
        answer=var1-var2
        continueLoop=False

    outputFunction(answer,)
    calculation=calculation+1