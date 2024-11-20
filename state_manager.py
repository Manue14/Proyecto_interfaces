class StateManager:
    state = {
        "panel": 0,
        "historico_cli": False,
        "historico_pro": False,
        "cliente_query_object": {},
        "propiedad_query_object": {},
    }

    def __init__(self):
        self.state["panel"] = 0
        self.state["historico_cli"] = False
        self.state["historico_pro"] = False
        self.state["cliente_query_object"] = {}
        self.state["propiedad_query_object"] = {}

    @staticmethod
    def change_state(key, value):
        try:
            StateManager.state[key] = value
        except Exception as e:
            print(e)
