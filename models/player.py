from tinydb import TinyDB


database = TinyDB('db.json')
players_table = database.table('players')


class Player:
    """Represents a player"""

    PLAYERS = []  # Class attribute, will contains the list of all players

    def __init__(self, index, family_name, first_name, birth_date, gender, rank, player_score_at_round_scale=0,
                 player_total_score_at_tournament_scale=0):
        self.index = index
        self.family_name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.player_score_at_round_scale = player_score_at_round_scale
        self.player_total_score_at_tournament_scale = player_total_score_at_tournament_scale

    @classmethod
    def add_player_to_PLAYERS_list(cls, player):
        """Adds a player in the class attribute PLAYER"""

        cls.PLAYERS.append(player)

    @classmethod
    def listing_all_players(cls):
        """Returns a list containing all players in PLAYERS"""

        return cls.PLAYERS

    @classmethod
    def save_players_serialisation_from_python_to_json(cls):
        """Serialises python objects (players) at the json format and returns a list of these serialized objects"""

        all_players_python = cls.PLAYERS
        serialized_players = []

        for player_instance in all_players_python:
            serialized_player = {
                'index': player_instance.index,
                'family_name': player_instance.family_name,
                'first_name': player_instance.first_name,
                'birth_date': player_instance.birth_date,
                'gender': player_instance.gender,
                'rank': player_instance.rank,

                'player_score_at_round_scale': player_instance.player_score_at_round_scale,
                'player_total_score_at_tournament_scale': player_instance.player_total_score_at_tournament_scale
            }
            serialized_players.append(serialized_player)
        return serialized_players

    @classmethod
    def write_serialized_player_in_tinydb_database(cls):
        """Inserts serialized players at json format into player table of the tinydb database"""

        serialized_players = Player.save_players_serialisation_from_python_to_json()
        players_table.truncate()  # clear the table first
        players_table.insert_multiple(serialized_players)

    @classmethod
    def load_players_from_tinydb_at_python_format(cls):
        "Loads all players from the tinydb database and convert them in python objects"

        serialized_players = players_table.all()
        for serialized_player in serialized_players:
            player_index = serialized_player['index']
            player_family_name = serialized_player['family_name']
            player_first_name = serialized_player['first_name']
            player_birth_date = serialized_player['birth_date']
            player_gender = serialized_player['gender']
            player_rank = serialized_player['rank']

            player_score_at_round_scale = serialized_player['player_score_at_round_scale']
            player_total_score_at_tournament_scale = serialized_player['player_total_score_at_tournament_scale']

            # int() : used in the model as we import data, in the present case it is not the user who
            # gives the information but the program
            player_instance = Player(int(player_index), player_family_name, player_first_name, player_birth_date,
                                     player_gender, int(player_rank), player_score_at_round_scale,
                                     player_total_score_at_tournament_scale)
            Player.add_player_to_PLAYERS_list(player_instance)
