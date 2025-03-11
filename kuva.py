import tkinter
from tkinter import *
from tkinter import messagebox
# Kuva Costs
KUVA_COST = [900, 1000, 1200, 1400, 1700, 2000, 2350, 2750, 3150]  
MAX_COST = 3500  # After 9th roll

def calculate_kuva_spent(rolls):
    total_kuva = 0
    for i in range(rolls):
        if i < len(KUVA_COST):
            total_kuva += KUVA_COST[i]
        else:
            total_kuva += MAX_COST  # 3500 from here               
    return total_kuva

def calculate():
    try:
        rolls=int(EntryRolls.get())
        if rolls<=0:
            messagebox.showerror("error", "Please enter a valid number of rolls.")
        
        kuva_spent= calculate_kuva_spent(rolls)
        result_label.config(text=f"Your Riven has {rolls} Rolls\nTotal Kuva spent: {kuva_spent}")

    except ValueError:
        result_label.config(text=f"Invalid input. Please enter a number.")

#GUI
screen= tkinter.Tk()
screen.title("Kuva Calculator")
screen.geometry ("300x300")
screen.resizable(0, 0)

title =tkinter.Label(screen, text="Kuva Calculator", bg="gray", font=("Arial",20), border=10)
title.pack(fill=tkinter.X)

Subtitle=tkinter.Label(screen,text="Enter the roll number of your riven", font=("Arial",11), border=20)
Subtitle.pack()

exit_button=tkinter.Button(screen, text="Exit", padx=50, pady=10, command = quit)
exit_button.pack(side=BOTTOM, pady=5)

EntryRolls=tkinter.Entry(screen, font=("",15))
EntryRolls.pack()

calculate_button=tkinter.Button(screen,text="Calculate", padx=10, pady=5, command= calculate)
calculate_button.pack(pady=7)

result_label = tkinter.Label(screen, text="", font=("Arial", 13))
result_label.pack()

#run
screen.mainloop()



    
