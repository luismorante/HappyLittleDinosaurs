from tkinter import *
from PIL import ImageTk, Image
import random
import sqlite3
from sqlite3 import Error
from os.path import exists as file_exists

dbFile = r"tpch.sqlite"

print("Open database: ", dbFile)

conn = None
try:
    conn = sqlite3.connect(dbFile)
    print("success")
except Error as e:
    print(e)

sql = """DELETE FROM hand"""
conn.execute(sql)
conn.commit()
sql = """DELETE FROM disasterArea"""
conn.execute(sql)
conn.commit()
sql = """DELETE FROM escapeRoute"""
conn.execute(sql)
conn.commit()
sql = """DELETE FROM scoring"""
conn.execute(sql)
conn.commit()
sql = """DELETE FROM field"""
conn.execute(sql)
conn.commit()
sql = """DELETE FROM upcoming"""
conn.execute(sql)
conn.commit()
sql = """DELETE FROM lastDisaster"""
conn.execute(sql)
conn.commit()


###########      Resize Cards    #################
def resize_cards(card): # for the hand cards for player
    card_img = Image.open(card)

    resized_card_img = card_img.resize((150, 218))

    global resized_card
    resized_card = ImageTk.PhotoImage(resized_card_img)

    return resized_card

def resize_cards_2(card): #for the opponent hand cards
    card_img = Image.open(card)

    resized_card_img = card_img.resize((75, 109))

    global resized_card
    resized_card = ImageTk.PhotoImage(resized_card_img)

    return resized_card

def resize_cards_3(card): # for the dino photos
    card_img = Image.open(card)

    resized_card_img = card_img.resize((200, 350))

    global resized_card
    resized_card = ImageTk.PhotoImage(resized_card_img)

    return resized_card
#_______________________________________________________________


######################### Title Screen ##############################

def title_screen():
    global title_root
    title_root = Tk()

    title_root.title("Screen")
    title_root.overrideredirect(True) #Hide Title
    title_root.geometry("400x300")
    title_root.eval('tk::PlaceWindow . center') #center of screen

    title_label = Label(title_root, text="Title Screen", font = ("Helvetica", 18))
    title_label.pack(pady=50)
    play_Button = Button(title_root, text = "Play", command=choose_your_character)
    play_Button.pack(pady=20)
    play_Button.pack()
    quitButton = Button(title_root, text="Exit", command = title_root.quit)
    quitButton.pack()

    title_root.config(bg = 'LightBlue')

# ________________________________________________________________________


######################### Choose Character ##############################
def choose_your_character():
    title_root.destroy()
    global character_root
    character_root = Tk()

    character_root.config(bg = 'LightGreen')
    
    character_root.title("Screen")
    character_root.overrideredirect(True) #Hide Title
    character_root.geometry("1000x600")
    #character_root.eval('tk::PlaceWindow . center') #center of screen

    title_label = Label(character_root, text="Choose Your Character", font = ("Helvetica", 18))
    title_label.pack(pady=50)

    ButtonFrames = Frame(character_root)
    ButtonFrames.pack(pady = 20)

    global NervousRex_photo
    global Stego_photo
    global CryCeratops_photo
    global BadLuckBronto_photo

    NervousRex_photo = resize_cards_3(f'images/NERVOUS_REX.jpg')
    Stego_photo = resize_cards_3(f'images/STEGO.jpg')
    CryCeratops_photo = resize_cards_3(f'images/CRYCERATOPS.jpg')
    BadLuckBronto_photo = resize_cards_3(f'images/BAD_LUCK_BRONTO.jpg')

    Button_1_Position = LabelFrame(ButtonFrames)
    Button_1_Position.grid(row = 0, column = 1, padx = 10, pady = 10)
    Button_1 = Button(Button_1_Position, text = "NERVOUS REX", image = NervousRex_photo, command =  chose_NERVOUS_REX) #command = main_window("NERVOUS_REX")
    Button_1.pack(pady = 10)

    Button_2_Position = LabelFrame(ButtonFrames)
    Button_2_Position.grid(row = 0, column = 0, padx = 10, pady = 10)
    Button_2 = Button(Button_2_Position, text = "STEGO", image = Stego_photo, command = chose_STEGO)#command = main_window("STEGO")
    Button_2.pack(pady = 10)

    Button_3_Position = LabelFrame(ButtonFrames)
    Button_3_Position.grid(row = 0, column = 2, padx = 10, pady = 10)
    Button_3 = Button(Button_3_Position, text = "CRYCERATOPS", image = CryCeratops_photo, command = chose_CRYCERATOPS)#command = main_window("CRYCERATOPS")
    Button_3.pack(pady = 10)

    Button_4_Position = LabelFrame(ButtonFrames)
    Button_4_Position.grid(row = 0, column = 3, padx = 10, pady = 10)
    Button_4 = Button(Button_4_Position, text = "BAD LUCK BRONTO", image = BadLuckBronto_photo, command = chose_BAD_LUCK_BRONTO)#command = main_window("BAD_LUCK_BRONTO")
    Button_4.pack(pady = 10)

    quitButton = Button(character_root, text="Exit", command = character_root.quit)
    quitButton.pack()
# ________________________________________________________________________


def chose_STEGO():

    global playerkey
    playerkey = 1
    main_window()

def chose_NERVOUS_REX():
    global playerkey
    playerkey = 2
    main_window()

def chose_CRYCERATOPS():
    global playerkey
    playerkey = 3
    main_window()

def chose_BAD_LUCK_BRONTO():
    global playerkey
    playerkey = 4
    main_window()


def main_window():

    character_root.destroy()
    root = Tk()

    print(playerkey)

    #############  Full Screen  ##############
    root.title("HAPPY LITTLE DINOSAURS")
    root.overrideredirect(True) #Hide Title
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    #-_______________________________________
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

        global cardNames
        cardNames = []
        count = 0

        cards = """SELECT h_mainkey
                    FROM hand
                    WHERE h_playerkey = ?
                    ORDER BY h_finger"""
        args = [playerkey]
        playerCards = conn.cursor()
        playerCards.execute(cards, args)
        playerCards = playerCards.fetchall()
        global names
        names = []

        for card in playerCards:
            sql = """SELECT m_name
                    FROM mainCards
                    WHERE m_mainkey = ?"""
            result = conn.cursor()
            result.execute(sql, card)
            results = result.fetchall()[0]
            
            for name in results:
                names.append(name)
                cardNames.append(names[count].replace(' ', '_'))
                count += 1
            # print(cardNames[count])

        if len(cardNames) > 0 and file_exists(f'images/cards/{cardNames[0]}.jpg'):
            card_image1 = resize_cards(f'images/cards/{cardNames[0]}.jpg')
            playercard1.config(image = card_image1)
        else:
            card_image1 = resize_cards(f'images/cards/none.jpg')
            playercard1.config(image = card_image1)

        if len(cardNames) > 1 and file_exists(f'images/cards/{cardNames[1]}.jpg'):
            card_image2 = resize_cards(f'images/cards/{cardNames[1]}.jpg')
            playercard2.config(image = card_image2)
        else:
            card_image2 = resize_cards(f'images/cards/none.jpg')
            playercard2.config(image = card_image2)

        if len(cardNames) > 2 and file_exists(f'images/cards/{cardNames[2]}.jpg'):
            card_image3 = resize_cards(f'images/cards/{cardNames[2]}.jpg')
            playercard3.config(image = card_image3)
        else:
            card_image3 = resize_cards(f'images/cards/none.jpg')
            playercard3.config(image = card_image3)

        if len(cardNames) > 3 and file_exists(f'images/cards/{cardNames[3]}.jpg'):
            card_image4 = resize_cards(f'images/cards/{cardNames[3]}.jpg')
            playercard4.config(image = card_image4)
        else:
            card_image4 = resize_cards(f'images/cards/none.jpg')
            playercard4.config(image = card_image4)

        if  len(cardNames) > 4 and file_exists(f'images/cards/{cardNames[4]}.jpg'):
            card_image5 = resize_cards(f'images/cards/{cardNames[4]}.jpg')
            playercard5.config(image = card_image5)    
        else:
            card_image5 = resize_cards(f'images/cards/none.jpg')
            playercard5.config(image = card_image5)    

    
 

    
    def detect_key_press(event):

        if (len(playerhand) > 0):
            playerkeylist = [playerkey]

            if event.char == '1':
                search = """SELECT h_mainkey
                            FROM hand
                            WHERE h_finger = 1 AND
                                h_playerkey = ?"""
                result = conn.cursor()
                result.execute(search, playerkeylist)
                card = result.fetchall()
                print(card)
                if card:
                    sql = """INSERT INTO field(f_playerkey, f_mainkey)
                            VALUES(?, ?)"""
                    args = [playerkey, card[0][0]]
                    delete = """DELETE FROM hand
                                WHERE h_playerkey = ? AND
                                h_finger = 1"""
                    conn.execute(delete, playerkeylist)
                    conn.commit()
                    conn.execute(sql, args)
                    conn.commit()
                    playerhand[0] = "none"
                    sql = """SELECT *
                            FROM field"""
                    st = conn.cursor()
                    st.execute(sql)
                    print(st.fetchall())

                show_hand()

            if event.char == '2':
                search = """SELECT h_mainkey
                            FROM hand
                            WHERE h_finger = 2 AND
                                h_playerkey = ?"""
                result = conn.cursor()
                result.execute(search, playerkeylist)
                card = result.fetchall()
                print(card)
                if card:
                    sql = """INSERT INTO field(f_playerkey, f_mainkey)
                            VALUES(?, ?)"""
                    args = [playerkey, card[0][0]]
                    delete = """DELETE FROM hand
                                WHERE h_playerkey = ? AND
                                h_finger = 2"""
                    conn.execute(delete, playerkeylist)
                    conn.commit()
                    conn.execute(sql, args)
                    conn.commit()
                    playerhand[1] = "none"
                    sql = """SELECT *
                            FROM field"""
                    st = conn.cursor()
                    st.execute(sql)
                    print(st.fetchall())
                show_hand()

            if event.char == '3':
                search = """SELECT h_mainkey
                            FROM hand
                            WHERE h_finger = 3 AND
                                h_playerkey = ?"""
                result = conn.cursor()
                result.execute(search, playerkeylist)
                card = result.fetchall()
                print(card)
                if card:
                    sql = """INSERT INTO field(f_playerkey, f_mainkey)
                            VALUES(?, ?)"""
                    args = [playerkey, card[0][0]]
                    delete = """DELETE FROM hand
                                WHERE h_playerkey = ? AND
                                h_finger = 3"""
                    conn.execute(delete, playerkeylist)
                    conn.commit()
                    conn.execute(sql, args)
                    conn.commit()
                    playerhand[2] = "none"
                    sql = """SELECT *
                            FROM field"""
                    st = conn.cursor()
                    st.execute(sql)
                    print(st.fetchall())
                show_hand()

            if event.char == '4':
                search = """SELECT h_mainkey
                            FROM hand
                            WHERE h_finger = 4 AND
                                h_playerkey = ?"""
                result = conn.cursor()
                result.execute(search, playerkeylist)
                card = result.fetchall()
                print(card)
                if card:
                    sql = """INSERT INTO field(f_playerkey, f_mainkey)
                            VALUES(?, ?)"""
                    args = [playerkey, card[0][0]]
                    delete = """DELETE FROM hand
                                WHERE h_playerkey = ? AND
                                h_finger = 4"""
                    conn.execute(delete, playerkeylist)
                    conn.commit()
                    conn.execute(sql, args)
                    conn.commit()
                    playerhand[3] = "none"
                    sql = """SELECT *
                            FROM field"""
                    st = conn.cursor()
                    st.execute(sql)
                    print(st.fetchall())
                show_hand()

            if event.char == '5':
                search = """SELECT h_mainkey
                            FROM hand
                            WHERE h_finger = 5 AND
                                h_playerkey = ?"""
                result = conn.cursor()
                result.execute(search, playerkeylist)
                card = result.fetchall()
                print(card)
                if card:
                    sql = """INSERT INTO field(f_playerkey, f_mainkey)
                            VALUES(?, ?)"""
                    args = [playerkey, card[0][0]]
                    delete = """DELETE FROM hand
                                WHERE h_playerkey = ? AND
                                h_finger = 5"""
                    conn.execute(delete, playerkeylist)
                    conn.commit()
                    conn.execute(sql, args)
                    conn.commit()
                    playerhand[4] = "none"
                    sql = """SELECT *
                            FROM field"""
                    st = conn.cursor()
                    st.execute(sql)
                    print(st.fetchall())
                show_hand()


    root.bind('<Key>', detect_key_press)

    #Shuffle the cards
    def shuffle():
        #Define our Deck
        global deck
        global playerhand
        global opponenthand1
        global opponenthand2
        global opponenthand3


        ########## Build Deck from Database ######### 
        cards = """SELECT *
                    FROM mainCards"""
        cardList = conn.cursor()
        cardList.execute(cards)
        qtyCardList = cardList.fetchall()
        deck = []
        for card in qtyCardList:
            for i in range(card[5]):
                deck.append(card)
        # print(qtyCardList)
        # deck = ["COOL_STICK","HANDY_PAN","GRAVE_MAKER","BONEHEAD","RUNHOMEBAT","BOW_AND_DINO","STING_STABBER","ICED_PTEA","METEOR_CANNON"]
        # for i in range (9):
        #     deck.append(deck[i])
        # for i in range (18):
        #     deck.append(deck[i])
        playerhand = []
        # ___________________________________________

        #card = random.choice(deck)
        random.shuffle(deck)

        sql = """INSERT INTO hand(h_playerkey, h_mainkey, h_finger)
                VALUES(?, ?, ?)"""


        playerkeys = [1, 2, 3, 4]
        playerkeys.remove(playerkey)
        print(playerkeys)

        opponenthand1 = []
        opponenthand2 = []
        opponenthand3 = []
        for i in range (5):
            card = deck[0]
            mainkey = card[0]
            args = [playerkey, mainkey, i + 1]
            conn.execute(sql, args)
            conn.commit()
            playerhand.append(card)
            deck.pop(0)

            card = deck[0]
            mainkey = card[0]
            args = [playerkeys[0], mainkey, i + 1]
            conn.execute(sql, args)
            conn.commit()
            opponenthand1.append(card)
            deck.pop(0)

            card = deck[0]
            mainkey = card[0]
            args = [playerkeys[1], mainkey, i + 1]
            conn.execute(sql, args)
            conn.commit()
            opponenthand2.append(card)
            deck.pop(0)

            card = deck[0]
            mainkey = card[0]
            args = [playerkeys[2], mainkey, i + 1]
            conn.execute(sql, args)
            conn.commit()
            opponenthand3.append(card)
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



title_screen()

mainloop() 

try:
    conn.close()
    print("success")
except Error as e:
    print(e)
