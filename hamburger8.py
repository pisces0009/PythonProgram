##############################################################
#	fILE: 	humberger8.py
#	Author:	Prasad Kale
#	Date:	january.24,2018
#	Purpose: Nested if statement
##############################################################

# print headings
print("\n ... Hamburger 8 ....")
print("======================\n")

	#prompt uses for order
qty			= input("\n Enter the number of hamburgers desired ==> ")
hamburgerType = input("\nType? Enter C for cheese, P for plain, or D for double ==> ")

	#determine cost of hamburgers
if hamburgerType =='C' or hamburgerType =='c':
	cost = 2.79
else:
	if hamburgerType == 'P' or hamburgerType == 'p':
		cost = 2.05
	else:
		if hamburgerType =='D' or hamburgerType == 'd':
			cost = 3.59
		else:
			print("Wrong type!Run again!")
			cost = 0.0
		#endif
	#endif
#endif
	#calc total
total = cost * float(qty)
	#output total cost
print("\nTotal cost is==>",total)

	#prompt user for amount tended
amtGiven = input("\nEnter amount tended ==>$")

	#calc and print change
change = float(amtGiven) - total
print("\nYour change is ==>$",change)
print("\n...end of job...\n")
#end main
################################################################
OUTPUT:

C:\Users\PRASAD>hamburger8.py

 ... Hamburger 8 ....
======================


 Enter the number of hamburgers desired ==> 10

Type? Enter C for cheese, P for plain, or D for double ==> p

Total cost is==> 20.5

Enter amount tended ==>$50

Your change is ==>$ 29.5

...end of job...


C:\Users\PRASAD>hamburger8.py

 ... Hamburger 8 ....
======================


 Enter the number of hamburgers desired ==> 1

Type? Enter C for cheese, P for plain, or D for double ==> c

Total cost is==> 2.79

Enter amount tended ==>$10

Your change is ==>$ 7.21

...end of job...
####################################################################