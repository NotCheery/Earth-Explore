#Main file that executes the game, run the files here

#bring files here
from menu import show_menu
from game import run_game

def start_game():
    run_game() #run the pygame file

if __name__ == "__main__": #good python practice
    show_menu(start_game_callback=start_game)