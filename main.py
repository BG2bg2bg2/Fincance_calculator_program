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
import budgeting_and_savings_goal,helper,login_logout,program_stucture,utill_functions,random_password_generator
def main():
    data=utill_functions.csv_file("data.csv")
    if not(login_logout.login(data)):
        return
    while True:
        choise=utill_functions.get_valid_type(int,"0 to log out\n1 to see stats\n2 to change stats",valid=(0,2))
        if choise==0:
            return
        if choise==1:
            
if __name__=="__main__":
    main()