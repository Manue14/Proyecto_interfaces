import var
import eventos
import clientes
import propiedades
import conexion
import styles

class StateManager:
    state = {
        "historico_cli": False,
        "historico_pro": False,
        "historico_ven": False,
        "cliente_query_object": [],
        "propiedad_query_object": [],
        "vendedor_query_object": [],
        "factura_query_object": [],
        "precio_alquiler_propiedad": False,
        "precio_venta_propiedad": False,
        "check_alquiler_propiedad": False,
        "check_venta_propiedad": False,
        "current_cli_pagina": 0,
        "cliente_pagination": 20,
        "current_pro_pagina": 0,
        "propiedad_pagination": 10,
        "last_cliente_function": conexion.Conexion.listar_clientes,
        "last_cliente_params": [],
        "last_propiedad_function": conexion.Conexion.listar_propiedades,
        "last_propiedad_params": [],
        "last_vendedor_function": conexion.Conexion.listar_vendedores,
        "last_vendedor_params": [],
        "last_factura_function": conexion.Conexion.listar_facturas,
        "last_factura_params": [],
    }

    @staticmethod
    def change_state(key, value):
        try:
            StateManager.state[key] = value

            if (key == "current_cli_pagina" or key == "cliente_query_object"):
                eventos.Eventos.cargar_tabla_clientes()
                if (StateManager.state["current_cli_pagina"] == 0):
                    var.ui.btn_cli_anterior.setEnabled(False)
                else:
                    var.ui.btn_cli_anterior.setEnabled(True)
                if (StateManager.state["current_cli_pagina"] ==
                    int(len(StateManager.state["cliente_query_object"]) / StateManager.state["cliente_pagination"])
                        or
                        (StateManager.state["current_cli_pagina"] + 1 ==
                         int(len(StateManager.state["cliente_query_object"]) / StateManager.state["cliente_pagination"])
                            and
                            len(StateManager.state["cliente_query_object"]) % StateManager.state["cliente_pagination"] == 0)
                ):
                    var.ui.btn_cli_siguiente.setEnabled(False)
                else:
                    var.ui.btn_cli_siguiente.setEnabled(True)

            elif (key == "historico_cli" or key == "last_cliente_function"):
                StateManager.update_tabla_clientes()

            elif (key == "current_pro_pagina" or key == "propiedad_query_object"):
                eventos.Eventos.cargar_tabla_propiedades()
                if (StateManager.state["current_pro_pagina"] == 0):
                    var.ui.btn_pro_anterior.setEnabled(False)
                else:
                    var.ui.btn_pro_anterior.setEnabled(True)
                if (StateManager.state["current_pro_pagina"] ==
                    int(len(StateManager.state["propiedad_query_object"]) / StateManager.state["propiedad_pagination"])
                        or
                        (StateManager.state["current_pro_pagina"] + 1 ==
                         int(len(StateManager.state["propiedad_query_object"]) / StateManager.state["propiedad_pagination"])
                            and
                         len(StateManager.state["propiedad_query_object"]) % StateManager.state["propiedad_pagination"] == 0)
                ):
                    var.ui.btn_pro_siguiente.setEnabled(False)
                else:
                    var.ui.btn_pro_siguiente.setEnabled(True)

            elif (key == "historico_pro" or key == "last_propiedad_function"):
                StateManager.update_tabla_propiedades()

            elif (key == "precio_alquiler_propiedad" or key == "precio_venta_propiedad"
            or key == "check_alquiler_propiedad" or key == "check_venta_propiedad"):
                StateManager.update_propiedad_fields_state()

            elif (key == "last_vendedor_function"):
                eventos.Eventos.cargar_tabla_vendedores()

            elif (key == "historico_ven" or key == "last_vendedor_function"):
                StateManager.update_tabla_vendedores()

            elif (key == "last_factura_function"):
                StateManager.update_tabla_facturas()

        except Exception as e:
            print(e)

    def update_propiedad_fields_state():
        propiedades.Propiedades.inicializar_campos()

        if StateManager.state["precio_alquiler_propiedad"] == True:
            propiedades.Propiedades.campos["check_alquiler"].setEnabled(True)
            if StateManager.state["check_alquiler_propiedad"] == True:
                propiedades.Propiedades.campos["radio_alquilado"].setEnabled(True)
            else:
                propiedades.Propiedades.campos["radio_alquilado"].setEnabled(False)
                propiedades.Propiedades.campos["radio_alquilado"].setChecked(False)
        else:
            propiedades.Propiedades.campos["check_alquiler"].setEnabled(False)
            propiedades.Propiedades.campos["check_alquiler"].setChecked(False)
            propiedades.Propiedades.campos["radio_alquilado"].setEnabled(False)
            propiedades.Propiedades.campos["radio_alquilado"].setChecked(False)
            if not propiedades.Propiedades.campos["radio_vendido"].isChecked():
                propiedades.Propiedades.campos["radio_disponible"].setChecked(True)

        if StateManager.state["precio_venta_propiedad"] == True:
            propiedades.Propiedades.campos["check_venta"].setEnabled(True)
            if StateManager.state["check_venta_propiedad"] == True:
                propiedades.Propiedades.campos["radio_vendido"].setEnabled(True)
            else:
                propiedades.Propiedades.campos["radio_vendido"].setEnabled(False)
                propiedades.Propiedades.campos["radio_vendido"].setChecked(False)
        else:
            propiedades.Propiedades.campos["check_venta"].setEnabled(False)
            propiedades.Propiedades.campos["check_venta"].setChecked(False)
            propiedades.Propiedades.campos["radio_vendido"].setEnabled(False)
            propiedades.Propiedades.campos["radio_vendido"].setChecked(False)
            if not propiedades.Propiedades.campos["radio_alquilado"].isChecked():
                propiedades.Propiedades.campos["radio_disponible"].setChecked(True)

        styles.reload_style(propiedades.Propiedades.campos["check_alquiler"])
        styles.reload_style(propiedades.Propiedades.campos["radio_alquilado"])
        styles.reload_style(propiedades.Propiedades.campos["check_venta"])
        styles.reload_style(propiedades.Propiedades.campos["radio_vendido"])

    @staticmethod
    def initialize_state():
        StateManager.update_tabla_clientes()
        StateManager.update_tabla_propiedades()
        StateManager.update_tabla_vendedores()
        StateManager.update_tabla_facturas()
        StateManager.update_propiedad_fields_state()
        StateManager.change_state("current_cli_pagina", 0)
        StateManager.change_state("current_pro_pagina", 0)

    @staticmethod
    def update_tabla_clientes():
        StateManager.change_state("cliente_query_object", StateManager.state["last_cliente_function"]())
        eventos.Eventos.cargar_tabla_clientes()

    @staticmethod
    def update_tabla_propiedades():
        if (StateManager.state["last_propiedad_function"] == var.clase_conexion.filtrar_propiedades):
            StateManager.change_state("propiedad_query_object",
                                      StateManager.state["last_propiedad_function"](
                                          StateManager.state["last_propiedad_params"][0],
                                          StateManager.state["last_propiedad_params"][1]))
        else:
            StateManager.change_state("propiedad_query_object", StateManager.state["last_propiedad_function"]())
        eventos.Eventos.cargar_tabla_propiedades()

    @staticmethod
    def update_tabla_vendedores():
        StateManager.change_state("vendedor_query_object", StateManager.state["last_vendedor_function"]())
        eventos.Eventos.cargar_tabla_vendedores()

    @staticmethod
    def update_tabla_facturas():
        StateManager.change_state("factura_query_object", StateManager.state["last_factura_function"]())
        eventos.Eventos.cargar_tabla_facturas()