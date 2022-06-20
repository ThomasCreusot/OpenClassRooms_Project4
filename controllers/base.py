"""Define the main controller."""


from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


TIME_CONTROLERS = ["bullet", "blitz", "coup rapide"]

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

        player = Player(player_index, player_family_name, player_first_name, player_birth_date, player_gender, player_rank)
        print(player)

        return player


    def add_player_to_a_tournament(self, tournament_instance_name, player_instance_index):
        for tournament in Tournament.TOURNAMENTS:
            if tournament.name == tournament_instance_name:
                for player in Player.PLAYERS:
                    if player.index == player_instance_index:
                        tournament.players.append(player)
                        print(player, "added to", tournament)
            else:
                pass


    def round_initialization(self):
        round_information = self.view.information_for_round_initialization()
        round_name = round_information[0]
        round_date_and_time_beginning = round_information[1] 
        round_date_and_time_ending = round_information[2]

        round = Round(round_name, round_date_and_time_beginning, round_date_and_time_ending)
        return round

    def run(self):
        menu_choice = self.view.menu()

        if menu_choice == "1": #Create a new tournament
            self.tournament_initialization()
            self.run()


        elif menu_choice == "2": #Create a new player
            player_instance = self.player_initialization()
            self.view.player_initialization_confirmation()
            Player.add_player_to_PLAYERS_list(player_instance)
            self.run()


        elif menu_choice == "3": #Add player to a tournament
            information = self.view.information_for_adding_player_to_tournament()
            self.add_player_to_a_tournament(information[0], information[1])
            self.run()


        elif menu_choice == "4": #List of all players of the tournament
            self.view.print_all_tournament_players(Player.PLAYERS)
            self.run()


        elif menu_choice == "5": #Play a tournament
            tournament_to_play_name = self.view.information_tournament_to_play()

            for tournament in Tournament.TOURNAMENTS:
                if tournament.name == tournament_to_play_name:
                    ongoing_tournament = tournament

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

                    ongoing_match.player_1_score += int(ongoing_match_player_1_score) #player_1_score : à retrouver: c'est ou , c'est quoi ? 
                    ongoing_match.player_2_score += int(ongoing_match_player_2_score)

                    #Adding match representation (tuple) to the ongoing round
                    round_instance.matches_tuples_representations.append(ongoing_match.match_tuple_representation()) 

                #end of the round
            #end of the tournament




        #=============AUTOMATISATION OF CREATION OF 8 PLAYER=====================
        #========================================================================
        elif menu_choice == "Test": #gain of time for testing
            print("Creation of 8 factice players and a tournament named 'a', please made the choice 5")
            
            #creation 8 joueurs
            player1 = Player(1, "family_name_1", "first_name_1", "birth_date_1", "gender_1", "rank_1")
            player2 = Player(2, "family_name_2", "first_name_2", "birth_date_2", "gender_2", "rank_2")
            player3 = Player(3, "family_name_3", "first_name_3", "birth_date_3", "gender_3", "rank_3")
            player4 = Player(4, "family_name_4", "first_name_4", "birth_date_4", "gender_4", "rank_4")
            player5 = Player(5, "family_name_5", "first_name_5", "birth_date_5", "gender_5", "rank_5")
            player6 = Player(6, "family_name_6", "first_name_6", "birth_date_6", "gender_6", "rank_6")
            player7 = Player(7, "family_name_7", "first_name_7", "birth_date_7", "gender_7", "rank_7")
            player8 = Player(8, "family_name_8", "first_name_8", "birth_date_8", "gender_8", "rank_8")
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






