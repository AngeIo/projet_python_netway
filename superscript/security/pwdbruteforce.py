# Ce fichier contient une fonction permettant de vérifier la compléxité d'un mot de passe

# Permet la recherche
import re

# Permet de faire une pause dans le programme
import time

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')
from utils import func

# Vérifie la validité du mot de passe
def pwdvalid(password):
    if secretpwd.lower() == password.lower():
        return True
    return False

# Test les possibilités de mot de passe, renvoie le mot de passe si ça match sinon False
def pwdtry():
    successful = False
    # Ouvre le fichier et le lit ligne par ligne
    with open('security/pwd.dict', encoding="utf8") as f:
        lines = f.read().splitlines()
    # Lance le chrono pour calculer le temps d'exécution total du brute force
    start_time = time.time()
    for i, line in enumerate(lines):
        # Simule le check avec la base de données pour voir si le mot de passe correspond
        if pwdvalid(line):
            # Le mot de passe a bien été trouvé
            successful = True
            break
    return {
        'successful' : successful,
        'line' : line,
        'tries' : i,
        # Calcul le temps d'exécution total du brute force
        'time' : (time.time() - start_time),
    }

# Cette fonction permet de brute force le mot de passe en testant toutes les possibilités grâce à un dictionnaire
def pwdbrute(passwordtocrack):
    """
    Tester toutes les combinaisons possibles de mot de passe grâce à un dictionnaire fourni via un fichier txt.
    La boucle s'arrête dès que le mot de passe entré est correct et que nous avons pu nous connecter au compte utilisateur.
    """

    # Défini globalement cette variable pour qu'il puisse être lu par une autre fonction
    global secretpwd
    secretpwd = passwordtocrack

    # Retourne le résultat du brute force
    return pwdtry()
