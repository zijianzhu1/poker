import tkinter as tk
import threading
import socket

class Player_UI:
    """initialize the first part
    it will have two text entry on both interface for port and ip information
    enter player2(server) informations first, then enter player1(server) to connect
    e.g. port: 8000
         ip address: 127.0.0.1
    """
    def __init__(self, player_board, players_card):

        self.num_of_real_players=1
        Player_UI.window(self, "Texas Hold'em")
        Player_UI.label(self, "                            ", 0, 0)
        Player_UI.label(self, "                            ", 0, 1)
        Player_UI.label(self, "gait information", 0, 2)
        Player_UI.button(self,"enter",2,1,Player_UI.clear_window(self))

    def window(self,interface_name):
        self.interface = tk.Tk()
        self.interface.title(interface_name)
        self.interface.geometry('700x700')

    def label(self,word,row,column):
        self.LABEL=tk.Label(self.interface,text=word)
        self.LABEL.grid(row=row,column=column)
    def button(self,text,row,column,func):
        def action_trigger():
            print("enter")
        self.enterbutton  = tk.Button(self.interface,text=text,command = func)#action_trigger)
        self.enterbutton.grid(row=row,column=column)
    def disp(self):
        print("what")
        turnlabel = tk.Label(self.interface, textvariable=self.turn)
        turnlabel.grid(row=5, column=3)
    def clear_window(self):
        for i in self.interface.winfo_children():
            i.grid_forget()


    def run(self):
        self.interface.mainloop()