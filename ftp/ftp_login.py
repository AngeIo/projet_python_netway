# Ce script permet de se connecter sur le serveur FTP pour les 3 clients FTP AC distants

from ftplib import FTP

# Les paramètres de connexion au serveur FTP
#ftp_host = '127.0.0.1'
#ftp_login = 'Laurent'
#ftp_password = 'G20'

# Connexion au serveur pour chacun des AC
#ftp = FTP(ftp_host, ftp_login, ftp_password)
#print(ftp.getwelcome()) # Message de bienvenue

def login():
    ftp_host = '127.0.0.1'
    ftp_login = 'Laurent'
    ftp_password = 'G20'
    ftp = FTP(ftp_host, ftp_login, ftp_password)
    print(ftp.getwelcome())
    return ftp
