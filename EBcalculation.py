Cno=int(input())
unit=int(input())
amt=0
Toatl=unit*amt
if(unit>=1 and unit<=20):
    amt=3
    Total=unit*amt
    print("       EB BILL     ")
    print("consumer no    :",Cno)
    print("Consumed Unit  :",unit)
    print("price per unit :",amt)
    print("Total Amount   :",Total)
elif(unit>=21 and unit<=40):
    amt=7
    Total=unit*amt
    print("       EB BILL     ")
    print("consumer no    :",Cno)
    print("Consumed Unit  :",unit)
    print("price per unit :",amt)
    print("Total Amount   :",Total)
elif(unit>=41 and unit<=100):
    amt=15
    Total=unit*amt
    print("       EB BILL     ")
    print("consumer no    :",Cno)
    print("Consumed Unit  :",unit)
    print("price per unit :",amt)
    print("Total Amount   :",Total)
