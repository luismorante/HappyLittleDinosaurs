from tkinter import *
from PIL import ImageTk, Image
import random

#resize cards
def resize_cards(card):
    card_img = Image.open(card)

    resized_card_img = card_img.resize((150, 218))

    global resized_card
    resized_card = ImageTk.PhotoImage(resized_card_img)

    return resized_card

def main_window():

    title_root.destroy()
    root = Tk()
    root.title("HAPPY LITTLE DINOSAURS")
    root.geometry("2500x1000")
    root.config(bg = "#EAD1AC")


    playerhand_frame = Frame(root)#bg = "green"
    playerhand_frame.pack(side = "bottom",pady=20)

    text_one = '1'
    text_two = '2'
    text_three = '3'
    text_four = '4'
    text_five = '5'

    def creating_hand(frame_of_hand, hand_index_text, row_position, column_position):
        card_hand_index = LabelFrame(frame_of_hand, text = hand_index_text, font = ("Helvetica",18), bd = 0)
        card_hand_index.grid(row = row_position, column = column_position, padx = 20, ipadx = 20 )

        image_of_card = Label(card_hand_index)
        image_of_card.pack(pady = 10, padx= 10)

        return image_of_card

    playercard1 = creating_hand(playerhand_frame, text_one, 0, 0)
    playercard2 = creating_hand(playerhand_frame, text_two, 0, 1)
    playercard3 = creating_hand(playerhand_frame, text_three, 0, 2)
    playercard4 = creating_hand(playerhand_frame, text_four, 0, 3)
    playercard5 = creating_hand(playerhand_frame, text_five, 0, 4)


    #Shuffle the cards
    def shuffle():
        #Define our Deck
        global deck
        global playerhand

        ########## Build Deck from Database ######### 
        deck = ["COOL_STICK","HANDY_PAN","GRAVE_MAKER","BONEHEAD","RUNHOMEBAT","BOW_AND_DINO","STING_STABBER","ICED_PTEA","METEOR_CANNON"]
        for i in range (9):
            deck.append(deck[i])
        for i in range (18):
            deck.append(deck[i])
        playerhand = []
        # ___________________________________________

        #card = random.choice(deck)
        random.shuffle(deck)

        for i in range (5):
            card = deck[0]
            playerhand.append(card)
            deck.pop(0)

        global card_image1
        global card_image2
        global card_image3
        global card_image4
        global card_image5

        card_image1 = resize_cards(f'images/cards/{playerhand[0]}.jpg')
        playercard1.config(image = card_image1)

        card_image2 = resize_cards(f'images/cards/{playerhand[1]}.jpg')
        playercard2.config(image = card_image2)

        card_image3 = resize_cards(f'images/cards/{playerhand[2]}.jpg')
        playercard3.config(image = card_image3)

        card_image4 = resize_cards(f'images/cards/{playerhand[3]}.jpg')
        playercard4.config(image = card_image4)

        card_image5 = resize_cards(f'images/cards/{playerhand[4]}.jpg')
        playercard5.config(image = card_image5)            


    def deal_cards():
        try:

            pass

        except:
            root.title(f'No cards in deck')

    def q (event):
        


    ######### Creating a couple of buttons #######

    quitButton = Button(root, text="Exit", command = root.quit)
    quitButton.pack()

    global mainDeck_image
    mainDeck_image = resize_cards(f'images/cards/Main_Card.jpg')
    global disasterDeck_image
    disasterDeck_image = resize_cards(f'images/cards/Disaster_Card.jpg')

    card_button = Button(root,image = mainDeck_image, command = deal_cards)
    card_button.pack(pady=10)

    disaster_button = Button(root,image = disasterDeck_image)
    disaster_button.pack(pady=10)

    shuffle_button = Button(root, text = "Shuffle Deck", font =("Helvetica",18), command = shuffle)
    shuffle_button.pack(pady = 20)

    # ___________________________________________


######################### Title Screen ##############################
title_root = Tk()

title_root.title("Screen")
title_root.overrideredirect(True) #Hide Title
title_root.geometry("400x300")
title_root.eval('tk::PlaceWindow . center') #center of screen

title_label = Label(title_root, text="Title Screen", font = ("Helvetica", 18))
title_label.pack(pady=50)
play_Button = Button(title_root, text = "Play", command=main_window)
play_Button.pack(pady=20)
play_Button.pack()
quitButton = Button(title_root, text="Exit", command = title_root.quit)
quitButton.pack()

title_root.config(bg = 'LightBlue')

# ________________________________________________________________________


mainloop() 