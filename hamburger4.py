##############################################################
#	fILE: 	humberger4.py
#	Author:	Prasad Kale
#	Date:	january.20,2018
##############################################################

priceBigHugo		=3.27
priceDoubleCheese	=2.50
priceCheese			=1.55

noBigHugo		=input("\n Enter amount of Big Hugo burgers desired ==>")
noDoubleCheese	=input("\n Enter anount of Double Cheese burgers desired ==>")
noCheese		=input("\n Enter amount of Cheese burgers desired ==>")
amountGiven		=input("\n Enter dollar amount given by customer ==>")


costBigHugo			=float(noBigHugo)*priceBigHugo
costDoubleCheese	=float(noDoubleCheese)*priceDoubleCheese
costCheese			=float(noCheese)*priceCheese

total=costBigHugo + costDoubleCheese + costCheese

change = float(amountGiven) - total

print("\n the total cost of these burgers is $", total)
print("your change from", amountGiven,"dollars is $",change)
print("\t thank you \n \t Come again") 

#END PROGRAM

############################################################################
OUTPUT:

C:\Users\PRASAD>python hamburger4.py

 Enter amount of Big Hugo burgers desired ==>1

 Enter anount of Double Cheese burgers desired ==>0

 Enter amount of Cheese burgers desired ==>1

 Enter dollar amount given by customer ==>10

 the total cost of these burgers is $ 4.82
your change from 10 dollars is $ 5.18
         thank you
         Come again

C:\Users\PRASAD>
###########################################################################