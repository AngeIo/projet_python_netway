# Ce script permet les fichiers en lien avec le FTP

# Permet de faire une pause dans le programme
import time

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')
from utils import func

# Importe toutes les fonctions FTP dans ce programme pour pouvoir les lancer depuis superscript
from ftp import ftp_login
from ftp import ftp_download
from ftp import ftp_upload

# Importer les variables globales
import settings

# Charge les paramètres
settings.init()

def ftp():
    while True:
        opschoice = func.myChoice("Bienvenue, veuillez choisir une option", "Login", "Download", "Upload", "Exit")
        if opschoice == 1:
            ftp_login.login()
        elif opschoice == 2:
            ftp_download.download()
        elif opschoice == 3:
            ftp_upload.upload()
        elif opschoice == 4:
            # On exit
            print("Arrêt du système...")
            time.sleep(1)
            break
