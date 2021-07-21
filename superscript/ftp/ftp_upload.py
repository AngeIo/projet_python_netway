# Ce script permet d'upload un fichier sur le serveur FTP

from ftplib import FTP

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')

from ftp import ftp_login

# Importer les variables globales
import settings

# Charge les paramètres
settings.init()

ftp = ftp_login.login()

def upload():
    # Ouverture du fichier en read binary, ce qui renvoie un descripteur source_file
    file = open("Test1.txt", 'rb') # Dans notre cas, ouverture d'un fichier txt
    ftp.storbinary('STOR Test1.txt', file)
    print("File uploaded\nClosing file...\n")
    file.close() # Fermer le fichier
