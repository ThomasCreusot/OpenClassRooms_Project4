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


class Tournament:
    """Represents a tournament"""

    TOURNAMENTS = [] # Attribut de classe qui contiendra la liste de tous les tournois

    # Possibilité de renseigner les joueurs lors de la création du tournois de la manière suivante : 
    # tournois1 = Tournament(..., players = ["joueur1, joueur2, ..."]) ; on pourra également utiliser 
    # tournois.players.append(joueur1)
    def __init__(self, name, localisation, date_of_beginning, date_of_ending, time_controler, description, 
                number_of_rounds = "4", players=[]) : # renseigner players de la manière suivante : tournois=Tournament(...., players = ["joueur1, joueur2, ..."])
        self.name = name
        self.localisation = localisation
        self.date_of_beginning = date_of_beginning
        self.date_of_ending = date_of_ending
        self.time_controler = time_controler
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.rounds = []
        self.players = players


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

        all_players_of_tournament_sorted_by_family_name = sorted(self.players, key=lambda x: x.family_name, reverse=False)
        return all_players_of_tournament_sorted_by_family_name
        #VIEWS : print(Tournament.tournament_players_listing_alphabectic_order())


    def tournament_players_listing_by_ronk_order(self):
        """Returns the list containing all players of a tournament, by rank order"""

        all_players_of_tournament_sorted_by_rank = sorted(self.players, key=lambda x: x.rank, reverse=False)
        return all_players_of_tournament_sorted_by_rank
        #VIEWS : print(Tournament.tournament_players_listing_by_ronk_order())


    def tournament_rounds_listing(self):
        """Returns the list containing all rounds of a tournament"""
        
        return self.rounds
        #VIEWS : print(tournamentX.tournament_rounds_listing())


    def tournament_matches_listing(self):
        """Returns the list containing all matches of a tournament"""

        #il faut aller chercher tous les matches d'un round, à faire une fois que j'ai fini la classe Round
        # essayer return self.rounds.matches
        pass


    def SwissAlgorithm_applied_to_the_tournament_by_rank_classification(self): #serait interessant de definir cette méthode à l'echelle du round, les deux sont possibles, jepars sur l'echelle tournament
        """Returns pairs of players of a tournament; for matches of a round, based on their classification (rank)"""

        # 1. Au début du premier tour, triez tous les joueurs en fonction de leur classement
        #https://docs.python.org/fr/3/library/functions.html#sorted
        #https://docs.python.org/fr/3/howto/sorting.html#sortinghowto 
        all_players_of_tournament_sorted_by_ranks = sorted(self.players, key=lambda x: x.rank, reverse=False)
        #TEST_OK for player in players_sorted_by_ranks:
        #TEST_OK    print(player.rank)

        # 2. Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
        #Note : j'utilise int() et pas "round" car on devrait avoir un nombre pair de joueurs
        higher_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[0:int(len(all_players_of_tournament_sorted_by_ranks)/2)] #0:4 --> 0,1,2,3
        lower_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[int(len(all_players_of_tournament_sorted_by_ranks)/2):int(len(all_players_of_tournament_sorted_by_ranks))] #4:8 --> 4,5,6,7


        # 2(suite) : Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié 
        # inférieure, et ainsi de suite. 
        
        #verification qu'on a deux listes de meme longueur
        if (len(higher_half_of_players_sorted_by_ranks)) == (len(lower_half_of_players_sorted_by_ranks)): 
            #Pairs: variable dans laquelle on va stocker les paires de joueurs qui vont s'affronter
            pairs = []
            for x in range(0,(len(higher_half_of_players_sorted_by_ranks))):
                pair = (higher_half_of_players_sorted_by_ranks[x], lower_half_of_players_sorted_by_ranks[x])
                pairs.append(pair)
            #TEST_OK print("Pairs, established from rank of players " + str(pairs))

        else:
            print("Even number of players")

        return pairs

        #3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points (perso:classement/rang 
        # semble independent du tournois alors que nombre de points est relatif au joueur au sein du tournois). Si 
        # plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        #--> nouvelle fonction


    def SwissAlgorithm_applied_to_the_tournament_by_score_classification(self): 
        """Returns pairs of players of a tournament for matches of a round, based on their number of points"""

        #Pour chaque joueur, on cherche la somme de ces points:
        #Etapes: pour chaque joueur du tournois, parcourir tous les rounds du tournois et tous les matchs de chaque round; chercher les points acquis par le joueur (somme), établir une nouvelle liste et la trier
        for player in self.players:

            #Reinitialisation of the player score at the round scale
            player.player_score_at_round_scale = 0

            print()
            print("Recherche des points du joueur", player)
            
            #On parcourt donc tous les rounds qui ont eu lieu
            for round in self.rounds:
                print()
                print()
                print("Recherche des points dans le round", round.name)

                print("re")
                for match in round.matches_tuples_representations: #pb à resoudre ici : il sort tous les matchs de tous les rounds alors qu'on veut juste les matchs du round en question
                    print("Recherche des points dans les tous les matchs du round", match)
                    
                    #print("match: ", match) #sous la forme ([instanceJoueurA, scoreJoueurA],[instanceJoueurB, scoreJoueurB])
                    for player_and_its_score in match:
                        #print("player_and_its_score", player_and_its_score) # sous la forme [instanceJoueurA, scoreJoueurA]
                        if player == player_and_its_score[0]:
                            print(player_and_its_score[0].family_name, "got the score", player_and_its_score[1], "during the match", match)
                            player.player_score_at_round_scale += player_and_its_score[1]
                            print(player.player_score_at_round_scale)
        all_players_of_tournament_sorted_by_score_at_round_scale = sorted(self.players, key=lambda x: x.player_score_at_round_scale, reverse=True) #Ordre decroissant pour avoir le meilleur score en premier
        print("list of players from the higher number of points to the lower one: ", all_players_of_tournament_sorted_by_score_at_round_scale)
        #TEST_OK for playerr in all_players_of_tournament_sorted_by_score_at_round_scale:
            #print(playerr.player_score_at_round_scale)

        #verification qu'on a un nombre impair de joueurs
        if (len(all_players_of_tournament_sorted_by_score_at_round_scale)) % 2 == 0 : 
            #Pairs: variable dans laquelle on va stocker les paires de joueurs qui vont s'affronter
            pairs = []
            
            #on parcourt la liste de 2 en deux : index 0 associé à 1, 2 associé à 3 et ainsi de suite
            for x in range(0,len(all_players_of_tournament_sorted_by_score_at_round_scale), 2):
                pair = (all_players_of_tournament_sorted_by_score_at_round_scale[x], all_players_of_tournament_sorted_by_score_at_round_scale[x+1])
                pairs.append(pair)

        else:
            print("Even number of players")

        #TEST-OK
        for pair in pairs:
            print()
            print("Chaque joueur et son score cumulé a l'echelle du round")
            print(pair[0].family_name," ", pair[0].player_score_at_round_scale)
            print(pair[1].family_name," ", pair[1].player_score_at_round_scale)

        return pairs






""" PREMIRE TENTATIVE
    def SwissAlgorithm_applied_to_the_tournament_by_score_classification(self, previous_matches_tuple_representation): #A REFAIRE, les points sont à l'echelle du match mais le total des points est à l'echelle du TOUR
        #Returns pairs of players of a tournament for matches of a round, based on their number of points
        #print(previous_matches_tuple_representation)
        #j'ai des tuples (4 maximum, si j'ai 8 joueurs)
        #chaque tuple contient une liste : un joueur et son score, c'est ça qui m'interesse : les récupérer et les mettre dans une meme liste: ma liste de joueurs avec leur score pour le prochain round
        
        list_of_players_and_their_score_for_the_next_round = []

        for previous_match_tuple_representation in previous_matches_tuple_representation:
            #print("_________")
            #print(previous_match_tuple_representation)
            for player_and_its_score in previous_match_tuple_representation:
                list_of_players_and_their_score_for_the_next_round.append(player_and_its_score) #print(list_of_players_and_their_score_for_the_next_round) : ok

        #Reverse : Plus un joueur a un score élevé, meilleur il est, donc classification reverse        
        list_of_players_and_their_score_for_the_next_round_classified_by_point = sorted(list_of_players_and_their_score_for_the_next_round, key=lambda x: x[1], reverse=True) #x[1] : le score; x[0] : l'instance du joueur
        print(list_of_players_and_their_score_for_the_next_round_classified_by_point) #résultat ok

        #Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        for i in range(len(list_of_players_and_their_score_for_the_next_round_classified_by_point)-1):
            if list_of_players_and_their_score_for_the_next_round_classified_by_point[i][1] == list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1][1]: #[i][1]: le score (champ[1]) du joueur à l'index i [i]
                print("deux joueurs ont le même score") #REPRENDRE ICI : il faut trier list_of_players_and_their_score_for_the_next_round_classified_by_point[i][1] et list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1][1] selon leur rank (déja fait dans une autre méthode, la difficulté sera de ne pas toucher au reste de la liste je pense)
                if list_of_players_and_their_score_for_the_next_round_classified_by_point[i][0].rank > list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1][0].rank: #comparaison du rank des instances (instance = [0])
                    #je pars du principe qu'un rank plus élevé mathématiquement représente un niveau moins bon; donc si le rank du premier joueur [i] est plus grand, il doit etre placé après l'autre joueur [i+1]
                    list_of_players_and_their_score_for_the_next_round_classified_by_point[i], list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1]=list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1], list_of_players_and_their_score_for_the_next_round_classified_by_point[i]
                elif list_of_players_and_their_score_for_the_next_round_classified_by_point[i][0].rank < list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1][0].rank:
                    pass #les joueurs sont dans le bon ordre
                else:
                    print("problem, two players have the same rank (and the same score)")

        print()
        print("list_of_players_and_their_score_for_the_next_round_classified_by_point" +str (list_of_players_and_their_score_for_the_next_round_classified_by_point)) 


        #4.	Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. 

        if (len(list_of_players_and_their_score_for_the_next_round_classified_by_point))%2 == 0 : #verification qu'on a un nombre pair de joueurs
            #Pairs: variable dans laquelle on va stocker les paires
            pairs = []
            #On parcours la liste avec un 'step' de 2, et on associe une instance de la liste à l'instance suivante donc 0et1, 2et3, 4et5 
            for x in range(0,int(len(list_of_players_and_their_score_for_the_next_round_classified_by_point)), 2):
                print(x)
                pair = [list_of_players_and_their_score_for_the_next_round_classified_by_point[x][0], list_of_players_and_their_score_for_the_next_round_classified_by_point[x+1][0]] #[0] : instance de joueur, si on ne le met pas, ca prend l'instance et le score du round precedent
                pairs.append(pair)
            #print("pairs, established from rank of players " + str(pairs))

        else:
            print("Even number of players")

        return pairs

        # Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        #A FAIRE : pour associer j1 et J2, et ainsi de suite, ok, mais reflexion en cours sur : comment éviter de renouveler un match déja fait ^^
        #parmi les matchs existants --> for match in round (il le faudra en argument de la méthode)
        #si list_of_players_and_their_score_for_the_next_round_classified_by_point[0][0] (instance de joueur = le joueur1 dans la présente classification) ; list_of_players_and_their_score_for_the_next_round_classified_by_point[1][0]

"""


class Rounds:
    """Represents a round"""

    def __init__(self, name, date_and_time_beginning, date_and_time_ending) : #INTERESSANT ! si je mets 'matches_tuples_representations = []' dans les parametres, j'avais une liste déja remplie avec les résultats du premier round des que je créais le second : WHAT ! ? demander explication à Samuel, et revoir les autres classes :)
        self.name = name
        self.date_and_time_beginning = date_and_time_beginning
        self.date_and_time_ending = date_and_time_ending
        self.matches_tuples_representations = []



class Matches:
    """Represent a match"""

    def __init__(self, player_1_instance, player_2_instance, player_1_score=0, player_2_score =0) : #je mets des scores par défaut de 0, on modifiera à la fin du match
        self.player_1_instance = player_1_instance
        self.player_2_instance = player_2_instance
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score


    def match_tuple_representation(self):
        self.match_tuple_representation = ([self.player_1_instance, self.player_1_score], [self.player_2_instance, self.player_2_score])

        print("Match tuple representation", self.match_tuple_representation)
        return self.match_tuple_representation


class Players:
    """Represents a player"""

    PLAYERS = [] # Attribut de classe Note : "Un attribut de classe est une variable dont le champ d'action s'étend 
    # à l'ensemble d'une classe. Ils sont très utilisés pour compter le nombre d'instances d'une classe par exemple" 
    # source: Cours OC


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
    #TESTS
    """Creation de 8 joueurs (instances de la classe Players)
    for i in range(1,9):
        i = str(i)
        player = Players("family_name"+i, "first_name"+i, "birth_date"+i, "gender"+i, "rank"+i)

        #Ajout de chaque joueur créé (instances de classe) à l'attribut de classe PLAYERS qui est la liste contenant tous les joueurs
        Players.add_player_to_PLAYERS_list(player)
    """

    #creation 8 joueurs
    player1 = Players("family_name_1", "first_name_1", "birth_date_1", "gender_1", "rank_1")
    player2 = Players("family_name_2", "first_name_2", "birth_date_2", "gender_2", "rank_2")
    player3 = Players("family_name_3", "first_name_3", "birth_date_3", "gender_3", "rank_3")
    player4 = Players("family_name_4", "first_name_4", "birth_date_4", "gender_4", "rank_4")
    player5 = Players("family_name_5", "first_name_5", "birth_date_5", "gender_5", "rank_5")
    player6 = Players("family_name_6", "first_name_6", "birth_date_6", "gender_6", "rank_6")
    player7 = Players("family_name_7", "first_name_7", "birth_date_7", "gender_7", "rank_7")
    player8 = Players("family_name_8", "first_name_8", "birth_date_8", "gender_8", "rank_8")

    #Ajout de chaque joueur créé (instances de classe) à l'attribut de classe PLAYERS qui est la liste contenant tous les joueurs
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
    tournament1 = Tournament("LeTournoirDesTroisSorciers", "Toulouse", "début", "fin", "blitz", "description blablabla")
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
    print("Liste des joueurs du tournois tournament 1" + str (tournament1.players))
    print()
    print("Nom du premier joueur du tournois tournament 1" + str (tournament1.players[0].family_name))



    #Creation d'un tour
    round1 = Rounds("round_1", "date_begin_round_1","date_ending_round_1")

    #Ajouter les joueurs: perso, les consignes disent d'ajouter les joueurs à un tournoi, puis les round sont créés
    #'l'ordinateur génère des paires de joueurs pour les matches du premier tour"
    #les joueurs du tour sont donc... les joueurs du tournois : P ajouté aux questions 

    #ajout du round au tournois
    tournament1.rounds.append(round1)

    #L'ordinateur génère des paires de joueurs pour le premier tour.
    #donc on doit utiliser l'algorithme suisse ici, sur les 8 joueurs du tournois, on doit obtenir 4 paires de joueurs
    #chaque paire permettra de créer un match
    #chaque match sera ajouté à round1.matches qui est une liste

    #Generation des paires
    #print("Swiss algortihem return :" + str (tournament1.SwissAlgorithm_applied_to_the_tournament_by_rank_classification()))
    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_rank_classification()
    for pair in pairs:
        print()
        print("Pair générée pour le prochain match, composée de deux instances de Player: ", pair)

    #création d'un match
        match_x_of_round1 = Matches(pair[0],pair[1]) 
        print("LE MATCH SE DEROULE")

        #Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match avant de générer les paires suivantes
        #on rentre les scores
        match_x_of_round1.player_1_score += int(input("score joueur 1"))
        match_x_of_round1.player_2_score += int(input("score joueur 2"))
        #match_x_of_round1.match_tuple_representation()

    #chaque match est ajouté à round1.match_tuple_representations qui est une liste
        round1.matches_tuples_representations.append(match_x_of_round1.match_tuple_representation())


    #3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points (perso:classement/rang semble 
    # independent du tournois alors que nombre de points est relatif au joueur au sein du tournois). Si plusieurs joueurs 
    # ont le même nombre de points, triez-les en fonction de leur rang.


    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_score_classification()

    round2 = Rounds("round_2", "date_begin_round_2","date_ending_round_2")
    print("TEST !!!!!!!! ", round2.matches_tuples_representations) #devrait etre vide ici

    tournament1.rounds.append(round2)

    for pair in pairs:
        print()
        print("Pair générée pour le prochain match, composée de deux instances de Player: ", pair)

    #création d'un match
        match_x_of_round2 = Matches(pair[0],pair[1]) 
        print("LE MATCH SE DEROULE")

        #Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match avant de générer les paires suivantes
        #on rentre les scores
        match_x_of_round2.player_1_score += int(input("score joueur 1"))
        match_x_of_round2.player_2_score += int(input("score joueur 2"))
        #match_x_of_round1.match_tuple_representation()

    #chaque match est ajouté à round1.match_tuple_representations qui est une liste
        round2.matches_tuples_representations.append(match_x_of_round2.match_tuple_representation())
        print(round2.matches_tuples_representations)


#Pour le 3eme tour: 
    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_score_classification()


"""
    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_score_classification(round1.match_tuple_representations)

    print(pairs)

    #On a les paires pour le round2; 

    round2 = Rounds("round_2", "date_begin_round_2","date_ending_round_2")
    tournament1.rounds.append(round2)

    for pair in pairs:

    #création d'un match
        match_x_of_round2 = Matches(pair[0],pair[1]) 
        print("LE MATCH SE DEROULE")

        #Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match avant de générer les paires suivantes
        #on rentre les scores
        match_x_of_round2.player_1_score += int(input("score joueur 1"))
        match_x_of_round2.player_2_score += int(input("score joueur 2"))
        #match_x_of_round1.match_tuple_representation()

        #chaque match est ajouté à round1.matches qui est une liste
        round2.match_tuple_representations.append(match_x_of_round2.match_tuple_representation())

    pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_score_classification(round2.match_tuple_representations) #le pb c'est qu'il ne faut pas générer les paires sur la base des matches du round2 mais sur la base de la somme des points des joueurs

    print(pairs)



    #On a les paires pour le round3 ?

#modifications à faire : si on a deux joueurs aui ont le meme score: bug; mais avant cela: on se retrouve avec trop de joueurs : ils sont dédoublés comme s'ils avaient deux scores
#c'est parceque le score est enregistré à l'echelle du match 
#il faut la garder à l'échelle du match, c'est demandé pour 'représenter le match' en console il me semble
#mais du coup il faut aussi le faire remonter à l'echelle du round.
#reprendre ici

"""

mainTestingModel()