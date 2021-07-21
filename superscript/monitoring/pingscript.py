# This program checks that a machine is up by sending it a ping. It shows if the ping to a device was "ok" or "unsuccessful".

from subprocess import check_call, CalledProcessError,PIPE
import time

def pingiprange():

    # Principe du programme :
    print("This program will run a Ping request every 5 seconds on a round of IP's until told to stop (using ctrl+c).")
    # Combien d'ip faut-il surveiller ?
    n = int(input("How many IP's are we checking: "))
    ips = []

    while n<1:
        # On se prépare à l'exception ou un nombre d'ip inférieur à 1 est saisi.
        n = int(input("Please input a number above 0 :"))
    if n>0:
        ips = [input("Enter IP number {}: ".format(i)) for i in range(1, n + 1)]


    while True:
        # Pour chaque ip renseignée, on envoie un ping :
        for ip in ips:
            try:
                out = check_call(['ping', '-n', '2', ip],stdout=PIPE)
            except CalledProcessError as e:
                # Si absence de réponse au ping alors :
                print("Ping to {} unsuccessful".format(ip))
                continue
            # Si on arrive jusqu'ici, le ping a fonctionné :
            print("Ping to {} ok".format(ip))
        print("Ctrl+c to stop this program.")
        time.sleep(3)
