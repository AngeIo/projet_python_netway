#!/usr/bin/env python3
# coding: utf-8

# Permet de rendre compatible ce script avec Python2 et Python3
from __future__ import print_function

# Importer les variables globales
import settings

##################################################################################
###                    Utility functions used in the script                    ###
##################################################################################

# Fonction myChoice :
#     Cette fonction sert à générer un prompt pour répondre à une question, les réponses possibles sont 1 2 3 4 etc.
#     Utilisation de la fonction :
#     myChoice("QUESTION", "RÉPONSE 1", "RÉPONSE 2", "RÉPONSE 3", "RÉPONSE 4", "etc.")
#     et Affiche la sortie suivante :
#     QUESTION :
#     [1] RÉPONSE 1
#     [2] RÉPONSE 2
#     [3] RÉPONSE 3
#     [4] RÉPONSE 4
#     Entrez un numéro correspondant à la liste ci-dessus: [NUMÉRO LISTE]

def myChoice(*args):
  startLst = 1
  endLst = len(args) - 1
  if endLst < 1:
    print('At least 2 arguments are needed using the following format : mychoice "QUESTION" "ANSWER 1" "ANSWER 2" etc.', file=stderr)
    return -1
  lines = ''
  lines += args[0] + " :\n----\n"
  i = 1
  while i < endLst + 1:
    if args[i][0] == '/':
        lines += "[/] " + args[i][:1] + "\n"
    else:
        lines += "[" + str(i) + "] " + args[i] + "\n"
    i += 1
  invalidchoice = 1
  while invalidchoice:
    invalidchoice = 0
    print(lines)
    if settings.isFr:
        choicenumber = input('Entrez un numéro correspondant à la liste ci-dessus et appuyer sur "Entrée": ')
    else:
        choicenumber = input('Enter a number from the list above and press "Enter": ')
    if choicenumber and choicenumber.isdigit():
        choicenumber = int(choicenumber)
    else:
        choicenumber = 0
    if not choicenumber or choicenumber < startLst or choicenumber > endLst:
      print("\n----\n")
      if settings.isFr:
          print("/!\ Choix invalide, veuillez réessayer /!\ \n\n")
      else:
          print("/!\ Invalid choice, please try again /!\ \n\n")
      invalidchoice = 1
    if not invalidchoice:
        if args[choicenumber][0] == '/':
            print("\n----\n")
            if settings.isFr:
                print("/!\ Choix interdit, veuillez réessayer /!\ \n\n")
            else:
                print("/!\ Forbidden choice, please try again /!\ \n\n")
            invalidchoice = 1
  return choicenumber
