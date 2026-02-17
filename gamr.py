from tkinter import *
from tkinter import messagebox 

def ButtonClick(button):
    global x_o, flag
    
    if button["text"] == "":
        button["bg"] = "#FFEDC7"
        
        if x_o:
            button["text"] = "X"
            x_o = False
        else:
            button["text"] = "O"
            x_o = True
            
        flag += 1
        check_winner() 
    else:
        messagebox.showinfo("Tic Tac Toe - Ced", "Player Has Already Entered!")

def check_winner():
    global flag

    wins = [
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button4, button7),
        (button2, button5, button8),
        (button3, button6, button9),
        (button1, button5, button9),
        (button3, button5, button7)
    ]

    for b1, b2, b3 in wins:
        if b1["text"] == b2["text"] == b3["text"] != "":
            b1["bg"] = b2["bg"] = b3["bg"] = "#32CD32"
            messagebox.showinfo("Tic Tac Toe", f"Player {b1['text']} Wins!")

    if flag == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        reset_game()

def reset_game():
    global flag, x_o
    
    flag = 0
    x_o = True
    
    buttons = [button1, button2, button3,
               button4, button5, button6,
               button7, button8, button9]
    
    for button in buttons:
        button["text"] = ""
        button["bg"] = "#0AC4E0"


main = Tk()
main.title ('Tic Tac Toe - Ced')

x_o = True
flag = 0

button1 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button1))
button1.grid(row=0,column=0)

button2 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button2))
button2.grid(row=0,column=1)

button3 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button3))
button3.grid(row=0,column=2)

button4 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button4))
button4.grid(row=1,column=0)

button5 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button5))
button5.grid(row=1,column=1)

button6 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button6))
button6.grid(row=1,column=2)

button7 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button7))
button7.grid(row=2,column=0)

button8 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button8))
button8.grid(row=2,column=1)

button9 = Button(main, text="", font=("Montserrat",70,"bold"), bg="#0AC4E0", fg="white",width=3, command=lambda: ButtonClick(button9))
button9.grid(row=2,column=2)

reset_btn = Button(main, text="Reset Game",
                   font=("Montserrat", 20, "bold"),
                   bg="#FF5733", fg="white",
                   command=reset_game)

reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")



mainloop()

