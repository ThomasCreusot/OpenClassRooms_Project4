# Use of sorted():
# https://docs.python.org/fr/3/library/functions.html#sorted
# https://docs.python.org/fr/3/howto/sorting.html#sortinghowto


from tinydb import TinyDB


DEFAULT_VALUE_NUMBER_ROUNDS_PER_TOURNAMENT = "4"


database = TinyDB('db.json')
tournaments_table = database.table('tournaments')


class Tournament:
    """Represents a tournament"""

    TOURNAMENTS = []  # Class attribute, will contains the list of all tournaments

    # def __init__(..., player = []) --> Not correct (variable at the scale of the class)
    # def __init__(..., player = None) --> Correct
    # def __init__(..., ) --> Correct
    def __init__(self, name, localisation, date_of_beginning, date_of_ending, time_controler, description,
                 number_of_rounds=DEFAULT_VALUE_NUMBER_ROUNDS_PER_TOURNAMENT, rounds=None, players=None):
        self.name = name
        self.localisation = localisation
        self.date_of_beginning = date_of_beginning
        self.date_of_ending = date_of_ending
        self.time_controler = time_controler
        self.description = description
        self.number_of_rounds = number_of_rounds
        if rounds is None:
            self.rounds = []
        else:
            self.rounds = rounds
        if players is None:
            self.players = []
        else:
            self.players = players

    @classmethod
    def add_tournament_to_TOURNAMENTS_list(cls, tournament):
        """Adds a tournament in the class attribute TOURNAMENTS"""

        cls.TOURNAMENTS.append(tournament)

    @classmethod
    def listing_all_tournaments(cls):
        """Returns the list containing all tournaments in TOURNAMENTS"""

        return Tournament.TOURNAMENTS

    def tournament_players_listing(self):
        """Returns the list containing all players of a tournament"""

        return self.players

    def tournament_rounds_listing(self):
        """Returns the list containing all rounds of a tournament"""

        return self.rounds

    def tournament_matches_listing(self):
        """Returns the list containing all matches of a tournament"""

        matches_tuples_representation_list = []

        for round in self.rounds:
            matches_tuples_representation_list.append(round.matches_tuples_representations)

        return matches_tuples_representation_list

    # Note: At the tournament scale, because it is applied to a player of a tournament.
    def SwissAlgorithm_applied_to_the_tournament_by_rank_classification(self, tournament_players):
        """Returns pairs of players of a tournament; for matches of a round, based on their classification (rank)"""

        # 1. At the beginning of the first round, sort player by their rank
        all_players_of_tournament_sorted_by_ranks = sorted(tournament_players, key=lambda x: x.rank, reverse=False)

        # Verification that we got an odd number of players
        if (len(all_players_of_tournament_sorted_by_ranks)) % 2 == 0:

            # 2. Separate players in two halves: higher and lower.
            # Note: Use int() and not "round" because there is not an even number of players
            higher_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[
                0:int(len(all_players_of_tournament_sorted_by_ranks)/2)]  # 0:4 --> 0,1,2,3
            lower_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[
                int(len(all_players_of_tournament_sorted_by_ranks)/2):
                int(len(all_players_of_tournament_sorted_by_ranks))]  # 4:8 --> 4,5,6,7

            # 2(next): The best player of the higher half plays against the best player of the lower one
            # Pairs: variable which contains the pair of players who will play against each other
            pairs = []
            for i in range(0, (len(higher_half_of_players_sorted_by_ranks))):
                pair = (higher_half_of_players_sorted_by_ranks[i], lower_half_of_players_sorted_by_ranks[i])
                pairs.append(pair)
            return pairs

        else:  # Even number of players
            return None

        # 3. At the next round, sort all players by their number of points. Number of point is relative to the player
        # in a tournament. If several players got the same number of point, sort them by their rank
        # --> new function

    def SwissAlgorithm_applied_to_the_tournament_by_score_classification(self, tournament_players):
        """Returns pairs of players of a tournament for matches of a round, based on their number of points"""

        # For each player, we search the sum of the points he/she accumulated during the round
        # Steps:
        # 1. For each player, browse the rounds of the tournament and matches of the round
        # 2. Search and count points
        # 3. Make a new list and sort it

        # Steps 1 et 2
        for player in tournament_players:
            # Reinitialisation of the player score at the round scale
            player.player_score_at_round_scale = 0

            # Browsing all round
            for round in self.rounds:
                # Browsing matches
                for match in round.matches_tuples_representations:
                    # print("match", match) >>> match ([2, 0.0], [6, 1.0])
                    for player_index_and_its_score in match:
                        if player.index == player_index_and_its_score[0]:
                            # print(player_and_its_score[0].family_name, "got the score", player_and_its_score[1], \
                            #    "during the match", match)

                            player.player_score_at_round_scale += player_index_and_its_score[1]
        # Step 3
        # Decreasing order to get the best score in first place
        all_players_of_tournament_sorted_by_score_at_round_scale = sorted(tournament_players,
                                                                          key=lambda x: x.player_score_at_round_scale,
                                                                          reverse=True)

        # https://docs.python.org/fr/3/howto/sorting.html#sortinghowto
        # We sort again, and as we do not create a new variable, the list preserves its first sorting (based on score)
        sorted(all_players_of_tournament_sorted_by_score_at_round_scale, key=lambda x: x.rank, reverse=True)

        # Verification : odd number of players
        if (len(all_players_of_tournament_sorted_by_score_at_round_scale)) % 2 == 0:
            # Pairs: variable which contains pairs of players who will play against each other
            pairs = []

            # List of players who already played against each other
            couple_of_index_player_already_played_together_list = []
            for round in self.rounds:
                matches = round.matches_tuples_representations
                for match in matches:
                    # match[0][0]= an index et not an instance anymore (old version)
                    couple_of_index_player_already_played_together = (match[0][0], match[1][0])

                    couple_of_index_player_already_played_together_list.append(
                        couple_of_index_player_already_played_together)

                    # reversed: we need to found matches X vs. Y but also Y vs. X
                    couple_of_index_player_already_played_together_reversed = (match[1][0], match[0][0])
                    couple_of_index_player_already_played_together_list.append(
                        couple_of_index_player_already_played_together_reversed)

            # Pairs creation
            for x in range(0, int(len(all_players_of_tournament_sorted_by_score_at_round_scale)/2)):
                i = 0
                j = i + 1
                adversary_has_been_found = False
                while adversary_has_been_found is False:
                    # print("Searching adversary against player at the position {0} of the list".format(i))
                    # print("Does the player at the position {0} of the list do the trick? ".format(j))
                    potential_pair = (all_players_of_tournament_sorted_by_score_at_round_scale[i].index,
                                      all_players_of_tournament_sorted_by_score_at_round_scale[j].index)

                    # Checking that the potential pair has not been already played, except if there are only two
                    # remaining players and that all other players have been assigned in pairs
                    if potential_pair not in couple_of_index_player_already_played_together_list or\
                            (len(all_players_of_tournament_sorted_by_score_at_round_scale)) == 2:
                        adversary_has_been_found is True
                        break

                    else:
                        adversary_has_been_found = False  # '==' worked ?
                        j += 1

                # We worked with index of players, now we want to get their instances to return them to the controller
                player_1_index = potential_pair[0]
                player_2_index = potential_pair[1]

                for player in all_players_of_tournament_sorted_by_score_at_round_scale:
                    if player.index == player_1_index:
                        player_1_instance = player
                    if player.index == player_2_index:
                        player_2_instance = player

                pair = (player_1_instance, player_2_instance)

                all_players_of_tournament_sorted_by_score_at_round_scale.remove(pair[0])
                all_players_of_tournament_sorted_by_score_at_round_scale.remove(pair[1])
                pairs.append(pair)

            return pairs  # returns pairs of players instances

        else:  # Even number of players
            return None

    # _____DATA BASE METHODS _____

    @classmethod
    def save_tournament_serialisation_from_python_to_json(cls):
        """Serialises python objects (tournament) at the json format and returns a list of these serialized objects"""

        all_tournaments_python = cls.TOURNAMENTS
        serialized_tournaments = []

        for tournament_instance in all_tournaments_python:

            serialised_rounds = []
            for round in tournament_instance.rounds:
                serialised_round = round.round_serialisation()
                serialised_rounds.append(serialised_round)

            serialized_tournament = {
                'name': tournament_instance.name,
                'localisation': tournament_instance.localisation,
                'date_of_beginning': tournament_instance.date_of_beginning,
                'date_of_ending': tournament_instance.date_of_ending,
                'time_controler': tournament_instance.time_controler,
                'description': tournament_instance.description,
                'number_of_rounds': tournament_instance.number_of_rounds,
                'rounds': serialised_rounds,
                'players': tournament_instance.players
            }

            serialized_tournaments.append(serialized_tournament)
        return serialized_tournaments

    @classmethod
    def write_serialized_tournament_in_tinydb_database(cls):
        """Inserts serialized tournaments at json format into player table of the tinydb database"""
        serialized_tournaments = Tournament.save_tournament_serialisation_from_python_to_json()
        tournaments_table.truncate()  # clear the table first
        tournaments_table.insert_multiple(serialized_tournaments)

    @classmethod
    def load_tournaments_from_tinydb_at_python_format(cls):
        "Loads all players from the tinydb database and convert them in python objects"

        tournament_rounds_json_dictionnary_format_list = []

        serialized_tournaments = tournaments_table.all()
        for serialized_tournament in serialized_tournaments:
            tournament_name = serialized_tournament['name']
            tournament_localisation = serialized_tournament['localisation']
            tournament_date_of_beginning = serialized_tournament['date_of_beginning']
            tournament_date_of_ending = serialized_tournament['date_of_ending']
            tournament_time_controler = serialized_tournament['time_controler']
            tournament_description = serialized_tournament['description']
            tournament_number_of_rounds = serialized_tournament['number_of_rounds']

            for round_at_json_format in serialized_tournament['rounds']:
                tournament_rounds_json_dictionnary_format_list.append(round_at_json_format)

            tournament_players = serialized_tournament['players']  # indexes of players

            tournament_instance = Tournament(tournament_name, tournament_localisation, tournament_date_of_beginning,
                                             tournament_date_of_ending, tournament_time_controler,
                                             tournament_description, tournament_number_of_rounds, rounds=None,
                                             players=tournament_players)

            Tournament.add_tournament_to_TOURNAMENTS_list(tournament_instance)

        return tournament_rounds_json_dictionnary_format_list  # for creation of rounds in the controler
