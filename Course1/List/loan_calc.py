#Loan Calculator
money_owed = float(input("How much money do you owe, in dollars\n")) #Get loan details. eg. £50,000
apr = float(input("What's the annual percentage rate of loan\n"))
payment = float(input("How much will you pay off each month in dollars\n"))
months = int(input("How many months do you want to see the results for\n"))
for i in range(0,months+1):
    monthly_rate = apr/100/12 
    interest_paid = money_owed*monthly_rate 
    money_owed = money_owed + interest_paid 
    money_owed = money_owed - payment 
    print('Paid', payment, 'of which',interest_paid,'was interest in month',i,end = "")
    print('Now I owe',money_owed)

