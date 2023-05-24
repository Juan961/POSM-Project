from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models import User


class AgregarEsView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inagre()

    def inagre(self):
        uic.loadUi('view/ui/agrgarmateria.ui',self)
        self.show()
        self.agregarno.clicked.connect(lambda: self.calno())

    def calno(self):
        codies=int(self.codiestu.text())
        mate=self.matees.text()
        labo=float(self.lab.text())
        Proy=float(self.pro.text())
        Parc=float(self.par.text())

        if self.corte1.isChecked()==True:
            nota = (labo*(1/3))+(Proy*1/3)+(Parc*1/3)
            corte = 1

        elif self.corte2.isChecked()==True:
            nota=(labo*(1/3))+(Proy*1/3)+(Parc*1/3)
            corte = 2

        else:
            nota=(labo*(1/4))+(Proy*1/4)+(Parc*2/4)
            corte = 3

        self.notac.setText(str(round(nota,1)))
        User.add_note(codies, mate, nota, corte)
