#Modelisation
"""
TYPE Client: ENREGISTREMENT
     VARIABLE nom [30]: CHAR
     VARIABLE prenom [30]: CHAR
     VARIABLE genre : CHAR
     VARIABLE suivant : Client*
FIN_ENREG
"""
#Constucteur
class Client:
    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.genre = ""
    #Fin constructeur
