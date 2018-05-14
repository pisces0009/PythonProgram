##############################################################
#	fILE: 	humberger7.py
#	Author:	Prasad Kale
#	Date:	january.24,2018
#	Purpose:Calculating cost or burgers, drinks and french fries
##############################################################

# print headings
print("\n ... Hamburger 7 ....")
print("======================\n")


	#declaration of price constant
costHamburger	=1.75
costCheese		=0.55
costDrink		=0.99
costFrenchFries	=1.55
	
	#i/p order and amount received from customer
noHamburgers = input("\n enter amount hamburgers desired==>")
cheese		= input("\nDo you want cheese on it?(Y/N)==>")
	
#decide weather cheese is required
if cheese == 'Y' or cheese == 'y':
	noCheeses = input("\nHow many with cheese?,0 for none ==>$")
else:
	noCheeses = 0
	#endif
	
#input number of drinks and fries
noDrinks	 =input("\nEnter amount of drink desired,0 for none ==>$ ")
noFrenchFries=input("\nEnter the number of french fries desired, 0 for none ==>$")
	
#calc cost of hamburgers	
hambCost = float(noHamburgers) * costHamburger
print("....cost of burger is $",hambCost)

#add cost of cheese	
cheeseCost = float(noCheeses) * costCheese
print("....cost of cheese is $",cheeseCost)
	
#add cost of drinks	
drinkCost = float(noDrinks) * costDrink
print("....cost of drink is $",drinkCost)
	
#add cost of french fries
ffCost = float(noFrenchFries) * costFrenchFries
print("....cost of french fries is $",ffCost)
	
totalCost = hambCost + cheeseCost + drinkCost + ffCost
print("....total cost is $",totalCost)

#input payment amount
amtGiven = input("\nAmount tended:$")
	
#calculate change
change = float(amtGiven) - totalCost
	
#output change
print("\n your change from", amtGiven,"dollars is $", change)
	
print("\n....end of job...")
	
	#end main
#########################################################################################
OUTPUT:
#########################################################################################
C:\Users\PRASAD>hamburger7.py

 ... Hamburger 7 ....
======================


 enter amount hamburgers desired==>10

Do you want cheese on it?(Y/N)==>y

How many with cheese?,0 for none ==>$10

Enter amount of drink desired,0 for none ==>$ 10

Enter the number of french fries desired, 0 for none ==>$10
....cost of burger is $ 17.5
....cost of cheese is $ 5.5
....cost of drink is $ 9.9
....cost of french fries is $ 15.5
....total cost is $ 48.4

Amount tended:$50

 your change from 50 dollars is $ 1.6000000000000014

....end of job...
#########################################################################################