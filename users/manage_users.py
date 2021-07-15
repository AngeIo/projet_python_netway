# Import des différents modules
import time
import os.path
import hashlib
import string
from random import *
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.digits

# Tous les utilisateurs sous la forme d'un JSON
users = {
    "adm-kany": {
        "password": "Respons12",
        "group": "admin",
        "Full name": "Admin Kany",
        "Mail": "adm-kany@esgi.com",
    },

    "adm-peche": {
        "password": "Respon13",
        "group": "admin",
        "Full name": "Admin Peche",
        "Mail": "adm-peche@esgi.com",
        
    },
    "kkany": {
        "password": "Resp",
        "group": "user",
        "Full name": "KANY Kevin",
        "Mail": "kkany@esgi.com",
    },

    "Lpeche": {
        "password": "Azerty11",
        "group": "user",
        "Full name": "Peche Laurent",
        "Mail": "lpeche@esgi.com",
    },
}  


f = open("users.txt","a+")


# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

#hash en MD5 qui permet de donner un mot de pas hashé lorsque que l'on s'enregistre
def hash_password(password):
    b = bytes(password, 'utf-8')
    return hashlib.md5(b).hexdigest()

# autorisation du Login qui permet de se connecter 
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]: # prend la variable dans le JSON users
            print("Login successful")
            return True
    return False

# Fonction login
def login():
 
    while True:
        username = input("Username: ")
        if not len(username) > 0: 
            print("Votre Username ne peut pas être vide")
        else:
            break       
    for j in range(3):  # Permettra de bloqué le compte au bout de 3 essaie.        
        while True:
            password = input("Password: ")
            if not len(password) > 0:
                print("Votre Password ne peut pas être vide")
            else:
                break

        if loginauth(username, password):  #utilise les donnée de la fonction autorisation du login
            return session(username, password)
        else:
            print("Votre username ou password est invalide")
        if j==2:
            print("Votre compte est bloqué, veuillez contacter votre support informatique.")
            break

# Enregistrement d'un nouvel utilisateur
def register():
        username = input("New username: ")
        if not len(username) > 0:
            print("Votre Username ne peut pas être vide")
        elif username in users:
            print("L'utilisateur existe déja")
        else:
            password = "".join(choice(allchar) for x in range(randint(min_char, max_char))) # creation d'un mot de passe hashé de min 8 caractère max 12 et que des lettres
            tpassword = hash_password(password.strip('\n'))
            print("Creation du compte...")
            print ("Voici votre mot de passe :",password)
            users[username] = {}
            users[username]["password"] = password
            users[username]["group"] = "user"
            f.write( str(users) )
            time.sleep(1)
            print("Votre compte à été créer")


# Fonction User session avec la fenetre pour les différentes options
def session(username, password): #permet la selection des options
    print("Bienvenue sur votre compte " + username)
    print("Options: consultation | modification | delete account |  logout")
    if users[username]["group"] == "admin":
        print("")
    while True:
        option = input(username + " > ") # option logout 
        if option == "logout":
            print("Logging out...")
            break
        elif option == "consultation": # option consuktation renvoie son login ainsi que son mot de passe
            print("Voici votre nom d'utilisateur : ", users[username]["Full name"])
            print("Voici votre login utilisateur : ", username)
            print("Voici votre mot de passe : ", password)
            print("Voici votre adress mail : ", users[username]["Mail"])

        elif option == "modification": #option modification qui permet de changer le mot de passe de l'utilisateur
            print ("Quel est votre mdp actuel?")
            passe = input ("> ")
            newpassword = input("tapez nouveau mdp : ")
            for passe in users[username]["password"]:
                if passe == password :
                    users[passe] = newpassword
                    replace_value(users[username]["password"])
            print("Your new password is : ", newpassword)

        elif option == "delete account": #option qui permet de supprimer un utilisateur (fonctionne seulement avec un compte admin)
            print("quel compte voulez-vous supprimer?")
            userinfo = input("> ")
            if userinfo in users:
                print("Etes-vous sûr de vouloir supprimer compte de  " + userinfo + "'?")
                print("Options: yes | no")
                while True:
                    confirm = input("> ")
                    if confirm == "yes":
                        if users[username]["group"] == "admin":
                            print("Suppression du compte de " + userinfo + "'...")
                            del users[userinfo]
                            time.sleep(1)
                            print("Le compte de " +userinfo + "'à été supprimé")
                            break
                        else:
                            print ("Vous devez être admin pour effectuer cette fonction")
                            break
                    elif confirm == "no":
                        print("Canceling account deletion...")
                        time.sleep(1)
                        print("Account deletion canceled")
                        break
                    else:
                        print(confirm + " n'est pas une option")
            else:
                print("il n'y a pas de compte avec cette username")
    else:
        print(option + " n'est pas une option")

# Menu des options 
print("Bienvenue veuillez taper register ou login pour utiliser les options")
print("Options: register | login | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " n'est pas une option")

# On exit
print("Arrêt du système...")
time.sleep(1)

f.close() #ferme le fichier users.txt