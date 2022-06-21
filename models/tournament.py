# Use of sorted() :
# https://docs.python.org/fr/3/library/functions.html#sorted
# https://docs.python.org/fr/3/howto/sorting.html#sortinghowto 

DEFAULT_VALUE_NUMBER_ROUNDS_PER_TOURNAMENT = "4"

class Tournament:
    """Represents a tournament"""

    TOURNAMENTS = [] # Class attribut, will contains the list of all tournaments 

    # def __ini__(..., player = []) --> Not correct (variable at the scale of the class) 
    # def __ini__(..., player = None) --> Correct 
    # def __ini__(..., ) --> Correct 
    def __init__(self, name, localisation, date_of_beginning, date_of_ending, time_controler, description, 
                number_of_rounds = DEFAULT_VALUE_NUMBER_ROUNDS_PER_TOURNAMENT) :
        self.name = name
        self.localisation = localisation
        self.date_of_beginning = date_of_beginning
        self.date_of_ending = date_of_ending
        self.time_controler = time_controler
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.rounds = []
        self.players = []


    @classmethod
    def add_tournament_to_TOURNAMENTS_list(cls, tournament):
        """Adds a tournament in the class attribute TOURNAMENTS"""

        cls.TOURNAMENTS.append(tournament)


    @classmethod 
    def listing_all_tournaments(cls):
        """Returns the list containing all tournaments in TOURNAMENTS"""

        return Tournament.TOURNAMENTS
        #VIEWS : print(Tournament.listing_all_tournaments())


    def tournament_players_listing_alphabectic_order(self):
        """Returns the list containing all players of a tournament, by alphabetic order"""

        all_players_of_tournament_sorted_by_family_name = \
            sorted(self.players, key=lambda x: x.family_name, reverse=False)

        return all_players_of_tournament_sorted_by_family_name
        #VIEWS : print(Tournament.tournament_players_listing_alphabectic_order())


    def tournament_players_listing_by_rank_order(self):
        """Returns the list containing all players of a tournament, by rank order"""

        all_players_of_tournament_sorted_by_rank = sorted(self.players, key=lambda x: x.rank, reverse=False)
        return all_players_of_tournament_sorted_by_rank
        #VIEWS : print(Tournament.tournament_players_listing_by_rank_order())


    def tournament_rounds_listing(self):
        """Returns the list containing all rounds of a tournament"""

        return self.rounds
        #VIEWS : print(tournamentX.tournament_rounds_listing())


    def tournament_matches_listing(self):
        """Returns the list containing all matches of a tournament"""

        matches_tuples_representation_list = []

        for round in self.rounds:
            matches_tuples_representation_list.append(round.matches_tuples_representations)

        return matches_tuples_representation_list


    def SwissAlgorithm_applied_to_the_tournament_by_rank_classification(self): 
        # Note : At the tournament scale, because it is applied to player of a tournament.
        """Returns pairs of players of a tournament; for matches of a round, based on their classification (rank)"""

        # 1. Au début du premier tour, triez tous les joueurs en fonction de leur classement
        all_players_of_tournament_sorted_by_ranks = sorted(self.players, key=lambda x: x.rank, reverse=False)

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

        else:
            print("Even number of players")

        return pairs

        #3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points  : 
        # nombre de points est relatif au joueur au sein du tournois). Si plusieurs joueurs ont le même nombre de 
        # points, triez-les en fonction de leur rang.
        #--> nouvelle fonction


    def SwissAlgorithm_applied_to_the_tournament_by_score_classification(self): 
        """Returns pairs of players of a tournament for matches of a round, based on their number of points"""

        #Pour chaque joueur, on cherche la somme de ces points accumulés pendant le round :
        # Etapes : 
        # 1. Pour chaque joueur du tournois, parcourir tous les rounds du tournois et tous les matchs de chaque round; 
        # 2. Chercher les points acquis par le joueur et  en faire la somme ; 
        # 3. Etablir une nouvelle liste et la trier

        #Etapes 1 et 2
        for player in self.players:
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
        all_players_of_tournament_sorted_by_score_at_round_scale = sorted(self.players, key=lambda x: \
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

        else:
            print("Even number of players")

        return pairs
