class Round:
    """Represents a round"""

    def __init__(self, name_of_tournament_in_which_round_was_played, name, date_and_time_beginning,
                 date_and_time_ending, matches_tuples_representations=None):
        self.name_of_tournament_in_which_round_was_played = name_of_tournament_in_which_round_was_played
        self.name = name
        self.date_and_time_beginning = date_and_time_beginning
        self.date_and_time_ending = date_and_time_ending

        if matches_tuples_representations is None:
            self.matches_tuples_representations = []
        else:
            self.matches_tuples_representations = matches_tuples_representations

    def round_serialisation(self):
        """Serialises a python object (round) at the json format and returns this serialized object"""

        serialized_round = {
            'name_of_tournament_in_which_round_was_played': self.name_of_tournament_in_which_round_was_played,
            'name': self.name,
            'date_and_time_beginning': str(self.date_and_time_beginning),
            'date_and_time_ending': str(self.date_and_time_ending),
            'matches_tuples_representations': self.matches_tuples_representations
        }

        return serialized_round

    @classmethod
    def round_deserialization_from_json_to_python_format(cls, rounds_at_json_dictionnary_format):
        """Converts rounds at json dictionnary format into rounds at python objet format : instances of Round class"""

        all_rounds_instances_from_database_python_format = []
        round_matches_tuples_representations_json_format_list = []
        for serialized_round in rounds_at_json_dictionnary_format:

            name_of_tournament_in_which_round_was_played = \
                serialized_round['name_of_tournament_in_which_round_was_played']
            name = serialized_round['name']
            date_and_time_beginning = serialized_round['date_and_time_beginning']
            date_and_time_ending = serialized_round['date_and_time_ending']

            round_matches_tuples_representations_json_format_list.append(
                serialized_round['matches_tuples_representations'])

            round_instance = Round(name_of_tournament_in_which_round_was_played, name, date_and_time_beginning,
                                   date_and_time_ending)

            all_rounds_instances_from_database_python_format.append(round_instance)

        return all_rounds_instances_from_database_python_format, round_matches_tuples_representations_json_format_list
