

def yearc():
    n=input ("Enter a year :")

    if len(n)==4:
        print("You have enter an year.")
        num = int(n)
        num=(num+100)
        print("You will turn 100 years in the year:" , num)
    else:
        print("You typed an age")
        cy=input("Enter current year:")
        num = int(cy)
        n=int(n)
        num = (100-n)
        num=(cy+num)
        print("You will turn 100 years in the year:", num)
yearc()