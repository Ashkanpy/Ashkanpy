def func(num1,num2,num3):
    if (num1>num2 and num1>num3):
        x=num1
        print(x," is biggest")
    elif (num2>num1 and num2>num3):
        x=num2
        print (x," is biggest")
    elif (num3>num1 and num3> num2):
        x=num3
        print (x," is biggest")
    else:
        print ("some of numbers are equal") 
func (1,3,4)