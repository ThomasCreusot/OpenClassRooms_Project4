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

        # I add the tournament and round names for import from the database; I could create a function
        # match_serialisation, however, it implies to create a new table in the databse as rounds do not contain
        # matches instances but their representation as lists
        self.match_tuple_representation = ([self.player_1_index, self.player_1_score],
                                           [self.player_2_index, self.player_2_score],
                                           self.name_of_tournament_in_which_match_was_played,
                                           self.name_of_round_in_which_round_was_played)

        return self.match_tuple_representation
