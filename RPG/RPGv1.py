from random import randint

#Initialisation des valeurs
ndv = "Note de version : error(input) == crash == reset TwT"
b=0
n=0
n2 = 1
victoire=False
counter = 0
choice = 0
affectionCuik = 0


#Définition du personnage
class personnage:
    def __init__(self,nom,sexe,clas,num_classe,type):
        self.nom = nom
        self.sexe = sexe
        self.clas = clas
        self.num_classe = num_classe
        self.type = type

moi = personnage(None,None,None,None,None)

#Définition des enemis
class ennemi:
    def __init__(self,nom,force,poison,poison_deg,vie,pv,poisoned,att_nom,heal_nom):
        self.nom = nom
        self.force = force
        self.vie = vie
        self.pv = pv*vie
        self.poisoned = poisoned
        self.att_nom = att_nom
        self.heal_nom = heal_nom
        self.poison = poison
        self.poison_deg = poison_deg

gobelinfaible = ennemi("Un Gobelin faible",10,False,0,5,10,False,"coup de massue","petite potion")
gobelin = ennemi("Un Gobelin banal",15,False,0,10,15,False,"coup de massue","petite potion")
gobelinfort = ennemi("Un Gobelin fort",20,False,0,15,20,False,"coup de massue","petite potion")
gobelindelabo = ennemi("Un Gobelin de labo",15,True,10,20,10,False,"Flêchette empoisonnée","Antidote")

#/!\-----------------en cas d'ajout d'adversaire : update sync function and ennemis list

ennemis = [gobelinfaible,gobelin,gobelinfort,gobelindelabo]

#Définition des attaques
class att:
    def __init__(self,nom,deg,heal,healendu,cost_endu,cost_pv, poison, bouclier):
        self.nom = nom
        self.deg = deg
        self.heal = heal
        self.healendu = healendu
        self.cost_endu = cost_endu
        self.cost_pv = cost_pv
        self.poison = poison
        self.bouclier = bouclier


#Definition des classes
class classe:
    def __init__(self, force, agi, vie, magie, pv, endu, poisoned ,parade):
        self.force = force +5*n
        self.agi = agi +5*n
        self.vie = vie +5*n
        self.magie = magie +5*n
        self.pv = pv*vie +5*n
        self.endu = endu*agi +5*n
        self.parade = parade
        self.poisoned = poisoned

Chevalier = classe(10, 2, 10, 0, 10, 10, False, False)
Assassin = classe(4, 10, 6, 2, 10, 10, False ,False)
Mage = classe(2, 6, 4, 10, 10, 10, False ,False)




#Fonction de synchronisation moi.clas et classe
def sync():
    global Chevalier
    global Assassin
    global Mage
    global moi
    Chevalier = classe(10, 2, 10, 0, 10, 10, False, False)
    Assassin = classe(4, 10, 6, 2, 10, 10, False ,False)
    Mage = classe(2, 6, 4, 10, 10, 10, False ,False)
    if moi.num_classe == 1 :
        moi.clas = Chevalier
    elif moi.num_classe == 2 :
        moi.clas = Assassin
    else :
        moi.clas = Mage

    global gobelinfaible
    global gobelin
    global gobelinfort
    global gobelindelabo
    gobelinfaible = ennemi("Un Gobelin faible",10,False,0,5,10,False,"coup de massue","petite potion")
    gobelin = ennemi("Un Gobelin banal",15,False,0,10,15,False,"coup de massue","petite potion")
    gobelinfort = ennemi("Un Gobelin fort",20,False,0,15,20,False,"coup de massue","petite potion")
    gobelindelabo = ennemi("Un Gobelin de labo",15,True,10,20,10,False,"Flêchette empoisonnée","Antidote")




#Fonction de niveau +1
def niveau_suivant():
    global n
    global n2
    n=n+(1*n2)
    sync()



#----DEBUT----#

#Initialisation du personnage
print("\n----------/!\ Avant de commencer le jeu, nous vous mettont en garde : il n'y a pas de sauvegarde, donc si jamais vous relancez le jeu, vous recommencez.\n", ndv, "----------/!\\")
print("\n\n<<<(OvO)>>>  Bonjour, je suis Cuik, et c'est moi qui vais vous guider tout au long de votre partie. \nMaintenant que les présentations sont faites, on commence !!")
print("\n---Initialisation du personnage (irréversible)---")

#Choix du nom
moi.nom = input("\nComment voulez vous vous appeler ?")

#Choix du sexe
while b != 1 and b != 2 and b!=3:
    b = int(input("\nVoulez-vous être désigné.e comme: \n1)Un homme \n2)Une femme\n3)Neutre \n->> Je choisis: (un chiffre)"))
if b == 1 :
    moi.sexe = "H"
elif b == 2:
    moi.sexe = "F"
elif b == 3:
     moi.sexe = "N"

#Choix de la classe
print ("\nChoisissez votre classe")
print ("1)Chevalier\n2)Assasin\n3)Mage")
while moi.num_classe != 1 and moi.num_classe != 2 and moi.num_classe != 3 :
    moi.num_classe = int(input(">>> Je choisis: (un chiffre)"))

#Initialisation des stats et de l'appelation
if moi.num_classe == 1 :
    moi.clas = Chevalier
    if moi.sexe == "H" :
        moi.type = "un chevalier"
    elif moi.sexe == "F":
        moi.type = "une chevalière"
    elif moi.sexe =="N":
        moi.type = "un.e chevalier.e"
elif moi.num_classe == 2 :
    moi.clas = Assassin
    if moi.sexe == "H" :
        moi.type = "un assassin"
    elif moi.sexe == "F":
        moi.type = "une assassine"
    elif moi.sexe =="N":
        moi.type = "un.e assassin.e"
else :
    moi.clas = Mage
    if moi.sexe == "H" :
        moi.type = "un mage"
    elif moi.sexe == "F":
        moi.type = "une mage"
    elif moi.sexe =="N":
        moi.type = "un.e mage"
         
#Affichage des Stats
def stats():
    print ("\n\n<<<(OvO)>>> " , moi.nom+",vous êtes" , moi.type + ".\n\nVoici vos stats.\nForce :" , moi.clas.force , "\nAgilitée :" , moi.clas.agi , "\nVitalitée :" , moi.clas.vie , "\nCompétences magiques:" , moi.clas.magie)
stats()


#---Encore de nouvelles variables et fonctions---

#Création des Attaques
Coup_droit = att("Coup droit", moi.clas.force*1,0,0, 2, 0, False, False)
Coup_puissant = att("Coup puissant",moi.clas.force*5, 0,0, 12, 0, False, False)
Bouclier = att("Bouclier preque parfait",0, 0,0, (20/moi.clas.force), 0, False, True)

Lancé = att("Lancé de dagues",moi.clas.agi*1, 0, 0,5, 0, False, False)
Lancé_empoisonné = att("Lancé empoisonné",moi.clas.agi*5, 0,0, 20, 0, True, False)
HealP = att("Potion de soin du maitre des poisons",0, moi.clas.agi ,moi.clas.agi, 0, 0, False, False)

Fireball = att("Boule de feu",moi.clas.magie*1 , 0,0,3, 0, False, False)
Firestorm = att("Tempête de feu",moi.clas.magie*5, 0,0, 17, 0, False, False)
Blood_Sacrifice = att("Sacrifice de sang",moi.clas.pv*moi.clas.magie*0.1, 0,0, 40, moi.clas.pv/2, False, False)
Healmag = att("Sort de soin",0,moi.clas.magie,moi.clas.magie,0,0,False,0)

Attaques = [Coup_droit,Coup_puissant,Bouclier,Lancé,Lancé_empoisonné,HealP,Fireball,Firestorm,Blood_Sacrifice,Healmag]

def combat(opp):
    global counter
    global moi
    global moi
    global choice
    opponent = opp
    print("\n\n----------COMBAT----------\n Vous allez affronter",opponent.nom,"\n Si vos pv ou votre endurence tombe sous 0, vous mourerez.\n")
    tour = randint(0,1)
    if tour == 0:
        print("Vous commencez.")
    else:
        print("C'est votre advesaire qui commence.")

    while moi.clas.pv > 0 and opponent.pv > 0 and moi.clas.endu > 0:
        print("\n-----Nouveau tour-----\n",str(opponent.nom)[3:],":",opponent.pv,"pv")
        print(" Vous :",moi.clas.pv,"pv et",moi.clas.endu,"endu")
        if tour==0:
            for counter in range (0,len(Attaques)):
             print(counter+1,")",Attaques[counter].nom)
            choice = int(input(">>> Je choisis: (un chiffre)"))

            if opponent.poisoned == True:
                opponent.pv = opponent.pv - moi.clas.magie
            opponent.pv = opponent.pv - Attaques[choice-1].deg
            opponent.poisoned = Attaques[choice-1].poison
            moi.clas.pv = moi.clas.pv + Attaques[choice-1].heal
            moi.clas.endu = moi.clas.endu + Attaques[choice-1].healendu+3
            moi.clas.endu = moi.clas.endu - Attaques[choice-1].cost_endu
            moi.clas.pv = moi.clas.pv - Attaques[choice-1].cost_pv
            moi.clas.parade = Attaques[choice-1].bouclier
            tour = 1
        elif tour == 1:
            attorheal = randint(0,1)
            # Choix si att ou heal
            if moi.clas.poisoned == True:
                moi.clas.pv = moi.clas.pv - opponent.poison_deg
            if attorheal == 0:
                print("Votre avdversaire utilise :",opponent.att_nom)
                if moi.clas.poisoned == True:
                    moi.clas.pv = moi.clas.pv - opponent.poison_deg
                if moi.clas.parade == False:
                    moi.clas.pv = moi.clas.pv - opponent.force
                    moi.clas.poisoned = opponent.poison
                else :
                    moi.clas.poisoned = opponent.poison
            else:
                print("Votre avdversaire utilise :",opponent.heal_nom)
                opponent.pv = opponent.pv + opponent.vie
            tour = 0

    if moi.clas.pv < 0 or moi.clas.endu < 0:
        print("\nVous avez perdu...")
    if opponent.pv < 0:
        print("\nVous avez gagné !!!\nVous passez au niveau",n+1,"!!!")
        niveau_suivant()
    sync()

def home():
    global n
    global affectionCuik
    print ("\n\n\n----------HOME----------")
    print ("<<<(OvO)>>>  Vous êtes niveau",n,"!!!")
    print ("Que voulez vous faire ?\n1) Combattre\n2) Voir vos stats\n3) Me caresser\n4) Me frapper")
    counter = int(input(">>> Je choisis: (un chiffre)"))
    if counter == 1:
        combat(ennemis[randint(0,len(ennemis)-1)])
    if counter == 2:
        stats()
    if counter == 3:
        affectionCuik = affectionCuik+1
        print("\n<<<(OvO)>>>  Mmmmh... Merki !! (⁠◕⁠દ⁠◕⁠)")
        if affectionCuik == 500:
            print("...Personne n'a jamais été aussi zentil aevc moi.... Allez, Kdo ! ＼⁠(⁠^⁠o⁠^⁠)⁠／")
            print("\n----------Information----------\nVous avez reçu un buff pour tendresse exeptionnelle. Ce buff peut être annulé par un debuff.")
            n2 = n2*2
    if counter == 4:
        affectionCuik = affectionCuik-1
        print("\n<<<(OvO)>>>  AIE !! ARRETEZ, PITIE !!! Vous me faites mal... ಥ⁠‿⁠ಥ")
        if affectionCuik == -500:
            print("...C'EST BON LA, Y'EN A MARD A LA FIN !! VOUS AVEZ APPARU DANS UN MODE DONT VOUS SAVEZ RIEN, ET VOUS ME FRAPPEZ COMME CA ?? C'EST BON, J'EN AIS PLUS QU'ASSEZ DE LA SOUS-MERDE QUE VOUS ETES : DEBUFFFFF !!!! (⁠ﾉ⁠≧⁠∇⁠≦⁠)⁠ﾉ⁠ ⁠ﾐ⁠ ⁠┻⁠━⁠┻ ")
            print("\n----------Information----------\nVous avez reçu un debuff pour méchancetée acrue. ce debuff peut être annulé par un buff.")
            n2 = n2*0.5

while 0==0 :
    home()