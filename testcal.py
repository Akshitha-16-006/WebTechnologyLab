from mymodule import Calculator

option=0
try:
    input1=float(input('Enter a number:'))
    input2=float(input('Enter a number:'))
    print('Enter 1 for add')
    print("Enter 2 for sub")
    print('Enter 3 for mul')
    print('Enter 4 for div')

    option=int(input('Enter option:'))
    c1=Calculator(input1,input2)

    if option==1:
        print(c1.add())
    elif option==2:
        print(c1.sub())
    elif option==3:
        print(c1.mul())
    elif option==4:
        print(c1.div())
except ValueError:
    print('Please enter a number')
    
