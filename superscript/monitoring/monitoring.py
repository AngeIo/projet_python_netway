# Ce script permet les fichiers en lien avec le Monitoring

# Permet de faire une pause dans le programme
import time

# Importe nos fonctions utiles
import sys
sys.path.insert(0, '../')
from utils import func

# Importe toutes les fonctions de Monitoring dans ce programme pour pouvoir les lancer depuis superscript
from monitoring import pingscript
from monitoring import portscanning

# Importer les variables globales
import settings

# Charge les paramètres
settings.init()

def monitor():
    while True:
        opschoice = func.myChoice("Bienvenue, veuillez choisir une option", "Ping", "Port scanning", "Exit")
        if opschoice == 1:
            pingscript.pingiprange()
        elif opschoice == 2:
            portscanning.portscanning()
        elif opschoice == 3:
            # On exit
            print("Arrêt du système...")
            time.sleep(1)
            break
