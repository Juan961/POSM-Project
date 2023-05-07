from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


from .student import StudentView
from .professor import ProfessorView


class MainView(QMainWindow):
    def __init__(self) -> None:
        super(MainView, self).__init__()
        uic.loadUi('view/inicio.ui', self)
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        self.pushButton.clicked.connect(self.handle_professor_view)
        self.pushButton_2.clicked.connect(self.handle_student_view)
        self.pushButton_3.clicked.connect(self.handle_exit)


    def handle_professor_view(self):
        self.profesor_view = ProfessorView()


    def handle_student_view(self):
        self.student_view = StudentView()


    def handle_exit(self):
        QApplication.quit()
