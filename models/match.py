class Match:
    """Represent a match"""

    def __init__(self, name_of_tournament_in_which_match_was_played, name_of_round_in_which_round_was_played,
                 player_1_index, player_2_index, player_1_score=0, player_2_score=0):
        self.name_of_tournament_in_which_match_was_played = name_of_tournament_in_which_match_was_played
        self.name_of_round_in_which_round_was_played = name_of_round_in_which_round_was_played
        self.player_1_index = player_1_index
        self.player_2_index = player_2_index
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score

    def match_tuple_representation(self):
        """Returns a representation of the match, under a tuple format """

        # j'ajoute nom du tournois et du round pour l'import depuis la bdd, j'aurai pu créer une fonction
        # match_serialisation, mais il aurait fallu créer une nouvelle table dans la base de données étant donné que
        # les rounds ne contiennent pas les instances de match mais leur représentation sous forme de liste
        self.match_tuple_representation = ([self.player_1_index, self.player_1_score],
                                           [self.player_2_index, self.player_2_score],
                                           self.name_of_tournament_in_which_match_was_played,
                                           self.name_of_round_in_which_round_was_played)

        return self.match_tuple_representation
