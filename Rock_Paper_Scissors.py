import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock paper Scissors Game")

User_score = 0
Comp_score = 0
User_choice = ""
Comp_choice = ""

def Choice_to_number(choice):
    reps = {"rock":0,"paper":1,"scissors":2}
    return reps[choice]

def Number_to_choice(number):
    reps = {0:"rock", 1:"paper", 2:"scissors"}
    return reps[number]

def Computer_Choice():
    Comp_choice = random.choice(["rock","paper","scissors"])
    return Comp_choice

def result(User_choice,Comp_choice):
    global User_score
    global Comp_score
    if User_choice == Comp_choice:
        print("It's a tie")
    elif Choice_to_number(User_choice) < Choice_to_number(Computer_Choice):
        User_score += 1
        print("Comp lose")
    else:
        Comp_score += 1
        print("You win")

    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    text_area.insert(tk.END,f"User score: {User_score}\nComp score: {Comp_score}")

def rock():
    global User_choice
    global Comp_choice
    User_choice = "rock"
    Comp_choice = Computer_Choice()
    result(User_choice,Comp_choice)

def paper():
    global User_choice
    global Comp_choice
    User_choice = "paper"
    Comp_choice = Computer_Choice()
    result(User_choice,Comp_choice)

def scissors():
    global User_choice
    global Comp_choice
    User_choice = "scissors"
    Comp_choice = Computer_Choice()
    result(User_choice,Comp_choice)

button1 = tk.Button(master=window,text="rock",command=rock, bg="skyblue")
button1.grid(column=0,row=0)
button2 = tk.Button(master=window,text="paper",command=paper, bg="pink")
button2.grid(column=0, row=1)
button3 = tk.Button(master= window,text="scissors", command= scissors)
button3.grid(column=0,row=2)

window.mainloop()