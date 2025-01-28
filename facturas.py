from datetime import datetime

import mapper
import var
import conexion
import eventos
import clientes

class Facturas:
    campos = {}
    botones = {}
    _numero, _fecha_registro,  = "", ""
    _dni_cliente, _apellidos_cliente, _nombre_cliente = "", "", ""
    (_codigo_propiedad, _tipo_propiedad, _precio_propiedad,
     _direccion_propiedad, _localidad_propiedad) = "", "", "", "", ""
    _id_vendedor = ""

    @staticmethod
    def inicializar_campos():
        Facturas.campos = {
            "numero": var.ui.txt_fac_numero,
            "fecha_registro": var.ui.txt_fac_alta,
            "dni_cliente": var.ui.txt_fac_cli_dni,
            "apellidos_cliente": var.ui.txt_fac_cli_apellidos,
            "nombre_cliente": var.ui.txt_fac_cli_nombre,
            "codigo_propiedad": var.ui.txt_fac_pro_codigo,
            "tipo_propiedad": var.ui.txt_fac_pro_tipo,
            "precio_propiedad": var.ui.txt_fac_pro_precio,
            "direccion_propiedad": var.ui.txt_fac_pro_direccion,
            "localidad_propiedad": var.ui.txt_fac_pro_localidad,
            "id_vendedor": var.ui.txt_fac_ven_id
        }

    @staticmethod
    def inicializar_valores():
        Facturas._numero = Facturas.campos["numero"].text()
        Facturas._fecha_registro = Facturas.campos["fecha_registro"].text()
        Facturas._dni_cliente = Facturas.campos["dni_cliente"].text()
        Facturas._apellidos_cliente = Facturas.campos["apellidos_cliente"].text()
        Facturas._nombre_cliente = Facturas.campos["nombre_cliente"].text()
        Facturas._codigo_propiedad = Facturas.campos["codigo_propiedad"].text()
        Facturas._tipo_propiedad = Facturas.campos["tipo_propiedad"].text()
        Facturas._precio_propiedad = Facturas.campos["precio_propiedad"].text()
        Facturas._direccion_propiedad = Facturas.campos["direccion_propiedad"].text()
        Facturas._localidad_propiedad = Facturas.campos["localidad_propiedad"].text()
        Facturas._id_vendedor = Facturas.campos["id_vendedor"].text()

    def inicializar_botones(self):
        Facturas.botones = {
            "btn_grabar": var.ui.btn_fac_grabar,
            "btn_grabar_ven": var.ui.btn_fac_ven_grabar
        }

    @staticmethod
    def populate_fields(factura):
        Facturas.campos["numero"].setText(factura["id"])
        Facturas.campos["fecha_registro"].setText(factura["fecha_registro"])

        cliente = conexion.Conexion.get_cliente(factura["dni_cliente"])
        Facturas.populate_cliente_fields(cliente)

    @staticmethod
    def populate_cliente_fields(cliente):
        Facturas.campos["dni_cliente"].setText(cliente["dni"])
        Facturas.campos["apellidos_cliente"].setText(cliente["apellido"])
        Facturas.campos["nombre_cliente"].setText(cliente["nombre"])

    @staticmethod
    def populate_propiedad_fields(propiedad):
        Facturas.campos["codigo_propiedad"].setText(propiedad["codigo"])
        Facturas.campos["tipo_propiedad"].setText(propiedad["tipo"])
        Facturas.campos["precio_propiedad"].setText(propiedad["precio_venta"])
        Facturas.campos["direccion_propiedad"].setText(propiedad["direccion"])
        Facturas.campos["localidad_propiedad"].setText(propiedad["municipio"])

    @staticmethod
    def populate_vendedor_fields(vendedor):
        Facturas.campos["id_vendedor"].setText(vendedor["codigo"])

    @staticmethod
    def cargar_factura():
        """

        :param None: None
        :type None: None
        :return: None
        :rtype: None

        Obtiene una factura de la tabla de facturas en la vista y carga sus datos

        """
        Facturas.inicializar_campos()
        try:
            fila = var.ui.tab_fac.selectedItems()
            datos = [dato.text() for dato in fila]
            factura = conexion.Conexion.get_factura(str(datos[0]))
            Facturas.populate_fields(factura)
        except Exception as error:
            print("error cargar_factura", error)

    @staticmethod
    def alta_factura():
        response = Facturas.check_if_factura_valid_for_create()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            factura = mapper.Mapper.map_factura(Facturas.campos)
            if factura["fecha_registro"].strip() == "":
                factura["fecha_registro"] = datetime.strftime(datetime.now(), '%d/%m/%Y')

            last_inserted_id = conexion.Conexion.alta_factura(factura)
            if (last_inserted_id != -1):
                eventos.Eventos.mensaje_exito("Aviso", "Alta factura en la base de datos")
                var.state_manager.update_tabla_facturas()
                Facturas.populate_fields(conexion.Conexion.get_factura(last_inserted_id))
            else:
                eventos.Eventos.mensaje_error("Aviso", "La factura ya existe")
        except Exception as error:
            print("factura", error)

    @staticmethod
    def eliminar_factura(id_fac):
        try:
            factura = conexion.Conexion.get_factura(id_fac)
            if not factura["id"]:
                eventos.Eventos.mensaje_error("Aviso", "La factura no existe")
            else:
                if conexion.Conexion.eliminar_factura(factura):
                    eventos.Eventos.mensaje_exito("Aviso", "Factura eliminada con éxito")
                    var.state_manager.update_tabla_facturas()
                    eventos.Eventos.limpiar_panel()
                else:
                    eventos.Eventos.mensaje_error("Aviso", "No se pudo eliminar la factura")
        except Exception as error:
            print("Error al eliminar factura", error)

    @staticmethod
    def alta_venta():
        response = Facturas.check_if_venta_valid_for_create()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            venta = mapper.Mapper.map_venta(Facturas.campos)
            last_inserted_id = conexion.Conexion.alta_venta(venta)
            if (last_inserted_id != -1):
                eventos.Eventos.mensaje_exito("Aviso", "Alta venta en la base de datos")
                #var.state_manager.update_tabla_ventas()
                #Facturas.populate_fields(conexion.Conexion.get_venta(last_inserted_id))
            else:
                eventos.Eventos.mensaje_error("Aviso", "La venta ya existe")
        except Exception as error:
            print("Error al dar de alta la venta", error)

    @staticmethod
    def check_if_factura_valid_for_create():
        response = {
            "valid": True,
            "messages": []
        }

        Facturas.inicializar_campos()
        Facturas.inicializar_valores()

        if Facturas._numero != "":
            response["valid"] = False
            response["messages"].append("Para registrar una nueva factura no debes introducir un código de factura")

        if Facturas._fecha_registro:
            if not eventos.Eventos.validar_fecha(Facturas._fecha_registro):
                response["valid"] = False
                response["messages"].append("Debes introducir una fecha de registro válida")

        if Facturas._dni_cliente:
            if not eventos.Eventos.validar_dni(Facturas._dni_cliente):
                response["valid"] = False
                response["messages"].append("DNI introducido no válido")
            if not conexion.Conexion.get_cliente(Facturas._dni_cliente):
                response["valid"] = False
                response["messages"].append("El DNI introducido no se corresponde con ningún cliente")
        else:
            response["valid"] = False
            response["messages"].append("Una factura necesita el DNI del cliente asociado")

        return response

    @staticmethod
    def check_if_venta_valid_for_create():
        response = {
            "valid": True,
            "messages": []
        }

        Facturas.inicializar_campos()
        Facturas.inicializar_valores()

        if not Facturas._numero:
            response["valid"] = False
            response["messages"].append("Para registrar una venta es necesario seleccionar una factura")

        if not Facturas._codigo_propiedad:
            response["valid"] = False
            response["messages"].append("Para registrar una venta es necesario seleccionar una propiedad")

        if not Facturas._id_vendedor:
            response["valid"] = False
            response["messages"].append("Para registrar una venta es necesario seleccionar un vendedor")

        if not Facturas._precio_propiedad:
            response["valid"] = False
            response["messages"].append("Es necesario establecer un precio para la venta de la propiedad")

        return response