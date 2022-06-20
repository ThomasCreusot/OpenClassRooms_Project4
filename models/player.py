class Player:
    """Represents a player"""

    PLAYERS = [] # Class attribut, will contains the list of all players


    def __init__(self, index, family_name, first_name, birth_date, gender, rank) :
        self.index = index
        self.family_name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.player_score_at_round_scale = 0


    @classmethod
    def add_player_to_PLAYERS_list(cls, player):
        """Adds a player in the class attribute PLAYER"""
        
        cls.PLAYERS.append(player)


    @classmethod
    def listing_all_players(cls):
        pass
        """Returns the list containing all players in PLAYERS"""
        
        return Players.PLAYERS
        #VIEWS : print(Players.listing_all_players())


    def update_player_rank(self, updated_rank):
        self.rank = updated_rank
        # à utiliser de la maniere player27.update_player_rank(123456) --> le rank du joueur devient 123456
        # question : impact du rank des joueurs avant/apres, en fonction de si le rank est < ou > au updated rank
        pass
