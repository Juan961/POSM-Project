from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from .agregarMateria import AgregarEsView
from .consultarMateria import ConsultarEsView


class IngresarViewEs(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/ui/despuesdeingreestu.ui', self)
        self.show()
        self.inres()

    def inres(self):
        self.agregar.clicked.connect(lambda: self.agre())
        self.consul.clicked.connect(lambda: self.con())

    def agre(self):
        viewagregar=AgregarEsView()
        viewagregar.show()

    def con(self):
        viewconsul=ConsultarEsView()
        viewconsul.show()