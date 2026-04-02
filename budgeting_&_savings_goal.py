# GNB - Gov Stuff (Budgeting & Savings Goal Tracker)

# End up here from Edwing's menu if user selects budgeting/savings options

# Before user gets here:
# - Categories already exist (Rent, Food, Transportation, etc.)
# - Income/expenses may already be stored by Edwing/Liam


# Ask user:
# 1. Set budget limits
# 2. View budgeting plan
# 3. Compare expenses to budget
# 4. Savings goal tracker
# 5. Go back to main menu


# BUDGETING SECTION

# define function as set_budget_limits()

    # ask user for total monthly income

    # for each category:
        # ask user to set a spending limit

    # store budget limits (will be saved by Liam's data system)

    # display:
        # "Budget limits successfully set"


# define function as create_budget_plan()

    # get user's income

    # get all category limits

    # calculate total planned spending

    # calculate remaining money:
        # remaining = income - total planned spending

    # display:
        # "Your income is $___"
        # "Your total planned spending is $___"
        # "Money left after budgeting: $___"


# define function as compare_expenses_to_budget()

    # get actual expenses from Edwing's tracking system

    # for each category:
        # compare actual spending vs budget limit

        # if spending > limit:
            # display warning:
                # "You went over budget in [category]"

        # else:
            # display:
                # "You are within budget for [category]"

    # calculate total remaining money:
        # income - total expenses

    # display:
        # "You have $___ left this month"


# SAVINGS GOAL SECTION


# define function as savings_goal_tracker()

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

