#!/usr/bin/env python3
# coding: utf-8
# ******************************************************************************
#
# Script Name: superscript.py
# Version: 0.2 (Alpha)
# Authors: BRETAGNOLLE Guillaume, GERARD Angelo, KANY Kevin, PECH Laurent
# Creation date: 12 june 2021
#
# Description : This script is designed for IT technicians to help them manage
# their IT infrastructure easily.
#
# ******************************************************************************

# Importer les variables globales
import settings

# Importe la bibliothèque qui permet d'afficher un message d'erreur
from sys import stderr

# Importe la bibliothèque qui permet d'effacer l'écran
from os import system, name

# Importe nos fonctions utiles
from utils import func

# Charge les paramètres
settings.init()

# Importe la fonction de gestion des utilisateurs
from users import manageusers as usr

# Importe la fonction de gestion du protocole FTP
from ftp import ftpmain as ftp

# Importe la fonction de gestion de la fonction monitoring
from monitoring import monitoring as mon

# Importe la fonction de gestion de la fonction monitoring
from security import pwdcheck as pwd

##################################################################################
###                           Main script function                             ###
##################################################################################

def main():
    # Permet d'effacer l'écran
    system('cls' if name == 'nt' else 'clear')

    # Affiche le message de bienvenue du script
    print ("""*****************************************************
                                         _       _
 ___ _   _ _ __   ___ _ __ ___  ___ _ __(_)_ __ | |_
/ __| | | | '_ \ / _ \ '__/ __|/ __| '__| | '_ \| __|
\__ \ |_| | |_) |  __/ |  \__ \ (__| |  | | |_) | |_
|___/\__,_| .__/ \___|_|  |___/\___|_|  |_| .__/ \__|
          |_|                             |_|

*****************************************************""")
    if settings.isFr:
        print("Bienvenue sur superscript ! Fait pour vous aider à gérer votre infrastructure informatique !")
        print("Par BRETAGNOLLE Guillaume, GERARD Angelo, KANY Kevin, PECH Laurent\n")
    else:
        print("Welcome to superscript! Made to help you manage your IT infrastructure!")
        print("By BRETAGNOLLE Guillaume, GERARD Angelo, KANY Kevin, PECH Laurent\n")

    if settings.isFr:
        menuchoice = func.myChoice("Menu principal", "Gérer les utilisateurs", "Gérer le serveur FTP", "Supervision", "Securité", "Quitter")
    else:
        menuchoice = func.myChoice("Main Menu", "Manage User", "Manage FTP Server", "IT Monitoring", "Cybersecurity", "Exit")

    if menuchoice == 1:
        print("\nChoice 1 - Manage User\n")
        usr.manusers()
    elif menuchoice == 2:
        print("\nChoice 2 - Manage FTP Server\n")
        ftp.ftp()
    elif menuchoice == 3:
        print("\nChoice 3 - IT Monitoring\n")
        mon.monitor()
    elif menuchoice == 4:
        print("\nChoice 4 - Cybersecurity\n")
        pwd.pwdtest()
    elif menuchoice == 5:
        print("\nChoice 5 - Exit\n")
    else:
        print('Error', file=stderr)

# ---

# Démarre le script
main()
