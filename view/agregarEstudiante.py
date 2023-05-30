from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models import User


class AgregarEsView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inagre()


    def inagre(self):
        uic.loadUi('view/ui/agregarestu.ui', self)
        self.show()
        self.agregarno.clicked.connect(lambda: self.calno())
        self.err_es.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_no.setVisible(False)


    def calno(self):
        self.err_es.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_no.setVisible(False)

        try:
            codies = int(self.codiestu.text())

        except ValueError:
            self.err_es.setVisible(True)
            return

        mate = self.matees.text()

        if mate == "":
            self.err_ma.setVisible(True)
            return

        try:
            labo=float(self.lab.text())
            Proy=float(self.pro.text())
            Parc=float(self.par.text())

        except ValueError:
            self.err_no.setVisible(True)
            return
            
        if self.corte1.isChecked():
            note = (labo*(1/3))+(Proy*1/3)+(Parc*1/3)
            court = 1

        elif self.corte2.isChecked():
            note = (labo*(1/3))+(Proy*1/3)+(Parc*1/3)
            court = 2

        else:
            note = (labo*(1/4))+(Proy*1/4)+(Parc*2/4)
            court = 3

        self.notac.setText(str(round(note,1)))

        User.add_note_professor(codies, mate, note, court)
