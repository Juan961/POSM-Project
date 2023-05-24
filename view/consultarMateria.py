from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models import User


class ConsultarEsView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.incon()

    def incon(self):
        uic.loadUi('view/ui/consultarpes.ui',self)
        self.show()
        self.burcarno.clicked.connect(lambda: self.bus())
        self.err_es.setVisible(False)
        self.err_ma.setVisible(False)

    def bus(self):
        codies=int(self.codiesc.text())
        mate=self.mateesc.text()

        notes, err = User.get_notes(codies, mate)

        if not notes:
            print(err)

            if err == "student":
                self.err_es.setVisible(True)
            else:
                self.err_es.setVisible(False)

            if err == "note":
                self.err_ma.setVisible(True)
            else:
                self.err_ma.setVisible(False)

            return

        self.err_es.setVisible(False)
        self.err_ma.setVisible(False)

        corte1b = notes["court_1"]
        corte2b = notes["court_2"]
        corte3b = notes["court_3"]

        self.c1.setText(str(round(corte1b,1)))
        self.c2.setText(str(round(corte2b,1)))
        self.c3.setText(str(round(corte3b,1)))

        nf=(corte1b*0.3)+(corte2b*0.3)+(corte3b*0.4)
        self.nf.setText(str(round(nf,1)))