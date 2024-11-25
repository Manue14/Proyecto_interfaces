import clientes
import propiedades
import eventos
import conexion
import var

class StateManager:
    state = {
        "panel": 0,
        "historico_cli": False,
        "historico_pro": False,
        "cliente_query_object": [],
        "propiedad_query_object": [],
    }

    def __init__(self):
        self.state["historico_cli"] = False
        self.state["historico_pro"] = False

    @staticmethod
    def default_queries():
        try:
            StateManager.state["cliente_query_object"] = conexion.Conexion.listar_clientes()
            StateManager.state["propiedad_query_object"] = conexion.Conexion.listar_propiedades()
            #StateManager.update_state()
        except Exception as error:
            print("Error al obtener información de la base de datos", error)

    @staticmethod
    def change_state(key, value):
        try:
            StateManager.state[key] = value
            StateManager.update_state()
        except Exception as e:
            print(e)

    def update_state():
        eventos.Eventos.cargar_tabla_clientes()
        eventos.Eventos.cargar_tabla_propiedades()