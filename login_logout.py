#ES log in log out 

#make file_path be the file path to the csv or where the accounts are kept

import utill_functions
import random_password_generator
#make a function called login 
def login(data):
    #make a while true loop 
    while True:
        chose = utill_functions.get_valid_type(int,"0 to exit\n1 to to login\n2 to to make an account\nwhat do you want: ",valid=(0,2))
          
        #if choice is to exit break and go to the main funtion   
        if chose == 0:
            return False,False
        #else if choice is to login
        elif chose == 1:
            #make username match to an input asking for the username
            user = utill_functions.get_valid_type(str,"Enter your username: ")
            passw=utill_functions.get_valid_type(str,"what is your password: ")
            #open the filepath and read it as file 
            for x in data:
                if x["username"]==user and passw==x["password"]:
                    return user,passw
            #make user found false
            else:
            #make a loop in row 
                print("no acount with that name and password")
                #if there is not in row return 
                #if there is a account make user found true

            #call the funtion for gov to handle his part 
        #else if choice of the user create an account
        elif chose == 2:
            while True:
                #make a input asking the user for a name 
                username=utill_functions.get_valid_type(str,"what is your username: ")
                if utill_functions.get_valid_type(str,f"do you want {username} to be your username (this canot be changed later)(y/n): ",valid=["y",'n'])=="y":
                    break
            #ask the user if they want to type their own password 
            if utill_functions.get_valid_type(str,"do you want a random password(y/n): ",valid=["y","n"])=="y":
                #if choice is to type their own password, make them type the password
                password=random_password_generator.make_password()#use this
                #elif choice is to generate a password call the random password generator
                print(f"this is your password: {password}\nwrite it down")
            else:
            #else print to select an acual option
                while True:
                    password=utill_functions.get_valid_type(str,"what is your password: ")
                    if utill_functions.get_valid_type(str,f"do you want {password} to be your password (this canot be changed later)(y/n): ",valid=["y",'n'])=="y":
                        break
            #save the password to the csv file
            while True:
                income=utill_functions.get_valid_type(int,"what is your hourly income: ",valid=(0,10000000000))
                if utill_functions.get_valid_type(str,f"is ${income} your hourly wage (y/n): ",valid=["y",'n'])=="y":
                    break
            expenses=[]
            amounts=[]
            budgets=[]
            count=0
            while True:
                count+=1
                expence=utill_functions.get_valid_type(str,f"what is the name of your #{count} expence(0 to stop adding more): ")
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
            while True:
                savings=utill_functions.get_valid_type(int,"how much is in your savings: ",valid=(0,100**100))
                if utill_functions.get_valid_type(str,f"is ${savings} your savings(y/n): ",valid=["y",'n'])=="y":
                    break
            data.add([username,password,income,utill_functions.csv_file.to_list(expenses),utill_functions.csv_file.to_list(amounts),utill_functions.csv_file.to_list(budgets),savings])
            continue





