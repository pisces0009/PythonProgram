##############################################################
#	fILE: 	humberger3.py
#	Author:	Prasad Kale
#	Date:	january.20,2018
##############################################################

priceBigHugo		=3
priceDoubleCheese	=2
priceCheese			=1

noBigHugo		=input("\n Enter amount of Big Hugo burgers desired ==>")
noDoubleCheese	=input("\n Enter anount of Double Cheese burgers desired ==>")
noCheese		=input("\n Enter amount of Cheese burgers desired ==>")
amountGiven		=input("\n Enter dollar amount given by customer ==>")


costBigHugo			=int(noBigHugo)*priceBigHugo
costDoubleCheese	=int(noDoubleCheese)*priceDoubleCheese
costCheese			=int(noCheese)*priceCheese

total=costBigHugo + costDoubleCheese + costCheese

change = int(amountGiven) - total

print("\n the total cost of these burgers is $", total)
print("your change from", amountGiven,"dollars is $",change)
print("\t thank you \n \t Come again") 

#END PROGRAM

#################################################################################
OUTPUT:

C:\Users\PRASAD>python hamburger3.py

 Enter amount of Big Hugo burgers desired ==>3

 Enter anount of Double Cheese burgers desired ==>2

 Enter amount of Cheese burgers desired ==>1

 Enter dollar amount given by customer ==>100

 the total cost of these burgers is $ 14
your change from 100 dollars is $ 86
         thank you
         Come again

C:\Users\PRASAD>
##################################################################################