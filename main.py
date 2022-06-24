"""Entry point."""


from views.base import View
from controllers.base import Controller
# from models.X import X --> si besoin d'un modele dans le controleur, comme un jeu de carte par exemple
# on le fournira au controller comme argument pour l'instantiation avec def __init__ : comme la vue.


def main():
    viewInstance = View()
    controller = Controller(viewInstance)
    controller.run()


if __name__ == "__main__":
    main()
