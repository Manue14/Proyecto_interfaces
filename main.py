import conexion
import eventos
import styles
from ventana_principal import *
import sys
import var
import clientes
from ventana_auxiliar import *
import conexion_server
import propiedades

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VentanaPrincipal()
        var.ui.setupUi(self)
        var.ui_calendar = Calendar()
        var.dlg_abrir = FileDialogAbrir()
        var.dlg_gestion_propiedad_tipo = DlgGestionPropiedadTipo()
        self.setStyleSheet(styles.load_stylesheet())
        styles.initialize_styles()
        conexion.Conexion.db_conexion(self)
        var.historico_cli = 1
        var.historico_pro = 1
        #conexionserver.ConexionServer.crear_conexion(self)
        clientes.Clientes.cargar_cli_tab()
        propiedades.Propiedades.cargar_pro_tab()

        '''
        Zona de eventos de tablas
        '''
        eventos.Eventos.resize_cli_tab(self)
        var.ui.tab_cli.clicked.connect(clientes.Clientes.cargar_cliente)
        eventos.Eventos.resize_pro_tab(self)
        var.ui.tab_pro.clicked.connect(propiedades.Propiedades.cargar_propiedad)

        '''
        Zona de eventos del menubar
        '''
        var.ui.action_archivo_salir.triggered.connect(eventos.Eventos.mensaje_salir)
        var.ui.action_archivo_backup_crear.triggered.connect(eventos.Eventos.crear_backup)
        var.ui.action_archivo_backup_restaurar.triggered.connect(eventos.Eventos.restaurar_backup)
        var.ui.action_gestion_propiedades_tipo.triggered.connect(eventos.Eventos.abrir_dlg_propiedades_tipo)

        '''
        Zona eventos comprobaciones
        '''
        var.ui.txt_cli_email.editingFinished.connect(clientes.Clientes.validar_email)
        var.ui.txt_cli_dni.editingFinished.connect(clientes.Clientes.validar_dni)
        var.ui.txt_cli_movil.editingFinished.connect(clientes.Clientes.validar_movil)
        var.ui.txt_cli_alta.editingFinished.connect(clientes.Clientes.validar_fecha_alta)
        var.ui.txt_cli_baja.editingFinished.connect(clientes.Clientes.validar_fecha_baja)

        var.ui.txt_pro_movil.editingFinished.connect(propiedades.Propiedades.validar_movil)
        var.ui.txt_pro_alta.editingFinished.connect(propiedades.Propiedades.validar_fecha_alta)
        var.ui.txt_pro_baja.editingFinished.connect(propiedades.Propiedades.validar_fecha_baja)
        var.ui.txt_pro_postal.editingFinished.connect(propiedades.Propiedades.validar_postal)
        var.ui.txt_pro_superficie.editingFinished.connect(propiedades.Propiedades.validar_superficie)
        var.ui.txt_pro_precio_alquiler.editingFinished.connect(propiedades.Propiedades.validar_precio_alquiler)
        var.ui.txt_pro_precio_venta.editingFinished.connect(propiedades.Propiedades.validar_precio_venta)

        '''
        Zona eventos botones
        '''
        var.ui.btn_cli_grabar.clicked.connect(clientes.Clientes.alta_cliente)
        var.ui.btn_cli_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(0))
        var.ui.btn_cli_baja.clicked.connect(lambda: eventos.Eventos.abrir_calendar(1))
        var.ui.btn_pro_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(0))
        var.ui.btn_pro_baja.clicked.connect(lambda: eventos.Eventos.abrir_calendar(1))
        var.ui.btn_cli_modificar.clicked.connect(clientes.Clientes.modificar_cliente)
        var.ui.btn_cli_eliminar.clicked.connect(clientes.Clientes.baja_cliente)
        var.ui.btn_pro_grabar.clicked.connect(propiedades.Propiedades.alta_propiedad)
        var.ui.btn_pro_modificar.clicked.connect(propiedades.Propiedades.modificar_propiedad)
        var.ui.btn_pro_eliminar.clicked.connect(propiedades.Propiedades.baja_propiedad)

        '''
        Zona eventos combox
        '''
        eventos.Eventos.cargar_provincias(self)
        eventos.Eventos.cargar_municipios_cli(self)
        eventos.Eventos.cargar_municipios_pro(self)
        var.ui.cmb_cli_provincia.currentIndexChanged.connect(lambda: eventos.Eventos.cargar_municipios_cli(self, var.ui.cmb_cli_provincia.itemData(var.ui.cmb_cli_provincia.currentIndex())))
        var.ui.cmb_pro_provincia.currentIndexChanged.connect(lambda: eventos.Eventos.cargar_municipios_pro(self, var.ui.cmb_pro_provincia.itemData(var.ui.cmb_pro_provincia.currentIndex())))
        eventos.Eventos.cargar_propiedad_tipos(var.ui.cmb_pro_tipo)

        '''
        Zona eventos toolbar
        '''
        var.ui.action_tool_salir.triggered.connect(eventos.Eventos.mensaje_salir)
        var.ui.action_tool_limpiar.triggered.connect(eventos.Eventos.limpiar_panel)
        var.ui.action_tool_gestionar_tipos_propiedad.triggered.connect(eventos.Eventos.abrir_dlg_propiedades_tipo)
        var.ui.action_tool_filtrar_propiedades.triggered.connect(propiedades.Propiedades.filtrar_propiedades)
        var.ui.action_exportar_propiedades_CSV.triggered.connect(eventos.Eventos.exportar_propiedades_csv)
        var.ui.action_exportar_propiedades_JSON.triggered.connect(eventos.Eventos.exportar_propiedades_json)

        '''
        Zona eventos checkbox
        '''
        var.ui.chk_cli_historico.stateChanged.connect(clientes.Clientes.set_historico_cliente)
        var.ui.chk_pro_historico.stateChanged.connect(propiedades.Propiedades.set_historico_propiedad)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())