import PIL.ImageGrab
from PIL import Image
import os
import pytesseract
import time
import win32api, win32con

# GLOBABLS
# -------------------

x_pad = 134
y_pad = 248

answer={}
answer[r'What special plant was Barley developing In his Garden?']='Woodsmen'
answer[r'In Azteca, Morganthe enlisted the help of the:']='Necromancer'
answer[r'Morganthe gar the Horned Crown from the Sprlggan:']=r"G‘"
answer['who tells yau\' "A shield fsjusf as much a weapon as the sword. "']='Mavra'
answer[r'What badge do you earn by defeating 100 Samoorai?']='Yopmbo'
answer['Who taunts you with: "Mzald, you Will know the meaning of the ward pain after we battle,”']='chl'
answer[r'Who needs the healing pDIIDﬂ from Master Yip?']='H'
answer['Wha taunts you With\' "Prepare to be broken, Kid!"']='anker'
answer[r'Who tries to raise a Gorgon Army?']='horcys'
answer[r'Who makes the harpslcard far Shelus?']='Dark'
answer[r'Where has Pharenar been Imprisoned?']='Skyl'
answer[r'Who helps Morganthe ﬁnd the Horn of Huracan?']='Beuoq'
answer[r'What did Prospector Zeke lose In Marleybons?']='The Stray Cats'
answer[r'What is a very common last name of the cats in Marleybone?']="O'Leary"
answer[r'What time does the clack always read In Marleybons?']='155'
answer[r'What color are the Marleybane mailboxes?']='Red'
answer[r"Who Is not an ofﬁcer you'll ﬁnd around Marleybone?"]='Dwgmore'
answer[r'What event is Abigail Doolittle sending out invitations for?']='ceman'
answer[r"Which is no! a street in Regent's Square?"]='en Ave'
answer[r"Anhur Wethersﬁeld is A.'.."]='Dog'
answer[r'Which of these folks can you ﬁnd in the Royal Museum?']='Pembroke'
answer[r'What two names are on the Statues in the Marleybone cathedral?']='Saml Bernard and Salnt Huberl'
answer[r'What sort of beverage is served in Air Dales Hideaway?']='Root Beer'
answer[r'What course did Herold D/‘gmoore study?']='Myths for Parhament'
answer[r'What school is the spell Dark Nova']='Shadow'
answer[r'What is the name of the secret society in Krakotopia']='Fang'
answer[r'Who is in the top level of the Tower of the Hs/sphanr?']='Lyon Loreslnker'
answer[r'How long do you have to wait tajam a new match after fleeing In PVP?']='5 mmu'
answer[r'Shaka Zebu Is known best as:']='The Grealesl Lwlng Zebra Wamur'
answer[r'Which ofthese are not a [are spell?']='ere Dragon'
answer[r'What hand does Lady Oriel hold her wand in?']='she has a sword'
answer[r'What does the Time Ribbon Protect against?']='me Flux'
answer[r'In Grizzlshsr‘m, the Ravens want to bring about:']='The Everwmler,'
answer[r'What Is Professor Falmsa’s favorite food?']='Arrab‘ala'
answer[r'What is the name of the new dance added WIIh Khrysalls?']='The bee dance'
answer[r'An unmodiﬁed Sun Serpent does what?']='900 01000 F‘re Damage + 300 Fve Damage'
answer[r'Who is the King of the Burrowers?']='Mournmgsword'
answer[r'What is the shape on the weather vanes in the Shopping District?']='Ha'
answer[r'Which Queen is mentioned in the Marleybone book "The Golden Age"?']='en'
answer[r'How many portal summoning candles are in the Burial Mound?']='Three'
answer[r'The Swordsman Destreza was killed by:']='Gorgon'
answer[r'What level must you be to wear Draganspyre crafted clothing?']='33'
answer[r'What was the name of the powerful Grendel Shaman who sealed the runic doors?']='Thu‘lnn'
answer[r'What did Abigail Dollms accuse Wadsworth of stealing?']='Golden Ruby'
answer[r'Kirby Longspear Was once a student of which school of magic?']='Dea'
answer[r'Who Is NOT a member of the Council of Light?']='Cyrus Drake'
answer[r"What book was Anna Flamen'ghf accused of stealing?"]='Advanced'
answer[r"Sir Edward Halley is the Spiral’s most famous'"]='Aziecusaumloglsl'
answer[r'What type of rank 8 spell is granted to Death students a! level 58?']='Damage + DoT'
answer[r'WhEIIS unique about Falmsa’s Classroom?']='ch marks '
answer[r'Which of these Is NOT a Zafarla Anchor Stone?']='Ras‘k Anchur Stone'
answer[r'What is the name of the book stolen from the Royal Museum?']='The Krukunomlcon'
answer[r'What determines the colors of the manders in Krok?']='Where may come'
answer[r"Who is Bill Tanner's sister?"]='Sarah Tanner'
answer[r'What color: make up the ngs/sle Iago?']='Orange and Grey'
answer[r'Kings/s/s makes games for which audience?']='ages'
answer[r"What Kingsls/e mobile game ties into a player's per in Wizardw1?"]='Grub Guard‘an'
answer[r'What year was KIngs/s/s’s founded?']='2005'
answer[r'WhEIIS the name of Kingsls/s’s free game site?']='FreeK'
answer[r'Who founded Kfngsls/e Entertainment, Inc. .7']='E‘Ie A'
answer[r'What year did ngs/sle launch Wizard101?']='2008'
answer[r'Which Plano charity has Kfngsls/e donated to?']='Center at Legacy'
answer[r'Which celebrity composed music for a Kfngsls/e game?']='N‘ck Jona'
answer[r'In whatstats are Kingsls/s’s ofﬁces located?']='Texas'
answer[r'What was the name of Kingsls/s’s ﬁrst game?']='WIZard101'
answer[r'What countries can play W/‘zard101?']='the above'
answer[r'Which below are NOT a type of Om In Maashu?']='Ruby'
answer[r'Who Is the Registrar of PIgSWICk Academy?']='Mrs Dowager'
answer[r'Who prophss/‘zes this? "The minor Will break, The ham Will Call, From the shadows I SIIIKE , And the skies will fall..."']='Morganme'
answer[r"What can be used to diminish the Nirr'ni’s powers in Kmkctcpia?"]='F‘ame Gems'
answer[r"What's the name ofths balance tree?"]='N'
answer[r'Merle Ambrose Is originally from which world?']='Avalon'
answer[r'What color is the door/‘ns/‘de the boys dormroom?']='Red'
answer[r'What book does Professor Drake send you to the library to check out?']='Book an the Wumpus'
answer[r"Zafan'a is home to what cultures?"]='Gonna'
answer[r'What is the shape of the pink piece In potion motion?']='Hearl'
answer[r'What did Prospector Zeke lose track of in Mooshu?']='Bme Oysters'
answer[r'Which of these locations is no! in Wizard City?']='Dwgmore 51am'
answer[r'What transports you from place to place In Marlsybons?']='HotAlr Bal‘uuns'
answer[r'What time of day is it always in Marleybone?']='nghl'
answer[r'What style of artifacts are in the Royal Museum?']='Kru'
answer[r'Who Is the dangerous criminal that is locked up, but escapes from Newgate Prison?']='Meowwarty'
answer[r"What is Sgt. Major Talbat's full name?"]='ester Qmmby Tam m'
answer[r'Whatmmals were on the doctor’s glove?']='' #Always makes mistakes, doesn't recognize XX
answer[r'Which symbol Is no! on the stained glass window in Regent’s Square?']='ATenm'
answer[r'Thaddeus Price is the P/‘gswfck Academy Professor of what school?']='Tempest'
answer[r"In Reagent's Square, the Professor is standing in front ofa'"]='egraph Box'
answer[r'Who gives you permission to ride the boat to (he Krokosphinx?']='Sergenl Major Ta'
answer[r'King Axaya Knifemoon needs what to unify the people around him?']='The Badge 0! Leadership'
answer[r'Where is the only pure fire In the Spiral found?']='Wizard '
answer[r'Who did Fa/ynn Greensleeves fall in love with?']='Swr Mahck de Lugres'
answer[r'What is used to {re ve/ to the Isle of Arachnis .7']='Ice Archway'
answer[r'Which villain terrorize: the fair maidens af Marleybons?']='Jaques the Scatcher'
answer[r'What Was Ponce de Gibbon lacking for In Aztecs?']='The Water 0!'
answer[r'Who asks you to find Khrysanthemums?']='se Merrywea'
answer[r"Who is the Emperor of Mooshu's Royal Guard?"]='Noboru Akwtame'
answer[r"King Neza Is anzsn Seven Star’s'?"]='Grandlalher'
answer[r'Sumner Fis/dgo/d twice asks you to recover what for him?']='Shrubbeﬂeﬁ'
answer["What does Silenus name you once you've defeated Hades?"]='Archun'
answer['Who grants the ﬁrst Shadow Magic spell?']='Sopma DarkSMe'
answer["Who is Haraku Yip's apprentice?"]='Bmh Hua'
answer['Cassie the Panycarn teaches this kind of spell:']='Prlsm'
answer["lfyou'rs a storm wizard with 4 power pips and 3 regular pips, how powerful would your supercharge charm be?"]='110%'
answer['Who teaches you balance magic?']='hazred'
answer['Moms can (each you (his.']='Tranqumze'
answer['What term best ﬁts Star Magic Spells?']='Auras'
answer['If you can cast Storm Trap, Wild Bolt, Catalan, and the Tempest spell, what are you polymorphsd as?']='Plera'
answer['What term best fits Sun Magic Spells?']='Enchantment'
answer[r"Which spell can'tbs cast WhI/E polymorphsd as a Gobbler?"]='m the sky'
answer[r'T/‘sh’Mah specializes In spells that mostly affect these.']='Mlnlons'
answer['Ether Shield protects against what?']='e and Death atlacks'
answer['Mildred Farsserfeaches you what kind of spa”?']='Dwspe'
answer['What level of spell does Enya Filemoon Teach?']='80'
answer['What are the school colors of Balance?']='Tan and Maru'
answer['What school Is all about Creativity?']='Slorm'
answer['Who is the Princess of the Seraphs?']='ne' #Can choose Desane, depends on the order
answer[r'Who is the Wizard City m/‘N foreman?']='Sohomer Sunb‘ade'
answer["What is andy’s last name (she's on Colossus Blvd)?"]='walecruwn'
answer['What are the mam calars far the Myth School?']='e and G' #Can choose Gold and Green, depends on the order
answer['What school does Malarn Ashtharn think Is the best?']='Death'
answer['Who is the Fire School professor?']='Da‘la Fa‘mea'
answer['What is the gemstone far Balance?']='C‘tr'
answer['What is something that (he Gobblers are NOTstockpiling in Colossus Way?']='Brucc'
answer['Who sang the Dragons, Tritons and Giants into existence?']='Bartleby'
answer['What is the name of the grandfathertree?']='Bartleby'
answer['What does Lethu Blunthaaf says about Ghostmanss?']='You never Can te‘l wwth theml'
answer['Jambo means:']='He‘lo'
answer['Zebu Blackstripes legendary blade was called:']='The Sword loe Due‘lsl'
answer['Esop Tharnpaw gives you a magic:']='Djembe Drum'
answer['Who is not one of the Zebu Kings:']='Zaﬂe Zoﬂer'
answer['Baobab is governed by:']='A Counc'
answer["Rasik Pn'defall is:"]='An 0‘yphanl lrom smne Town'
answer[r"Zamunda‘s great assassin is known as'"]='the Jacka'
answer['Vir Goodhealt is an assistant Mr']='Ras‘k Pndelal‘'
answer['Who is the missing prince?']='TIZm SI‘verlusk'
answer['Zebu Blackstripes legendary blade was forged:']='Valenc'
answer['Umlilo Sunchaser hired who as a local guide?']='Redband'
answer['What school Is the Gunak Demon focused on?']='Death'
answer['Who Is the Nameless Knight?']='Swr Malory'
answer['Which one ofthese are not a symbol on the battle Slgll?']='Wand'
answer['Wha guards the entrance to Unicorn Way?']='sun'
answer['Which of these locations is no! in Wizard City?']='Dwgmore 51am'
answer['Why are the Gobbler: so afraid to go home?']='Wllches'
answer[r'What currency do Kfngsls/e MMO games use?']='Cr'
answer[r'What kind of game: does ngs/sle make?']='ayer Onlme Games (MMOS)'
answer[r'What year did Kfngsls/e launch P/‘rate101?']='2012'
answer[r'What was the name of Kingsls/s’s ﬁrst mobile game?']='WIZardB‘uX'
answer['Who thinks you are there to take their precious feathers?']='Takeda Kanryu'
answer['The Swallows of Calfbum migrate (0 Avalon from where each year?']='Zalana and Marleybone'
answer["Who taunts' Why I oughta knock you to the mean, you psskyllms creep]"]='Mugsy'
answer['WhEIIS ﬂying around in Regent’s Square?']='Newspapers'
answer['Who tells you how to get to Aquila?']='eslon'
answer['Who is (he only person Who knows how to enter the Tomb of Storms?']='Hetch AI'
answer['Wha haunts the Night Wanens?']='Noslerabmt'
answer['Who can teach you the Life Shield Spell?']='Sabrma Greens'
answer['What type of spells are Ice, Fire, and Storm?']='E‘ementa‘'
answer['What is the name of the bridge In front of the Cave Io NighISIdE?']='Rambow'
answer['Where is Sabrina Greenstar?']='Fawregrounds'
answer[r'Who taught L/‘fe Magic before Moolinda Wu?']='Drake'
answer['Who resides In the Hedge Maze?']='Lady'
answer['What is the name of the Ice Tree in Ravsnwood?']='Ke‘vln'
answer["Sir Regina! Baxby’s cousin is'"]='Mondh Greenh'
answer['Bellaq is ﬁrs! found in:']='The Sook'
answer['Koyate Ghastmane accuses the player of:']='Bemg a true!'
answer['Which Aztecan ponders the Great Questions of Life?']='Pmlosora'
answer[r'What year did KIngsIs/s’s W/‘zard101 get nominated for the MMO Hall of Fame?']='2014'
answer['Why are the pixies and {series on Unicorn Wa y evil?']='Ratllebones Corrupted them'
answer['What is the We of the book that is floating around the Wizard City Library?']='Baswc szardlng & Proper Care'
answer['How many worlds of The Spiral are unlocked as ofMay 21st, 2014?']='12'
answer[r'Who was the greateszqu/‘Ian Gladiator of all time?']='D‘machaerus'
answer['Hrundle Fjord Is part of what section of Grizzlshslm?']='usk'
answer['Who tells you to speak these words only unto your mentor: "Means Kano Jajuka!"']='Pnya me Dryad'
answer["How many pips does It cast to cast Dr. Von's Monster?"]=''  #Doesn't recognize one-digit numbers
answer['Which spell would not be very effective when going forthe elixir vitae Badge?']='ang‘e'
answer["What is Diego '5 full name ?"]='Santiago Quanquez Ramirez'
answer[r'WhEIIS the name of the school newspaper? Boris Ta/lstaffknows...']='Ravenwood Bu‘letln'
answer['What does every Rotting Fodder In the Dark Caves carry WIIh them?']='A spade'
answer["Who are Hannibal Onetusk's brother and :o-pr'lor?"]='o and Sobaka' #cannot recognize Mago
answer['The Inzinzebu Bandits are harassing the good merchants In:']='Baobab Market'
answer[r'The Fire L/‘on Ravager: are led by:']='Nerga‘ me Burned Llon'
answer[r'Who is the Bear King of Grizz/eheim?']='Va'
answer[r'Which Austin charity has Kfngsls/e donated to?']='She‘ler'
answer[r'What was the name of the ﬁrst charity Mount created by Kingsls/e called?']='Meowmudon'
answer['In what world would you ﬁnd the Spider Temple']='Zalana'
answer['Which is the only school left standing In Dragonspyrs?']='F‘re'
answer[r'How many pips does it cost to cast Stormzi/Ia?']='' #Doesn't recognize one-digit
answer['lnyanga calls Umlia a:']='F‘re feather'
answer['Unalhi Nighlmrmer is:']='Baubab'
answer['Who takes you across the River of Souls?']='Charon'
answer["What 1517'! a shadow magic spell?"]='n R‘bbons'
answer['Which Firs spell both damages and heals overtime?']='Power Lmk'
answer['Who Was ordered to guard the Sword of Kings?']='The nghls loe SI‘ver Rose'
answer['What does Forsaken Banshee do?']='375'
answer["Who sells Valentine's Day items in Wizard City?"]='Heansong'

"""

All coordinates assume a screen resolution of 1280x1024, and Firefox maximized
with the Bookmarks turned on.
Nothing else changed.
x_pad=134
y_pad=248
Play area = x_pad, y_pad, x_pad+994, y_pad+337
Coordinates of the buttons :
Top Left : (x_pad+106,y_pad+188)
Top Right : (x_pad+543, y_pad+188)
Bottom left : (x_pad+107, y_pad+235)
Bottom right : (x_pad+543, y_pad+235)
Next Question : (x_pad+497, y_pad+287)
See your score : (x_pad+309, y_pad+231)
Coordinates of the questions and answers :
Question : (x_pad+11,y_pad+104,x_pad+990,y_pad+171)
Answer Top Left : (x_pad+11,y_pad+171, x_pad+528, y_pad+212)
Answer Top Right : (x_pad+528,y_pad+171, x_pad+990, y_pad+212)
Answer Bottom Left :(x_pad+11, y_pad+212, x_pad+528, y_pad+252)
Answer Bottom Right : (x_pad+528, y_pad+212, x_pad+990, y_pad+252)
"""

def grabquestion():
    box=(x_pad+11,y_pad+100,x_pad+990,y_pad+171)
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
    box=(x_pad+126, y_pad+212, x_pad+528, y_pad+252)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\answer3.png', 'PNG')
def grabanswer4():
    box=(x_pad+560, y_pad+212, x_pad+990, y_pad+252)
    im=PIL.ImageGrab.grab(box)
    im=im.convert('L')
    im.save(os.getcwd()+r'\answer4.png', 'PNG')

def grabanswers():
    grabanswer1()
    grabanswer2()
    grabanswer3()
    grabanswer4()

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
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def mousePos(cord):   #Moves the mouse to the coordinates
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():   #Gets the coordinates, used for debugging
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)
    

def findanswer(question):     #Finds and pressses the right answer
    if answer[question] in textit(1):
        mousePos((106, 188))
        leftClick()
        time.sleep(1)
    elif answer[question] in textit(2):
        mousePos((543, 188))
        leftClick()
        time.sleep(1)
    elif answer[question] in textit(3):
        mousePos((107, 235))
        leftClick()
        time.sleep(1)
    elif answer[question] in textit(4):
        mousePos((543, 235))
        leftClick()
        time.sleep(1)
    mousePos((497, 287))
    leftClick()
    time.sleep(1)


def play(i):        #Runs the bot
    is_ok=True
    while i<=11:
        time.sleep(6)
        print("Answering question " + str(i+1))
        grabquestion()
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


