class Match:
    """Represent a match"""

    def __init__(self, player_1_index, player_2_index, player_1_score=0, player_2_score =0) : 
        #self.player_1_instance = player_1_instance
        #self.player_2_instance = player_2_instance
        self.player_1_index = player_1_index
        self.player_2_index = player_2_index
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score


    def match_tuple_representation(self):
        """Returns a representation of the match, under a tuple format """

        self.match_tuple_representation = ([self.player_1_index, self.player_1_score], \
            [self.player_2_index, self.player_2_score])

        #self.match_tuple_representation = ([self.player_1_instance, self.player_1_score], \
        #    [self.player_2_instance, self.player_2_score])

        return self.match_tuple_representation
