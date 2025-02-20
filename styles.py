import clientes
import propiedades
import vendedores
import facturas
import alquileres
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
    clientes.Clientes.inicializar_botones()
    propiedades.Propiedades.inicializar_campos()
    propiedades.Propiedades.inicializar_botones()
    vendedores.Vendedores.inicializar_campos()
    vendedores.Vendedores.inicializar_botones()
    facturas.Facturas.inicializar_campos()
    facturas.Facturas.inicializar_botones()
    alquileres.Alquiler.inicializar_campos()
    alquileres.Alquiler.inicializar_botones()

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

    clientes.Clientes.botones["btn_grabar"].setProperty("qssClass", "general_button")
    clientes.Clientes.botones["btn_modificar"].setProperty("qssClass", "general_button")
    clientes.Clientes.botones["btn_eliminar"].setProperty("qssClass", "danger_button")
    clientes.Clientes.botones["btn_anterior"].setProperty("qssClass", "general_button")
    clientes.Clientes.botones["btn_siguiente"].setProperty("qssClass", "general_button")

    propiedades.Propiedades.campos["codigo"].setProperty("qssClass", "non_editable_general_label")
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

    propiedades.Propiedades.botones["btn_grabar"].setProperty("qssClass", "general_button")
    propiedades.Propiedades.botones["btn_modificar"].setProperty("qssClass", "general_button")
    propiedades.Propiedades.botones["btn_eliminar"].setProperty("qssClass", "danger_button")
    propiedades.Propiedades.botones["btn_anterior"].setProperty("qssClass", "general_button")
    propiedades.Propiedades.botones["btn_siguiente"].setProperty("qssClass", "general_button")

    vendedores.Vendedores.campos["codigo"].setProperty("qssClass", "non_editable_general_label")
    vendedores.Vendedores.campos["dni"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["fecha_alta"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["fecha_baja"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["nombre"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["email"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["movil"].setProperty("qssClass", "general_label")
    vendedores.Vendedores.campos["provincia"].setProperty("qssClass", "general_combobox")

    vendedores.Vendedores.botones["btn_grabar"].setProperty("qssClass", "general_button")
    vendedores.Vendedores.botones["btn_modificar"].setProperty("qssClass", "general_button")
    vendedores.Vendedores.botones["btn_eliminar"].setProperty("qssClass", "danger_button")

    facturas.Facturas.campos["numero"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["fecha_registro"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["dni_cliente"].setProperty("qssClass", "general_label")
    facturas.Facturas.campos["apellidos_cliente"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["nombre_cliente"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["codigo_propiedad"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["tipo_propiedad"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["precio_propiedad"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["direccion_propiedad"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["localidad_propiedad"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["id_vendedor"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["subtotal"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["impuestos"].setProperty("qssClass", "non_editable_general_label")
    facturas.Facturas.campos["total"].setProperty("qssClass", "non_editable_general_label")

    facturas.Facturas.botones["btn_grabar"].setProperty("qssClass", "general_button")
    facturas.Facturas.botones["btn_grabar_ven"].setProperty("qssClass", "general_button")

    alquileres.Alquiler.campos["id_contrato"].setProperty("qssClass", "non_editable_general_label")
    alquileres.Alquiler.campos["fecha_registro"].setProperty("qssClass", "non_editable_general_label")
    alquileres.Alquiler.campos["dni_cliente"].setProperty("qssClass", "general_label")
    alquileres.Alquiler.campos["id_contrato"].setProperty("qssClass", "non_editable_general_label")
    alquileres.Alquiler.campos["id_propiedad"].setProperty("qssClass", "non_editable_general_label")
    alquileres.Alquiler.campos["id_vendedor"].setProperty("qssClass", "non_editable_general_label")
    alquileres.Alquiler.campos["precio"].setProperty("qssClass", "non_editable_general_label")
    alquileres.Alquiler.campos["fecha_inicio"].setProperty("qssClass", "non_editable_general_label")
    alquileres.Alquiler.campos["fecha_fin"].setProperty("qssClass", "non_editable_general_label")

    alquileres.Alquiler.botones["btn_grabar"].setProperty("qssClass", "general_button")
    alquileres.Alquiler.botones["btn_cargar_mensualidades"].setProperty("qssClass", "general_button")

    for widget in clientes.Clientes.campos.values():
        reload_style(widget)

    for button in clientes.Clientes.botones.values():
        reload_style(button)

    for widget in propiedades.Propiedades.campos.values():
        reload_style(widget)

    for button in propiedades.Propiedades.botones.values():
        reload_style(button)

    for widget in vendedores.Vendedores.campos.values():
        reload_style(widget)

    for button in vendedores.Vendedores.botones.values():
        reload_style(button)

    for widget in facturas.Facturas.campos.values():
        reload_style(widget)

    for button in facturas.Facturas.botones.values():
        reload_style(button)

    for widget in alquileres.Alquiler.campos.values():
        reload_style(widget)

    for button in alquileres.Alquiler.botones.values():
        reload_style(button)

def set_style(widget, style):
    widget.setProperty("qssClass", style)
    reload_style(widget)

def reload_style(widget):
    widget.setStyleSheet(widget.styleSheet())