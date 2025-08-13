name = input("ur name :")
science = int(input("Science Mark: "))
tamil  = int(input("Tamil Mark: "))
social = int(input("Social Mark: "))
maths = int(input("Maths Mark: "))
english = int(input("English Mark: "))

totalmark = (science+tamil+social+maths+english)
print("Your Total Mark :",totalmark)

Averagemark = (totalmark/5)
print("Your Average Mark :",Averagemark)

if(Averagemark>=50):
    print("Your Pass")
    if(Averagemark>=75):
        print(" Your Grade is A")
    elif(Averagemark>=60 and Averagemark<=75):
        print(" Your Grade is B")
    elif(Averagemark>=50 and Averagemark<=60):
        print(" Your Grade is C")
else:
    print("Your are Fail")