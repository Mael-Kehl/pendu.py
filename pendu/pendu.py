import getpass #sert à cacher le mot sélectionné, comme un mot de passe
import tkinter #interface graphique
import random #permet de choisir aléatoirement un mot
import platform #permet de tester dans quel système d'exploitation nous nous trouvons
import os #permet d'excecuter des commandes shell

#######################################################################
#définition de l'interface graphique qui répondra sous le nom de pendu
pendu = tkinter.Tk()
pendu.title("JEU DU PENDU - Maël") #Ajout d'un titre à l'interface
pendu.minsize(800,600) #définition de la taille minimum de l'interface
pendu.geometry("800x600+200+50")#definition de la taille de l'interface
Status = tkinter.Canvas(pendu, height=400, width=400, highlightthickness=0)#définition d'une fenêtre à l'intérieur de l'interface graphique dans laquelle on pourra dessiner / highlightthickness sert à enlever la bordure de 2px peu esthétique autour du canvas
#Je le nomme Status car sa principale fonction est d'indiquer le Status de la partie
#Définition dans un tableau bidimentionnel les coordonnées de toutes les formes que l'on va tracer, il suffira d'appeler coords[i] avec i la forme que l'on désire
coords = [
[100,350,300,350],
[200,350,200,50],
[195,50,300,50],
[200,100,250,50],
[300,45,300,100],
[275,100,325,150],
[300,150,300,225],
[300,220,340,275],
[300,220,260,275],
[300,175,330,200],
[300,175,270,200]
]
#######################################################################
####       Définition des fonctions dont nous auront besoin        ####
#définition d'une fonction qui choisi un mot au hasard dans la liste wordlist.txt
def listword():
    with open('wordlist.txt', 'r') as w: #ouverture de wordlist.txt en lecture (read ou r) comme w
        words = w.readlines()#on sotck dans words tous les mots du fichier, sachant qu'il y a un mot par ligne
        word = random.choice(words)[:-1] #on choisit ensuite un mot aléatoirement. [:-1] est une solution trouvée sur de la documentation python, cela permet de ne pas lire le \n à la fin de la ligne et donc de ne pas mettre de retour à la ligne dans word.
        return word #on renvoie word
#définition d'une fonction qui permet à l'utilisateur d'entre un mot
def userword():
    word = getpass.getpass("Mot : ")#getpass cache le mot sélectionné
    return word#on renvoie word
#la fonction clear sert simplement à nettoyer l'écran
def clear():
    if platform.system()=='Windows': #la commande système de windows étant différente de Mac et Linux, on test si on est sous wndows
       os.system('cls') #si c'est le cas on entre 'cls'
    else:
        os.system('clear')#sinon on entre 'clear'
#si l'utilisateur veut jouer seul, on lui donne un mot au hasard, sinon un deuxième utilisateur devra entrer un mot
#le but de passer par une fonction pour récupérer le choix du mode de jeu est que l'on peut appeler à nouveau cette fonction si l'entrée n'est pas un entier
def gamemode():
    try: #On essaie donc de récupérer un entier
        gametype = int(input("Choisissez le mode de jeu (1 ou 2) :"))
    except ValueError:#Dans le cas où on a une erreur de valeur, on affiche un message d'erreur et on appelle la fonction
        print("Merci de rentrer 1 ou 2")
        gamemode()
    else:
        return gametype#une fois que l'on pas d'erreur, on retourne gametype
#######################################################################

clear() #On clear l'écran afin d'avoir uniquement le jeu d'affiché par la suite
print("**************************************************************")
print("***  _______   _______   ____    __    ______    __    __  ***")
print("*** |   _   | |   ____| |    \  |  |  |  _   \  |  |  |  | ***")
print("*** |  |_|  | |  |__    |  |  \ |  |  | | |  |  |  |  |  | ***")
print("*** |   ____| |   __|   |  | \ \|  |  | | |  |  |  |  |  | ***")
print("*** |  |      |  |____  |  |  \    |  | |_|  |  |  |__|  | ***")
print("*** |__|      |_______| |__|   \ __|  |______/  |________| ***")
print("***                                                        ***")
print("**************************************************************")
print("**********************  MODE D'EMPLOI  ***********************")
print("* Le but du jeu est de trouver un mot en moins de 10 essais  *")
print("* Le jeu vous permet de jouer de 2 manières différentes :    *")
print("* 1- Choisir le mot à trouver manuellement                   *")
print("* 2- Laisser le programme choisir un mot au hasard           *")
print("**************************************************************")

if gamemode() == 1: #Étant donné que gamemode renvoie un entier, on le compare à un entier, Si la valeur renvoyée est 1, on appelle userword()
    choosed_word = userword()
else: #Sinon on appelle listword()
    choosed_word = listword()

choosed_word = choosed_word.upper()#Transformation du mot choisi en MAJUSCULES
word = list(choosed_word)#Création d'un tableau word à partir du string choosed_word
answer = []#Création d'un tableau answer (réponse)
L=len(choosed_word) #stockage dans L de la longueur du mot choisi
for i in range(0,L):#On remplit answer d'étoiles
    answer.append('*')
clear()
print("Mot choisi, à vous de jouer !")
# .join sert à afficher le contenu d'un tableau (ici des lettres) comme une chaine de caractères, très pratique dans ce cas
print("".join(answer))
UserLetters = [] #Servira à stocker les lettres entrées par l'utilisateur
u = 0 #nombre d'échecs, d'erreurs de l'utilisateur
Trys = 11 #Trys représente le nombre d'essais restants, il est par défaut de 11
TestValue = 1 #Valeur de test pour à chaque boucle déterminer si une erreur a été commise (dans le cadre du jeu)
i=0 #valeur qui nous servira à afficher les traits de notre dessin (coords[i])
while u<=10:#Tant que le nombre d'erreurs est inférieur ou égal à 10, on demande d'entrer une lettre ou un mot.
    #On demande à l'utilisateur d'entrer une lettre ou un mot, puis on transforme le string en MAJUSCULES.
    choosed_letter = input("Entrez une lettre, ou un mot : ")
    choosed_letter = choosed_letter.upper()
    UserLetters.append(choosed_letter)
    #si la longueur de la lettre choisie est supérieur à 1, il s'agit d'un mot.
    if len(choosed_letter)>1:
        #On compare donc directement le choix de l'utilisateur à la chaine de caractère choosed_word
        if choosed_letter==choosed_word:
            answer = word#Si la réponse est correcte, alors le tableau answer est égal au tableau word, l'utilsateur a gagné
            break #on sort de la boucle

    if choosed_letter in word: #si la lettre choisie est dans le tableau word, alors on cherche case par case l'emplacement de la lettre
        for n in range(0,L): #Ainsi pour n allant de 0 à L on vérifie si la lettre est égale à la nème valeur du tableau word
            if choosed_letter == word[n]:
                answer[n]=choosed_letter #si c'est le cas on remplace la ou les étoile(s) de réponse par la lettre choisie
        clear()
        print("Choix précédents :", UserLetters)
        print("État du mot :","".join(answer)) #Affichage de l'état de answer (avancement dans la recherche du mot)
        print("Bonne réponse, il vous reste", Trys, "essai(s).")
        if word == answer: #On vérifie ensuite si answer est égal à word, si c'est le cas on sort de le boucle, l'utilisateur a gagné
            break #On sort de la boucle
    else: #si la lettre choisie n'est pas dans le tableau word, on ajoute 1 à u le nombre d'erreurs
        u+=1
        Trys = 11 - u #à chaque nouvelle erreur on stock 11(nombre d'essais)-u(nombre d'échecs) pour obtenir le nombre d'essais restants
        if u == TestValue: #Si u est égal à la valeur Testvalue, cela veut dire que l'utilisateur a commis une erreur et donc que u le nb d'erreur a augmenté
        ###### On s'intéresse à l'interface graphique ######
        # Si u=6, alors nous sommes à la sixième erreur et c'est à ce moment qu'il nous faut afficher la tête du pendu, on doit donc faire une condition spécifique pour créer un cercle (Status.create_oval) et non une ligne.
            if u == 6:
                Status.create_oval(coords[5], width=5)
                Status.pack() #Pack signifie que l'on ajoute ce que l'on vient de créer à l'environnement graphique
            else:
        #Pour toutes les autres parties du dessin, on affiche des lignes ayant pour coordonnées coords[i]
                Status.create_line(coords[i], width=10, fill="black")
                Status.pack()
            TestValue+=1 #On incrémente TestValue de manière à ce qu'il soit égal à u+1
            i+=1 #On incrémente i de manière à utiliser différentes coordonnées lors du prochain affichage
        clear()
        print("Choix précédents :", UserLetters)
        print("État du mot :","".join(answer))
        print("Mauvaise réponse, il vous reste", Trys,"essai(s).") #On affiche "mauvaise réponse" avec le Trys le nombre d'essais restants
#Rappel : On sort de la boucle quand la réponse est juste ou quand on a atteint le nombre maximum d'essais
#On fait alors un test : si le joueur a perdu, alors le fond d'écran devient rouge et on affiche que l'utilisateur a perdu
if u>=10 and answer!=word:
    clear()
    print("************************************************************")
    print("***  _______   _______   ________    ______    __    __  ***")
    print("*** |   _   | |   ____| |    _   |  |  _   \  |  |  |  | ***")
    print("*** |  |_|  | |  |__    |   |_|  |  | | |  |  |  |  |  | ***")
    print("*** |   ____| |   __|   |   _____|  | | |  |  |  |  |  | ***")
    print("*** |  |      |  |____  |  | \  \   | |_|  |  |  |__|  | ***")
    print("*** |__|      |_______| |__|  \__\  |______/  |________| ***")
    print("***                                                      ***")
    print("************************************************************")
    print("Vous avez Perdu ! le mot était :","".join(word))
    pendu.configure(bg="red")
    Status.configure(bg="red")
    #On affiche également que l'utilisateur a perdu sur l'interface graphique (coordonnées x,y, text , police, taille, gras)
    Status.create_text(200,382, text="PERDU !", font="Verdana 30 bold")
    Status.pack()
#Sinon le fond d'écran devient vert et on affiche que l'utilisateur a gagné
else:
    clear()
    print("*****************************************************************")
    print("***  _______    ________    _______    ____    __    _______  ***")
    print("*** /  _____|  |   __   |  /  _____|  |    \  |  |  |   ____| ***")
    print("*** | |  ___   |  |__|  |  | |  ___   |  |  \ |  |  |  |__    ***")
    print("*** | | |_  |  |   __   |  | | |_  |  |  | \ \|  |  |   __|   ***")
    print("*** | |___| |  |  |  |  |  | |___| |  |  |  \    |  |  |____  ***")
    print("*** \_______/  |__|  |__|  \_______/  |__|   \ __|  |_______| ***")
    print("***                                                           ***")
    print("*****************************************************************")
    print("Vous avez gagné, le mot était :", "".join(answer))
    pendu.configure(bg="green")
    Status.configure(bg="green")
    Status.create_text(200,382, text="GAGNÉ !", font="Verdana 30 bold")
    Status.pack()
#Manière simple de quitter le programme
leave = input("Tappez sur une touche et appuyez sur Entrée (Enter) pour quitter ")
if leave != '':
    exit()
pendu.mainloop() #Sert à ce que l'interface graphique reste ouverte durant tout le programme
