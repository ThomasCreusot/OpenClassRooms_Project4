"""Entry point."""


from views.base import View
from controllers.base import Controller


def main():
    viewInstance = View()
    controller = Controller(viewInstance)
    controller.run()


if __name__ == "__main__":
    main()
