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
    def __init__(self, player_board, players_card,all_cards):
        self.image_keeper=[]
        self.players_card = players_card
        self.num_of_real_players=1
        self.all_cards=all_cards
        Player_UI.image_reference(self)
        Player_UI.window(self, "Texas Hold'em")
        for i in range(10):
            Player_UI.label(self, "                   ", i, 0)
        #Player_UI.label(self, "gait information", 0, 2)
        Player_UI.login_button(self,"login",i,2)
        #self.players_card=players_card



    def window(self,interface_name):
        self.interface = tk.Tk()
        self.interface.title(interface_name)
        self.interface.geometry('2000x1000')

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
       # image_keeper=[]
        self.clear_window()
        X_cord = [350,470,600,720,650,550,400,300,250]
        Y_cord = [400,400,400,300,200,200,200,200,300]
        self.player_image = ImageTk.PhotoImage(Player_UI.open_image(self).resize((40, 40)))
        self.image_keeper.append(self.player_image)
        for i in range(9):
            #image_label = tk.Label(self.interface, image=self.player_image)
            #image_label.place(x=X_cord[i], y=Y_cord[i])
            a=tk.Label(self.interface, image=self.player_image)#.place(x=X_cord[i], y=Y_cord[i])
            a.place(x=X_cord[i], y=Y_cord[i])

        #self.show_player_cards()
        card1_path = self.image_dict["player 1"][0]
        card2_path = self.image_dict["player 1"][1]
        print("here")
        print(card1_path)
        print(card2_path)
        card1_image = Image.open(card1_path)
       # card2_image = Image.open(card2_path)
        card1_image_resized = ImageTk.PhotoImage(card1_image.resize((50, 70)))
        #card2_image_resized = ImageTk.PhotoImage(card2_image.resize((20, 20)))
        b=tk.Label(self.interface, image=card1_image_resized)#.place(x=340, y=390)
        b.place(x=340, y=390)
        self.image_keeper.append(card1_image_resized)
       # self.image_keeper=image_keeper
    def image_reference(self):
        self.image_dict={}
        self.image_dict.update({"player_image":"C:\\Users\\zijian\\Desktop\\poker_image\\player_image.png"})
        keys = list(self.players_card.keys())
        card_number=0
        for i in keys:
            card_path_name= i
            card1_path="C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\"+self.players_card[i][0].name+".png"
            card2_path="C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\"+self.players_card[i][1].name+".png"
            print(self.players_card[i][0].name)
            self.image_dict.update({card_path_name:[card1_path,card2_path]})

    def show_player_cards(self):
        X_cord = [320, 470, 600, 720, 650, 550, 400, 300, 250]
        Y_cord = [370, 400, 400, 300, 200, 200, 200, 200, 300]
        keys = list(self.players_card.keys())
        print("here")
        print(self.image_dict)
        #for i in keys:
        #one_player_card=[self.players_card[i][0],self.players_card[i][1]]
        #print([self.players_card[i][0].name,self.players_card[i][1].name])
        #card1_path="C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\"+self.players_card[i][0].name+".png"
       # card2_path="C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\"+self.players_card[i][1].name+".png"
        card1_path=self.image_dict["player 1"][0]
        card2_path = self.image_dict["player 1"][1]
        print("here")
        print(card1_path)
        print(card2_path)
        card1_image=Image.open(card1_path)
        card2_image=Image.open(card2_path)
        card1_image_resized=ImageTk.PhotoImage(card1_image.resize((40, 40)))
        card2_image_resized=ImageTk.PhotoImage(card2_image.resize((20, 20)))
        tk.Label(self.interface, image=card1_image_resized).place(x=320, y=370)
       # tk.Label(self.interface, image=card2_image).place(x=X_cord[0], y=Y_cord[0])
        #"C:\Users\zijian\Desktop\poker_image\PNG-cards-1.3\2 Clubs.png"


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
