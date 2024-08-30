#!/usr/bin/env python3

import statistics
import os

# Money constants
pr_pallet = 1000                                        # Producion cost per pallet    
worker_cost = 4000                                        # Price per worker per Round
rent = 5000                                             # Rent per Round

# Machines constants
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
list_sell_price = []

# Clear Console
def clear():
    os.system("clear")

while current_round != max_rounds:
    # Buy round
    clear()
    loop_buy = 1
    while loop_buy == 1:

        amount_workers = amount_standard + amount_economy + amount_excellence
        total_price_workers = amount_workers * worker_cost
        total_production_cost = (amount_standard * standard_production + amount_economy * economy_production + amount_excellence * excellence_production) * pr_pallet
        total_production = amount_standard * standard_production + amount_economy * economy_production + amount_excellence * excellence_production
        prognosed_costs = rent + total_price_workers + total_production_cost
        prognosed_profit = total_production * sell_value - prognosed_costs

        action = int(input("""
####################

Current Balance: %i€

1. Buy a machine
2. Set sell Value
3. Show Statistics
4. Next Round 

####################
""" %capital))
        clear()

        if action == 1:
            buy_select_machine = int(input("""
        ####################

        1. Buy standard machine     20,000€
        2. Buy economy machine      30,000€
        3. Buy excellence machine   40,000€

        4. Cancel

        ####################
        """))

            if buy_select_machine == 1:
                if capital >= standard_price and capital - standard_price >= prognosed_costs + worker_cost + standard_production * pr_pallet:
                    capital -= standard_price
                    amount_standard += 1
                    input("Press Enter to continue...")
                    clear()
                elif capital - standard_price <= prognosed_costs + worker_cost + standard_production * pr_pallet:
                    print("You are not able to maintain this machine with the available funds!")
                    input("Press Enter to continue...")
                    clear()
                elif capital <= standard_price:
                    print("Insufficent funds!")
                    input("Press Enter to continue...")
                    clear()

            elif buy_select_machine == 2:
                if capital >= economy_price and capital - economy_price >= prognosed_costs + worker_cost + economy_production * pr_pallet:
                    capital -= economy_price
                    amount_economy += 1
                    clear()
                elif capital - economy_price <= prognosed_costs + worker_cost + economy_production * pr_pallet:
                    print("You are not able to maintain this machine with the available funds!")
                    input("Press Enter to continue...")
                    clear()
                elif capital <= economy_price:
                    print("Insufficent funds!")
                    input("Press Enter to continue...")
                    clear()
    
            elif buy_select_machine == 3:
                if capital >= excellence_price and capital - excellence_price >= prognosed_costs + worker_cost + excellence_production * pr_pallet:
                    capital -= excellence_price
                    amount_excellence += 1
                elif capital - excellence_price <= prognosed_costs + worker_cost + excellence_production * pr_pallet:
                    print("You are not able to maintain this machine with the available funds!")
                    input("Press Enter to continue...")
                    clear()
                elif capital <= excellence_price:
                    print("Insufficent funds!")
                    input("Press Enter to continue...")
                    clear()

            elif buy_select_machine == 4:
                pass

        elif action == 2:
            sell_value = int(input("Set a new sell value: "))
        elif action == 3:
            print("""
            ####################

            Standard machines: %i
            Economy machines: %i
            Excellence machines: %i

            Rent: %i€
            Worker Expenses: %i€
            Production Expenses: %i€
            Prognosed Costs: %i€

            Total Production: %i Pallets
            Sell Value: %i€
            Prognosed Profit: %i€

            ####################
            """ % (amount_standard, amount_economy, amount_excellence, rent, total_price_workers, total_production_cost, prognosed_costs, total_production, sell_value, prognosed_profit))
            input("Press Enter to continue...")
            clear()
        elif action == 4:
            loop_buy = 0

    # Production round
    list_sell_price.append(sell_value)
    capital -= rent + total_price_workers + total_production_cost
    if capital < 0:
        print("haha loser, you're bankrupt")
        break
    capital += total_production * sell_value
    current_round += 1
    print(list_sell_price)
    print(str(current_round) + ". " + str(capital))

    # Score
    devaluation_count = 0                   # Used to calculate the devaluation of machines due to wear and tear
    machine_actual_value = standard_price * amount_standard + economy_price * amount_economy + excellence_price * amount_excellence 
    while devaluation_count <= current_round:
        machine_actual_value *= 0.9
        devaluation_count += 1

    company_value = capital + machine_actual_value
    avg_sell_price = statistics.mean(list_sell_price)
    clear()
    print("""
    Balance:            %i€
    Company Value:      %i€
    Average sell price: %i€""" % (capital, company_value, avg_sell_price))
    input("Press Enter to continue...")
