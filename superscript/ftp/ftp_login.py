# Ce script permet de se connecter sur le serveur FTP pour les 3 clients FTP AC distants

from ftplib import FTP

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')
from utils import func

# Importer les variables globales
import settings

# Charge les paramètres
settings.init()

def login():
    # Les paramètres de connexion au serveur FTP
    ftp_host = '127.0.0.1'
    ftp_login = 'Laurent'
    ftp_password = 'G20'
    # Connexion au serveur pour chacun des users
    try:
        ftp = FTP(ftp_host, ftp_login, ftp_password)
        print(ftp.getwelcome()) # Message de bienvenue
        return ftp
    except Exception as e:
        print("/!\ Error occured while login /!\ \n", e)
    return 1
