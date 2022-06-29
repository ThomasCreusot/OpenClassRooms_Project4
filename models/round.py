class Round:
    """Represents a round"""

    def __init__(self, name, date_and_time_beginning, date_and_time_ending) : 
        self.name = name
        self.date_and_time_beginning = date_and_time_beginning
        self.date_and_time_ending = date_and_time_ending
        self.matches_tuples_representations = []


    def round_serialisation(self):
        """Serialises a python object (round) at the json format and returns this serialized object"""

        serialized_round = {
            'name' : self.name, 
            'date_and_time_beginning' : str(self.date_and_time_beginning),
            'date_and_time_ending' : str(self.date_and_time_ending),
            'matches_tuples_representations' : str(self.matches_tuples_representations)
        }

        return serialized_round