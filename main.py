"""
MODELS
Étape 2 : Définir (et coder) les modèles pour ce projet
Modèle : Le modèle contient les informations relatives à l’état du système. Ce sont les fonctionnalités brutes de 
l’application.
A partir du Use Case: identification des principaux éléments
Note : ne devrait pas contenir la «logique» du jeu

-Commencer par les modèles : avec quelles entités votre programme va-t-il fonctionner ? 
-Doivent-elles contenir des données (= attributs) ? 
-Appliquent-elles des comportements spécifiques (= méthodes) ?
"""

# Use of sorted() :
# https://docs.python.org/fr/3/library/functions.html#sorted
# https://docs.python.org/fr/3/howto/sorting.html#sortinghowto 



class Tournament:
    """Represents a tournament"""

    TOURNAMENTS = [] # Class attribut, will contains the list of all tournaments 

    # def __ini__(..., player = []) --> Not correct (variable at the scale of the class) 
    # def __ini__(..., player = None) --> Correct 
    # def __ini__(..., ) --> Correct 
    def __init__(self, name, localisation, date_of_beginning, date_of_ending, time_controler, description, 
                number_of_rounds = "4") :
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

        # A FAIRE il faut aller chercher tous les matches d'un round, à faire une fois que j'ai fini la classe Round
        # essayer return self.rounds.matches ou alors, for round in self.rounds ... avec un apped sur une liste qui sera
        # le return de la fontion
        pass


    def SwissAlgorithm_applied_to_the_tournament_by_rank_classification(self): 
        # Note : At the tournament scale, because it is applied to player of a tournament.
        """Returns pairs of players of a tournament; for matches of a round, based on their classification (rank)"""

        # 1. Au début du premier tour, triez tous les joueurs en fonction de leur classement
        all_players_of_tournament_sorted_by_ranks = sorted(self.players, key=lambda x: x.rank, reverse=False)
        #TEST_OK: for player in players_sorted_by_ranks:
        #TEST_OK:    print(player.rank)

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
            #TEST_OK print("Pairs, established from rank of players " + str(pairs))

        else:
            print("Even number of players")

        return pairs

        #3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points  : 
        # nombre de points est relatif au joueur au sein du tournois). # Si plusieurs joueurs ont le même nombre de 
        # points, triez-les en fonction de leur rang.
        #--> nouvelle fonction


    def SwissAlgorithm_applied_to_the_tournament_by_score_classification(self): 
        """Returns pairs of players of a tournament for matches of a round, based on their number of points"""

        print()
        print("=================== SWISS ALGORITHM : BY SCORE ===================")

        #Pour chaque joueur, on cherche la somme de ces points accumulés pendant le round :
        # Etapes : 
        # 1. Pour chaque joueur du tournois, parcourir tous les rounds du tournois et tous les matchs de chaque round; 
        # 2. Chercher les points acquis par le joueur et  en faire la somme ; 
        # 3. Etablir une nouvelle liste et la trier

        #Etapes 1 et 2
        for player in self.players:
            #Reinitialisation of the player score at the round scale
            player.player_score_at_round_scale = 0
            #TESTOK: print("Recherche des points du joueur", player)

            #On parcourt tous les rounds qui ont eu lieu
            for round in self.rounds:
                #TESTOK: print("Recherche des points dans le round", round.name)

                #On parcourt tous les matches du round
                for match in round.matches_tuples_representations: 
                    #TESTOK: print("Recherche des points dans les tous les matchs du round", match)
                    #TESTOK : print("match: ", match) #sous la forme ([instanceJoueurA, scoreJoueurA],[instanceJoueurB, 
                    # scoreJoueurB])

                    for player_and_its_score in match:
                        #TESTOK: print("player_and_its_score", player_and_its_score) # sous la forme [instanceJoueurA, 
                        # scoreJoueurA]

                        #Si le joueur est bien celui qui nous interesse dans la boucle actuelle
                        if player == player_and_its_score[0]:
                            print(player_and_its_score[0].family_name, "got the score", player_and_its_score[1], \
                                "during the match", match)

                            player.player_score_at_round_scale += player_and_its_score[1]
                            #TESTOK: print(player.player_score_at_round_scale)

        #Etape 3
        all_players_of_tournament_sorted_by_score_at_round_scale = sorted(self.players, key=lambda x: \
            x.player_score_at_round_scale, reverse=True) #Ordre decroissant pour avoir le meilleur score en premier


        # ce qu'il manque ici : le fait de trier les joueurs en fonction de leur rank, si ils ont le meme score
        # https://docs.python.org/fr/3/howto/sorting.html#sortinghowto
        # [...] Cette propriété fantastique vous permet de construire des tris complexes dans des tris en plusieurs étapes. 
        # Par exemple, afin de sortir les données des étudiants en ordre descendant par grade puis en ordre ascendant 
        # par age, effectuez un tri par age en premier puis un second tri par grade : [...]

        # On re-trie avec le rank; mais comme on n'assigne pas une nouvelle variable, la liste conserve le premier tri, 
        # fait avec le score
        sorted(all_players_of_tournament_sorted_by_score_at_round_scale, key=lambda x: x.rank, reverse=True)
        #Ne marche pas si on attribue une nouvelle variable
        # all_players_of_tournament_sorted_by_score_and_rank_at_round_scale = sorted(all_players_of_tournament_sorted_by_score_at_round_scale, key=lambda x: x.rank, reverse=True)

        #TESTOK: 
        for playerr in all_players_of_tournament_sorted_by_score_at_round_scale:
            print("test 20220617", playerr.player_score_at_round_scale, playerr.rank)


        print("list of players from the higher number of points to the lower one: ", \
            all_players_of_tournament_sorted_by_score_at_round_scale)
        #TEST_OK: for playerr in all_players_of_tournament_sorted_by_score_at_round_scale:
            #print(playerr.player_score_at_round_scale)

        # Verification qu'on a un nombre impair de joueurs
        if (len(all_players_of_tournament_sorted_by_score_at_round_scale)) % 2 == 0 : 
            # Pairs: variable dans laquelle on va stocker les paires de joueurs qui vont s'affronter
            pairs = []
            
            # On parcourt la liste de deux en deux : index 0 associé à 1, 2 associé à 3 et ainsi de suite




            # Création des paires
            for x in range(0,int(len(all_players_of_tournament_sorted_by_score_at_round_scale)/2)):
                print("x", x)
                i = 0
                j = i + 1
                adversary_has_been_found = False
                while adversary_has_been_found == False :
                    print("recherche d'adversaire contre le joueur à la position {0} de la liste".format(i))
                    print("est ce que le joueur à la position {0} de la liste fera l'affaire ? ".format(j))
                    #paire potentielle
                    pair = (all_players_of_tournament_sorted_by_score_at_round_scale[i], \
                        all_players_of_tournament_sorted_by_score_at_round_scale[j])

                    #Vérification si les deux joueurs ont déja joué l'un contre l'autre
                    for round in self.rounds:
                        matches = round.matches_tuples_representations
                        for match in matches:
                            couple_of_player_already_played_together = (match[0][0], match[1][0])
                            #TESTOK: print(couple_of_player_already_played_together)

                            if pair == couple_of_player_already_played_together:
                                print("ALREADY PLAYED:", couple_of_player_already_played_together[0].family_name, couple_of_player_already_played_together[1].family_name)
                                adversary_has_been_found == False
                                j+=1

                                # Signalement avec print : OK
                                # Pour modifier l'algorithme, en revanche...
                                # récursivité en créant une fonction dédiée ?
                                # Note : 4 rounds, 8 joueurs; donc un joueur n'aura pas joué contre tous les autres joueurs.
                                # il faut arriver à sortir les joueurs de la liste une fois qu'ils sont dans une paire : méthode pop(); non car on est sur une paire potentielle, pas avérée
                                # utiliser une valeur j initialement = à i+1; et qui += à chaque fin de boucle (une nouvelle boucle créée à l'échelle  j)

                            else :
                                print("-->les joueurs ne se sont pas afrontés, la paire va etre créée ")
                                print()
                                adversary_has_been_found == True
                                #on sort les joueurs de la liste pour ne pas qu'ils soient assignés à deux matches
                                break
                                #REPRENDRE ICI : le probleme c'est que la liste a été vidée; pourtant je pensais que ça allait avec le adversary_has_been_found == True et le break
                                #explication : il le fait pour chaque round et chaque match
                                #il faut donc mettre la boucle while dans la boucle for round et for math ?
                                #il faut donc faire attention à l'indentation 
                    all_players_of_tournament_sorted_by_score_at_round_scale.remove(pair[0])
                    all_players_of_tournament_sorted_by_score_at_round_scale.remove(pair[1])
                    print(all_players_of_tournament_sorted_by_score_at_round_scale)
                    #Toujours pas...

                """SAUVEGARDE DU CODE FONCTIONNELLE AVANT DE METTRE LA BOUCLE J
                            # Création des paires
                            for i in range(0,len(all_players_of_tournament_sorted_by_score_at_round_scale), 2):
                                print("recherche d'adversaire contre le joueur à la position {0} de la liste".format(i))
                                #paire potentielle
                                pair = (all_players_of_tournament_sorted_by_score_at_round_scale[i], \
                                    all_players_of_tournament_sorted_by_score_at_round_scale[i+1])

                                #Vérification si les deux joueurs ont déja joué l'un contre l'autre
                                for round in self.rounds:
                                    matches = round.matches_tuples_representations
                                    for match in matches:
                                        couple_of_player_already_played_together = (match[0][0], match[1][0])
                                        print(couple_of_player_already_played_together)

                                        if pair == couple_of_player_already_played_together:
                                            print("ALREADY PLAYED:", couple_of_player_already_played_together[0].family_name, couple_of_player_already_played_together[1].family_name)

                                            # Signalement avec print : OK
                                            # Pour modifier l'algorithme, en revanche...
                                            # récursivité en créant une fonction dédiée ?
                                            # Note : 4 rounds, 8 joueurs; donc un joueur n'aura pas joué contre tous les autres joueurs.
                                            # il faut arriver à sortir les joueurs de la liste une fois qu'ils sont dans une paire : méthode pop()
                                            # utiliser une valeur j initialement = à i+1; et qui += à chaque fin de boucle (une nouvelle boucle créée à l'échelle  j)
                """

                pairs.append(pair)

        else:
            print("Even number of players")

        #TESTOK:
        #for pair in pairs:
        #    print("Chaque joueur et son score cumulé a l'echelle du round")
        #    print(pair[0].family_name," ", pair[0].player_score_at_round_scale)
        #    print(pair[1].family_name," ", pair[1].player_score_at_round_scale)

        return pairs


class Rounds:
    """Represents a round"""

    def __init__(self, name, date_and_time_beginning, date_and_time_ending) : 
        self.name = name
        self.date_and_time_beginning = date_and_time_beginning
        self.date_and_time_ending = date_and_time_ending
        self.matches_tuples_representations = []



class Matches:
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


class Players:
    """Represents a player"""

    PLAYERS = [] # Class attribut, will contains the list of all players


    def __init__(self, family_name, first_name, birth_date, gender, rank) :
        self.family_name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.player_score_at_round_scale = 0


    @classmethod
    def add_player_to_PLAYERS_list(cls, player):
        """Adds a player in the class attribute PLAYER"""
        
        cls.PLAYERS.append(player)


    @classmethod
    def listing_all_players(cls):
        pass
        """Returns the list containing all players in PLAYERS"""
        
        return Players.PLAYERS
        #VIEWS : print(Players.listing_all_players())


    def update_player_rank(self, updated_rank):
        self.rank = updated_rank
        # à utiliser de la maniere player27.update_player_rank(123456) --> le rank du joueur devient 123456
        # question : impact du rank des joueurs avant/apres, en fonction de si le rank est < ou > au updated rank
        pass



def mainTestingModel():

    #creation 8 joueurs
    player1 = Players("family_name_1", "first_name_1", "birth_date_1", "gender_1", "rank_1")
    player2 = Players("family_name_2", "first_name_2", "birth_date_2", "gender_2", "rank_2")
    player3 = Players("family_name_3", "first_name_3", "birth_date_3", "gender_3", "rank_3")
    player4 = Players("family_name_4", "first_name_4", "birth_date_4", "gender_4", "rank_4")
    player5 = Players("family_name_5", "first_name_5", "birth_date_5", "gender_5", "rank_5")
    player6 = Players("family_name_6", "first_name_6", "birth_date_6", "gender_6", "rank_6")
    player7 = Players("family_name_7", "first_name_7", "birth_date_7", "gender_7", "rank_7")
    player8 = Players("family_name_8", "first_name_8", "birth_date_8", "gender_8", "rank_8")

    #Ajout de chaque joueur créé (instances de classe) à l'attribut de classe PLAYERS qui est la liste contenant tous 
    # les joueurs
    Players.add_player_to_PLAYERS_list(player1)
    Players.add_player_to_PLAYERS_list(player2)
    Players.add_player_to_PLAYERS_list(player3)
    Players.add_player_to_PLAYERS_list(player4)
    Players.add_player_to_PLAYERS_list(player5)
    Players.add_player_to_PLAYERS_list(player6)
    Players.add_player_to_PLAYERS_list(player7)
    Players.add_player_to_PLAYERS_list(player8)


    #print de la liste de tous les joueurs
    print()
    print("Liste de tous les joueurs", Players.PLAYERS)
    #print du family name du 1er joueur dans la liste de tous les joueurs
    #print("Nom de famille du premier joueur de la liste" + Players.PLAYERS[0].family_name)
    #print("Nom de famille du deuxieme joueur de la liste" + Players.PLAYERS[1].family_name)


    #Creation d'un tournoi
    tournament1 = Tournament("LeTournoirDesTroisSorciers", "Toulouse", "début", "fin", "blitz", "description blabla")
    #Ajout du tournoi à la liste des tournois
    Tournament.add_tournament_to_TOURNAMENTS_list(tournament1)
    #Print de la liste des tournois
    print()
    print("Liste des tournois", Tournament.listing_all_tournaments())

    #ajouter 8 joueurs au tournois:
    tournament1.players.append(player1)
    tournament1.players.append(player2)
    tournament1.players.append(player3)
    tournament1.players.append(player4)
    tournament1.players.append(player5)
    tournament1.players.append(player6)
    tournament1.players.append(player7)
    tournament1.players.append(player8)

    print()
    print("Liste des joueurs du tournois tournament 1", tournament1.players)

    #Creation d'un tour
    round1 = Rounds("round_1", "date_begin_round_1","date_ending_round_1")

    #Ajouter les joueurs: les consignes disent d'ajouter les joueurs à un tournoi, puis les round sont créés
    #'l'ordinateur génère des paires de joueurs pour les matches du premier tour"
    #les joueurs du tour sont donc... les joueurs du tournois 

    #ajout du round au tournois
    tournament1.rounds.append(round1)

    #Generation des paires
    #TESTOK: print("Swiss algorithm returns :", tournament1.SwissAlgorithm_applied_to_the_tournament_by_rank_classification())
    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_rank_classification()
    for pair in pairs:
        print()
        print("Pair générée pour le prochain match, composée de deux instances de joueurs, ayant comme family_name: \
            {0} et {1} ".format(pair[0].family_name, pair[1].family_name))

    #création d'un match
        match_x_of_round1 = Matches(pair[0],pair[1]) 
        print("LE MATCH SE DEROULE")

        #Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match avant de générer 
        # les paires suivantes
        print("Dear tournament manager, please enter the scores of the match")
        match_x_of_round1.player_1_score += int(input("score joueur 1 ({0}): ".format(pair[0].family_name)))
        match_x_of_round1.player_2_score += int(input("score joueur 2 ({0}): ".format(pair[1].family_name)))
        #TESTOK: match_x_of_round1.match_tuple_representation()

        #chaque match est ajouté à round1.match_tuple_representations qui est une liste
        round1.matches_tuples_representations.append(match_x_of_round1.match_tuple_representation())


    #3.Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le
    # même nombre de points, triez-les en fonction de leur rang.
    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_score_classification()

    round2 = Rounds("round_2", "date_begin_round_2","date_ending_round_2")

    tournament1.rounds.append(round2)

    for pair in pairs:
        print()
        print("Pair générée pour le prochain match, composée de deux instances de joueurs, ayant comme family_name: \
            {0} et {1} ".format(pair[0].family_name, pair[1].family_name))

    #création d'un match
        match_x_of_round2 = Matches(pair[0],pair[1]) 
        print("LE MATCH SE DEROULE")

        #Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match avant de générer les paires suivantes
        #on rentre les scores
        print("Dear tournament manager, please enter the scores of the match")
        match_x_of_round2.player_1_score += int(input("score joueur 1 ({0}): ".format(pair[0].family_name)))
        match_x_of_round2.player_2_score += int(input("score joueur 2 ({0}): ".format(pair[1].family_name)))
        #match_x_of_round1.match_tuple_representation()

    #chaque match est ajouté à round1.match_tuple_representations qui est une liste
        round2.matches_tuples_representations.append(match_x_of_round2.match_tuple_representation())
        print(round2.matches_tuples_representations)


#Pour le 3eme tour: 
    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_score_classification()



mainTestingModel()