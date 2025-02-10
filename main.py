import facturas
import styles
import vendedores
from ventana_principal import *
import sys
import var
import clientes
from ventana_auxiliar import *
import conexion_server
import propiedades
import informes
import state_manager

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VentanaPrincipal()
        var.ui.setupUi(self)
        var.ui_calendar = Calendar()
        var.dlg_abrir = FileDialogAbrir()
        var.dlg_gestion_propiedad_tipo = DlgGestionPropiedadTipo()
        var.dlg_about = DlgAbout()
        var.dlg_buscar_propiedad = DlgBuscarPropiedad()
        var.clase_conexion = conexion.Conexion
        #var.clase_conexion = conexion_server.ConexionServer
        var.clase_conexion.db_conexion()
        var.state_manager = state_manager.StateManager()
        var.state_manager.initialize_state()
        self.setStyleSheet(styles.load_stylesheet())
        styles.initialize_styles()
        #conexionserver.ConexionServer.crear_conexion(self)
        eventos.Eventos.cargar_tabla_clientes()
        eventos.Eventos.cargar_tabla_propiedades()
        eventos.Eventos.cargar_tabla_vendedores()

        '''
        Zona de eventos de tablas
        '''
        eventos.Eventos.resize_cli_tab(self)
        var.ui.tab_cli.clicked.connect(clientes.Clientes.cargar_cliente)

        eventos.Eventos.resize_pro_tab(self)
        var.ui.tab_pro.clicked.connect(propiedades.Propiedades.cargar_propiedad)

        eventos.Eventos.resize_ven_tab(self)
        var.ui.tab_ven.clicked.connect(vendedores.Vendedores.cargar_vendedor)

        eventos.Eventos.resize_fac_tab(self)
        var.ui.tab_fac.clicked.connect(facturas.Facturas.cargar_factura)

        eventos.Eventos.resize_fac_ven_tab(self)
        var.ui.tab_fac_ven.clicked.connect(facturas.Facturas.cargar_venta)

        '''
        Zona de eventos del menubar
        '''
        var.ui.action_archivo_salir.triggered.connect(eventos.Eventos.mensaje_salir)
        var.ui.action_archivo_backup_crear.triggered.connect(eventos.Eventos.crear_backup)
        var.ui.action_archivo_backup_restaurar.triggered.connect(eventos.Eventos.restaurar_backup)
        var.ui.action_gestion_propiedades_tipo.triggered.connect(eventos.Eventos.abrir_dlg_propiedades_tipo)
        var.ui.action_listado_clientes.triggered.connect(informes.Informes.reportClientes)
        var.ui.action_listado_propiedades.triggered.connect(eventos.Eventos.abrir_dlg_buscar_propiedades)

        '''
        Zona eventos comprobaciones
        '''
        var.ui.txt_cli_email.editingFinished.connect(lambda: eventos.Eventos.observar_email(var.ui.txt_cli_email))
        var.ui.txt_cli_dni.editingFinished.connect(lambda: eventos.Eventos.observar_dni(var.ui.txt_cli_dni))
        var.ui.txt_cli_movil.editingFinished.connect(lambda: eventos.Eventos.observar_movil(var.ui.txt_cli_movil))
        var.ui.txt_cli_alta.editingFinished.connect(lambda: eventos.Eventos.observar_fecha_alta(var.ui.txt_cli_alta))
        var.ui.txt_cli_baja.editingFinished.connect(lambda: eventos.Eventos.observar_fecha_baja(var.ui.txt_cli_baja))

        var.ui.txt_pro_movil.editingFinished.connect(lambda: eventos.Eventos.observar_movil(var.ui.txt_pro_movil))
        var.ui.txt_pro_alta.editingFinished.connect(lambda: eventos.Eventos.observar_fecha_alta(var.ui.txt_pro_alta))
        var.ui.txt_pro_baja.editingFinished.connect(lambda: eventos.Eventos.observar_fecha_baja(var.ui.txt_pro_baja))
        var.ui.txt_pro_postal.editingFinished.connect(lambda: eventos.Eventos.observar_codigo_postal(var.ui.txt_pro_postal))
        var.ui.txt_pro_superficie.editingFinished.connect(lambda: eventos.Eventos.observar_superficie(var.ui.txt_pro_superficie))
        var.ui.txt_pro_precio_alquiler.editingFinished.connect(lambda: eventos.Eventos.observar_precio(var.ui.txt_pro_precio_alquiler))
        var.ui.txt_pro_precio_venta.editingFinished.connect(lambda: eventos.Eventos.observar_precio(var.ui.txt_pro_precio_venta))

        var.ui.txt_ven_email.editingFinished.connect(lambda: eventos.Eventos.observar_email(var.ui.txt_ven_email))
        var.ui.txt_ven_dni.editingFinished.connect(lambda: eventos.Eventos.observar_dni(var.ui.txt_ven_dni))
        var.ui.txt_ven_movil.editingFinished.connect(lambda: eventos.Eventos.observar_movil(var.ui.txt_ven_movil))
        var.ui.txt_ven_alta.editingFinished.connect(lambda: eventos.Eventos.observar_fecha_alta(var.ui.txt_ven_alta))
        var.ui.txt_ven_baja.editingFinished.connect(lambda: eventos.Eventos.observar_fecha_baja(var.ui.txt_ven_baja))

        var.ui.txt_fac_alta.editingFinished.connect(lambda: eventos.Eventos.observar_fecha_baja(var.ui.txt_fac_alta))

        '''
        Zona eventos botones
        '''
        var.ui.btn_cli_grabar.clicked.connect(clientes.Clientes.alta_cliente)
        var.ui.btn_cli_modificar.clicked.connect(clientes.Clientes.modificar_cliente)
        var.ui.btn_cli_eliminar.clicked.connect(clientes.Clientes.baja_cliente)
        var.ui.btn_cli_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(0))
        var.ui.btn_cli_baja.clicked.connect(lambda: eventos.Eventos.abrir_calendar(1))
        var.ui.btn_cli_buscar.clicked.connect(clientes.Clientes.buscar_cliente)
        
        var.ui.btn_pro_grabar.clicked.connect(propiedades.Propiedades.alta_propiedad)
        var.ui.btn_pro_modificar.clicked.connect(propiedades.Propiedades.modificar_propiedad)
        var.ui.btn_pro_eliminar.clicked.connect(propiedades.Propiedades.baja_propiedad)
        var.ui.btn_pro_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(0))
        var.ui.btn_pro_baja.clicked.connect(lambda: eventos.Eventos.abrir_calendar(1))

        var.ui.btn_ven_grabar.clicked.connect(vendedores.Vendedores.alta_vendedor)
        var.ui.btn_ven_modificar.clicked.connect(vendedores.Vendedores.modificar_vendedor)
        var.ui.btn_ven_eliminar.clicked.connect(vendedores.Vendedores.baja_vendedor)
        var.ui.btn_ven_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(0))
        var.ui.btn_ven_baja.clicked.connect(lambda: eventos.Eventos.abrir_calendar(1))

        var.ui.btn_fac_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(0))
        var.ui.btn_fac_grabar.clicked.connect(facturas.Facturas.alta_factura)
        var.ui.btn_fac_ven_grabar.clicked.connect(facturas.Facturas.alta_venta)

        var.ui.btn_cli_anterior.clicked.connect(eventos.Eventos.retroceder_pagina_cliente)
        var.ui.btn_cli_siguiente.clicked.connect(eventos.Eventos.avanzar_pagina_cliente)

        var.ui.btn_pro_anterior.clicked.connect(eventos.Eventos.retroceder_pagina_propiedad)
        var.ui.btn_pro_siguiente.clicked.connect(eventos.Eventos.avanzar_pagina_propiedad)

        var.ui.btn_alq_contrato_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(0))
        var.ui.btn_alq_contrato_baja.clicked.connect(lambda: eventos.Eventos.abrir_calendar(1))
        var.ui.btn_alq_alta.clicked.connect(lambda: eventos.Eventos.abrir_calendar(2))

        '''
        Zona eventos combox
        '''
        eventos.Eventos.cargar_provincias(var.ui.cmb_cli_provincia)
        eventos.Eventos.cargar_municipios(var.ui.cmb_cli_municipio)
        var.ui.cmb_cli_provincia.currentIndexChanged.connect(lambda:
            eventos.Eventos.cargar_municipios(var.ui.cmb_cli_municipio, var.ui.cmb_cli_provincia.itemData(var.ui.cmb_cli_provincia.currentIndex())))

        eventos.Eventos.cargar_provincias(var.ui.cmb_pro_provincia)
        eventos.Eventos.cargar_municipios(var.ui.cmb_pro_municipio)
        eventos.Eventos.cargar_propiedad_tipos(var.ui.cmb_pro_tipo)
        var.ui.cmb_pro_provincia.currentIndexChanged.connect(lambda:
            eventos.Eventos.cargar_municipios(var.ui.cmb_pro_municipio, var.ui.cmb_pro_provincia.itemData(var.ui.cmb_pro_provincia.currentIndex())))

        eventos.Eventos.cargar_provincias(var.ui.cmb_ven_provincia)

        '''
        Zona eventos toolbar
        '''
        var.ui.action_tool_salir.triggered.connect(eventos.Eventos.mensaje_salir)
        var.ui.action_tool_limpiar.triggered.connect(eventos.Eventos.limpiar_panel)
        
        var.ui.action_tool_gestionar_tipos_propiedad.triggered.connect(eventos.Eventos.abrir_dlg_propiedades_tipo)
        var.ui.action_tool_filtrar_propiedades.triggered.connect(propiedades.Propiedades.filtrar_propiedades)
        var.ui.action_exportar_propiedades_CSV.triggered.connect(eventos.Eventos.exportar_propiedades_csv)
        var.ui.action_exportar_propiedades_JSON.triggered.connect(eventos.Eventos.exportar_propiedades_json)

        var.ui.action_abrir_about.triggered.connect(eventos.Eventos.abrir_dlg_about)

        '''
        Zona eventos checkbox
        '''
        var.ui.chk_cli_historico.stateChanged.connect(lambda: var.state_manager.change_state("historico_cli", var.ui.chk_cli_historico.isChecked()))
        var.ui.chk_pro_historico.stateChanged.connect(lambda: var.state_manager.change_state("historico_pro", var.ui.chk_pro_historico.isChecked()))
        var.ui.chk_ven_historico.stateChanged.connect(lambda: var.state_manager.change_state("historico_ven", var.ui.chk_ven_historico.isChecked()))

        var.ui.chk_pro_alquiler.stateChanged.connect(lambda: eventos.Eventos.observar_checkbox(var.ui.chk_pro_alquiler))
        var.ui.chk_pro_venta.stateChanged.connect(lambda: eventos.Eventos.observar_checkbox(var.ui.chk_pro_venta))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())