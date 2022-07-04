# OpenClassRooms_Project4
Develop a program software in Python


# Project presentation
The present project is the fourth one of the training course *Python Application Developer*, offered by OpenClassRooms and aims to *Develop a program software with Python*.

The main goal is to develop an **offline program** wich allows to **manage and record chess tournaments**.
This program must:
-follow the **MVC (Model, View, Controller) design pattern**
-allow to **save and load data in/from a database** (use of tinyDB)
-be compliant with **PEP8**

When executed, the program invites the user to : 
-Create a tournament
-Create a player
-Associate a player within a tournament
-Play a tournament (see Note, hereunder)
-Update a player rank
-Display players (all players, or players of a specific tournament; sorted by name or by rank)
-Display all tournaments, all rounds of a tournament or all matches of a tournament
-Access the database options: save or load players and/or tournament data

Note about tournaments: the tournaments organisation follows the *"Swiss tournament system"* which is as follows:
-For the first round: players are sorted by their rank. The list of players is separated in two halves: the higher one and the lower one.
The best player of the higher half plays against the best player of the lower one. The second player of the higher half plays against the second player of the lower one, and so on.
-For the next rounds: at the beginning of the round, players are sorted by their number of points. If several players got the same number of points, they are sorted by their rank. The first player plays against the second one; the third player plays against the fourth one, and so on. However, there is an exception : if the first player already played against the second one; the first player will play against the third one.


# Project execution
To correctly execute the program, you need to activate the associated virtual environment which has been recorded in the ‘requirements.txt’ file.

## To create and activate the virtual environment 
Please follow theses instructions:

1. Open your Shell 
-Windows: 
*windows + R* 
> *cmd*  
-Mac: 
*Applications > Utilitaires > Terminal.app*

2. Find the folder which contains the program (with *cd* command)

3. Create a virtual environment: write the following command in the console
*python -m venv env*

4. Activate this virtual environment : 
-Linux or Mac: write the following command in the console
*source env/bin/activate*
-Windows: write the following command in the console 
*env\Scripts\activate.bat*

5. Install the python packages recorded in the *requirements.txt* file : write in the console the following command
*pip install -r requirements.txt*

## To execute the program
Please follow this instruction
6. Execute the code : write the following command in the console (Python must be installed on your computer and virtual environment must be activated)
*python main.py*


# Flake8 report generation
Please follow theses instructions:
1. Open your shell, find the folder which contains the program, and activate the virtual environment (see instructions above)
2. Execute the code : write the following command in the console
*flake8 --max-line-length 119 --format=html --htmldir=flake-report --exclude env*
3. The report has been generated in the 'flake-report' folder, which is located at the same location than the programm.
