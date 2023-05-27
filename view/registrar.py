from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models import User


class RegistrarView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/ui/registrarse.ui', self)
        self.show()
        self.inregis()


    def inregis(self):
        self.err_us.setVisible(False)
        self.err_code.setVisible(False)
        self.err_no.setVisible(False)
        self.registrar.clicked.connect(lambda: self.crearu())
        self.login_btn.clicked.connect(lambda: self.login())


    def crearu(self):
        self.err_us.setVisible(False)
        self.err_code.setVisible(False)
        self.err_no.setVisible(False)

        nombre = self.nombre.text()

        if nombre == "":
            self.err_no.setVisible(True)
            return

        try:
            codi = int(self.codigo.text())

        except ValueError:
            self.err_code.setVisible(True)
            return

        if self.profesor.isChecked():
            rol='PROFESSOR'

        else:
            rol='STUDENT'

        user = User.get_user(codi)

        if user:
            self.err_us.setVisible(True)
            return

        User(codi,nombre,rol)
        self.close()


    def login(self):
        self.close()
