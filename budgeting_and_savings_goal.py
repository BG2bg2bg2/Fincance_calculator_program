# GNB - Gov Stuff (Budgeting + Savings Goal Tracker)

# End up here from Edwing's menu if user selects budgeting/savings options

# Before user gets here:
# - Categories already exist (Rent, Food, Transportation, etc.)
# - Income/expenses may already be stored by Edwing/Liam
import utill_functions
print("Welcome to the Budgeting/Savings Goal sector.")

choice = utill_functions.get_valid_type(int,"0 Go back to main men\n1 to set budget limits\n2 to view budgeting plan\n3 to Compare expenses to budget\n4 to Savings goal tracker\nWhat do you want: ",valid=(0,4))
# Ask user:
# 1. Set budget limits
# 2. View budgeting plan
# 3. Compare expenses to budget
# 4. Savings goal tracker
# 5. Go back to main menu


# BUDGETING SECTION

# define function as set_budget_limits()
def set_budget_limits():
    # ask user for total monthly income
    income = utill_functions.get_valid_type(float, "What is your monthly income?: $")
    # for each category:
        # ask user to set a spending limit

    # store budget limits (will be saved by Liam's data system)

    # display:
        # "Budget limits successfully set"

# If 2 is the option, then all this: 

# define function as create_budget_plan()
def create_budget_plan(data):
        def add_budget_categories(data):
        #make thing so user just keeps listing categories till they say some
            pass
    # get user's incomepass    income = utill_functions.get_valid_type(float,"Enter how much money you have right now: ")
    # get all category limits
    
    # calculate total planned spending

    # calculate remaining money:
        # remaining = income - total planned spending

    # display:
        # "Your income is $___"
        # "Your total planned spending is $___"
        # "Money left after budgeting: $___"


# define function as compare_expenses_to_budget()
def compare_expenses_to_budget(data):
    with open("data.csv", "r+") as data:
        # for each category:
        for spending in data:    
            # compare actual spending vs budget limit
            spending = 0
            limit = 0
            # if spending > limit:
            if spending > limit:
        # di    splay warning:
                print("WARNING")
                # "You went over budget in [category]"                
                print(f"You are over budget in {file}")


            #else:
                #display:
                    #"You are within budget for [category]"

    # calculate total remaining money:
        # income - total expenses

    # display:
        # "You have $___ left this month"


# SAVINGS GOAL SECTION


# define function as savings_goal_tracker()
def savings_goals_tracker(data):
    # while user does not exit:
        # ask user:
            # "What is your savings goal amount?"

        # ask user:
            # "What is your income?"

        # ask user:
            # "What percentage of your income goes to savings?"

        # convert percent to decimal

        # calculate monthly savings:
            # savings = income * percent

        # ask user:
            # "What is your current savings amount?"

        # calculate progress:
            # progress = current savings / goal * 100

        # display:
            # "You save $___ per month"
            # "You are ___% towards your goal"


        # INTEREST CALCULATION (concerning savings)


        # ask user:
            # "Enter interest rate (optional, press enter to skip)"

        # if user enters rate:
            # convert rate to decimal

            # calculate interest:
                # interest_amount = current savings * rate

            # add interest to savings

            # display:
                # "With interest, your savings is now $___"


        # FUTURE PROJECTION


        # calculate months needed:
            # months = (goal - current savings) / monthly savings

        # display:
            # "You will reach your goal in ___ months"

        # if goal reached:
            # display:
                # "Congrats! You reached your savings goal!"

        # ask user:
            # "Press enter to continue or type exit to go back"

        # if user types exit:
            # break loop

