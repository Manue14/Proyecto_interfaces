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
        "cliente_query_object": [],
        "propiedad_query_object": [],
        "precio_alquiler_propiedad": False,
        "precio_venta_propiedad": False,
        "check_alquiler_propiedad": False,
        "check_venta_propiedad": False
    }

    @staticmethod
    def default_queries():
        try:
            StateManager.state["cliente_query_object"] = var.clase_conexion.listar_clientes()
            StateManager.state["propiedad_query_object"] = var.clase_conexion.listar_propiedades()
        except Exception as error:
            print("Error al obtener información de la base de datos", error)

    @staticmethod
    def change_state(key, value):
        try:
            StateManager.state[key] = value

            if (key == "historico_cli" or key == "historico_pro"
                or key == "cliente_query_object" or key == "propiedad_query_object"):
                StateManager.update_tables_state()
            elif (key == "precio_alquiler_propiedad" or key == "precio_venta_propiedad"
            or key == "check_alquiler_propiedad" or key == "check_venta_propiedad"):
                StateManager.update_propiedad_fields_state()
        except Exception as e:
            print(e)

    def manage_propiedad_state():
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
    def update_state():
        StateManager.update_tables_state()
        StateManager.update_propiedad_fields_state()

    def update_tables_state():
        eventos.Eventos.cargar_tabla_clientes()
        eventos.Eventos.cargar_tabla_propiedades()
        
    def update_propiedad_fields_state():
        StateManager.manage_propiedad_state()