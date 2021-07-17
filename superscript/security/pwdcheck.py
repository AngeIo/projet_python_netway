# Ce fichier contient une fonction permettant de vérifier la compléxité d'un mot de passe

# Permet la recherche
import re

# Permet de faire une pause dans le programme
import time

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')
from utils import func

# Cette fonction permet de vérifier si le mot de passe correspond aux exigences de sécurité de la société
def pwdcheck(password):
    """
    Vérifier la compléxité du mot de passe : 'password'
    Retour un dict qui spécifie ce qui ne va pas
    Un mot de passe est considéré comme fort s'il a :
        8 caractères de longueur ou plus
        1 chiffre ou plus
        1 symbole ou plus
        1 lettre majuscule ou plus
        1 lettre minuscule ou plus
    """

    # Calculer la longueur
    length_error = len(password) < 8

    # Recherche de chiffres
    digit_error = re.search(r"\d", password) is None

    # Recherche de majuscules
    uppercase_error = re.search(r"[A-Z]", password) is None

    # Recherche de minuscules
    lowercase_error = re.search(r"[a-z]", password) is None

    # Recherche de symboles
    symbol_error = re.search(r"\W", password) is None

    # Résultat global
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }

# Tests
def pwdtest():
    while True:
        opschoice = func.myChoice("Bienvenue, veuillez choisir une option", "Test password", "Exit")
        if opschoice == 1:
            password = "CoucouLaFamille*1" # Mot de passe fort
            # password = "CA" # Mot de passe faible

            flag = pwdcheck(password)['password_ok']
            if flag:
                print("Password OK")
            else:
                print("Password KO")
        elif opschoice == 2:
            # On exit
            print("Arrêt du système...")
            time.sleep(1)
            break
