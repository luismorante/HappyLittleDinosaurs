from tkinter import *
from PIL import ImageTk, Image
import random

###########      Resize Cards    #################
def resize_cards(card):
    card_img = Image.open(card)

    resized_card_img = card_img.resize((150, 218))

    global resized_card
    resized_card = ImageTk.PhotoImage(resized_card_img)

    return resized_card

def resize_cards_2(card):
    card_img = Image.open(card)

    resized_card_img = card_img.resize((75, 109))

    global resized_card
    resized_card = ImageTk.PhotoImage(resized_card_img)

    return resized_card

#_______________________________________________________________

def main_window():

    title_root.destroy()
    root = Tk()
    root.title("HAPPY LITTLE DINOSAURS")
    root.geometry("2500x1000")
    root.config(bg = "#EAD1AC")

    playerhand_frame = Frame(root)#bg = "green"
    playerhand_frame.pack(side = "bottom",pady=20)

    opponenthand_frame = Frame(root)
    opponenthand_frame.pack(side = "left", padx = 10)

    opponent2hand_frame = Frame(root)
    opponent2hand_frame.pack(side = "right", padx = 10)

    opponent3hand_frame = Frame(root)
    opponent3hand_frame.pack(side = "top", padx = 10)

    def creating_hand(frame_of_hand, hand_index_text, row_position, column_position):
        card_hand_index = LabelFrame(frame_of_hand, text = hand_index_text, font = ("Helvetica",18), bd = 0)
        card_hand_index.grid(row = row_position, column = column_position, padx = 20, ipadx = 20 )

        image_of_card = Label(card_hand_index)
        image_of_card.pack(pady = 5, padx= 10)

        return image_of_card

    playercard1 = creating_hand(playerhand_frame, '1', 0, 0)
    playercard2 = creating_hand(playerhand_frame, '2', 0, 1)
    playercard3 = creating_hand(playerhand_frame, '3', 0, 2)
    playercard4 = creating_hand(playerhand_frame, '4', 0, 3)
    playercard5 = creating_hand(playerhand_frame, '5', 0, 4)

    opponentcard1 = creating_hand(opponenthand_frame, '', 0, 0)
    opponentcard2 = creating_hand(opponenthand_frame, '', 1, 0)
    opponentcard3 = creating_hand(opponenthand_frame, '', 2, 0)
    opponentcard4 = creating_hand(opponenthand_frame, '', 3, 0)
    opponentcard5 = creating_hand(opponenthand_frame, '', 4, 0)

    opponent2card1 = creating_hand(opponent2hand_frame, '', 0, 0)
    opponent2card2 = creating_hand(opponent2hand_frame, '', 1, 0)
    opponent2card3 = creating_hand(opponent2hand_frame, '', 2, 0)
    opponent2card4 = creating_hand(opponent2hand_frame, '', 3, 0)
    opponent2card5 = creating_hand(opponent2hand_frame, '', 4, 0)

    opponent3card1 = creating_hand(opponent3hand_frame, '', 0, 0)
    opponent3card2 = creating_hand(opponent3hand_frame, '', 0, 1)
    opponent3card3 = creating_hand(opponent3hand_frame, '', 0, 2)
    opponent3card4 = creating_hand(opponent3hand_frame, '', 0, 3)
    opponent3card5 = creating_hand(opponent3hand_frame, '', 0, 4)


    def show_opponenthand():

        global opponent_card_image
        opponent_card_image = resize_cards_2(f'images/cards/Main_Card.jpg')

        opponentcard1.config(image = opponent_card_image)
        opponentcard2.config(image = opponent_card_image)
        opponentcard3.config(image = opponent_card_image)
        opponentcard4.config(image = opponent_card_image)
        opponentcard5.config(image = opponent_card_image)

        opponent2card1.config(image = opponent_card_image)
        opponent2card2.config(image = opponent_card_image)
        opponent2card3.config(image = opponent_card_image)
        opponent2card4.config(image = opponent_card_image)
        opponent2card5.config(image = opponent_card_image)

        opponent3card1.config(image = opponent_card_image)
        opponent3card2.config(image = opponent_card_image)
        opponent3card3.config(image = opponent_card_image)
        opponent3card4.config(image = opponent_card_image)
        opponent3card5.config(image = opponent_card_image)

    def show_hand():

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

    
    def detect_key_press(event):

        if (len(playerhand) > 0):

            if event.char == '1':
                playerhand[0] = "none"
                show_hand()

            if event.char == '2':
                playerhand[1] = "none"
                show_hand()

            if event.char == '3':
                playerhand[2] = "none"
                show_hand()

            if event.char == '4':
                playerhand[3] = "none"
                show_hand()

            if event.char == '5':
                playerhand[4] = "none"
                show_hand()

    root.bind('<Key>', detect_key_press)

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
        
        global playerhand
        playerhand = []
        # ___________________________________________

        #card = random.choice(deck)
        random.shuffle(deck)

        for i in range (5):
            card = deck[0]
            playerhand.append(card)
            deck.pop(0)     

        show_hand()      

        show_opponenthand()


    def deal_cards():
        try:
            pass

        except:
            root.title(f'No cards in deck')

    ############     FRAME FOR THE DECKS AND START / QUIT GAME #############

    global mainDeck_image
    mainDeck_image = resize_cards(f'images/cards/Main_Card.jpg')
    global disasterDeck_image
    disasterDeck_image = resize_cards(f'images/cards/Disaster_Card.jpg')

    DeckFrame = Frame(root)
    DeckFrame.pack(pady = 20)
    mainDeckPosition = LabelFrame(DeckFrame)
    mainDeckPosition.grid(row = 0, column = 0, padx= 10, pady = 10)

    card_button = Button(mainDeckPosition,image = mainDeck_image, command = deal_cards)
    card_button.pack(pady=10)

    disasterDeckPosition = LabelFrame(DeckFrame)
    disasterDeckPosition.grid(row = 0, column = 1,  padx= 10, pady = 10)

    disaster_button = Button(disasterDeckPosition,image = disasterDeck_image)
    disaster_button.pack(pady=10)

    startGamePosition = LabelFrame(DeckFrame)
    startGamePosition.grid(row = 0, column = 2, padx = 10, pady = 10)

    shuffle_button = Button(startGamePosition, text = "Start Game", font =("Helvetica",18), command = shuffle)
    shuffle_button.pack(pady = 20)

    quitGamePosition = LabelFrame(DeckFrame)
    quitGamePosition.grid(row = 0, column = 3, padx = 10, pady = 10)

    shuffle_button = Button(startGamePosition, text = "Quit Game", font =("Helvetica",18), command = root.quit)
    shuffle_button.pack(pady = 20)

    # ______________________________________________________________
    

    FieldFrame = Frame(root)
    FieldFrame.pack(pady = 10)
    
    FirstPosition = LabelFrame(FieldFrame)
    FirstPosition.grid(row = 0, column = 0, padx= 10, pady = 10)

    SecondPosition = LabelFrame(FieldFrame)
    SecondPosition.grid(row = 0, column = 1, padx= 10, pady = 10)

    ThirdPosition = LabelFrame(FieldFrame)
    ThirdPosition.grid(row = 0, column = 2, padx= 10, pady = 10)

    FourthPosition = LabelFrame(FieldFrame)
    FourthPosition.grid(row = 0, column = 3, padx= 10, pady = 10)

    FivePosition = LabelFrame(FieldFrame)
    FivePosition.grid(row = 0, column = 4, padx= 10, pady = 10)
    

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