##############################################################
#	fILE: 	humberger5.py
#	Author:	Prasad Kale
#	Date:	january.24,2018
#	Purpose	Post-test loop
##############################################################

# initialize character variable answer to character value 'y'
answer = 'Y'		# initialize variable ans to char 'Y'

# print headlines
print("\n... Hamburger 5  Post-test Loop..")
print("==================================\n")

# post-test loop
while True:
	# input order and amount received from customer
	noBigHugo = input("\nEnter amount of Big Hugo Burgers desired ==>")
	noDoubleCheese = input("\nEnter amount of Double Cheese burgers desired ==>")
	noCheese = input("\n Enterb amount of Cheese burgers desired ==>")
	amtGiven = input("\n Enter dollar amount given by customer ==>$")
	
	#constant declaration
	priceBigHugo 		= 3.27
	priceDoubleCheese 	= 2.50
	priceCheese			= 1.55
	
	#calc cost of burgers
	costBigHugo		=float(noBigHugo)*(priceBigHugo)
	costDoubleCheese=float(noDoubleCheese)*(priceDoubleCheese)
	costCheese		=float(noCheese)*(priceCheese)
	
	#calc total cost of all burgers
	total = costBigHugo + costDoubleCheese + costCheese
	
	#calc change from 20 dollars
	change = float(amtGiven)-total
	
	#output cost and change
	print("\n The total cost of these burgers is $",total)
	print("\n Your change from ",amtGiven,"dollars is $",change )
	
	#prompt the user for more orders
	answer = input("\n Do again ?(Y/N)")
	if answer =='Y' or answer =='Y':break #endif 
	#end while loop
	print("\n....end of job....\n")
	#end main
##########################################################################
OUTPUT:
	
C:\Users\PRASAD>hamburger5.py

... Hamburger 5  Post-test Loop..
==================================


Enter amount of Big Hugo Burgers desired ==>2

Enter amount of Double Cheese burgers desired ==>1

 Enterb amount of Cheese burgers desired ==>1

 Enter dollar amount given by customer ==>$30

 The total cost of these burgers is $ 10.59

 Your change from  30 dollars is $ 19.41

 Do again ?(Y/N) Y

....end of job....


Enter amount of Big Hugo Burgers desired ==>2

Enter amount of Double Cheese burgers desired ==>2

 Enterb amount of Cheese burgers desired ==>2

 Enter dollar amount given by customer ==>$40

 The total cost of these burgers is $ 14.639999999999999

 Your change from  40 dollars is $ 25.36

 Do again ?(Y/N) n

....end of job....
##########################################################################
