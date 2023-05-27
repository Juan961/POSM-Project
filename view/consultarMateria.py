from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models import Assigment


class ConsultarEsView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.incon()


    def incon(self):
        uic.loadUi('view/ui/consultarpes.ui', self)
        self.show()
        self.burcarno.clicked.connect(lambda: self.bus())
        self.err_code.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_notes.setVisible(False)


    def bus(self):
        self.err_code.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_notes.setVisible(False)

        try:
            codies = int(self.codiesc.text())

        except ValueError:
            self.err_es.setVisible(True)
            return

        mate = self.mateesc.text()

        if mate == "":
            self.err_ma.setVisible(True)
            return

        notes, err = Assigment.get_notes(None, mate, codies)

        if not notes:
            if err == "student":
                self.err_es.setVisible(True)
            else:
                self.err_es.setVisible(False)

            if err == "note":
                self.err_ma.setVisible(True)
            else:
                self.err_ma.setVisible(False)

            return


        corte1b = notes["court_1"]

        if not corte1b:
            self.err_notes.setVisible(True)
            return

        self.c1.setText(str(round(corte1b,1)))

        corte2b = notes["court_2"]

        if not corte1b:
            self.err_notes.setVisible(True)
            return

        self.c2.setText(str(round(corte2b,1)))

        corte3b = notes["court_3"]

        if not corte1b:
            self.err_notes.setVisible(True)
            return

        self.c3.setText(str(round(corte3b,1)))

        nf = (corte1b*0.3)+(corte2b*0.3)+(corte3b*0.4)
        self.nf.setText(str(round(nf,1)))
