from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


from models import Student, Professor, Assigment
from utils.exception import ModelNotFound


class StudentView(QMainWindow):
    def __init__(self) -> None:
        super(StudentView, self).__init__()
        uic.loadUi('view/soyestudiante/notasMate.ui', self)
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        self.pushButton.clicked.connect(self.handle_first_quarter)
        self.pushButton_2.clicked.connect(self.handle_second_quarter)
        self.pushButton_3.clicked.connect(self.handle_third_quarter)
        self.pushButton_4.clicked.connect(self.handle_final_notes)


    def handle_first_quarter(self):
        self.first_quarter = FirstQuarter()
        self.first_quarter.show()


    def handle_second_quarter(self):
        self.second_quarter = SecondQuarter()
        self.second_quarter.show()


    def handle_third_quarter(self):
        self.third_quarter = ThirdQuarter()
        self.third_quarter.show()


    def handle_final_notes(self):
        self.final = FinalNotes()
        self.final.show()


    def handle_exit(self):
        QApplication.quit()


class FirstQuarter(QMainWindow):
    def __init__(self) -> None:
        super(FirstQuarter, self).__init__()
        uic.loadUi('view/soyestudiante/Corte1E.ui', self)
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        self.pushButton.clicked.connect(self.handle_calculate)
        self.pushButton_2.clicked.connect(self.handle_go_back)

        # Test
        self.plainTextEdit_4.setPlainText("Matemáticas")
        self.plainTextEdit.setPlainText("4.0")
        self.plainTextEdit_2.setPlainText("4.0")
        self.plainTextEdit_3.setPlainText("4.0")


    def handle_calculate(self):
        assigment_name = self.plainTextEdit_4.toPlainText()
        try:
            laboratory_note = float( self.plainTextEdit.toPlainText() )
            project_note = float( self.plainTextEdit_2.toPlainText() )
            partial_note = float( self.plainTextEdit_3.toPlainText() )

        except ValueError:
            print("Value not valid is not float")

        total_note = (laboratory_note + project_note + partial_note) / 3

        self.textBrowser.setPlainText( str( round( total_note, 4 ) ) )


    def handle_go_back(self):
        self.close()


class SecondQuarter(QMainWindow):
    def __init__(self) -> None:
        super(SecondQuarter, self).__init__()
        uic.loadUi('view/soyestudiante/Corte2E.ui', self)
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        self.pushButton.clicked.connect(self.handle_calculate)
        self.pushButton_2.clicked.connect(self.handle_go_back)

        # Test
        self.plainTextEdit_4.setPlainText("Matemáticas")
        self.plainTextEdit.setPlainText("4.0")
        self.plainTextEdit_2.setPlainText("4.0")
        self.plainTextEdit_3.setPlainText("4.0")


    def handle_calculate(self):
        assigment_name = self.plainTextEdit_4.toPlainText()
        try:
            laboratory_note = float( self.plainTextEdit.toPlainText() )
            project_note = float( self.plainTextEdit_2.toPlainText() )
            partial_note = float( self.plainTextEdit_3.toPlainText() )

        except ValueError:
            print("Value not valid is not float")

        total_note = (laboratory_note + project_note + partial_note) / 3

        self.textBrowser.setPlainText( str( round( total_note, 4 ) ) )


    def handle_go_back(self):
        self.close()


class ThirdQuarter(QMainWindow):
    def __init__(self) -> None:
        super(ThirdQuarter, self).__init__()
        uic.loadUi('view/soyestudiante/Corte3E.ui', self)
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        self.pushButton.clicked.connect(self.handle_calculate)
        self.pushButton_2.clicked.connect(self.handle_go_back)

        # Test
        self.plainTextEdit_4.setPlainText("Matemáticas")
        self.plainTextEdit.setPlainText("4.0")
        self.plainTextEdit_2.setPlainText("4.0")
        self.plainTextEdit_3.setPlainText("4.0")


    def handle_calculate(self):
        assigment_name = self.plainTextEdit_4.toPlainText()
        try:
            laboratory_note = float( self.plainTextEdit.toPlainText() )
            project_note = float( self.plainTextEdit_2.toPlainText() )
            partial_note = float( self.plainTextEdit_3.toPlainText() )

        except ValueError:
            print("Value not valid is not float")

        total_note = (laboratory_note + project_note + partial_note) / 3

        self.textBrowser.setPlainText( str( round( total_note, 4 ) ) )


    def handle_go_back(self):
        self.close()


class FinalNotes(QMainWindow):
    def __init__(self) -> None:
        super(FinalNotes, self).__init__()
        uic.loadUi('view/soyestudiante/NotaFinalE.ui', self)
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        self.pushButton.clicked.connect(self.handle_search)
        self.pushButton_2.clicked.connect(self.handle_go_back)

        # Test
        self.textEdit.setPlainText("Matemáticas")

    def handle_search(self):
        assigment_name = self.textEdit.toPlainText()

        # Search

        # Test
        assigment = { "first": 5.0, "second": 5.0, "third": 0.0 }

        first_note = assigment["first"]
        second_note = assigment["second"]
        third_note = assigment["third"]

        self.textBrowser.setPlainText( str( first_note ) )
        self.textBrowser_2.setPlainText( str( second_note ) )
        self.textBrowser_3.setPlainText( str( third_note ) )

        total_note = ( first_note * 0.3 ) + ( second_note * 0.3 )  + ( third_note * 0.4 )

        self.textBrowser_4.setPlainText( str( round( total_note, 4 ) ) )


    def handle_go_back(self):
        self.close()
