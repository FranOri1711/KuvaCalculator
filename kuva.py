#Kuva Costs
KUVA_COST = [900, 1000, 1200, 1400, 1700, 2000, 2350, 2750, 3150]  
MAX_COST = 3500 #After 9th roll

def calculate_kuva_spent(rolls):
    total_kuva = 0
    for i in range(rolls):
        if i < len(KUVA_COST):
            total_kuva += KUVA_COST[i]
        else:
            total_kuva += MAX_COST  #3500 from here               
    return total_kuva

# Main
print("----------------")
print("Kuva Calculator")
print("----------------")
#Only accepts numbers
try:
    rolls = int(input("Enter the number of rolls from your Riven: "))
    if rolls < 0:
        print("Please enter a valid number of rolls (0 or more).")
    else:
        kuva_spent = calculate_kuva_spent(rolls)
        print(f"Your Riven has {rolls} Rolls and has spent {kuva_spent} Kuva.")
        quit
except ValueError:
    print("Invalid input. Please enter a number.")
