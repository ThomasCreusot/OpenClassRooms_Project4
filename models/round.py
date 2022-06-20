class Round:
    """Represents a round"""

    def __init__(self, name, date_and_time_beginning, date_and_time_ending) : 
        self.name = name
        self.date_and_time_beginning = date_and_time_beginning
        self.date_and_time_ending = date_and_time_ending
        self.matches_tuples_representations = []
