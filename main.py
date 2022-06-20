"""Entry point."""
#l’affichage (et en partie, de la réception) des données à destination (ou en provenance) de l’utilisateur.

from views.base import View
from controllers.base import Controller
# from models.X import X --> si besoin d'un modele, comme un jeu de carte par exemple; on le fournira au controller 
# comme argument pour l'instantiation avec def __init__


def main():
    viewInstance = View()
    controller = Controller(viewInstance)
    controller.run()


if __name__ == "__main__":
    main()
