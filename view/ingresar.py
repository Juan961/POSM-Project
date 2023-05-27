from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from .agregarEstudiante import AgregarEsView
from .consultarEstudiante import ConsultarEsView


class IngresarView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/ui/despuesdeingre.ui', self)
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
