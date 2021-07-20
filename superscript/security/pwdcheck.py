# Ce fichier contient une fonction permettant de vérifier si le mot de passe est assez complexe et s'il peut être brute force grâce à un dictonnaire de mots communs

# Permet la recherche
import re

# Permet de faire une pause dans le programme
import time

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')
from utils import func

# Importe toutes les fonctions en lien aux mots de passe dans ce programme pour pouvoir les lancer depuis superscript
from security import pwdbruteforce

# Cette fonction permet de vérifier si le mot de passe est facilement devinable via brute force ou non
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

def pwdcheckdisplay(tab):
    print("\n")
    print("Results\n-------")
    if tab['password_ok']:
        print("Your password comply with security policy of the company\n")
        return True
    else:
        print("/!\ Your password doesn't comply with security policy of the company /!\ ")
        if tab['length_error']:
            print("- Length error : Password must contain at least 8 characters")
        if tab['digit_error']:
            print("- Digit error : Password must contain at least 1 digit")
        if tab['uppercase_error']:
            print("- Uppercase error : Password must contain at least 1 uppercase letter")
        if tab['lowercase_error']:
            print("- Lowercase error : Password must contain at least 1 lowercase letter")
        if tab['symbol_error']:
            print("- Symbol error : Password must contain at least 1 symbol (any non-alphanumeric character)")
        print("\n")
        # print("As a reminder, your password must contain at least:\n- 8 characters\n- 1 digit\n- 1 uppercase letter\n- 1 lowercase letter\n- 1 symbol (any non-alphanumeric character)\n\n") # Afficher les conditions à respecter pour que le mot de passe soit accepté
    return False

# Tests
def pwdtest():
    # password = "CoucouLaFamille*1" # Mot de passe fort
    # password = "CAcd" # Mot de passe faible
    flag = 0
    while True:
        while not flag:
            password = input("For the tests, please enter a new password: ")
            if len(password) < 4:
                print("Password must contain at least 4 characters in order to test it")
            else:
                flag = 1
                break
        opschoice = func.myChoice("\nCybersecurity - Welcome, please choose an option", "Testing password compliance with policy", "Cracking password with brute force", "Enter a new password to test", "Exit")
        if opschoice == 1:
            pwdcheckdisplay(pwdcheck(password))
        elif opschoice == 2:
            result = pwdbruteforce.pwdbrute(password)
            if result['successful']:
                print("\n")
                print("Results\n-------\nPassword found in %s seconds after testing %s words from our dictionnary\n/!\ Password is not secure /!\ \n" % (result['time'], result['tries']))
            else:
                print("\n")
                print("Results\n-------\nPassword wasn't found in our dictionnary\nPassword is secure\n")
        elif opschoice == 3:
            while True:
                password = input("For the tests, please enter a new password:")
                if pwdcheckdisplay(pwdcheck(password)):
                    break
        elif opschoice == 4:
            # On exit
            print("Arrêt du système...")
            time.sleep(1)
            break
