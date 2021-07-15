#!/usr/bin/env python3
# coding: utf-8
# This program is used to scan network ports on devices. It shows if the port is open or closed.


import socket
# Prise en charge regex
import re

def checkip(ip):
    return re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip)

def checkport(server, port):
    #Crée une socket sur la machine hôte qui sera utilisée pour communiquer avec une machine distante.
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:  # Gestion de l'exception
        mysocket.connect(server, port)
        result = True
    except:
        # Si erreur de connexion sur le serveur alors on ferme la connexion :
        result = False
    mysocket.close()
    return result

def portscanning():
    server = ""
    # On fait un regex pour vérifier que l'adresse ip est au bon format :
    while not checkip(server):
        server=input("Enter the ip address of the machine whose ports you want to scan: ")
    # Initialisation des variables :
    p1=0
    p2=0

    # On se prépare à l'exception ou un numéro de port inférieur à 1 ou supérieur à 65536 est saisi.
    while p1<1 or p1>65536:
        p1 = int(input("Enter a port number between 1 and 65536 for the starting port : "))


    while p2<p1 or p2>65536:
        p2 = int(input("Enter a port number between " + str(p1) + " and 65536 for the finishing port : "))

    # On ajoute +1 à p2 pour compenser le fonctionnement de Python.
    for port in range(p1,p2+1):
        # Soit le port est ouvert :
        if checkport(server, port):
            print("Port", port, "is open.")
        # Soit il est fermé :
        else:
            print("Port", port, "is closed.")
            continue

portscanning()
