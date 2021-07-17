# Ce script permet de télécharger un fichier du serveur FTP vers un dossier en local défini

from ftplib import FTP
import os

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')
from utils import func

from ftp import ftp_login

# Importer les variables globales
import settings

# Charge les paramètres
settings.init()

ftp = ftp_login.login()

def download():
    # Client dossier sauvegarde
    savedir = "C:/Users/laure/Reception"
    os.chdir(savedir)

    # Serveur - se mettre dans le bon répertoire
    ftp.cwd("Test")
    # Serveur - nom fichier à copier
    filename = "Test.txt"
    try:
        file = open(filename, "wb")
    except Exception as e:
        print("Problème lors de l'ouverture du fichier")
        print("Erreur complète :\n", e)
    ftp.retrbinary('RETR ' + filename, file.write, 1024)
    try:
        file.close()
    except Exception as e:
        print("Problème lors de la fermeture du fichier")
        print("Erreur complète :\n", e)
    print("Téléchargement terminé")
