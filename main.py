"""
MODELS

Étape 2 : Définir (et coder) les modèles pour ce projet
Modèle : Le modèle contient les informations relatives à l’état du système. Ce sont les fonctionnalités brutes de 
l’application.
A partir du Use Case: identification des principaux éléments
Note : ne devrait pas contenir la «logique» du jeu


-Commencer par les modèles : avec quelles entités votre programme va-t-il fonctionner ? 
-Doivent-elles contenir des données (= attributs) ? 
-Appliquent-elles des comportements spécifiques (= méthodes) ?

"""


class Tournament:
    """Represents a tournament"""

    TOURNAMENTS = [] # Attribut de classe Note : "Un attribut de classe est une variable dont le champ d'action s'étend 
    # à l'ensemble d'une classe. Ils sont très utilisés pour compter le nombre d'instances d'une classe par exemple" 
    # source: Cours OC

    def __init__(self, name, localisation, date_of_beginning, date_of_ending, time_controler, description, 
                number_of_rounds = "4", rounds=[], players=[]) :
        self.name = name
        self.localisation = localisation
        self.date_of_beginning = date_of_beginning
        self.date_of_ending = date_of_ending
        self.time_controler = time_controler
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.rounds = rounds
        self.players = players
    
    @classmethod
    def add_tournament_to_TOURNAMENTS_list(cls, tournament):
        """Adds a tournament in the method attribute TOURNAMENTS"""
        
        cls.TOURNAMENTS.append(tournament)


    @classmethod 
    def Tournaments_listing(cls):
        """Returns the list containing all tournaments in TOURNAMENTS"""
        
        return Tournament.TOURNAMENTS
        #VIEWS : print(Tournament.Tournaments_listing())


    def tournament_players_listing_alphabectic_order(self):
        """Returns the list containing all players of a tournament, by alphabetic order"""
        pass


    def tournament_players_listing_by_ronk_order(self):
        """Returns the list containing all players of a tournament, by rank order"""
        pass


    def tournament_rounds_listing(self):
        """Returns the list containing all rounds of a tournament"""
        
        return self.rounds
        #VIEWS : print(tournamentX.tournament_rounds_listing())


    def tournament_matchs_listing(self):
        """Returns the list containing all matchs of a tournament"""

        pass



"""
tournament1 = Tournament("thom", "pau", "being", "ending", "blitch", "description")
print(tournament1.time_controler)
Tournament.add_tournament_to_TOURNAMENTS_list(tournament1)

tournament2 = Tournament("moth", "tlse", "aze", "qsd", "timee", "description2", rounds=["aze","qwsdqsd"])
print(tournament2.time_controler)
Tournament.add_tournament_to_TOURNAMENTS_list(tournament2)


print(Tournament.Tournaments_listing())

print(tournament2.tournament_rounds_listing())
"""

class Rounds:
    def __init__(self) -> None:
        pass #RESUME HERE