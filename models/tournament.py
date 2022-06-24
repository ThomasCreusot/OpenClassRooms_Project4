# Use of sorted() :
# https://docs.python.org/fr/3/library/functions.html#sorted
# https://docs.python.org/fr/3/howto/sorting.html#sortinghowto 


from tinydb import TinyDB
import json


DEFAULT_VALUE_NUMBER_ROUNDS_PER_TOURNAMENT = "4"


database = TinyDB('db.json') 
tournaments_table = database.table('tournaments')


class Tournament:
    """Represents a tournament"""

    # Class attribute, will contains the list of all tournaments
    TOURNAMENTS = []  

    # def __init__(..., player = []) --> Not correct (variable at the scale of the class) 
    # def __init__(..., player = None) --> Correct 
    # def __init__(..., ) --> Correct 
    def __init__(self, name, localisation, date_of_beginning, date_of_ending, time_controler, description, 
                number_of_rounds = DEFAULT_VALUE_NUMBER_ROUNDS_PER_TOURNAMENT, rounds = None, players = None) : #rounds = None, players = None 24062022
        self.name = name
        self.localisation = localisation
        self.date_of_beginning = date_of_beginning
        self.date_of_ending = date_of_ending
        self.time_controler = time_controler
        self.description = description
        self.number_of_rounds = number_of_rounds
        if rounds == None:
            self.rounds = []
        else:
            self.rounds = rounds 
        if players == None:
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

    # Note : At the tournament scale, because it is applied to player of a tournament.
    def SwissAlgorithm_applied_to_the_tournament_by_rank_classification(self, tournament_players): 
        """Returns pairs of players of a tournament; for matches of a round, based on their classification (rank)"""

        # 1. Au début du premier tour, triez tous les joueurs en fonction de leur classement
        all_players_of_tournament_sorted_by_ranks = sorted(tournament_players, key=lambda x: x.rank, reverse=False)

        # Verification qu'on a un nombre impair de joueurs
        if (len(all_players_of_tournament_sorted_by_ranks)) % 2 == 0 : 

            # 2. Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
            #Note : Use int() and not "round" because there is not an even number of players
            higher_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[\
                0:int(len(all_players_of_tournament_sorted_by_ranks)/2)] # 0:4 --> 0,1,2,3
            lower_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[\
                int(len(all_players_of_tournament_sorted_by_ranks)/2):\
                    int(len(all_players_of_tournament_sorted_by_ranks))] # 4:8 --> 4,5,6,7

            # 2(suite) : Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié 
            # inférieure, et ainsi de suite. 
            # Pairs: variable dans laquelle on va stocker les paires de joueurs qui vont s'affronter
            pairs = []
            for i in range(0,(len(higher_half_of_players_sorted_by_ranks))):
                pair = (higher_half_of_players_sorted_by_ranks[i], lower_half_of_players_sorted_by_ranks[i])
                pairs.append(pair)
            return pairs

        else: #Even number of players
            return None 

        #3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points  : 
        # nombre de points est relatif au joueur au sein du tournois). Si plusieurs joueurs ont le même nombre de 
        # points, triez-les en fonction de leur rang.
        #--> nouvelle fonction


    def SwissAlgorithm_applied_to_the_tournament_by_score_classification(self, tournament_players): 
        """Returns pairs of players of a tournament for matches of a round, based on their number of points"""

        #Pour chaque joueur, on cherche la somme de ces points accumulés pendant le round :
        # Etapes : 
        # 1. Pour chaque joueur du tournois, parcourir tous les rounds du tournois et tous les matchs de chaque round; 
        # 2. Chercher les points acquis par le joueur et  en faire la somme ; 
        # 3. Etablir une nouvelle liste et la trier

        #Etapes 1 et 2
        for player in tournament_players:
            #Reinitialisation of the player score at the round scale
            player.player_score_at_round_scale = 0

            #On parcourt tous les rounds qui ont eu lieu
            for round in self.rounds:
                #On parcourt tous les matches du round
                for match in round.matches_tuples_representations: 
                    for player_and_its_score in match:
                        #Si le joueur est bien celui qui nous interesse dans la boucle actuelle
                        if player == player_and_its_score[0]:
                            #print(player_and_its_score[0].family_name, "got the score", player_and_its_score[1], \
                            #    "during the match", match)

                            player.player_score_at_round_scale += player_and_its_score[1]

        #Etape 3
        all_players_of_tournament_sorted_by_score_at_round_scale = sorted(tournament_players, key=lambda x: \
            x.player_score_at_round_scale, reverse=True) #Ordre decroissant pour avoir le meilleur score en premier

        # https://docs.python.org/fr/3/howto/sorting.html#sortinghowto
        # On re-trie avec le rank; mais comme on n'assigne pas une nouvelle variable, la liste conserve le premier tri, 
        # fait avec le score
        sorted(all_players_of_tournament_sorted_by_score_at_round_scale, key=lambda x: x.rank, reverse=True)

        # Verification qu'on a un nombre impair de joueurs
        if (len(all_players_of_tournament_sorted_by_score_at_round_scale)) % 2 == 0 : 
            # Pairs: variable dans laquelle on va stocker les paires de joueurs qui vont s'affronter
            pairs = []
            
            # Liste des joueurs déja affrontés déja joués
            couple_of_player_already_played_together_list = []
            for round in self.rounds:
                matches = round.matches_tuples_representations
                for match in matches:
                    couple_of_player_already_played_together = (match[0][0], match[1][0])
                    couple_of_player_already_played_together_list.append(couple_of_player_already_played_together)
                    #reversed: we need to found matches x-y or y-x
                    couple_of_player_already_played_together_reversed = (match[1][0], match[0][0])
                    couple_of_player_already_played_together_list.append(couple_of_player_already_played_together_reversed)                    

            # Création des paires
            for x in range(0,int(len(all_players_of_tournament_sorted_by_score_at_round_scale)/2)):
                i = 0
                j = i + 1
                adversary_has_been_found = False
                while adversary_has_been_found == False :
                    #print("recherche d'adversaire contre le joueur à la position {0} de la liste".format(i))
                    #print("est ce que le joueur à la position {0} de la liste fera l'affaire ? ".format(j))
                    # Paire potentielle
                    potential_pair = (all_players_of_tournament_sorted_by_score_at_round_scale[i], \
                        all_players_of_tournament_sorted_by_score_at_round_scale[j])

                    #On vérifie que la paire potentielle n'a pas été jouée, sauf s'il ne reste plus que deux joueurs et que les autres ont été assignés à des paires
                    if not potential_pair in couple_of_player_already_played_together_list or (len(all_players_of_tournament_sorted_by_score_at_round_scale)) == 2 :
                        adversary_has_been_found == True
                        break

                    else :
                        adversary_has_been_found == False
                        j+=1

                pair = potential_pair
                all_players_of_tournament_sorted_by_score_at_round_scale.remove(pair[0])
                all_players_of_tournament_sorted_by_score_at_round_scale.remove(pair[1])
                pairs.append(pair)

            return pairs

        else: #Even number of players
            return None


    #_____DATA BASE METHODS _____

    @classmethod
    def save_tournament_serialisation_from_python_to_json(cls):
        """Serialises python objects (tournament) at the json format and returns a list of these serialized objects"""

        all_tournaments_python = cls.TOURNAMENTS
        serialized_tournaments = []

        #Question: ne peut on pas automatiser avec quelque chose de la forme
        # ' for attr_name, attr_value in player_instance.items() '
        # peut etre pas 'items' car ce n'est pas un tableau mais une instance
        for tournament_instance in all_tournaments_python:
            serialized_tournament = {
                'name' : tournament_instance.name, 
                'localisation' : tournament_instance.localisation, 
                'date_of_beginning' : tournament_instance.date_of_beginning, 
                'date_of_ending' : tournament_instance.date_of_ending, 
                'time_controler' : tournament_instance.time_controler, 
                'description' : tournament_instance.description,
                'number_of_rounds' : tournament_instance.number_of_rounds,
                #'rounds' : tournament_instance.rounds,
                'players' : tournament_instance.players
            }

            serialized_tournaments.append(serialized_tournament)
        return serialized_tournaments

    @classmethod
    def write_serialized_tournament_in_tinydb_database(cls):
        """Inserts serialized tournaments at json format into player table of the tinydb database"""
        serialized_tournaments = Tournament.save_tournament_serialisation_from_python_to_json()
        tournaments_table.truncate() #clear the table first
        tournaments_table.insert_multiple(serialized_tournaments)


    @classmethod
    def load_tournaments_from_tinydb_at_python_format(cls):
        "Load all players from the tinydb database and convert them in python objects"

        serialized_tournaments = tournaments_table.all() 
        for serialized_tournament in serialized_tournaments:
            tournament_name = serialized_tournament['name']
            tournament_localisation = serialized_tournament['localisation']
            tournament_date_of_beginning = serialized_tournament['date_of_beginning']
            tournament_date_of_ending = serialized_tournament['date_of_ending']
            tournament_time_controler = serialized_tournament['time_controler']
            tournament_description = serialized_tournament['description']
            tournament_number_of_rounds = serialized_tournament['number_of_rounds']

            tournament_rounds = serialized_tournament['rounds']
            tournament_players = serialized_tournament['players']

            tournament_instance = Tournament(tournament_name, tournament_localisation, tournament_date_of_beginning, tournament_date_of_ending, tournament_time_controler, tournament_description, tournament_number_of_rounds, tournament_rounds, tournament_players)
            Tournament.add_tournament_to_TOURNAMENTS_list(tournament_instance)
