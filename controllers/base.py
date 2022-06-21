"""Define the main controller."""


from datetime import datetime

from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


TIME_CONTROLERS = ["bullet", "blitz", "coup rapide"]
SCORES = ["0", "0,5", "1"]

"""
Responsables de la logique du programme 
•	Vous pouvez avoir un contrôleur « Application », qui instanciera :
o	un contrôleur `MenuManager`;
o	un contrôleur `TournamentManager`;
o	un contrôleur `UserManager`.
"""


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
        for tournament in Tournament.TOURNAMENTS:
            if tournament.name == tournament_instance_name:
                for player in Player.PLAYERS:
                    if player.index == player_instance_index:
                        tournament.players.append(player)
                        print(player, "added to", tournament) # --> view
            else:
                pass


    def round_initialization(self):
        round_information = self.view.information_for_round_initialization()
        round_name = round_information
        round_date_and_time_beginning = datetime.now()
        round_date_and_time_ending = "" #Will be completed at the end of the round

        round = Round(round_name, round_date_and_time_beginning, round_date_and_time_ending)
        return round


    def round_termination(self, round):
        round.round_date_and_time_ending = datetime.now()


    def player_rank_manual_modification(self, tournament):
        for player in tournament.players:
            newrank = self.view.rank_player_information(player)
            if newrank.isdigit() :
                player.rank = newrank
            else:
                self.view.wrong_player_rank()



    def run(self):
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


        elif menu_choice == "4": #List of all players 
            for player in Player.PLAYERS:
                self.view.display_a_player(player)

            self.run()


        elif menu_choice == "5": #Play a tournament
            tournament_to_play_name = self.view.information_tournament_to_play()

            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == tournament_to_play_name:
                    ongoing_tournament = tournament

            for player in ongoing_tournament.players:
                player.player_total_score_at_tournament_scale = 0

            for round_index in range (0, int(ongoing_tournament.number_of_rounds)):

                round_number = round_index + 1
                #Round creation and association to the ongoing tournament
                round_instance = self.round_initialization()
                self.view.round_initialization_confirmation()

                ongoing_tournament.rounds.append(round_instance)

                #Round ready to be played
                self.view.announce_round_begins(round_number)

                #Pairs creation
                if round_number == 1:
                    pairs = ongoing_tournament.SwissAlgorithm_applied_to_the_tournament_by_rank_classification()
                elif round_number > 1:
                    pairs = ongoing_tournament.SwissAlgorithm_applied_to_the_tournament_by_score_classification()
                else:
                    pass

                for pair in pairs:
                    #Match annoucement and creation
                    self.view.match_annoucement(pair[0].family_name, pair[1].family_name)
                    ongoing_match = Match(pair[0],pair[1]) #pair[0] and pair[1] are a Player instance

                    #End of the match, time to enter the results 
                    match_result_information = self.view.match_results_information(pair[0], pair[1]) #pair[1] is a Player instance
                    ongoing_match_player_1_score = match_result_information[0] 
                    ongoing_match_player_2_score = match_result_information[1]

                    if ongoing_match_player_1_score in SCORES and ongoing_match_player_2_score in SCORES :
                        ongoing_match.player_1_score += int(ongoing_match_player_1_score)  
                        ongoing_match.player_2_score += int(ongoing_match_player_2_score)

                        #Compteur de points à l'échelle du tournois
                        for player in ongoing_tournament.players:
                            if player == pair[0]:
                                player.player_total_score_at_tournament_scale += int(ongoing_match_player_1_score)
                            if player == pair[1]:
                                player.player_total_score_at_tournament_scale += int(ongoing_match_player_2_score)


                        #Adding match representation (tuple) to the ongoing round
                        round_instance.matches_tuples_representations.append(ongoing_match.match_tuple_representation()) 

                    else:
                        self.view.wrong_player_score()


                #end of the round
                self.round_termination(round_instance)

            
            #end of the tournament
            self.player_rank_manual_modification(ongoing_tournament)
            
            #for proper display
            higher_player_name_lenght = 1
            for player in ongoing_tournament.players:
                if len(player.family_name) > higher_player_name_lenght:
                    higher_player_name_lenght = len(player.family_name)


            #results display
            self.view.tournament_results_displa_begin(ongoing_tournament.name, higher_player_name_lenght)


            for player in ongoing_tournament.players:
                self.view.tournament_player_results_display(player.family_name, player.player_total_score_at_tournament_scale, player.rank)

            self.view.tournament_results_display_ending()
            self.run()


        elif menu_choice == "6": #Player rank update 
            information = self.view.information_for_updating_player_rank()

            concerned_player_index = int(information[0])
            new_rank = int(information[1])

            for player in Player.PLAYERS :
                if player.index == concerned_player_index:
                    player.rank = new_rank

            self.run()


        elif menu_choice == "71": 
            #"If you want to see all players classified by alphabetical order, please press '71'" "\n"
            list_of_players_by_family_name = sorted(Player.PLAYERS, key=lambda x: x.family_name, reverse=False)
            for player in list_of_players_by_family_name:
                self.view.display_a_player(player)

            self.run()


        elif menu_choice == "72": 
            #"If you want to see all players classifiedby rank (classification) order, please press '72'" "\n"
            list_of_players_by_rank = sorted(Player.PLAYERS, key=lambda x: x.rank, reverse=False)
            for player in list_of_players_by_rank:
                self.view.display_a_player(player)

            self.run()


        elif menu_choice == "73": 
            #"If you want to see all players of a tournament classified by alphabetical order, please press '73'" "\n"
            information = self.view.information_for_displaying_tournament_players()
            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == information:
                    list_of_tournament_players_by_name = sorted(tournament.players, key=lambda x: x.family_name, reverse=False)
                    for player in list_of_tournament_players_by_name:
                        self.view.display_a_player(player)
                else: 
                    pass

            self.run()


        elif menu_choice == "74": 
            #"If you want to see all players of a tournament classifiedby rank (classification) order, please press '74'" "\n"
            information = self.view.information_for_displaying_tournament_players()
            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == information:
                    list_of_tournament_players_by_rank = sorted(tournament.players, key=lambda x: x.rank, reverse=False)
                    for player in list_of_tournament_players_by_rank:
                        self.view.display_a_player(player)
                else: 
                    pass

            self.run()

        elif menu_choice == "81": 
            #"If you want to see all tournaments, please press '81'" "\n"
            all_registered_tournaments = Tournament.listing_all_tournaments()
            self.view.display_all_tournaments(all_registered_tournaments)

            self.run()


        elif menu_choice == "82": 
            #"If you want to see all round of a tournament, please press '82'" "\n"
            information = self.view.information_for_displaying_tournament_rounds_or_matches()
            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == information:
                    list_of_rounds = tournament.tournament_rounds_listing()
                    self.view.display_rounds(list_of_rounds)

            self.run()


        elif menu_choice == "83": 
            #"If you want to see all matches of a tournament, please press '83'" "\n"
            information = self.view.information_for_displaying_tournament_rounds_or_matches()
            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == information:
                    matches_tuples_representation_list = tournament.tournament_matches_listing()
                    self.view.display_matches_result(matches_tuples_representation_list)

            self.run()







        #=============AUTOMATISATION OF CREATION OF 8 PLAYER=====================
        #========================================================================
        elif menu_choice == "Test": #gain of time for testing
            print("Creation of 8 factice players and a tournament named 'a', please made the choice 5")
            
            #creation 8 joueurs
            player1 = Player(1, "family_name_1", "first_name_1", "birth_date_1", "gender_1", 1)
            player2 = Player(2, "family_name_2", "first_name_2", "birth_date_2", "gender_2", 2)


            player3 = Player(3, "family_name_3", "first_name_3", "birth_date_3", "gender_3", 3)
            player4 = Player(4, "family_name_4", "first_name_4", "birth_date_4", "gender_4", 4)
            player5 = Player(5, "family_name_5", "first_name_5", "birth_date_5", "gender_5", 5)

            player6 = Player(6, "family_name_6", "first_name_6", "birth_date_6", "gender_6", 6)
            player7 = Player(7, "family_name_7", "first_name_7", "birth_date_7", "gender_7", 7)
            player8 = Player(8, "family_name_8", "first_name_8", "birth_date_8", "gender_8", 8)
            #Ajout de chaque joueur créé (instances de classe) à l'attribut de classe PLAYERS qui est la liste contenant tous 
            # les joueurs
            Player.add_player_to_PLAYERS_list(player1)
            Player.add_player_to_PLAYERS_list(player2)
            Player.add_player_to_PLAYERS_list(player3)
            Player.add_player_to_PLAYERS_list(player4)
            Player.add_player_to_PLAYERS_list(player5)
            Player.add_player_to_PLAYERS_list(player6)
            Player.add_player_to_PLAYERS_list(player7)
            Player.add_player_to_PLAYERS_list(player8)
            
            #Creation d'un tournoi
            tournament1 = Tournament("a", "Toulouse", "début", "fin", "blitz", "description blabla")
            #Ajout du tournoi à la liste des tournois
            Tournament.add_tournament_to_TOURNAMENTS_list(tournament1)
            #ajouter 8 joueurs au tournois:
            tournament1.players.append(player1)
            tournament1.players.append(player2)
            tournament1.players.append(player3)
            tournament1.players.append(player4)
            tournament1.players.append(player5)
            tournament1.players.append(player6)
            tournament1.players.append(player7)
            tournament1.players.append(player8)

            self.run()
            #========================================================================"""
            #========================================================================"""

        else:
            self.run()






