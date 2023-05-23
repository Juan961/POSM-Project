from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models import User


class RegistrarView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/ui/registrarse.ui',self)
        self.show()
        self.inregis()

    def inregis(self):
        self.registrar.clicked.connect(lambda: self.crearu())

    def crearu(self):
        nombre=self.nombre.text()
        codi=int(self.codigo.text())

        if self.profesor.isChecked():
            rol='PROFESSOR'

        else:
            rol='STUDENT'

        User(codi,nombre,rol)
        self.close()
