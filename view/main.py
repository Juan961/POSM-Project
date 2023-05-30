from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from .registrar import RegistrarView
from .ingresar import IngresarView
from .ingresares import IngresarViewEs

from models import User


class MainView(QMainWindow):
    def __init__(self) -> None:
        super(MainView, self).__init__()
        uic.loadUi('view/ui/ingresarui.ui', self)
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        self.ingresar.clicked.connect(lambda: self.ing())
        self.registrarse.clicked.connect(lambda: self.regis())
        self.err_us.setVisible(False)


    def ing(self):
        self.err_us.setVisible(False)

        try:
            cod=int(self.codigo.text())

        except ValueError:
            self.err_us.setVisible(True)
            return

        if User.login(cod)==None:
            self.err_us.setVisible(True)
            return 

        user = User.get_user(cod)

        if user["role"] == "PROFESSOR":
            IngresarView()

        elif user["role"] == "STUDENT":
            IngresarViewEs()


    def regis(self):
        viewregistrar= RegistrarView()
        viewregistrar.show()
