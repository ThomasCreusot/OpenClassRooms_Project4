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


from pydoc import plain


class Tournament:
    """Represents a tournament"""

    TOURNAMENTS = [] # Attribut de classe; Note : "Un attribut de classe est une variable dont le champ d'action s'étend 
    # à l'ensemble d'une classe. Ils sont très utilisés pour compter le nombre d'instances d'une classe par exemple" 
    # source: Cours OC


    def __init__(self, name, localisation, date_of_beginning, date_of_ending, time_controler, description, 
                number_of_rounds = "4", players=[]) : # renseigner players de la manière suivante : tournois=Tournament(...., players = ["joueur1, joueur2, ..."])
                # Je place rounds = [] dans le cors du def __init__ car d'abord on créée le tournois, puis on génère des
                #  rounds
                # Je place players=[] dans les parametres du def __init__ car d'abord on créée les joueurs, puis on 
                # créée le tournois; donc lors de la création du tournois, on peut directement renseigner les joueurs
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
        
        #il faut trier tous les joueurs d'un tournois par ordre alphabetique, je présume de leur family_name
        #self.players. methode qui trie une liste
        #note : list.sort(*key=none,reverse=false): ordone les élements dans la liste (les arguments peuvent personnaliser l’ordonnancement voir métode sorted() pour leur explication)
        #note: on est sur des instances, il faut trier sur l'attribut d'une instance
        #donc essayer self.players.sort(key = "family_name", reverse = False)
        # ou avec .sort(key=lambda x: x.family_name)
        #self.players.sort(key=lambda x: x.family_name, reverse = False)
        return self.players
        pass


    def tournament_players_listing_by_ronk_order(self):
        """Returns the list containing all players of a tournament, by rank order"""
        #voir tournament_players_listing_alphabectic_order
        pass


    def tournament_rounds_listing(self):
        """Returns the list containing all rounds of a tournament"""
        
        return self.rounds
        #VIEWS : print(tournamentX.tournament_rounds_listing())


    def tournament_matches_listing(self):
        """Returns the list containing all matches of a tournament"""

        #il faut aller chercher tous les matches d'un round, à faire une fois que j'ai fini la classe Round
        #essayer return self.rounds.matches
        pass


    def SwissAlgorithm_applied_to_the_tournament_by_rank_classification(self): #serait interessant de definir cette méthode à l'echelle du round, les deux sont possibles, jepars sur l'echelle tournament
        """Returns pairs of players for matches of a round, based on their classification"""

        # 1.	Au début du premier tour, triez tous les joueurs en fonction de leur classement
        #essayons deja de lister les joueurs d'un tournois, peu importe l'ordre
        #un joueur : return str(self.players[0].family_name)
        #les 8 joueurs return self.players
        #https://docs.python.org/fr/3/library/functions.html#sorted
        #https://docs.python.org/fr/3/howto/sorting.html#sortinghowto 
        all_players_of_tournament_sorted_by_ranks = sorted(self.players, key=lambda x: x.rank, reverse=False)
        #for player in players_sorted_by_ranks:
        #    print(player.rank)

        # 2.	Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
        higher_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[0:int(len(all_players_of_tournament_sorted_by_ranks)/2)] #0:4 --> 0,1,2,3
        lower_half_of_players_sorted_by_ranks = all_players_of_tournament_sorted_by_ranks[int(len(all_players_of_tournament_sorted_by_ranks)/2):int(len(all_players_of_tournament_sorted_by_ranks))] #4:8 --> 4,5,6,7
        #Note : j'utilise int() et pas "round" car on devrait avoir un nombre pair de joueurs

        # 2(suite) : Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié 
        # inférieure, et ainsi de suite. Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec le
        #  joueur 5, le joueur 2 est jumelé avec le joueur 6, etc

        if (len(higher_half_of_players_sorted_by_ranks)) == (len(lower_half_of_players_sorted_by_ranks)): #verification qu'on a deux listes de meme longueur
            #Pairs: variable dans laquelle on va stocker les paires
            pairs = []
            for x in range(0,(len(higher_half_of_players_sorted_by_ranks))):
                pair = (higher_half_of_players_sorted_by_ranks[x], lower_half_of_players_sorted_by_ranks[x])
                pairs.append(pair)
            #print("pairs, established from rank of players " + str(pairs))

        else:
            print("event number of players")

        return pairs

        #3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points (perso:classement/rang 
        # semble independent du tournois alors que nombre de points est relatif au joueur au sein du tournois). Si 
        # plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        #--> nouvelle fonction


    def SwissAlgorithm_applied_to_the_tournament_by_score_classification(self, previous_matches_tuple_representation): 
        """Returns pairs of players for matches of a round, based on their number of points"""

        #a faire une fois que j'aurai effectué le premier tour, avec un match, car c'est dans le match qu'on aura accès aux scores
        #print(previous_matches)
        #j'ai des tuples (4 maximum, si j'ai 8 joueurs)
        #chaque tuple contient une liste : un joueur et son score, c'est ça qui m'interesse : les récupérer et les mettre dans une meme liste: ma liste de joueurs avec leur score pour le prochain round
        
        list_of_players_and_their_score_for_the_next_round = []

        for previous_match_tuple_representation in previous_matches_tuple_representation:
            #print("_________")
            #print(previous_match_tuple_representation)
            for player_and_its_score in previous_match_tuple_representation:
                list_of_players_and_their_score_for_the_next_round.append(player_and_its_score) #print(list_of_players_and_their_score_for_the_next_round) : ok
        
        list_of_players_and_their_score_for_the_next_round_classified_by_point = sorted(list_of_players_and_their_score_for_the_next_round, key=lambda x: x[1], reverse=True) #x[1] : le score; x[0] : l'instance du joueur
        print(list_of_players_and_their_score_for_the_next_round_classified_by_point) #résultat ok

        #Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        for i in range(len(list_of_players_and_their_score_for_the_next_round_classified_by_point)-1):
            if list_of_players_and_their_score_for_the_next_round_classified_by_point[i][1] == list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1][1]:
                print("deux joueurs ont le même score") #REPRENDRE ICI : il faut trier list_of_players_and_their_score_for_the_next_round_classified_by_point[i][1] et list_of_players_and_their_score_for_the_next_round_classified_by_point[i+1][1] selon leur rank (déja fait dans une autre méthode, la difficulté sera de ne pas toucher au reste de la liste je pense)
        return "à finir"

class Rounds:
    """Represents a round"""

    def __init__(self, name, date_and_time_beginning, date_and_time_ending, matches=[]) :# voir si je garde matches 
                # en définitions dans l'init ou si je déplace, à mon sens cela dépendra de si on renseigne l'info 
                # lors de la création du Round
        self.name = name
        self.date_and_time_beginning = date_and_time_beginning
        self.date_and_time_ending = date_and_time_ending
        self.matches = matches



class Matches:
    """Represent a match"""

    def __init__(self, player_1_instance, player_2_instance, player_1_score=0, player_2_score =0) : #je mets des scores par défaut de 0, on modifiera à la fin du match
        self.player_1_instance = player_1_instance
        self.player_2_instance = player_2_instance
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score


    def match_tuple_representation(self):
        self.match_tuple_representation = ([self.player_1_instance, self.player_1_score], [self.player_2_instance, self.player_2_score])

        print(self.match_tuple_representation)
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

#j'avais fait une classe SwissSystem, je pense pouvoir m'en sortir avec une fonction, voire meme une méthode de la classe tournois
""" 
class SwissSystem:
    Returns pairs of players for matches of a round

    def __init__(self): #A UN MOMENT IL FAUT LUI DONNER LES JOUEURS d'UN round? donc autant communiquer le round
        first_half_of_players_sorted_by_ranks = []
        second_half_of_players_sorted_by_ranks = []
        first_half_of_players_sorted_by_points = []
        second_half_of_players_sorted_by_points = []


    def players_sorting_by_rank():
        pass

    def players_pairing_by_rank():
        pass

    def players_sorting_by_points():
        pass

    def players_pairing_by_points():
        pass
"""


"""
Assurez-vous que vos modèles sont bien séparés. 
    Vous pouvez écrire de petits « scripts » ou des programmes qui importent les modèles requis, créent quelques instances (voir ci-dessus), les font interagir et affichent les résultats. Exemple : 
        créer quelques joueurs ;
        créer un tour, ajouter les joueurs ;
        voir comment les joueurs sont associés (classements) ;
        gagner/perdre des matchs de manière aléatoire ;
        vérifier que les données des modèles sont correctement mises à jour.
"""


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
print("Liste de tous les joueurs" + str(Players.PLAYERS))
#print du family name du 1er joueur dans la liste de tous les joueurs
print("Nom de famille du premier joueur de la liste" + Players.PLAYERS[0].family_name)
print("Nom de famille du deuxieme joueur de la liste" + Players.PLAYERS[1].family_name)


#Creation d'un tournoi
tournament1 = Tournament("LeTournoirDesTroisSorciers", "Toulouse", "début", "fin", "blitz", "description blablabla")
#Ajout du tournoi à la liste des tournois
Tournament.add_tournament_to_TOURNAMENTS_list(tournament1)
#Print de la liste des tournois
print("Liste des tournois" + str(Tournament.listing_all_tournaments()))

#ajouter 8 joueurs au tournois:
tournament1.players.append(player1)
tournament1.players.append(player2)
tournament1.players.append(player3)
tournament1.players.append(player4)
tournament1.players.append(player5)
tournament1.players.append(player6)
tournament1.players.append(player7)
tournament1.players.append(player8)

print("Liste des joueurs du tournois tournament 1" + str (tournament1.players))
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
    print(pair)

#création d'un match

    match_x_of_round1 = Matches(pair[0],pair[1]) 
    print("LE MATCH SE DEROULE")

    #Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match avant de générer les paires suivantes
    #on rentre les scores
    match_x_of_round1.player_1_score += int(input("score joueur 1"))
    match_x_of_round1.player_2_score += int(input("score joueur 2"))
    #match_x_of_round1.match_tuple_representation()

#chaque match est ajouté à round1.matches qui est une liste
    round1.matches.append(match_x_of_round1.match_tuple_representation())


#3.	Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points (perso:classement/rang semble 
# independent du tournois alors que nombre de points est relatif au joueur au sein du tournois). Si plusieurs joueurs 
# ont le même nombre de points, triez-les en fonction de leur rang.

#comment accéder à un score donné ?


pairs = tournament1.SwissAlgorithm_applied_to_the_tournament_by_score_classification(round1.matches)


