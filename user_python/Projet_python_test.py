import random
import string
import hashlib 

class Salarié(object): #"Classe des salarié"
    def __init__(self, nom, pnom, login,pwd):
        print ("création d'un objet salarié...")
        self.nom = nom
        self.Prenom = pnom
        self.Login = login
        self.Password = pwd
  
  
    def get_nom(self):  
        return self.nom
    def get_pnom(self):
        return self.Prenom
    def get_login(self):
        return self.Login
    def get_pwd(self):
        return self.Password


    def set_nom(self, nouveau_nom): 
        if nouveau_nom =="":
            print("le nom de l'employé ne peut pas etre vide!")
        else:
            self.nom = nouveau_nom
            print("Le nom à été modifié.")

    def set_pnom(self, nouveau_pnom):
        if nouveau_pnom =="":
             print("le prénom de l'employé ne peut pas etre vide!")
        else:
            self.Prenom = nouveau_pnom
            print("Le prénom à été modifié.")

    def afficher(self):
        print (self.nom + self.Prenom ,"à été ajouté") 

    def set_pwd(self, new_pwd):
        if new_pwd =="":
             print("le password de l'employé ne peut pas etre vide!")
        else:
            self.Password = new_pwd
            print("Le password à été modifié.")


class User(Salarié): 
    def __init__(self, nom, pnom, login, pwd ):
        print("Création d'un objet User..")
        #Construction / création / initialisation d'un user
        Salarié.__init__(self, nom, pnom, login, pwd)
       
    def afficher_User(self):
        print ("User: ", self.get_nom(),"", self.get_pnom())

class Administrateur(Salarié): 
    def __init__(self, nom, pnom, login, pwd ):
        print("Création d'un objet Administrateur..")
        #Construction / création / initialisation d'un user
        Salarié.__init__(self, nom, pnom, login, pwd)
       
    def afficher_Administrateur(self):
        print ("Administrateur: ", self.get_nom(),"", self.get_pnom())


#Connexion a une seesion avec login et password
def login_password ():
    for j in range(5):
        Username = input("enter un login:")
        if Username == Admin1.get_login():
            print("login Correct")
            break
        else :
            print("login incorrect")
        if j==4:
            print("Votre login incorrect, veuillez contacter votre support informatique.")


    for i in range(3) : ### 3 tentatives
        pwd=input("Tapez votre password...")  # en clair
        pwd=pwd.encode()
        pwd_hashé=hashlib.md5(pwd).hexdigest()

        if pwd_hashé==mot_de_passe_hashé:
            print("Mot de pass correct.")
            break
        else:
            print("Mot de pass incorrect, il vous reste", i-2,"tentatives....")
        if i==2:
            print("Votre compte est bloqué")


############################### fin des classes ########################################

#main, programme principal
## classe mère: Salarié
salarié1 = Salarié("KANY ", "Kévin" , "kkany", "") 
print ("Nom de l'employé est", salarié1.get_nom())


User1=User ("KANY ", "Florent", "fkany", "²")
print("Nom du User:", User1.get_nom(),"", User1.get_pnom())
print("son login est:",User1.get_login())
print("et son MDP est:",User1.get_pwd())
mot_de_passe_hashé = hashlib.md5(User1.get_pwd().encode()).hexdigest()
print("mot de pass hashé de MR ", User1.get_nom(),"est:", mot_de_passe_hashé)

salarié2 = Salarié("BRETAGNOLLE ", "Guillaume" , "gbretagnolle","") 
print ("Nom de l'employé est", salarié2.get_nom())

User2=User ("BRETAGNOLLE", "Guillaume","gbretagnolle", "Edenred2021")
print("Nom du User:", User2.get_nom(),"", User2.get_pnom(),())
print("son login est:",User2.get_login())
print("et son MDP est:",User2.get_pwd())
mot_de_passe_hashé1 = hashlib.md5(User2.get_pwd().encode()).hexdigest()
print("mot de passe hashé: de MR ",User2.get_nom(),"est:" ,mot_de_passe_hashé1)

Administrateur1 = Salarié("KANY ", "Kévin" , "kkany", "") 
print ("Nom de l'employé est", Administrateur1.get_nom())

Admin1= Administrateur("adm ", "KANY", "adm-kany", "Respons11")
print("Nom de l'admin:", Admin1.get_nom(),"", Admin1.get_pnom())
print("son login est:",Admin1.get_login())
print("et son MDP est:",Admin1.get_pwd())
mot_de_passe_hashé = hashlib.md5(Admin1.get_pwd().encode()).hexdigest()
print("mot de pass hashé de ", Admin1.get_login(),"est:", mot_de_passe_hashé)

login_password()
  
New_pwd = input("enter un nouveau MDP:")
Admin1.set_pwd(New_pwd)
print ("Votre nouveau MDP est", Admin1.get_pwd())
print ("Bonjour " ,Admin1.get_login(),"vous etes mainenant connecter a votre session")