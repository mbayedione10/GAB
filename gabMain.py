import GAB.fonctionGab as gab


def main():
    listeClient = gab.initialiserFileClient()
    while True:

        choice = gab.menu()

        if(choice == 1):
            print("vous etes entrain d'ajouter un client")
            listeClient = gab.ajouterClient(listeClient)
            print("Client ajouté(s). Merci. Voici la liste d'attente...")
            gab.afficherFileClient(listeClient)


        elif(choice == 2):
            print("traitement d'un client")
            listeClient = gab.traiterClient(listeClient)
            print("Retrait efféctué. Merci!!")
            print("La liste des clients restants")
            gab.afficherFileClient(listeClient)

        elif(choice == 3):
            print("Affichage des clients en Attente")
            gab.afficherFileClient(listeClient)


        elif(choice == 4):
            print("Vider la liste des clients")
            gab.ViderFileClient(listeClient)
            print("deleting...")
            print("deleting...")
            print("deleting...")
            print("La liste est vide")
            quit()


        elif(choice == 5):
            gab.supprimerClient(listeClient)
            print("Le client a quitté la file")
            gab.afficherFileClient(listeClient)

        else:
            quit()




if __name__ == '__main__':
    main()




