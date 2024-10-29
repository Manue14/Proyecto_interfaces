import conexion
import eventos
import styles
from venPrincipal import *
import sys
import var
import clientes
from venAux import *
import conexionserver
import propiedades

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        var.dlgabrir = FileDialogAbrir()
        var.dlggestion = dlgGestionprop()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        var.historico = 1
        #conexionserver.ConexionServer.crear_conexion(self)
        clientes.Clientes.cargaTablaClientes(self)

        '''
        Zona de eventos de tablas
        '''
        eventos.Eventos.resizeTablaClientes(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargaOneCliente)
        eventos.Eventos.resizeTablaPropiedades(self)

        '''
        Zona de eventos del menubar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restaurarBackup)
        var.ui.actionTipo_Propiedades.triggered.connect(eventos.Eventos.abrirTipoprop)

        '''
        Zona eventos comprobaciones
        '''
        var.ui.txtEmailcli.editingFinished.connect(clientes.Clientes.checkEmail)
        var.ui.txtDnicli.editingFinished.connect(clientes.Clientes.checkDni)
        var.ui.txtMovilcli.editingFinished.connect(clientes.Clientes.checkPhone)

        '''
        Zona eventos botones
        '''
        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0))
        var.ui.btnBajacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(1))
        var.ui.btnFechaprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0))
        var.ui.btnFechabajaprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(1))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelcli.clicked.connect(clientes.Clientes.bajaCliente)
        var.ui.btnGrabarprop.clicked.connect(propiedades.Propiedades.altaPropiedad)

        '''
        Zona eventos combox
        '''
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargar_muni_cli(self)
        var.ui.cmbProcli.currentIndexChanged.connect(lambda: eventos.Eventos.cargar_muni_cli(self, var.ui.cmbProcli.itemData(var.ui.cmbProcli.currentIndex())))
        eventos.Eventos.cargarTipoprop(self)

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