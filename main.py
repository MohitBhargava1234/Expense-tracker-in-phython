# Expense Tracker Project
expenses=[]#list of expenses in form of dictionary
print("Welcome to Expense Tracker : Kharcha Soch Samjh ke Kiya Karo!!")
while True:
    print("|<====Menu====>|")
    print("1. Add Expense")
    print("2. View all Expense")
    print("3. View total Expense")
    print("4. Exit")

    choice=int(input("Please Enter Your Choice: ")) 

#add expense
    if(choice == 1):
        date=input("Enter the Date of Expense :")
        category=input("Enter the category of Expense: like (food, clothing, tech, books etc...)")
        description=input("enter more about category...")
        amount=float(input("Enter the Amount :"))
        expense={
             "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenses.append(expense)
        print("\n Expense Added Successfully... ")

#View all expenses
    elif(choice == 2):
        if (len(expenses)==0 ):
            print("No Expenses Found !!")
        else:
            print("Here is Your All Expenses...")
            count= 1
            for eachexpense in expenses:
                print(f"Expense number {count} ->{eachexpense["date"]} , {eachexpense["category"]} , {eachexpense["description"]} , {eachexpense["amount"]}")
                count=count+1

# veiw total spending
    elif(choice == 3):
        total=0
        for eachexpense in expenses:
            total=total + eachexpense["amount"]

        print("Your Total Expense is =",total)


 #exit
    elif(choice == 4):
        print("Thank You For Using My Expense Tracker...")
        break

    else:
        print("INVALID CHOICE!! Try Again ")
