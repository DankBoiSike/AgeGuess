whit = True
while whit:
    print("I will guess your age.")
    orinumber = input("Think of a number from one to ten: ")
    orinumbers = int(orinumber)

    if orinumbers <= 10:
        math = orinumbers*2
        math4 = math+5
        math5 = math4*50
        ques = input("Did you already have your birthday this year? (type 'yes' or 'no'): ")
            
        if ques.lower() == "yes":
            math2 = math5 + 1769
            born = input("Enter your birth year: ")
            born = int(born)

            if born >= 1850 and born <= 3000:
                calc = math2 - born
                print("The first digit of the below  number is the number you thought of and the remaining two digits are your age!")
                print(calc)
                    
        if ques.lower() == "no":
            math3 = math5 + 1768
            born = input("Enter your birth year: ")
            born = int(born)

            if born >= 1850 and born <= 3000:
                calc = math3 - born
                print("The first digit of the below number is the number you thought of and the remaining two digits are your age!")
                print(calc)

            else:
                print("Type a valid answer!")

        else:
            print("Type a valid answer!")

    else:
            print("Type a valid answer!")
                

    


    
     


