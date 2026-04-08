#ES main function 

#Liam imports the init csv class with the file path 

#BG from every file needed to be imputed input/bring in all/everything onto this file
#from BG_code file import enter new account
#from budgeting_&_savings file import all functions
#from login_logout file import all
#from randm_password_generator file import all


#make a function called main 

    #make a while true loop 
    
        #ask user if they want to create an account, log in, or exit 

        #if user choice is 1 then 
        
            #call create account
            
        #else if user choice is 2 then
            
            #call login
        
        #else if user choice is 3 then tell the user to select again, continue 
            
            #display thanks for using the FINANCE CALCULATOR PROGRAM
import budgeting_and_savings_goal, helper, login_logout, utill_functions, random_password_generator
def main():
    data=utill_functions.csv_file("data.csv")
    username,password=login_logout.login(data)
    if not(username):
        return
    while True:
        choise=utill_functions.get_valid_type(int,"0 to log out\n1 to see stats\n2 to change stats: ",valid=(0,2))
        if choise==0:
            return
        elif choise==1:
            for x in data:
                if x["username"]==username and password==x["password"]:
                    totalcost=0
                    formating={}
                    print(f"username:{x["username"]}\npassword:{x["password"]}\nincome:{x["income"]}\nsavings:{x["savings"]}")
                    expens=utill_functions.csv_file.from_underscore(x["expenses_name"])
                    mount=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                    budg=utill_functions.csv_file.from_underscore(x["budget_expense"])
                    for num,x in enumerate(expens):
                        print(f"expense name: {x} amount: ${mount[num]} budget: ${budg[num]}")
                        totalcost+=int(mount[num])
                    for num,x in enumerate(expens):    
                        percentage = (int(mount[num]) / int(totalcost)) * 100 if int(totalcost) > 0 else 0
                        formating[x]=[percentage,int(mount[num]),[int(mount[num]),int(budg[num])]]
                    utill_functions.parse_turtle_data(formating)
        elif choise==2:
            while True:
                choise=utill_functions.get_valid_type(int,"0 to return\n1 to add expenses\n2 to remove expenses\n3 to change expense\n4 to change income\n5 to change savings: ",valid=(0,5))
                if choise==0:
                    break
                elif choise==1:
                    userrow=None
                    for x in data:
                        if x["username"]==username and password==x["password"]:
                            expenses = utill_functions.csv_file.from_underscore(x["expenses_name"])
                            amounts = utill_functions.csv_file.from_underscore(x["expenses_amount"])
                            budgets = utill_functions.csv_file.from_underscore(x["budget_expense"])
                            userrow=x
                    count=0
                    while True:
                        count+=1
                        expence=utill_functions.get_valid_type(str,f"what is the name of your #{count} expence(0 to stop adding more): ").replace(",","").replace('"',"").replace("`","").replace("_","")
                        if expence=="0":
                            if len(expenses)>0:
                                break
                            else:
                                print("you cant have 0 expenses")
                                continue
                        amount=utill_functions.get_valid_type(int,f"what is the cost of {expence}: ")
                        budget=utill_functions.get_valid_type(int,f"what is your budget for {expence}: ")
                        if utill_functions.get_valid_type(str,f"do you want to add {expence}:{amount}:{budget}(y/n): ",valid=["y","n"])=="y":
                            expenses.append(expence)
                            amounts.append(amount)
                            budgets.append(budget)
                            userrow["expenses_name"] = utill_functions.csv_file.to_list(expenses)
                            userrow["expenses_amount"] = utill_functions.csv_file.to_list(amounts)
                            userrow["budget_expense"] = utill_functions.csv_file.to_list(budgets)
                            data.update_data(username, userrow)
                            data.update_data(username,userrow)
                elif choise==2:
                    for x in data:
                        if x["username"]==username and x["password"]=="password":
                            expenses = utill_functions.csv_file.from_underscore(x["expenses_name"])
                            amounts = utill_functions.csv_file.from_underscore(x["expenses_amount"])
                            budgets = utill_functions.csv_file.from_underscore(x["budget_expense"])
                            userrow = x
                    if len(expenses) <= 1:
                        print("You cannot have 0 expenses. Add one before removing this one.")
                        continue
                    print("0 to return")
                    for num,x in enumerate(expens):
                        print(f"{num+1} for: expense name: {x} amount: ${mount[num]} budget: ${budg[num]}")
                        maxi=num+1
                    inp=utill_functions.get_valid_type(int,"what do you want:",valid=(0,maxi))
                    if inp==0:
                        continue
                    if utill_functions.get_valid_type(str,f"do you want to delete {expenses[inp-1]}(y/n): ",valid=["y", "n"])=="y":
                        expenses.pop(inp-1)
                        amounts.pop(inp-1)
                        budgets.pop(inp-1)
                    userrow["expenses_name"] = utill_functions.csv_file.to_list(expenses)
                    userrow["expenses_amount"] = utill_functions.csv_file.to_list(amounts)
                    userrow["budget_expense"] = utill_functions.csv_file.to_list(budgets)                
                    data.update_data(username, userrow)
            
if __name__=="__main__":
    main()