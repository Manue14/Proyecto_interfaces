import clientes
import propiedades
# styles.py
def load_stylesheet():
    '''
    :return: boolean
    Carga y devuelve el contenido de styles.qss como una cadena
    '''
    with open("styles.qss", "r") as style_file:
        return style_file.read()

def initialize_styles():
    clientes.Clientes.inicializar_campos()
    propiedades.Propiedades.inicializar_campos()

    clientes.Clientes.campos["dni"].setProperty("qssClass", "obligatorio_valido")
    clientes.Clientes.campos["fecha_alta"].setProperty("qssClass", "obligatorio_valido")
    clientes.Clientes.campos["apellido"].setProperty("qssClass", "obligatorio_valido")
    clientes.Clientes.campos["nombre"].setProperty("qssClass", "obligatorio_valido")
    clientes.Clientes.campos["email"].setProperty("qssClass", "no_obligatorio_valido")
    clientes.Clientes.campos["movil"].setProperty("qssClass", "obligatorio_valido")
    clientes.Clientes.campos["direccion"].setProperty("qssClass", "obligatorio_valido")
    clientes.Clientes.campos["provincia"].setProperty("qssClass", "")
    clientes.Clientes.campos["municipio"].setProperty("qssClass", "")
    clientes.Clientes.campos["fecha_baja"].setProperty("qssClass", "no_obligatorio_valido")

    propiedades.Propiedades.campos["codigo"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["fecha_alta"].setProperty("qssClass", "obligatorio_valido")
    propiedades.Propiedades.campos["fecha_baja"].setProperty("qssClass", "no_obligatorio_valido")
    propiedades.Propiedades.campos["direccion"].setProperty("qssClass", "obligatorio_valido")
    propiedades.Propiedades.campos["provincia"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["municipio"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["postal"].setProperty("qssClass", "obligatorio_valido")
    propiedades.Propiedades.campos["tipo"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["habitaciones"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["banos"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["superficie"].setProperty("qssClass", "obligatorio_valido")
    propiedades.Propiedades.campos["precio_alquiler"].setProperty("qssClass", "no_obligatorio_valido")
    propiedades.Propiedades.campos["precio_venta"].setProperty("qssClass", "no_obligatorio_valido")
    propiedades.Propiedades.campos["descripcion"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["check_alquiler"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["check_venta"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["check_intercambio"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["radio_disponible"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["radio_alquilado"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["radio_vendido"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["propietario"].setProperty("qssClass", "obligatorio_valido")
    propiedades.Propiedades.campos["movil"].setProperty("qssClass", "obligatorio_valido")

    for widget in clientes.Clientes.campos.values():
        reload_style(widget)

    for widget in propiedades.Propiedades.campos.values():
        reload_style(widget)

def set_style(widget, style):
    widget.setProperty("qssClass", style)
    reload_style(widget)

def reload_style(widget):
    widget.setStyleSheet(widget.styleSheet())