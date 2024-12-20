import clientes
import propiedades
import vendedores
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
    vendedores.Vendedores.inicializar_campos()

    clientes.Clientes.campos["dni"].setProperty("qssClass", "general_label")
    clientes.Clientes.campos["fecha_alta"].setProperty("qssClass", "general_label")
    clientes.Clientes.campos["apellido"].setProperty("qssClass", "general_label")
    clientes.Clientes.campos["nombre"].setProperty("qssClass", "general_label")
    clientes.Clientes.campos["email"].setProperty("qssClass", "general_label")
    clientes.Clientes.campos["movil"].setProperty("qssClass", "general_label")
    clientes.Clientes.campos["direccion"].setProperty("qssClass", "general_label")
    clientes.Clientes.campos["provincia"].setProperty("qssClass", "general_combobox")
    clientes.Clientes.campos["municipio"].setProperty("qssClass", "general_combobox")
    clientes.Clientes.campos["fecha_baja"].setProperty("qssClass", "general_label")

    propiedades.Propiedades.campos["codigo"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["fecha_alta"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["fecha_baja"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["direccion"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["provincia"].setProperty("qssClass", "general_combobox")
    propiedades.Propiedades.campos["municipio"].setProperty("qssClass", "general_combobox")
    propiedades.Propiedades.campos["postal"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["tipo"].setProperty("qssClass", "general_combobox")
    propiedades.Propiedades.campos["habitaciones"].setProperty("qssClass", "general_spinbox")
    propiedades.Propiedades.campos["banos"].setProperty("qssClass", "general_spinbox")
    propiedades.Propiedades.campos["superficie"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["precio_alquiler"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["precio_venta"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["descripcion"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["check_alquiler"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["check_venta"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["check_intercambio"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["radio_disponible"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["radio_alquilado"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["radio_vendido"].setProperty("qssClass", "")
    propiedades.Propiedades.campos["propietario"].setProperty("qssClass", "general_label")
    propiedades.Propiedades.campos["movil"].setProperty("qssClass", "general_label")

    vendedores.Vendedores.campos["dni"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["fecha_alta"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["fecha_baja"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["nombre"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["email"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["movil"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["provincia"].setProperty("qssClass", "general_combobox")

    for widget in clientes.Clientes.campos.values():
        reload_style(widget)

    for widget in propiedades.Propiedades.campos.values():
        reload_style(widget)

    for widget in vendedores.Vendedores.campos.values():
        reload_style(widget)

def set_style(widget, style):
    widget.setProperty("qssClass", style)
    reload_style(widget)

def reload_style(widget):
    widget.setStyleSheet(widget.styleSheet())