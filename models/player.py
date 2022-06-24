from tinydb import TinyDB
import json


database = TinyDB('db.json') 
players_table = database.table('players')


class Player:
    """Represents a player"""

    PLAYERS = [] # Class attribute, will contains the list of all players


    # Je """.""" le code ci dessous sinon j'ai deux def __init__ et au final je n'en ai pas besoin, car dans la 
    # fonction save_players_serialisation_from_python_to_json : je recherche chaque attribut
    """
    #Si vos modèles n’en disposent pas encore, mettez en place un moyen de créer des instances à partir d’un « dictionnaire » ou de données orientées texte.
    def __init__(self, **player_attributes) :
        for attr_name, attr_value in player_attributes.items():
            #La méthode setattr() est équivalente au code suivant : my_object.attribute = value _source: cours OC
            setattr(self, attr_name, attr_value)
            
            #rappel, on avait deux valeurs par défaut qui n'étaient pas dans les parametres du def __ini__: 
            #self.player_score_at_round_scale = 0
            #self.player_total_score_at_tournament_scale = 0
    """ 


    # def __init__ initial, avant la mise en place de tinydb ; je le garde pour pouvoir continuer à créer de nouveaux 
    # joueurs
    def __init__(self, index, family_name, first_name, birth_date, gender, rank) :
        self.index = index
        self.family_name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.player_score_at_round_scale = 0
        self.player_total_score_at_tournament_scale = 0


    @classmethod
    def add_player_to_PLAYERS_list(cls, player):
        """Adds a player in the class attribute PLAYER"""

        cls.PLAYERS.append(player)


    @classmethod
    def listing_all_players(cls):
        """Returns the list containing all players in PLAYERS"""

        return cls.PLAYERS


    # Finally in the controller
    """
    def update_player_rank(self, updated_rank):
        self.rank = updated_rank
        pass
        
    """


    # Si vos modèles n’en disposent pas encore, mettez en place un moyen de créer des instances à partir d’un 
    # « dictionnaire » ou de données orientées texte.
    # lors de la mise en place de la db je retravaille la fonction : au final on revient à la meme chose que 
    # load_players_from_tinydb_database() : la source n'est juste pas la meme : players_json ou db
    """
    @classmethod
    def players_initialization_from_json_dictionnary(cls):
        #players_initialization_from_json_dictionnary and recording in PLAYERS list (method attribute)
        
        #code avant de mettre en place la bd : 
        #for player_attributes in json.load(open("players_json.json")): #il faut ouvrir la bdd "db.json" ; on veut acceder à la table appelée players_table en python
            #player = Player(**player_attributes)
            #Player.add_player_to_PLAYERS_list(player)
        
        #for player_attributes in players_table:
            #player = Player(**player_attributes)
            #Player.add_player_to_PLAYERS_list(player)
    """


    #Implémentez une méthode `save` sur vos modèles, qui sérialise tous les attributs de vos entités.
    #????? : Note : Veille à bien préserver l'ordre de la liste lorsque tu sérialises/désérialises les joueurs !
    @classmethod
    def save_players_serialisation_from_python_to_json(cls):
        """Serialises python objects (players) at the json format and returns a list of these serialized objects"""

        all_players_python = cls.PLAYERS
        serialized_players = []
        # ????? : Question: on ne peut on pas automatiser avec quelque chose de la forme
        # ' for attr_name, attr_value in player_instance.items() '
        # peut etre pas 'items' car ce n'est pas un tableau mais une instance
        for player_instance in all_players_python:
            serialized_player = {
                'index' : player_instance.index, 
                'family_name' : player_instance.family_name, 
                'first_name' : player_instance.first_name, 
                'birth_date' : player_instance.birth_date, 
                'gender' : player_instance.gender, 
                'rank' : player_instance.rank
            }
            print(serialized_player)
            serialized_players.append(serialized_player)
        return serialized_players


    @classmethod
    def write_serialized_player_in_tinydb_database(cls):
        """Inserts serialized players at json format into player table of the tinydb database"""

        serialized_players = Player.save_players_serialisation_from_python_to_json()
        players_table.truncate() #clear the table first
        players_table.insert_multiple(serialized_players)

    #????? : Note : Veille à bien préserver l'ordre de la liste lorsque tu sérialises/désérialises les joueurs !
    @classmethod
    def load_players_from_tinydb_at_python_format(cls):
        "Load all players from the tinydb database and convert them in python objects"

        serialized_players = players_table.all() 
        for serialized_player in serialized_players:
            player_index = serialized_player['index']
            player_family_name = serialized_player['family_name']
            player_first_name = serialized_player['first_name']
            player_birth_date = serialized_player['birth_date']
            player_gender = serialized_player['gender']
            player_rank = serialized_player['rank']

            player_instance = Player(player_index, player_family_name, player_first_name, player_birth_date, player_gender, player_rank)
            Player.add_player_to_PLAYERS_list(player_instance)

        # ????? : a tester: 
        #for attr_name, attr_value in serialized_player.items():
            #La méthode setattr() est équivalente au code suivant : my_object.attribute = value _source: cours OC
            #setattr(self, attr_name, attr_value)
        # --> sauf que le 'self' me pose probleme
