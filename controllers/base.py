"""Define the main controller."""

from datetime import datetime

from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


TIME_CONTROLERS = ["bullet", "blitz", "coup rapide"]
SCORES = [0, 0.5, 1]

"""
The controller is responsible for the logic of the program
"""


# CONSEIL OC : Vous pouvez avoir un contrôleur « Application », qui instanciera :
# un contrôleur `MenuManager`;
# un contrôleur `TournamentManager`;
# un contrôleur `UserManager`.
# Pas mis en place; Je suppose que ca donnerait : 
# Class Controller:
#     def __init__(self, MenuManager, TournamentManager, UserManager)
#         ...
# controller = Controler(menu_manager, ...)
# Class MenuManager:
#     def __init__(self)
#         ...
# menu_manager = MenuManager()
# et, dans l'instance de classe de Controller: 
# self.menu_manager.nom_de_methode()


class Controller:
    """Main controller"""

    def __init__(self, view) :
        self.view = view


    def tournament_initialization(self):
        """Initializes a tournament from the information retrieved from the view"""

        tournament_information = self.view.information_for_tournament_initialization()
        tournament_name = tournament_information[0]
        tournament_localisation = tournament_information[1]
        tournament_date_of_beginning = tournament_information[2]
        tournament_date_of_ending = tournament_information[3]
        tournament_time_controler = tournament_information[4]
        tournament_description = tournament_information[5]

        if tournament_time_controler.lower() in TIME_CONTROLERS : 
            tournament = Tournament(tournament_name, tournament_localisation, tournament_date_of_beginning, tournament_date_of_ending, tournament_time_controler, tournament_description)
            self.view.tournament_initialization_confirmation()
            Tournament.add_tournament_to_TOURNAMENTS_list(tournament)

        else:
            self.view.wrong_tournament_time_controler()


    def player_initialization(self):
        """Initializes a player from the information retrieved from the view"""

        player_information = self.view.information_for_player_initialization()
        player_index = player_information[0]
        player_family_name = player_information[1]
        player_first_name = player_information[2]
        player_birth_date = player_information[3]
        player_gender = player_information[4]
        player_rank = player_information[5]

        if player_index.isdigit() and player_rank.isdigit():
            player = Player(player_index, player_family_name, player_first_name, player_birth_date, player_gender, player_rank)
            return player

        else:
            self.view.wrong_player_index_or_rank()
            return None


    def add_player_to_a_tournament(self, tournament_instance_name, player_instance_index):
        """Add a player to the tournament.players list"""

        for tournament in Tournament.TOURNAMENTS:
            if tournament.name == tournament_instance_name:
                tournament.players.append(player_instance_index)
            else:
                pass

        """Avant les bases de données, j'ajoutais toute l'instance du joueur dans la liste tournamentX.players
        for tournament in Tournament.TOURNAMENTS:
            if tournament.name == tournament_instance_name:
                for player in Player.PLAYERS:
                    if player.index == player_instance_index:
                        tournament.players.append(player)
            else:
                pass
        """


    def round_initialization(self):
        """Allows to create a Round instance, with automatization of time of begining"""

        round_information = self.view.information_for_round_initialization()
        round_name = round_information
        round_date_and_time_beginning = datetime.now()
        round_date_and_time_ending = "" #Will be completed at the end of the round

        round = Round(round_name, round_date_and_time_beginning, round_date_and_time_ending)
        return round


    def round_termination(self, round):
        """Registers the ending time of a round"""

        round.round_date_and_time_ending = datetime.now()


    def player_rank_manual_modification(self, tournament):
        """Allows to modify the rank of a player"""

        list_of_tournament_players = self.list_of_tournament_players_objects_from_their_indexes(tournament.players)

        for player in list_of_tournament_players:
            newrank = self.view.rank_player_information(player)

            if newrank.isdigit() :
                player.rank = newrank

            else:
                self.view.wrong_player_rank()

        """ avant modif bdd 24062022
        for player in tournament.players:
            newrank = self.view.rank_player_information(player)

            if newrank.isdigit() :
                player.rank = newrank

            else:
                self.view.wrong_player_rank()
        """


    def player_rank_update(self):
        """Allows to modify the rank of a player at the end of the tournament"""

        information = self.view.information_for_updating_player_rank()

        concerned_player_index = information[0] # integer
        new_rank = information[1] # integer

        for player in Player.PLAYERS :
            if player.index == concerned_player_index:
                player.rank = new_rank


    def play_a_tournament(self):
        """Organise the succession of event for playing a tournament"""

        tournament_to_play_name = self.view.information_tournament_to_play()

        for tournament in Tournament.TOURNAMENTS:
            if tournament.name == tournament_to_play_name:
                ongoing_tournament = tournament

        # Player score reinitialization 
        list_of_tournament_players = self.list_of_tournament_players_objects_from_their_indexes(ongoing_tournament.players)
        for player in list_of_tournament_players:
        #for player in ongoing_tournament.players:
            player.player_total_score_at_tournament_scale = 0

        # Beginning of the round
        for round_index in range (0, int(ongoing_tournament.number_of_rounds)):
            round_number = round_index + 1

            # Round creation and association to the ongoing tournament
            round_instance = self.round_initialization()
            self.view.round_initialization_confirmation()

            ongoing_tournament.rounds.append(round_instance)

            # Round ready to be played
            self.view.announce_round_begins(round_number)

            # Pairs creation
            if round_number == 1:
                pairs = ongoing_tournament.SwissAlgorithm_applied_to_the_tournament_by_rank_classification(list_of_tournament_players)
            elif round_number > 1:
                pairs = ongoing_tournament.SwissAlgorithm_applied_to_the_tournament_by_score_classification(list_of_tournament_players)
            else:
                pass

            if pairs != None:

                for pair in pairs:
                    # Match annoucement and creation
                    self.view.match_annoucement(pair[0].family_name, pair[1].family_name)
                    ongoing_match = Match(pair[0],pair[1]) #pair[0] and pair[1] are a Player instance, respectively

                    # End of the match, time to enter the results 
                    match_result_information = self.view.match_results_information(pair[0], pair[1]) #pair[1] is a Player instance
                    ongoing_match_player_1_score = match_result_information[0] 
                    ongoing_match_player_2_score = match_result_information[1]

                    if ongoing_match_player_1_score in SCORES and ongoing_match_player_2_score in SCORES and ongoing_match_player_1_score+ongoing_match_player_2_score==1:
                        # Score counter at the round scale, registered at match scale but will be used at round scale 
                        ongoing_match.player_1_score += ongoing_match_player_1_score  
                        ongoing_match.player_2_score += ongoing_match_player_2_score

                        # Score counter at the tournament scale 
                        list_of_tournament_players = self.list_of_tournament_players_objects_from_their_indexes(ongoing_tournament.players)
                        for player in list_of_tournament_players:
                        #for player in ongoing_tournament.players:
                            if player == pair[0]:
                                player.player_total_score_at_tournament_scale += ongoing_match_player_1_score
                            if player == pair[1]:
                                player.player_total_score_at_tournament_scale += ongoing_match_player_2_score

                        # Adding match representation (tuple) to the ongoing round
                        round_instance.matches_tuples_representations.append(ongoing_match.match_tuple_representation()) 

                    else:
                        self.view.wrong_player_score()
            else : #Pairs == None
                self.view.even_players_alert()


            # End of the round
            self.round_termination(round_instance)
        
        # End of the tournament
        self.player_rank_manual_modification(ongoing_tournament)


        # For proper display
        higher_player_name_lenght = max(len(player.family_name) for player in self.list_of_tournament_players_objects_from_their_indexes(ongoing_tournament.players))
        # Results display
        self.view.tournament_results_displa_begin(ongoing_tournament.name, higher_player_name_lenght)

        list_of_tournament_players = self.list_of_tournament_players_objects_from_their_indexes(ongoing_tournament.players)
        for player in list_of_tournament_players:
        #for player in ongoing_tournament.players:
            self.view.tournament_player_results_display(player.family_name, player.player_total_score_at_tournament_scale, player.rank)

        self.view.tournament_results_display_ending()


    def players_displaying_general_method(self):
        """Organises the event to display players (all or from a tournament) by family name or rank order"""

        # "If you want to see all players or all players of a tournament, classified by alphabetical or rank (classification) order, please press '7'" "\n"
        all_players_or_players_of_a_tournament = self.view.all_players_or_players_of_a_tournament()
        list_of_players = [] # ????? pourquoi necessaire ? 

        # List of players = all players
        if all_players_or_players_of_a_tournament.lower() == "all":
            list_of_players = Player.listing_all_players()

        # List of players = all players of a tournament
        elif all_players_or_players_of_a_tournament.lower() == "tournament":
            information = self.view.information_for_displaying_tournament_players()
            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == information:
                    list_of_players_indexes = tournament.tournament_players_listing()
                    list_of_players = self.list_of_tournament_players_objects_from_their_indexes(list_of_players_indexes)
                else: 
                    self.run() # user did not choose a correct tournament name

        else: 
            self.run() # user did not choose all or tournament


        # Players order
        players_order_choice = self.view.players_order_choice()

        if players_order_choice.lower() == "name":
            ordered_list_of_players = sorted(list_of_players, key=lambda x: x.family_name, reverse=False)
        elif players_order_choice.lower() == "rank":
            ordered_list_of_players = sorted(list_of_players, key=lambda x: x.rank, reverse=False)
        else:
            ordered_list_of_players= list_of_players # not ordered

        # Display players
        for player in ordered_list_of_players:
            self.view.display_a_player(player)


    def list_of_tournament_players_objects_from_their_indexes(self, players_indexes): #players_indexes sera un tournamentX.players
        """Returns a list of players objects from their indexes"""
        
        list_of_tournament_players = []
        for player_index in players_indexes:
            for player in Player.PLAYERS :
                if player_index == player.index:
                    list_of_tournament_players.append(player)
                else:
                    pass
        return list_of_tournament_players


    #===== RUN METHOD =====
    def run(self):
        """Organises the succession of events constituting the application"""

        menu_choice = self.view.menu()

        if menu_choice == "1": #Create a new tournament
            self.tournament_initialization()
            self.run()


        elif menu_choice == "2": #Create a new player
            player_instance = self.player_initialization()

            if player_instance != None :
                self.view.player_initialization_confirmation()
                Player.add_player_to_PLAYERS_list(player_instance)

            self.run()


        elif menu_choice == "3": #Add player to a tournament
            information = self.view.information_for_adding_player_to_tournament()
            self.add_player_to_a_tournament(information[0], information[1])
            self.run()


        elif menu_choice == "4": # Play a tournament
            self.play_a_tournament()
            self.run()


        elif menu_choice == "5": #Player rank update 
            self.player_rank_update()
            self.run()


        elif menu_choice == "6": # Shows players (all or from a tournament), by family name or rank order
            self.players_displaying_general_method()
            self.run()


        elif menu_choice == "71": 
            #"If you want to see all tournaments, please press '81'" "\n"
            all_registered_tournaments = Tournament.listing_all_tournaments()
            self.view.display_all_tournaments(all_registered_tournaments)

            self.run()


        elif menu_choice == "72": 
            #"If you want to see all round of a tournament, please press '82'" "\n"
            information = self.view.information_for_displaying_tournament_rounds_or_matches()
            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == information:
                    list_of_rounds = tournament.tournament_rounds_listing()
                    self.view.display_rounds(list_of_rounds)

            self.run()


        elif menu_choice == "73": 
            #"If you want to see all matches of a tournament, please press '83'" "\n"
            information = self.view.information_for_displaying_tournament_rounds_or_matches()
            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == information:
                    matches_tuples_representation_list = tournament.tournament_matches_listing()
                    self.view.display_matches_result(matches_tuples_representation_list)

            self.run()


        elif menu_choice == "8": # Data base options

            database_menu_choice = self.view.database_menu_choice()

            if database_menu_choice == "1":
                Player.write_serialized_player_in_tinydb_database()
                self.view.database_action_confirmation()

            elif database_menu_choice == "2":
                Player.load_players_from_tinydb_at_python_format()
                self.view.database_action_confirmation()

            elif database_menu_choice == "3":
                Tournament.write_serialized_tournament_in_tinydb_database()
                self.view.database_action_confirmation()

            elif database_menu_choice == "4":
                Tournament.load_tournaments_from_tinydb_at_python_format()
                self.view.database_action_confirmation()

            elif database_menu_choice.lower() == "exit":
                self.run

            else:
                pass

            self.run()



        #=============AUTOMATISATION OF CREATION OF 8 PLAYER=====================
        #========================AND A TOURNAMENT================================

        # Gain of time for testing
        elif menu_choice.lower() == "test": # 
            print("Creation of 8 factice players and a tournament named 'a', please made the choice 5")

            # Creation 8 joueurs
            player1 = Player(1, "family_name_1", "first_name_1", "birth_date_1", "gender_1", 1)
            player2 = Player(2, "family_name_2", "first_name_2", "birth_date_2", "gender_2", 2)
            player3 = Player(3, "family_name_3", "first_name_3", "birth_date_3", "gender_3", 3)
            player4 = Player(4, "family_name_4", "first_name_4", "birth_date_4", "gender_4", 4)
            player5 = Player(5, "family_name_5", "first_name_5", "birth_date_5", "gender_5", 5)
            player6 = Player(6, "family_name_6", "first_name_6", "birth_date_6", "gender_6", 6)
            player7 = Player(7, "family_name_7", "first_name_7", "birth_date_7", "gender_7", 7)
            player8 = Player(8, "family_name_8", "first_name_8", "birth_date_8", "gender_8", 8)
            # Ajout de chaque joueur créé (instances de classe) à l'attribut de classe PLAYERS qui est la liste contenant tous 
            # les joueurs
            Player.add_player_to_PLAYERS_list(player1)
            Player.add_player_to_PLAYERS_list(player2)
            Player.add_player_to_PLAYERS_list(player3)
            Player.add_player_to_PLAYERS_list(player4)
            Player.add_player_to_PLAYERS_list(player5)
            Player.add_player_to_PLAYERS_list(player6)
            Player.add_player_to_PLAYERS_list(player7)
            Player.add_player_to_PLAYERS_list(player8)

            # Creation d'un tournoi
            tournament1 = Tournament("a", "Toulouse", "début", "fin", "blitz", "description blabla")
            # Ajout du tournoi à la liste des tournois
            Tournament.add_tournament_to_TOURNAMENTS_list(tournament1)
            # Ajouter 8 joueurs au tournois:
            tournament1.players.append(player1.index)
            tournament1.players.append(player2.index)
            tournament1.players.append(player3.index)
            tournament1.players.append(player4.index)
            tournament1.players.append(player5.index)
            tournament1.players.append(player6.index)
            tournament1.players.append(player7.index)
            tournament1.players.append(player8.index)

            self.run()
            #========================================================================"""
            #========================================================================"""

        else:
            self.run()
