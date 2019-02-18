import PIL.ImageGrab
from PIL import Image
import os
import pytesseract
import time
import mouse
import keyboard

# GLOBABLS
# -------------------

x_pad = 175
y_pad = 224

adventuring_link='https://www.freekigames.com/wizard101-adventuring-trivia'
kingsisle_link='https://www.freekigames.com/kingsisle-facts-trivia'
conjuring_link='https://www.freekigames.com/wizard101-conjuring-trivia'
magical_link='https://www.freekigames.com/wizard101-magical-trivia'
marleybone_link='https://www.freekigames.com/wizard101-marleybone-trivia'
mystical_link='https://www.freekigames.com/wizard101-mystical-trivia'
spellbinding_link='https://www.freekigames.com/wizard101-spellbinding-trivia'
spells_link='https://www.freekigames.com/wizard101-spells-trivia'
wizard_city_link='https://www.freekigames.com/wizard101-wizard-city-trivia'
zafaria_link='https://www.freekigames.com/wizard101-zafaria-trivia'

see_your_score=(315, 239)
first_answer_pos=(106, 188)
second_answer_pos=(543, 188)
third_answer_pos=(107, 231)
fourth_answer_pos=(543, 231)
next_question=(499, 283)
adress_bar=(710, -169)
focus_on_browser=(830, -214)
delay=4

#<full_path_to_your_tesseract_executable>
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

answer={}
answer[r'What special plant was Barley developing in his Garden?']='Woodsmen'
answer[r'In Azteca, Morganthe enlisted the help of the:']='Necromancer'
answer[r'Morganthe got the Horned Crown from the Spriggan:']=r"Gi"
answer[r'Who tells you: "A shield is just as much a weapon as the sword."']='wing'
answer[r'What badge do you earn by defeating 100 Samoorai?']='Yo'
answer[r'Who taunts you with: "Wizard, you will know the meaning of the word pain after we battle!"']='A'
answer[r'Who needs the healing potion from Master Yip?']='H'
answer[r'Who taunts you with: "Prepare to be broken, kid!"']='anker'
answer[r'Who tries to raise a Gorgon Army?']='horcys'
answer[r'Who makes the harpsicord for Shelus?']='Dark'
answer[r'Where has Pharenor been imprisoned?']='y'
answer[r'Who helps Morganthe find the Horn of Huracan?']='Be'
answer[r'What did Prospector Zeke lose in Marleybone?']='The Stray Cats'
answer[r'What is a very common last name of the cats in Marleybone?']="Leary"
answer[r'What time does the clock always read in Marleybone?']='1' #Doesn't always recognize the points
answer[r'What color are the Marleybone mailboxes?']='Red'
answer[r"Who is not an officer you'll find around Marleybone?"]='more'
answer[r'What event is Abigail Doolitile sending out invitations for?']='ceman'
answer[r"Which is not a street in Regent's Square?"]='en Ave'
answer[r'Arthur Wethersfield is A...']='Dog'
answer[r'Which of these folks can you find in the Royal Museum?']='Pembroke'
answer[r'What two names are on the Statues in the Marleybone cathedral?']='ard and Saint Hubert'
answer[r'What sort of beverage is served in Air Dales Hideaway?']='Root Beer'
answer[r'What course did Herold Digmoore study?']='Myths for'
answer[r'What school is the spell Dark Nova']='Shadow'
answer[r'What is the name of the secret society in Krokotopia']='Fang'
answer[r'Who is in the top level of the Tower of the Helephant?']='Lyon'
answer[r'How long do you have to wait to join a new match after fleeing in PVP?']='5 m'
answer[r'Shaka Zebu is known best as:']='The Greatest' 
answer[r'Which of these are not a lore spell?']='Dragon'
answer[r'What hand does Lady Orie! hold her wand in?']='question, she has a sword'
answer[r'What does the Time Ribbon Protect against?']='me Flux'
answer[r'In Grizzleheim, the Ravens want to bring about:']='The Eve'
answer[r"What is Professor Falmea's favorite food?"]='Arrab'
answer[r'What is the name of the new dance added with Khrysalis?']='The bee dance'
answer[r'An unmodified Sun Serpent does what?']='900'
answer[r'Who is the King of the Burrowers?']='Pyat Mou'
answer[r'What is the shape on the weather vanes in the Shopping District?']='Ha'
answer[r'Which Queen is mentioned in the Marleybone book "The Golden Age"?']='en'
answer[r'How many portal summoning candles are in the Burial Mound?']='Three'
answer[r'The Swordsman Destreza was killed by:']='Gorgon'
answer[r'What level must you be to wear Dragonspyre crafted clothing?']='' #does not recognize digits
answer[r'What was the name of the powerful Grendel Shaman who sealed the runic doors?']='Thu'
answer[r'What did Abigail Dolitle accuse Wadsworth of stealing?']='Golden Ruby'
answer[r'Kirby Longspear was once a student of which school of magic?']='Dea'
answer[r'Who Is NOT a member of the Council of Light?']='Cyrus Drake'
answer[r'What book was Anna Flameright accused of stealing?']='Advanced'
answer[r"Sir Edward Halley is the Spiral's most famous:"]='Aztecosaurologist'
answer[r'What type of rank 8 spell is granted to Death students at level 587']='Damage + Do'
answer[r"What is unique about Falmea's Classroom?"]='ch marks'
answer[r'Which of these is NOT a Zafaria Anchor Stone?']='R'
answer[r'What is the name of the book stolen from the Royal Museum?']='nomicon'
answer[r'What determines the colors of the manders in Krok?']='Where they come from and their school of focus'
answer[r"Who is Bill Tanner's sister?"]='Sarah Tanner'
answer[r'What colors make up the KingsIsle logo?']='Orange and Grey'
answer[r'Kingsisle makes games for which audience?']='ages'
answer[r"What Kings!sle mobile game ties into a player's pet in Wizard101?"]='Grub Guardian'
answer[r"What year was Kingsisle's founded?"]='2005'
answer[r"What is the name of Kingsisie's free game site?"]='Free' #confuses with KiFree Games
answer[r'Who founded Kingsisle Entertainment, Inc.?']='El'
answer[r'What year did Kingsisle launch Wizard101?']='2008'
answer[r'Which Plano charity has Kingsisle donated to?']='Center at Legacy'
answer[r'Which celebrity composed music for a KingsIsle game?']='Nick Jonas'
answer[r"In what state are Kingsisle's offices located?"]='Texas'
answer[r"What was the name of Kingsisle's first game?"]='rd101'
answer[r'What countries can play Wizard101?']='the above'
answer[r'Which below are NOT a type of Oni in MooShu?']='Ruby'
answer[r'Who is the Registrar of Pigswick Academy?']='Dowager'
answer[r'Who prophesizes this? "The mirror will break, The horn will call, From the shadows I strike , And the skies will fall.."']='Morgan'
answer[r"What can be used to diminish the Nirin's powers in Krokotopia?"]='Flame Gems'
answer[r"What's the name of the balance tree?"]='N'
answer[r'Merle Ambrose is originally from which world?']='Avalon'
answer[r'What color is the door inside the boys dormroom?']='Red'
answer[r'What book does Professor Drake send you to the library to check out?']='Book on the Wumpus'
answer[r'Zafaria is home to what cultures?']='Gorilas'
answer[r'What is the shape of the pink piece in potion motion?']='Hear'
answer[r'What did Prospector Zeke lose track of in MooShu?']='Oysters'
answer[r'Which of these locations is not in Wizard City?']='more'
answer[r'What transports you from place to place in Marleybone?']='Hot Air Balloons'
answer[r'What time of day is it always in Marleybone?']='Night'
answer[r'What style of artifacts are in the Royal Museum?']='pian'
answer[r'Who is the dangerous criminal that is locked up, but escapes from Newgate Prison?']='Meow'
answer[r"What is Sgt. Major Talbot's full name?"]='ester Quimby T'
answer[r"What initials were on the doctor's glove?"]='' #Always makes mistakes, doesn't recognize XX
answer[r"Which symbol is not on the stained glass window in Regent's Square?"]='A Tennis'
answer[r'Thaddeus Price is the Pigswick Academy Professor of what school?']='Tempest'
answer[r"In Reagent's Square, the Professor is standing in front of a:"]='egraph Box'
answer[r'Who gives you permission to ride the boat to the Krokosphinx?']='Major Ta'
answer[r'King Axaya Knifemoon needs what to unify the people around him?']='The Badge'
answer[r'Where is the only pure fire in the Spiral found?']='Wiz'
answer[r'Who did Falynn Greensleeves fallin love with?']='de Logres'
answer[r'What is used to travel to the Isle of Arachnis?']='Ice Archway'
answer[r'Which villain terrorizes the fair maidens of Marleybone?']='Scatcher'
answer[r'What was Ponce de Gibbon looking for in Azteca?']='The Water'
answer[r'Who asks you to find Khrysanthemums?']='se Merrywea'
answer[r"Who is the Emperor of Mooshu's Royal Guard?"]='Noboru'
answer[r"King Neza is Zenzen Seven Star's:?"]='Grand'
answer[r'Sumner Fieldgold twice asks you to recover what for him?']='Shrub'
answer["What does Silenus name you once you've defeated Hades?"]='Archon'
answer['Who grants the first Shadow Magic spell?']='Sophia'
answer["Who is Haraku Yip's apprentice?"]='Hoa'
answer['Cassie the Ponycorn teaches this kind of spell:']='Pr'
answer[r"If you're a storm wizard with 4 power pips and 3 regular pips, how powerful would your supercharge charm be?"]='110%'
answer['Who teaches you balance magic?']='' #Can't find Alhazred
answer['Mortis can teach you this.']='nq'
answer['What term best fits Star Magic Spells?']='Auras'
answer['If you can cast Storm Trap, Wild Bolt, Catalan, and the Tempest spell, what are you polymorphed as?']='P'
answer['What term best fits Sun Magic Spells?']='Enchantment'
answer[r"Which spell can't be cast while polymorphed as a Gobbler?"]='sky'
answer[r"Tish'Mah specializes in spells that mostly affect these:"]='ons'
answer['Ether Shield protects against what?']='e and Death'
answer['Mildred Farseer teaches you what kind of spell?']='D'
answer['What level of spell does Enya Firemoon Teach?']='80'
answer['What are the school colors of Balance?']='Tan and Mar'
answer['What school is all about Creativity?']='S'
answer['Who is the Princess of the Seraphs?']='ne' #Can choose Desane, depends on the order
answer[r'Who is the Wizard City mill foreman?']='Sunblade'
answer["What is Mindy's last name (she's on Colossus Blvc)?"]='ecrown'
answer['What are the main colors for the Myth School?']='e and G' #Can choose Gold and Green, depends on the order
answer['What school does Malorn Ashthorn think is the best?']='Death'
answer['Who is the Fire School professor?']='Dalia Falmea'
answer['What is the gemstone for Balance?']='t'
answer['What is something that the Gobblers are NOT stockpiling in Colossus Way?']='B'
answer['Who sang the Dragons, Tritons and Giants into existance?']='by'
answer['What is the name of the grandfather tree?']='by'
answer['What does Lethu Blunthoof says about Ghostmanes?']='You'
answer['Jambo means:']='He'
answer['Zebu Blackstripes legendary blade was called:']='The Sword'
answer['Esop Thompaw gives you a magic:']='Djembe Drum'
answer['Who is not one of the Zebu Kings:']='er'
answer['Baobab is governed by:']='A Counc'
answer['Rasik Pridefall is:']='An'
answer[r"Zemunda's great assassin is known as:"]='the Jacka'
answer['Vir Goodheart is an assistant to:']='Ras'
answer['Who is the missing prince?']='T'
answer['Zebu Blackstripes legendary blade was forged:']='Valenc'
answer['Umio Sunchaser hired who as a local guide?']='Redband'
answer[r'What school is the Gurtok Demon focused on?']='nce'
answer['Who is the Nameless Knight?']='Malory'
answer[r'Which one of these are not a symbol on the battle sigil?']='Wand'
answer['Who guards the entrance to Unicom Way?']='son' #Stillson or Stinson
answer['Which of these locations is no! in Wizard City?']='Dwgmore 51am'
answer['Why are the Gobblers so afraid to go home?']='Witches'
answer[r'What currency do Kings!sle MMO games use?']='Cr'
answer[r'What kind of games does Kingsisle make?']='(MMOs)'
answer[r'What year did Kings!Isie launch Pirate 101?']='2012'
answer[r"What was the name of Kingsisle's first mobile game?"]='Wi'
answer[r'Who thinks you are there to take their precious feathers?']='Takeda Kanryu'
answer[r'The Swallows of Caliburn migrate to Avalon from where each year?']='bone'
answer[r'Who taunts: Why I oughta knock you to the moon, you pesky litle creep!']='Mugsy'
answer[r"What is fying around in Regent's Square?"]='Newspapers'
answer['Who tells you how to get to Aquila?']='eston'
answer['Who is the only person who knows how to enter the Tomb of Storms?']='Hetch'
answer[r'Who haunts the Night Warrens?']='Nos'
answer['Who can teach you the Life Shield Spell?']='Green'
answer['What type of spells are Ice, Fire, and Storm?']='ement'
answer['What is the name of the bridge in front of the Cave to Nightside?']='R'
answer['Where is Sabrina Greenstar?']='F'
answer[r'Who taught Life Magic before Moolinda Wu?']='Drake'
answer['Who resides in the Hedge Maze?']='Lady'
answer['What is the name of the Ice Tree in Ravenwood?']='Ke'
answer[r"Sir Reginal Baxby's cousin is:"]='Green'
answer['Bellog is first found in:']='The Sook'
answer['Koyate Ghostmane accuses the player of.']='thie'
answer['Which Aztecan ponders the Great Questions of Life?']='losora'
answer[r"What year did Kingsisle's Wizard101 get nominated for the MMO Hall of Fame?"]='2014'
answer['Why are the pixies and faeries on Unicorn Way evil?']='bones'
answer['What is the title of the book that is floating around the Wizard City Library?']='Basic'
answer['How many worlds of The Spiral are unlocked as of May 21st, 20147']='12'
answer[r'Who was the greatest Aquilan Gladiator of all time?']='Dima'
answer[r'Hrundle Fjord is part of what section of Grizzleheim?']='usk'
answer['Who tells you to speak these words only unto your mentor: "Meena Korio Jajukal"']='Dryad'
answer[r"How many pips does it cost to cast Dr. Von's Monster?"]=''  #Doesn't recognize one-digit numbers
answer['Which spell would not be very effective when going for the elixir vitae Badge?']='ang'
answer["What is Diego's full name?"]='Santiago Qua' #Can throw an error, because of word order
answer[r'What is the name of the school newspaper? Boris Tallstaff knows...']='B'
answer['What does every Rotting Fodder in the Dark Caves carry with them?']='A spade'
answer[r"Who are Hannibal Onetusk's brother and co-pilot?"]='go and Sobaka' #cannot recognize Mago
answer['The Inzinzebu Bandits are harassing the good merchants in:']='Baobab Market'
answer[r'The Fire Lion Ravagers are led by:']='Nergal'
answer[r'Who is the Bear King of Grizzieheim?']='Va'
answer[r'Which Austin charity has Kingsisle donated to?']='She'
answer[r'What was the name of the first charity Mount created by Kingsiste called?']='Meowmodon'
answer['In what world would you find the Spider Temple']='Za'
answer['Which is the only school left standing in Dragonspyre?']='Fire'
answer[r'How many pips does it cost to cast Stormzilla?']='' #Doesn't recognize one-digit
answer['Inyanga calls Umlio a']='Fire feather'
answer['Unathi Nightrunner is:']='Ba'
answer['Who takes you across the River of Souls?']='Charon'
answer[r"What isn't a shadow magic spell?"]='bon'
answer['Which Fire spell both damages and heals over time?']='Power'
answer['Who was ordered to guard the Sword of Kings?']='Rose'
answer['What does Forsaken Banshee do?']='375'
answer["Who sells Valentine's Day items in Wizard City?"]='Heartsong'

"""

All coordinates assume a screen resolution of 1366x768, and Firefox 62.0.3
maximized with the Bookmarks turned off.
Nothing else changed.
x_pad=134
y_pad=248
Play area = x_pad, y_pad, x_pad+994, y_pad+337
Coordinates of the buttons :
Move away : (x_pad+318, y+pad+698)
Top Left : (x_pad+106,y_pad+188)
Top Right : (x_pad+543, y_pad+188)
Bottom left : (x_pad+107, y_pad+235)
Bottom right : (x_pad+543, y_pad+235)
Next Question : (x_pad+497, y_pad+287)
See your score : (x_pad+309, y_pad+231)
Take another quiz : (x_pad+342, y_pad+227)
View all Wizard101 Trivia : (x_pad+730, y_pad+587)
Coordinates of the questions and answers :
Question : (x_pad+11,y_pad+104,x_pad+990,y_pad+171)
Answer Top Left : (x_pad+11,y_pad+171, x_pad+528, y_pad+212)
Answer Top Right : (x_pad+528,y_pad+171, x_pad+990, y_pad+212)
Answer Bottom Left :(x_pad+11, y_pad+212, x_pad+528, y_pad+252)
Answer Bottom Right : (x_pad+528, y_pad+212, x_pad+990, y_pad+252)
"""

def grabquestion():
    box=(x_pad+30,y_pad+250,x_pad+950,y_pad+10)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\question.png', 'PNG')

def grabquestion():
    box=(x_pad+11,y_pad+100,x_pad+990,y_pad+171)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\question.png', 'PNG')

def grabanswer1():
    box=(x_pad+126,y_pad+168, x_pad+528, y_pad+212)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\answer1.png', 'PNG')
def grabanswer2():
    box=(x_pad+560,y_pad+168, x_pad+990, y_pad+212)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\answer2.png', 'PNG')
def grabanswer3():
    box=(x_pad+126, y_pad+205, x_pad+528, y_pad+245)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\answer3.png', 'PNG')
def grabanswer4():
    box=(x_pad+560, y_pad+205, x_pad+990, y_pad+245)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\answer4.png', 'PNG')

def grabanswers():
    grabanswer1()
    grabanswer2()
    grabanswer3()
    grabanswer4()

def grabscreen():
    grabquestion()
    grabanswers()

def textit(case):    #transforms answers to string
    ans=pytesseract.image_to_string(Image.open(os.getcwd()+'\\answer'+str(case)+'.png'))
    return ans

def prtans():   #prints all scanned answers, used for debugging
    print(textit(1))
    print(textit(2))
    print(textit(3))
    print(textit(4))

def qtt():          #transforms question to string
    question=pytesseract.image_to_string(Image.open(os.getcwd()+r'\question.png'))
    return question


def leftClick():             #Clicks left
    mouse.click(button='left')

def mousePos(cord):   #Moves the mouse to the coordinates
    mouse.move(x_pad + cord[0], y_pad + cord[1], absolute=True, duration=0.1)


def get_cords():   #Gets the coordinates, used for debugging
    x,y = mouse.get_position()
    x = x - x_pad
    y = y - y_pad
    print (x,y)
    return (x,y)

def move_away():
    mousePos((751, 415))



def findanswer(question):     #Finds and presses the right answer
    if answer[question] in textit(1):
        print("First answer")
        mousePos(first_answer_pos)
    elif answer[question] in textit(2):
        print("Second answer")
        mousePos(second_answer_pos)
    elif answer[question] in textit(3):
        print("Third answer")
        mousePos(third_answer_pos)
    elif answer[question] in textit(4):
        print("Fourth answer")
        mousePos(fourth_answer_pos)
    print("Moved")
    leftClick()
    print("Clicked")
    time.sleep(1)
    mousePos(next_question)
    leftClick()
    time.sleep(1)


def play(i=0):        #Runs the bot
    is_ok=True
    while i<12:
        if i==0 :
            time.sleep(delay)
        else:
            time.sleep(5)
        print("Answering question " + str(i+1))
        grabquestion()
        time.sleep(2)
        grabanswers()
        try:
            answer[qtt()]
            time.sleep(0.5)
            findanswer(qtt())
        except KeyError:
            print('Not set')
            is_ok=False
        i+=1
        if not is_ok:
            break
    time.sleep(delay)
    mousePos(see_your_score)
    leftClick()

def change_trivia(link=adventuring_link):
    mousePos(focus_on_browser)
    leftClick()
    mousePos(adress_bar) #Goes to the main menu
    leftClick()          #By clicking, it automatically selects all the text
    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('delete')
    keyboard.write(link, delay=0.05) #Changes the url
    keyboard.press_and_release('delete') #Ensures that there is no URL left
    time.sleep(1.5)
    keyboard.press_and_release('enter') #accesses the site
    move_away() #Goes to the "Choose Trivia" menu
    time.sleep(delay)
    leftClick()

def pick_trivia(name):
    if name=="Adventuring":
        change_trivia(adventuring_link)
    elif name=="Kingsisle":
        change_trivia(kingsisle_link)
    elif name=="Conjuring":
        change_trivia(conjuring_link)
    elif name=="Magical":
        change_trivia(magical_link)
    elif name=="Marleybone":
        change_trivia(marleybone_link)
    elif name=="Mystical":
        change_trivia(mystical_link)
    elif name=="Spellbinding":
        change_trivia(spellbinding_link)
    elif name=="Spells":
        change_trivia(spells_link)
    elif name=="Wizard City":
        change_trivia(wizard_city_link)
    elif name=="Zafaria":
        change_trivia(zafaria_link)
    play(0)
    while not keyboard.is_pressed('enter'):
        time.sleep(0.1)

def main(name='Adventuring'):                         
    if name=="Adventuring":
        pick_trivia("Adventuring")
        time.sleep(delay)
        pick_trivia("Kingsisle")
        time.sleep(delay)
        pick_trivia("Conjuring")
        time.sleep(delay)
        pick_trivia("Magical")
        time.sleep(delay)
        pick_trivia("Marleybone")
        time.sleep(delay)
        pick_trivia("Mystical")
        time.sleep(delay)
        pick_trivia("Spellbinding")
        time.sleep(delay)
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
        time.sleep(delay)
    elif name=="Kingsisle":
        pick_trivia("Kingsisle")
        time.sleep(delay)
        pick_trivia("Conjuring")
        time.sleep(delay)
        pick_trivia("Magical")
        time.sleep(delay)
        pick_trivia("Marleybone")
        time.sleep(delay)
        pick_trivia("Mystical")
        time.sleep(delay)
        pick_trivia("Spellbinding")        
        time.sleep(delay)
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
    elif name=="Conjuring":
        pick_trivia("Conjuring")
        time.sleep(delay)
        pick_trivia("Magical")
        time.sleep(delay)
        pick_trivia("Marleybone")
        time.sleep(delay)
        pick_trivia("Mystical")
        time.sleep(delay)
        pick_trivia("Spellbinding")
        time.sleep(delay)
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
        time.sleep(delay)
    elif name=="Magical":
        pick_trivia("Magical")
        time.sleep(delay)
        pick_trivia("Marleybone")
        time.sleep(delay)
        pick_trivia("Mystical")
        time.sleep(delay)
        pick_trivia("Spellbinding")
        time.sleep(delay)
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
        
    elif name=="Marleybone":
        pick_trivia("Marleybone")
        time.sleep(delay)
        pick_trivia("Mystical")
        time.sleep(delay)
        pick_trivia("Spellbinding")
        time.sleep(delay)
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
    elif name=="Mystical":
        pick_trivia("Mystical")
        time.sleep(delay)
        pick_trivia("Spellbinding")
        time.sleep(delay)
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
    elif name=="Spellbinding":
        pick_trivia("Spellbinding")
        time.sleep(delay)
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
    elif name=="Spells":
        pick_trivia("Spells")
        time.sleep(delay)
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
    elif name=="Wizard City":
        pick_trivia("Wizard City")
        time.sleep(delay)
        pick_trivia("Zafaria")
    elif name=="Zafaria":
        pick_trivia("Zafaria")

