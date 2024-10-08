#!/usr/bin/env python3

import platform
import statistics
import os

# Values
# Money values
pr_pallet = 1000                                        # Producion cost per pallet    
worker_cost = 4000                                      # Price per worker per Round
rent = 5000                                             # Rent per Round
material_cost = 1000

# Machines values
standard_price = 20000                                  # Price/Value
standard_production = 10                                # Production output in pallets
economy_price = 30000                                   # Price/Value
economy_production = 15                                 # Production output in pallets
excellence_price = 40000                                # Price/Value
excellence_production = 20                              # Production output in pallets

# Other constants
max_rounds = 6

# Variables
amount_standard = 0
amount_economy = 0
amount_excellence = 0
capital = 100000
current_round = 0
sell_value = 1000
actual_production = 0

# Functions
# Clear Console
def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")

# List members
def list_members():
    counter = 0
    for i in members:
        counter += 1
        print(counter, ". ", i )

# Setups
# Members setup
clear()
members = []
while True:
    clear()
    print("Members:")
    if not members:
        print("Empty")
    else:
        list_members()
    memb_setup = int(input("""
####################

Company Setup:

1. Add a new member
2. Remove a member
3. Finish setup

####################
> """))
    if memb_setup == 1:
        clear()
        add_member = input("Enter a name: ")
        members.append(add_member)
        print(members,"\n")
    elif memb_setup == 2:
        clear()
        list_members()
        member_rm = int(input("Remove a member: "))
        member_rm -= 1
        members.pop(member_rm)
    elif memb_setup == 3:
        break
    else:
        print("Invalid!")

# Select a Leader
clear()
list_members()
member_leader_select = int(input("Select a spokesperson: "))
member_leader_select -= 1
member_leader = members[member_leader_select]
print("The spokesperson is:", member_leader)
input("Press ENTER to continue...")

# Company Setup
clear()
company_name = input("Enter a company name: ")
product_name = input("Enter product name: ")
taste_name = input("Enter a taste: ")
slogan = input("Enter a slogan: ")
input("Press ENTER to continue...")

# Company presentation
clear()
print("Company name:            ", company_name)
print("Members:                 ", )
print("Company spokesperson:    ", member_leader)
print("Product name:            ", product_name)
print("Taste name:              ", taste_name)
print(slogan)
input("\n Press ENTER to continue...")

# Main game
while current_round != max_rounds:
    # Buy round
    clear()
    loop_buy = 1
    while True:

        amount_workers = amount_standard + amount_economy + amount_excellence
        total_price_workers = amount_workers * worker_cost
        total_production_cost = actual_production * pr_pallet + actual_production * material_cost
        total_production = amount_standard * standard_production + amount_economy * economy_production + amount_excellence * excellence_production
        prognosed_costs = rent + total_price_workers + total_production_cost
        prognosed_profit = actual_production * sell_value - prognosed_costs

        action = int(input("""
####################

Current Balance: %i€

1. Buy a machine
2. Set sell Value
3. Show Statistics
4. Set Production
5. Next Round 

####################
> """ %capital))
        clear()

        if action == 1:
            buy_select_machine = int(input("""
        ####################

        1. Buy standard machine     20,000€
        2. Buy economy machine      30,000€
        3. Buy excellence machine   40,000€

        4. Cancel

        ####################
        > """))

            if buy_select_machine == 1:
                capital -= standard_price
                amount_standard += 1
                actual_production += 10
                input("Machine purchased\n Press ENTER to continue...")
                clear()

            elif buy_select_machine == 2:
                capital -= economy_price
                amount_economy += 1
                actual_production += 15
                input("Machine purchased\n Press ENTER to continue...")
                clear()
    
            elif buy_select_machine == 3:
                capital -= excellence_price
                amount_excellence += 1
                actual_production += 20
                input("Machine purchased\n Press ENTER to continue...")
                clear()

            elif buy_select_machine == 4:
                pass

        elif action == 2:
            while True:
                sell_value = int(input("Set a new sell value: "))
                if sell_value <= 0:
                    print("Sell value cannot be lower than or equal to 0")
                else:
                    break

        elif action == 3:
            print("""
            ####################

            Standard machines: %i
            Economy machines: %i
            Excellence machines: %i

            Rent: %i€
            Worker Expenses: %i€
            Total Production Expenses (Material Expenses + Production Costs): %i€
            Prognosed Costs: %i€

            Maximal Production: %i Pallets
            Current Production: %i Pallets
            Sell Value: %i€
            Prognosed Profit: %i€

            ####################
            """ % (amount_standard, amount_economy, amount_excellence, rent, total_price_workers, total_production_cost, prognosed_costs, total_production, actual_production, sell_value, prognosed_profit))
            input("Press Enter to continue...")
            clear()

        elif action == 4:
            print("Current maximum production output: %i" % total_production)
            while True:
                print("Enter new production amount (0 - %i):" % total_production)
                actual_production = int(input())
                if actual_production >= 0 and actual_production <= total_production:
                    break                               # Success
                else:
                    print("Invalid Value")

        elif action == 5:
            break

    # Production round
    capital -= rent + total_price_workers + total_production_cost
    capital += actual_production * sell_value
    if capital < 0:
        print("you're bankrupt")
        break
    current_round += 1
    print(str(current_round) + ". " + str(capital))

    # Score
    devaluation_count = 0                   # Used to calculate the devaluation of machines due to wear and tear
    machine_actual_value = standard_price * amount_standard + economy_price * amount_economy + excellence_price * amount_excellence 
    while devaluation_count <= current_round:
        machine_actual_value *= 0.9
        devaluation_count += 1

    company_value = capital + machine_actual_value
    clear()
    print("""
    Balance:            %i€
    Company Value:      %i€""" % (capital, company_value))
    input("Press Enter to continue...")
