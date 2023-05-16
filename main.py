import sys


from PyQt5.QtWidgets import QApplication


from view import Main

from models import User

def main():
    try:
        # app = QApplication(sys.argv)
        # _ = Main()
        # sys.exit(app.exec_())

        user = User("99461", "Juan", "STUDENT")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
