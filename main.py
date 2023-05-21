import sys


from PyQt5.QtWidgets import QApplication


from view import Main


def main():
    try:
        app = QApplication(sys.argv)
        _ = Main()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
