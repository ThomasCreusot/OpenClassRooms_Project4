class View:
    """Chess tournament organisation view."""

    def __init__(self) :
        print("View created")

    def menu(self):
        """Asks to the user which action he/she wants to do"""
        
        menu_choice = input(
            "" "\n"
            "Welcome, what do you want to do ? " "\n"
            "If you want to create a new tournament, please write '1' " "\n"
            "If you want to add a player, please press '2'" "\n"
            "If you want to add a player to a tournament , please press '3'" "\n"
            "If you want to create 8 factices players and add them to a factice tournament, please write 'Test'" "\n" #Gain of time for testing.           
            "If you want to see all players of the tournament, please press '4'" "\n"
            "If you want to play a tournament, please press '5'" "\n"


            #"If you want to ..., please press '...'" "\n"
        )

        return menu_choice


    def no_menu_choice_was_made(self):
        """Explains to the user that no correct choice was made"""

        print("Your choice was not understood, please try again")


    def information_for_tournament_initialization(self):
        """Asks to the user the information required to create a tournament"""
        tournament_name = input("What is the tournament name ? ")
        tournament_localisation = input("What is the tournament localisation ? ")
        tournament_date_of_beginning = input("What is the tournament date of beginning ? ")
        tournament_date_of_ending = input("What is the tournament date of ending ? ")
        tournament_time_controler = input("What is the tournament time controler ? ")
        tournament_description = input("What is the tournament description ? ")
        print("Note: Number of rounds is 4 by default")

        return tournament_name, tournament_localisation, tournament_date_of_beginning, tournament_date_of_ending, tournament_time_controler, tournament_description


    def tournament_initialization_confirmation(self):
        """Confirmation of the initialization of a tournament"""

        print("The tournament has been created")


    def information_for_player_initialization(self):
        """Asks to the user the information required to create a Player"""
        player_index = input("What is the player index ? ")
        player_family_name = input("What is the player family name ? ")
        player_first_name = input("What is the player first name ? ")
        player_birth_date = input("What is the player birth date ? ")
        player_gender = input("What is the player gender ? ")
        player_rank = input("What is the player rank ? ")

        return player_index, player_family_name, player_first_name, player_birth_date, player_gender, player_rank


    def player_initialization_confirmation(self):
        """Confirmation of the initialization of a player"""

        print("The player has been created")


    def print_all_tournament_players(self, list_of_players):
        """Print all players of the tournament"""
        print("List of all player of the tournament ", list_of_players)


    def information_for_adding_player_to_tournament(self):
        """Asks information for adding a player to a tournament"""
        information_tournament = input("In which tournament do you want to add a Player ? ")
        information_player = input("Which player do you want to add to the tournament ? Please write the index of the player. ")
        return information_tournament, information_player


    def information_tournament_to_play(self):
        """."""
        tournament_to_play_name = input("Which tournament will be played ? Please enter the name of the tournament. ")
        return tournament_to_play_name


    def announce_round_begins(self, round_number):
        """Announces that a round is ready to begin"""
        print("Round number {0} is ready to begin".format(round_number))


    def information_for_round_initialization(self):
        """Asks information for initialization of a round"""
        round_name = input("What is the name of the round, please ? ")
        round_date_and_time_beginning = input("What is the date and time of beginning of the round, please ?" )
        round_date_and_time_ending = input("What is the date and time of ending of the round, please ?" )

        #A REVOIR : quand est ce qu'il renseigne la fin du round ?...
        return round_name, round_date_and_time_beginning, round_date_and_time_ending


    def round_initialization_confirmation(self):
        """Confirmation of the initialization of a round"""

        print("The round has been created")

    def match_annoucement(self, family_name_player1, family_name_player2):
        """Announces that a match must be played"""

        print("Player {0} must play against {1} .".format(family_name_player1, family_name_player2))


    def match_results_information(self, instance_player1, instance_player2):
        """Asks results of a match"""
        
        print("Dear tournament manager, please enter the scores of the match")
        ongoing_match_player_1_score = input("Score player 1 ({0}): ".format(instance_player1.family_name))
        ongoing_match_player_2_score = input("Score player 2 ({0}): ".format(instance_player2.family_name)) 
        return ongoing_match_player_1_score, ongoing_match_player_2_score
    
    def wrong_tournament_time_controler(self):
        """Advertissement about the time controler which is not in the list TIME_CONTROLERS"""
        print("Advertissement: the chosen time controler has not been controlled, please try again")