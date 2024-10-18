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
    def __init__(self, player_board, players_card,all_cards,flop_cards,turn_cards,river_cards):
        self.image_keeper=[]
        self.players_card = players_card
        self.num_of_real_players=1
        self.all_cards=all_cards
        self.flop_cards=flop_cards
        self.turn_cards=turn_cards
        self.river_cards=river_cards
        Player_UI.image_reference(self)
        Player_UI.window(self, "Texas Hold'em")

       # for i in range(10):
            #Player_UI.label(self, "                   ", i, 0)
        #Player_UI.label(self, "gait information", 0, 2)
        Player_UI.login_button(self,"login",0,0)
        #self.players_card=players_card
        #self.interface.bind("<Configure>", self.on_resize)

    def create_widgets(self):
        # Initial widget setup
        self.label("Welcome to Texas Hold'em!", 0, 0)  # Example label
        self.login_button("Login", 1, 0)  # Example login button
    def window(self,interface_name):
        self.interface = tk.Tk()
       # self.interface=tk.Frame(self.root)
        self.interface.title(interface_name)
        self.interface.geometry('2000x1000')
        #self.interface.bind("<Configure>", self.on_resize)
      #  self.button_placer = tk.Frame(self.interface)
      #  self.button_placer.grid(row=0, column=0, sticky='nsew')
      #  self.interface.grid_rowconfigure(0, weight=1)
      #  self.interface.grid_columnconfigure(0, weight=1)
    """
    def on_resize(self, event):

        window_width = self.interface.winfo_width()
        window_height = self.interface.winfo_height()

        # Resize the image proportionally
        new_image = self.open_image().resize((int(window_width * 0.1), int(window_height * 0.1)))
        self.tk_image = ImageTk.PhotoImage(new_image)

        # Update the image label
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image  # Keep a reference to avoid garbage collection

        # Recalculate positions based on relative percentages
        image_x = int(window_width * self.relative_positions['image_1'][0])
        image_y = int(window_height * self.relative_positions['image_1'][1])
        self.image_label.place(x=image_x, y=image_y)

        # Reposition the button similarly
        button_x = int(window_width * self.relative_positions['button_1'][0])
        button_y = int(window_height * self.relative_positions['button_1'][1])
        self.enterbutton.place(x=button_x, y=button_y)
    """
    def label(self,word,row,column):
        self.LABEL=tk.Label(self.interface,text=word)
        self.LABEL.grid(row=row,column=column)
    def login_button(self,text,row,column):
        self.enterbutton  = tk.Button(self.interface,text=text,command = self.player_interface)#action_trigger)
        self.enterbutton.grid(row=row,column=column)
    def disp(self):
       # print("what")
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
        #self.button_placer = tk.Frame(self.interface)
        #self.button_placer.grid(row=0, column=0, sticky='nsew')
        #self.interface.grid_rowconfigure(0, weight=1)
        #self.interface.grid_columnconfigure(0, weight=1)
        X_cord = [950, 1370, 1650, 1500, 1250, 650, 400, 250, 530]
        Y_cord = [780, 780,  550,  260,  180,  180, 260, 550, 780]
        self.player_image = ImageTk.PhotoImage(Player_UI.open_image(self).resize((100, 100)))
        self.image_keeper.append(self.player_image)
        for i in range(9):
            #image_label = tk.Label(self.interface, image=self.player_image)
            #image_label.place(x=X_cord[i], y=Y_cord[i])
            a=tk.Label(self.interface, image=self.player_image)#.place(x=X_cord[i], y=Y_cord[i])
            a.place(x=X_cord[i], y=Y_cord[i])

        self.show_player_cards()
        self.show_flop_card()
        self.show_turn_card()
        self.show_river_card()
        self.fold_button("fold",1550,830)
        self.check_button("check",1680,830)
        self.raise_button("raise",1810,830)
        #self.fold_button("fold",1000,500)
       # self.check_button("check",1100,500)
       # self.raise_button("raise",1200,500)
        """
        card1_path = self.image_dict["player 1"][0]
        card2_path = self.image_dict["player 1"][1]
        print("here")
        print(card1_path)
        print(card2_path)
        card1_image = Image.open(card1_path)
       # card2_image = Image.open(card2_path)
        card1_image_resized = ImageTk.PhotoImage(card1_image.resize((70, 98)))
        #card2_image_resized = ImageTk.PhotoImage(card2_image.resize((20, 20)))
        b=tk.Label(self.interface, image=card1_image_resized)#.place(x=340, y=390)
        b.place(x=340, y=390)
        self.image_keeper.append(card1_image_resized)
        """
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
         #   print(self.players_card[i][0].name)
            self.image_dict.update({card_path_name:[card1_path,card2_path]})

    def show_player_cards(self):
        X_cord = [915,1015,1335, 1435, 1465, 1565, 1465, 1565, 1215,1315,615,715,365,465,365,465,495,595]
        Y_cord = [672,672, 672, 672, 550, 550, 370, 370, 290,290,290,290,370,370,550,550,672,672]
        keys = list(self.players_card.keys())
       # print("here")
       # print(self.image_dict)
        card_one_index=0
        card_two_index=1
        for i in keys:
            one_player_card=[self.players_card[i][0],self.players_card[i][1]]
         #  print([self.players_card[i][0].name,self.players_card[i][1].name])
            card1_path="C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\"+self.players_card[i][0].name+".png"
            card2_path="C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\"+self.players_card[i][1].name+".png"
            #card1_path=self.image_dict["player 1"][0]
           # card2_path = self.image_dict["player 1"][1]
          #  print("here")
         #   print(card1_path)
         #   print(card2_path)
            card1_image=Image.open(card1_path)
            card2_image=Image.open(card2_path)
            card1_image_resized=ImageTk.PhotoImage(card1_image.resize((70, 98)))
            card2_image_resized=ImageTk.PhotoImage(card2_image.resize((70, 98)))
            tk.Label(self.interface, image=card1_image_resized).place(x=X_cord[card_one_index], y=Y_cord[card_one_index])
            tk.Label(self.interface, image=card2_image_resized).place(x=X_cord[card_two_index], y=Y_cord[card_two_index])
            self.image_keeper.append(card1_image_resized)
            self.image_keeper.append(card2_image_resized)
            card_one_index+=2
            card_two_index+=2
            #tk.Label(self.interface, image=card2_image).place(x=X_cord[0], y=Y_cord[0])
            #"C:\Users\zijian\Desktop\poker_image\PNG-cards-1.3\2 Clubs.png"
    def show_flop_card(self):

        #self.flop_card=flop_card
        card1_path = "C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\" + self.flop_cards[0].name + ".png"
        card2_path = "C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\" + self.flop_cards[1].name + ".png"
        card3_path = "C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\" + self.flop_cards[2].name + ".png"
        card1_image = Image.open(card1_path)
        card2_image = Image.open(card2_path)
        card3_image = Image.open(card3_path)
        card1_image_resized = ImageTk.PhotoImage(card1_image.resize((70, 98)))
        card2_image_resized = ImageTk.PhotoImage(card2_image.resize((70, 98)))
        card3_image_resized = ImageTk.PhotoImage(card3_image.resize((70, 98)))
        #start here
        tk.Label(self.interface, image=card1_image_resized).place(x=680, y=510)
        tk.Label(self.interface, image=card2_image_resized).place(x=820, y=510)
        tk.Label(self.interface, image=card3_image_resized).place(x=965, y=510)
        self.image_keeper.append(card1_image_resized)
        self.image_keeper.append(card2_image_resized)
        self.image_keeper.append(card3_image_resized)
    def show_turn_card(self):
        #self.flop_card=flop_card
        card1_path = "C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\" + self.turn_cards.name + ".png"
        card1_image = Image.open(card1_path)
        card1_image_resized = ImageTk.PhotoImage(card1_image.resize((70, 98)))
        #start here
        tk.Label(self.interface, image=card1_image_resized).place(x=1110, y=510)
        self.image_keeper.append(card1_image_resized)
    def show_river_card(self):
        #self.flop_card=flop_card
        card1_path = "C:\\Users\\zijian\\Desktop\\poker_image\\PNG-cards-1.3\\" + self.river_cards.name + ".png"
        card1_image = Image.open(card1_path)
        card1_image_resized = ImageTk.PhotoImage(card1_image.resize((70, 98)))
        #start here
        tk.Label(self.interface, image=card1_image_resized).place(x=1270, y=510)
        self.image_keeper.append(card1_image_resized)
    def check_button(self,text,row,column):
        blank_image = Image.new('RGBA', (120, 80), (255, 255, 255, 0))
        button_image = ImageTk.PhotoImage(blank_image)
        self.enterbutton = tk.Button(self.interface, text=text, image=button_image, compound="center",command=self.check_action)
        self.enterbutton.place(x=row, y=column, width=120, height=80)
        self.image_keeper.append(button_image)
        #self.check_button1 = tk.Button(self.interface, text=text, command=self.check_action)  # action_trigger)
        #self.check_button1.place(x=row, y=column)
    def fold_button(self,text,row,column):
        blank_image = Image.new('RGBA', (120, 80), (255, 255, 255, 0))
        button_image = ImageTk.PhotoImage(blank_image)
        self.enterbutton = tk.Button(self.interface, text=text, image=button_image, compound="center",command=self.fold_action)
        self.enterbutton.place(x=row, y=column, width=120, height=80)
        self.image_keeper.append(button_image)
        #self.fold_button1 = tk.Button(self.interface, text=text, command=self.fold_action)  # action_trigger)
        #self.fold_button1.place(x=row, y=column)
    def raise_button(self,text,row,column):
        blank_image = Image.new('RGBA', (120, 80), (255, 255, 255, 0))
        button_image = ImageTk.PhotoImage(blank_image)
        self.enterbutton = tk.Button(self.interface, text=text, image=button_image, compound="center",command=self.raise_action)
        self.enterbutton.place(x=row, y=column, width=120, height=80)
        self.image_keeper.append(button_image)
        #self.raise_button1 = tk.Button(self.interface, text=text, command=self.raise_action)  # action_trigger)
        #self.raise_button1.place(x=row, y=column)
    def check_action(self):
        print("check")
    def fold_action(self):
        print("fold")
    def raise_action(self):
        print("raise")


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
