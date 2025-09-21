expenses = []
n = int(input("How many expenses will you need "))
for i in range(0,n+1):
    expense = float(input("Enter expense: "))
    expenses.append(expense)
print(expenses)
print("Total: " + str(sum(expenses)))
