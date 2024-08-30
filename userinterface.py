import tkinter as tk
import threading
import socket
from PIL import Image, ImageTk

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
        for i in range(10):
            Player_UI.label(self, "                   ", i, 0)
        #Player_UI.label(self, "gait information", 0, 2)
        Player_UI.login_button(self,"login",i,2)

    def window(self,interface_name):
        self.interface = tk.Tk()
        self.interface.title(interface_name)
        self.interface.geometry('1000x700')

    def label(self,word,row,column):
        self.LABEL=tk.Label(self.interface,text=word)
        self.LABEL.grid(row=row,column=column)
    def login_button(self,text,row,column):
        self.enterbutton  = tk.Button(self.interface,text=text,command = self.player_interface)#action_trigger)
        self.enterbutton.grid(row=row,column=column)
    def disp(self):
        print("what")
        turnlabel = tk.Label(self.interface, textvariable=self.turn)
        turnlabel.grid(row=5, column=3)

    def clear_window(self):
        for i in self.interface.winfo_children():
            i.grid_forget()
    def open_image(self):
        original_image = Image.open("C:\\Users\\zijian\\Desktop\\poker_image\\player_image.png")
        return original_image

    def player_interface(self):
        self.clear_window()
        X_cord = [350,470,600,720,650,550,400,300,250]
        Y_cord = [400,400,400,300,200,200,200,200,300]
        self.player_image = ImageTk.PhotoImage(Player_UI.open_image(self).resize((40, 40)))
        for i in range(9):
            #image_label = tk.Label(self.interface, image=self.player_image)
           # image_label.place(x=X_cord[i], y=Y_cord[i])
            tk.Label(self.interface, image=self.player_image).place(x=X_cord[i], y=Y_cord[i])
    """
    def player_images_disp(self,number_of_player):
        self.clear_window()
        X_cord=[470]
        Y_cord=[400]
        self.player_image = ImageTk.PhotoImage(Player_UI.open_image(self).resize((30, 30)))
       # image_label = tk.Label(self.interface, image=self.player_image)
       # image_label.place(x=470, y=400)
    """
    def run(self):
        self.interface.mainloop()
