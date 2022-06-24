from controllers.base import TIME_CONTROLERS
from controllers.base import SCORES


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

            "If you want to play a tournament, please press '4'" "\n"
            "If you want to update a player rank, please press '5'" "\n"
            "If you want to see all players or all players from a tournament, classified by alphabetical or rank (classification) order, please press '6'" "\n"
            "If you want to see all tournaments, please press '71'" "\n"
            "If you want to see all round of a tournament, please press '72'" "\n"
            "If you want to see all matches of a tournament, please press '73'" "\n"

            "For database options, please press '8'" "\n"
        )

        return menu_choice


    def no_menu_choice_was_made(self):
        """Explains to the user that no correct choice was made"""

        print("Your choice was not understood, please try again. ")


    def information_for_tournament_initialization(self):
        """Asks to the user the information required to create a tournament"""

        tournament_name = input("What is the tournament name ? ")
        tournament_localisation = input("What is the tournament localisation ? ")
        tournament_date_of_beginning = input("What is the tournament date of beginning ? ")
        tournament_date_of_ending = input("What is the tournament date of ending ? ")
        tournament_time_controler = input("What is the tournament time controler ? ")
        tournament_description = input("What is the tournament description ? ")

        return tournament_name, tournament_localisation, tournament_date_of_beginning, tournament_date_of_ending, tournament_time_controler, tournament_description


    def tournament_initialization_confirmation(self):
        """Confirmation of the initialization of a tournament"""

        print("The tournament has been created. ")


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

        print("The player has been created. ")


    def players_order_choice(self):
        """Asks the user if he wants to display players ordered by their family name or by their rank"""

        players_order_choice = input("Display players ordered by family name or by rank ? (Name/Rank) ")

        return players_order_choice


    def all_players_or_players_of_a_tournament(self):
        """Asks the user if he wants to display all players or players from a specific tournament"""

        all_players_or_players_of_a_tournament = input("Do you want to display all players (All) or players from a specific tournament (Tournament) ? (All/Tournament) ")

        return all_players_or_players_of_a_tournament


    def display_a_player(self, player):
        """Prints a player """

        print("Index: {0} / Family name: {1} / First name: {2} / Rank: {3}".format(player.index, player.family_name, player.first_name, player.rank))


    def information_for_adding_player_to_tournament(self):
        """Asks information for adding a player to a tournament"""

        information_tournament = input("In which tournament do you want to add a Player ? ")
        information_player = input("Which player do you want to add to the tournament ? Please write the index of the player. ")

        return information_tournament, information_player


    def information_tournament_to_play(self):
        """Asks which tournament will be played"""

        tournament_to_play_name = input("Which tournament will be played ? Please enter the name of the tournament. ")
        return tournament_to_play_name


    def announce_round_begins(self, round_number):
        """Announces that a round is ready to begin"""

        print()
        print("ROUND NUMBER {0} IS READY TO BEGIN".format(round_number))


    def information_for_round_initialization(self):
        """Asks information for initialization of a round"""

        print()
        round_name = input("What is the name of the round, please ? ")

        return round_name 


    def round_initialization_confirmation(self):
        """Confirmation of the initialization of a round"""

        print()
        print("The round has been created. ")


    def match_annoucement(self, family_name_player1, family_name_player2):
        """Announces that a match must be played"""

        print()
        print("Player {0} must play against {1} .".format(family_name_player1, family_name_player2))


    def match_results_information(self, instance_player1, instance_player2):
        """Asks results of a match"""

        print("Dear tournament manager, please enter the scores of the match")
        ongoing_match_player_1_score = float(input("Score player 1 ({0}): ".format(instance_player1.family_name)))
        ongoing_match_player_2_score = float(input("Score player 2 ({0}): ".format(instance_player2.family_name)))

        return ongoing_match_player_1_score, ongoing_match_player_2_score


    def wrong_tournament_time_controler(self):
        """Advertissement about the time controler which is not in the list TIME_CONTROLERS"""

        print("Advertissement: the chosen time controler is not an allowed one ({0}), please try again".format(TIME_CONTROLERS))


    def wrong_player_rank(self):
        """Advertissement about the rank which is not a positive number"""

        print("Advertissement: the rank is not a positive number, please try again")


    def wrong_player_score(self):
        """Advertissement about the score which is not in the list SCORES or does not have a total equal to 1"""

        print("Advertissement: the score is not an allowed one ({0}) or its sum is different from 1, please try again; your input has not been considered by the program".format(SCORES))


    def rank_player_information(self, player):
        """Asks which is the new rank of a player at the end of a tournament"""

        new_rank = input("Please enter the new rank of the player {0} : ".format(player.family_name))

        return new_rank


    def wrong_player_index_or_rank(self):
        """Advertissement about the index or the rank which is not an integer"""

        print("Advertissement: the index or the rank is not an integer, please try again")


    def tournament_results_displa_begin(self, ongoing_tournament_name, higher_player_name_lenght):
        """Displays and introduction do the detailled results of a tournament"""

        space_in_display_if_long_family_name = max(higher_player_name_lenght-len("PLAYER")-1, len("PLAYER"))

        print()
        print()
        print("========== RESULTS OF THE TOUNRAMENT {0} ==========".format(ongoing_tournament_name.capitalize()))
        print("PLAYER", space_in_display_if_long_family_name * " ", "| SCORE | RANK")


    def tournament_player_results_display(self, player_name, player_total_score_at_tournament_scale, player_rank):
        """Displays the detailled results of a tournament"""

        print("{0} |   {1}   |  {2} ".format(player_name, player_total_score_at_tournament_scale, player_rank))
        #print("Player {0} got a total score of {1} during this tournament and its rank is {2}".format(player_name, player_total_score_at_tournament_scale, player_rank))


    def tournament_results_display_ending(self):
        print("===================CONGRATS ALL !===================")


    def information_for_updating_player_rank(self):
        """Asks which player is concerned by rank update, and which is the new rank value"""

        concerned_player_index = int(input("For which player do you want to update the rank ? Please write its index"))
        new_rank = int(input("What is the updated rank value, please ? "))

        return concerned_player_index, new_rank


    def information_for_displaying_tournament_players(self):
        """Asks information for displaying players of a tournament"""

        information_tournament = input("For which tournament do you want to display players ? Please write the name of the tournament")

        return information_tournament


    def display_all_tournaments(self, all_registered_tournaments):
        """Displays alltournaments"""

        for tournament in all_registered_tournaments:
            print("LIST OF ALL TOURNAMENTS")
            print("Tournament named {0}".format(tournament.name))
            print("    Was played in the city of: {0}".format(tournament.localisation))
            print("    Began on {0} and ended on {1} ".format(tournament.date_of_beginning, tournament.date_of_ending))
            print("    Time controler was: {0}".format(tournament.time_controler))
            print("    Description is as follows: {0}".format(tournament.description))


    def information_for_displaying_tournament_rounds_or_matches(self):
        """Asks information for displaying players of a tournament"""

        information_tournament = input("For which tournament do you want to display rounds or matches ? Please write the name of the tournament")

        return information_tournament


    def display_rounds(self, list_of_rounds):
        """Displays all rounds of a tournament"""

        for round in list_of_rounds: 
            print("Round named {0} began on {1} and ended on {2}".format(round.name, round.date_and_time_beginning, round.date_and_time_ending))


    def display_matches_result(self, matches_tuples_representation_list):
        """Displays all matches of a tournament"""

        for matches_tuples_representation in matches_tuples_representation_list:
            print()
            print("Round")            
            for match_tuple in matches_tuples_representation:
                print("")
                print("    Match result")
                print("    Player {0} played against {0}; results are as follows:".format(match_tuple[0][0].family_name, match_tuple[1][0].family_name))
                print("        Player {0} score of the match: {1}".format(match_tuple[0][0].family_name, match_tuple[0][1]))
                print("        Player {0} score of the match: {1}".format(match_tuple[1][0].family_name, match_tuple[1][1]))

    def even_players_alert():
        """Alerts the user that the number of players is event"""

        print("The number of players is even, pairs have not been created")


    def database_menu_choice(self):
        """Asks to the user which action he/she wants to do about the database"""

        database_menu_choice = input(
            "" "\n"
            "Database options " "\n"
            "What do you want to do ? " "\n"
            "If you want save all players of the program in the database, please write '1' " "\n"
            "If you want load all players from the database in the program, please write '2' " "\n"
            "If you want save all tournaments of the program in the database, please write '3' " "\n"
            "If you want load all tournaments from the database in the program, please write '4' " "\n"
            "If you want to return to the menu of the program, please write 'Exit' " "\n"
        )

        return database_menu_choice


    def database_action_confirmation(self):
        """Confirms that an action was well done about the tinydb database"""

        print("Confirmation, the action about the database has been performed")
