from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models import User


class ConsultarEsView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.incon()

    def incon(self):
        uic.loadUi('view/ui/consultarp.ui', self)
        self.show()
        self.burcarno.clicked.connect(lambda: self.bus())
        self.err_es.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_no.setVisible(False)

    def bus(self):
        self.err_es.setVisible(False)
        self.err_ma.setVisible(False)
        self.err_no.setVisible(False)

        try:
            codies = int(self.codiesc.text())

        except ValueError:
            self.err_es.setVisible(True)
            return

        mate = self.mateesc.text()

        if mate == "":
            self.err_ma.setVisible(True)
            return


        notes, err = User.get_notes(codies, mate, None)

        if not notes:
            if err == "student":
                self.err_es.setVisible(True)

            if err == "note":
                self.err_ma.setVisible(True)

            return

        corte1b = notes["court_1"]

        if not corte1b:
            self.err_no.setVisible(True)
            return

        self.c1.setText(str(round(corte1b,1)))

        corte2b = notes["court_2"]

        if not corte2b:
            self.err_no.setVisible(True)
            return

        self.c2.setText(str(round(corte2b,1)))

        corte3b = notes["court_3"]

        if not corte3b:
            self.err_no.setVisible(True)
            return

        self.c3.setText(str(round(corte3b,1)))

        nf = (corte1b*0.3)+(corte2b*0.3)+(corte3b*0.4)
        self.nf.setText(str(round(nf,1)))
