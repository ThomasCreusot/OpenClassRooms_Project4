class Match:
    """Represent a match"""

    def __init__(self, player_1_instance, player_2_instance, player_1_score=0, player_2_score =0) : 
        self.player_1_instance = player_1_instance
        self.player_2_instance = player_2_instance
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score


    def match_tuple_representation(self):
        self.match_tuple_representation = ([self.player_1_instance, self.player_1_score], \
            [self.player_2_instance, self.player_2_score])

        #TESTOK: print("Match tuple representation", self.match_tuple_representation)
        return self.match_tuple_representation
