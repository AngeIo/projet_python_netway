# Ce script permet d'upload un fichier sur le serveur FTP

from ftplib import FTP
import os

import ftp_login

ftp = ftp_login.login()

def upload():

    # Ouverture du fichier en read binary, ce qui renvoie un descripteur source_file
    file = open("Test.txt", 'rb') # Dans notre cas, ouverture d'un fichier txt
    ftp.storbinary('STOR Test.txt', file)
    file.close() # Fermer le fichier

upload()
