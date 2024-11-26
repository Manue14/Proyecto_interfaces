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
        "alta_cliente": False,
        "modificar_cliente": False,
        "baja_cliente": False,
        "baja_propiedad": False
    }

    def __init__(self):
        self.state["historico_cli"] = False
        self.state["historico_pro"] = False
        

    @staticmethod
    def default_queries():
        try:
            StateManager.state["cliente_query_object"] = conexion.Conexion.listar_clientes()
            StateManager.state["propiedad_query_object"] = conexion.Conexion.listar_propiedades()
        except Exception as error:
            print("Error al obtener información de la base de datos", error)

    @staticmethod
    def change_state(key, value):
        try:
            StateManager.state[key] = value

            if (key == "historico_cli" or key == "historico_pro"
                or key == "cliente_query_object" or key == "propiedad_query_object"):
                StateManager.update_tables_state()
            elif (key == "baja_cliente" or key == "baja_propiedad"):
                StateManager.update_fields_state()
        except Exception as e:
            print(e)

    def manage_cliente_state():
        clientes.Clientes.inicializar_campos()
        clientes.Clientes.inicializar_botones()

        if StateManager.state["baja_cliente"] == True:
            clientes.Clientes.botones["btn_grabar"].setEnabled(False)
            clientes.Clientes.botones["btn_eliminar"].setEnabled(True)
        else:
            clientes.Clientes.botones["btn_grabar"].setEnabled(True)
            clientes.Clientes.botones["btn_eliminar"].setEnabled(False)
        styles.reload_style(clientes.Clientes.botones["btn_grabar"])
        styles.reload_style(clientes.Clientes.botones["btn_eliminar"])

    @staticmethod
    def update_state():
        StateManager.update_tables_state()
        StateManager.update_fields_state()

    def update_tables_state():
        eventos.Eventos.cargar_tabla_clientes()
        eventos.Eventos.cargar_tabla_propiedades()
        
    def update_fields_state():
        StateManager.manage_cliente_state()