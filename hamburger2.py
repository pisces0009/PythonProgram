	##############################################################
#	fILE: 	humberger2.py
#	Author:	Prasad Kale
#	Date:	january.20,2018
##############################################################
	
	#cost of burgers
priceBigHugo		=3
priceDoubleCheese 	=2
priceCheese			=1

	#calc cost of burgers
costBigHugo			=2*priceBigHugo
costDoubleCheese	=2*priceDoubleCheese
costCheese			=2*priceCheese

	#calc total cost of all burgers
total = costBigHugo + costDoubleCheese + costCheese

	#calc change from $20
change = 20 - total

	#output cost and change
print("\n The total cost of these burgers is $",total)
print("your change from 20 dollars is $", change)
print("\t thank you \n \t come again")

#end program

#########################################################
#OUTPUT:

C:\Users\PRASAD>python hamburger2.py

 The total cost of these burgers is $ 12
your change from 20 dollars is $ 8
         thank you
        come again

C:\Users\PRASAD>
#########################################################