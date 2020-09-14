import GAB.modelGab as model


def poursuivre():
    print ("Poursuivre? (oui:1) (non:0)\t")
    continuer = int(input())
    return continuer


#Menu qui permet l'affichage des situations possibles
def menu():
    print("Action?: ")
    print("1- Ajouter un client dans  la file ?")
    print("2- Traiter un client au debut de la liste ?")
    print("3- Afficher la liste des clients en attente ?")
    print("4- vider la liste ?")
    print("5- identifier,vider un client et afficher la liste des clients restant dans la File?")
    print("Entrer votre choix: ")
    choice = int(input())
    return choice

#Ajoute un Client dans la file
def ajouterClient(file):
    a=1
    while(a==1):
        print("Entrer votre nom svp: ")
        model.Client.nom  = input()
        print("Entrer votre prenom svp: ")
        model.Client.prenom = input()
        print("Entrer votre genre svp: ")
        model.Client.genre = input()
        cli = [model.Client.nom,model.Client.prenom,model.Client.genre]
        file.append(cli)
        a = int(input("Poursuivre? (oui:1) (non:0)\t"))
    return file


#Supprime un client de la file
def traiterClient(file):
    file.pop(0)
    #print(file)
    return file

#affiche tous les clients de la file
def afficherFileClient(file):
    print("************************")
    for x in range(len(file)):
        print(" nom:",file[x][0])
        print(" prenom:",file[x][1])
        print(" genre:",file[x][2])
        print("************************")

#Vide la mémoire occupée
def ViderFileClient (file):
    file.clear()

#Supprime un client quelconque de la file.
def supprimerClient(file):
        print("Entrer votre nom svp:")
        model.Client.nom = input()
        print("Entrer votre prenom svp:")
        model.Client.prenom = input()
        #parcourir la file et supprimer le client avec le nom et prenom entre par le client
        for x in range(len(file)):
            if (file[x][0] == model.Client.nom or file[x][0] == model.Client.prenom):
                #find index
                #indx = file.index(file[x])

                print("************************")
                print(" nom:", file[x][0])
                print(" prenom:", file[x][1])
                print(" genre:", file[x][2])
                print("************************")
                #file.pop(indx)
                #supprimer l'element dans la liste
                file.remove(file[x])
                print("le client {} {} est supprimé dans la liste ".format(model.Client.prenom, model.Client.nom))
                print(file)
                break

            #else:
                #print("le client {} {} n'est pas dans la liste ".format(model.Client.prenom,model.Client.nom))




def initialiserFileClient():
    i = 1
    listeClient = []
    while (i == 1):
        print("Entrer votre nom svp: ")
        model.Client.nom = input()
        print("Entrer votre prenom svp: ")
        model.Client.prenom = input()
        print("Entrer votre genre svp: ")
        model.Client.genre = input()
        cli = [model.Client.nom, model.Client.prenom, model.Client.genre]
        listeClient.append(cli)
        print("Voulez vou continuer? (0:NON || 1:OUI)")
        #return listeClient
        i = int(input())
    return listeClient




list=[['dfd', 'fsd','ewfsdf'],['test1','test2','test3'],['te','tee','teee'],['pa','paa','paaa']]
#ajouterClient(list)
#afficherFileClient(list)
#print(list)
#initialiserFileClient()


