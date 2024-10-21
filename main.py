import conexion
import eventos
import styles
from venPrincipal import *
import sys
import var
import clientes
from venAux import *
import conexionserver

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        var.dlgabrir = FileDialogAbrir()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        var.historico = 0
        #conexionserver.ConexionServer.crear_conexion(self)
        clientes.Clientes.cargaTablaClientes(self)

        '''
        Zona de eventos de tablas
        '''
        eventos.Eventos.resizeTablaClientes(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargaOneCliente)
        '''
        Zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restaurarBackup)
        '''
        Zona eventos comprobaciones
        '''
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text)) #to-change parameter use
        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDni()) #to-change parameter use

        '''
        Zona eventos botones
        '''
        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 0))
        var.ui.btnBajacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 1))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelcli.clicked.connect(clientes.Clientes.bajaCliente)
        '''
        Zona eventos combox
        '''
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargar_muni_cli(self)
        var.ui.cmbProcli.currentIndexChanged.connect(lambda: eventos.Eventos.cargar_muni_cli(self, var.ui.cmbProcli.itemData(var.ui.cmbProcli.currentIndex())))

        '''
        Zona eventos toolbar
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionbarLimpiar.triggered.connect(eventos.Eventos.limpiarPanel)

        '''
        Zona eventos checkbox
        '''
        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())