import conexion
import eventos
import styles
from venPrincipal import *
import sys
import var
import clientes
from venPrincipal import *
from venAux import *

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        eventos.Eventos.dniTextBoxChecker(self)

        '''
        Zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)

        '''
        Zona eventos comprobaciones
        '''
        var.ui.txtEmailCli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailCli.text))
        '''
        Zona eventos botones
        '''
        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0))

        '''
        Zona eventos combox
        '''
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargar_muni_cli(self)
        var.ui.cmbProcli.currentIndexChanged.connect(lambda: eventos.Eventos.cargar_muni_cli(self, var.ui.cmbProcli.itemData(var.ui.cmbProcli.currentIndex())))
        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())