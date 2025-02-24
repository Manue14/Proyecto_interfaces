from datetime import datetime, timedelta

from reportlab.rl_settings import eps_ttf_embed

import conexion
import eventos
import mapper
import var

class Alquiler:
    campos = {}
    botones = {}
    _id, _fecha_registro, _dni_cliente, _id_propiedad, _id_vendedor = "", "", "", "", ""
    _precio, _fecha_inicio, _fecha_fin = "", "", ""

    @staticmethod
    def inicializar_campos():
        Alquiler.campos = {
            "id": var.ui.txt_alq_id,
            "fecha_registro": var.ui.txt_alq_alta,
            "dni_cliente": var.ui.txt_alq_cli_dni,
            "id_propiedad": var.ui.txt_alq_pro_id,
            "id_vendedor": var.ui.txt_alq_ven_id,
            "precio": var.ui.txt_alq_precio,
            "fecha_inicio": var.ui.txt_alq_fecha_inicio,
            "fecha_fin": var.ui.txt_alq_fecha_fin
        }

    @staticmethod
    def inicializar_valores():
        Alquiler._id = Alquiler.campos["id"].text()
        Alquiler._fecha_registro = Alquiler.campos["fecha_registro"].text()
        Alquiler._dni_cliente = Alquiler.campos["dni_cliente"].text()
        Alquiler._id_propiedad = Alquiler.campos["id_propiedad"].text()
        Alquiler._id_vendedor = Alquiler.campos["id_vendedor"].text()
        Alquiler._precio = Alquiler.campos["precio"].text()
        Alquiler._fecha_inicio = Alquiler.campos["fecha_inicio"].text()
        Alquiler._fecha_fin = Alquiler.campos["fecha_fin"].text()

    @staticmethod
    def inicializar_botones():
        Alquiler.botones = {
            "btn_grabar": var.ui.btn_alq_grabar,
            "btn_cargar_mensualidades": var.ui.btn_alq_cargar_mensualidades
        }

    @staticmethod
    def get_date_range(fecha_inicio: datetime, fecha_fin: datetime):
        days = (fecha_fin - fecha_inicio).days
        for day in range(days + 1):
            yield fecha_inicio + timedelta(days=day)

    @staticmethod
    def calcular_mensualidades(fecha_inicio, fecha_fin):
        inicio = datetime.strptime(fecha_inicio, '%d/%m/%Y')
        fin = datetime.strptime(fecha_fin, '%d/%m/%Y')

        date_range = Alquiler.get_date_range(inicio, fin)

        for date in date_range:
            print(date)

    @staticmethod
    def alta_alquiler():
        response = Alquiler.check_if_alquiler_valid_for_create()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            alquiler = mapper.Mapper.map_alquiler(Alquiler.campos)

            last_inserted_id = conexion.Conexion.alta_alquiler(alquiler)

            if last_inserted_id == -1:
                eventos.Eventos.mensaje_error("Aviso", "El alquiler ya existe")
                return

            eventos.Eventos.mensaje_exito("Aviso", "Alta en del contrato de alquiler en la base de datos")

            #Mensualidades, calcular y guardar en BD

            var.state_manager.update_tabla_alquileres()
            var.state_manager.update_tabla_mensualidades()
            Alquiler.populate_fields(conexion.Conexion.get_alquiler(last_inserted_id))
        except Exception as error:
            print("Error al dar de alta el contrato", error)

    @staticmethod
    def eliminar_alquiler(id_alquiler):
        try:
            contrato = conexion.Conexion.get_alquiler(id_alquiler)
            #Borrar alquiler y mensualidades relacionadas
        except Exception as error:
            print("Error al eliminar contrato", error)


    @staticmethod
    def check_if_alquiler_valid_for_create():
        response = {
            "valid": True,
            "messages": []
        }

        Alquiler.inicializar_campos()
        Alquiler.inicializar_valores()

        if Alquiler._id != "":
            response["valid"] = False
            response["messages"].append("Para registrar un nuevo contrato no debes introducir un código de contrato ya existente")

        if Alquiler._fecha_registro:
            if not eventos.Eventos.validar_fecha(Alquiler._fecha_registro):
                response["valid"] = False
                response["messages"].append("Debes introducir una fecha válida")
        else:
            Alquiler._fecha_registro = datetime.strftime(datetime.now(), '%d/%m/%Y')

        if Alquiler._dni_cliente:
            if not eventos.Eventos.validar_dni(Alquiler._dni_cliente):
                response["valid"] = False
                response["messages"].append("DNI introducido no válido")
            if not conexion.Conexion.get_cliente(Alquiler._dni_cliente):
                response["valid"] = False
                response["messages"].append("El DNI introducido no se corresponde con ningún cliente")
        else:
            response["valid"] = False
            response["messages"].append("Un contrato necesita el DNI del cliente asociado")

        if not Alquiler._id_propiedad:
            response["valid"] = False
            response["messages"].append("Para registrar un contrato es necesario seleccionar una propiedad")

        if not Alquiler._id_vendedor:
            response["valid"] = False
            response["messages"].append("Para registrar un contrato es necesario seleccionar un vendedor")

        if not Alquiler._precio:
            response["valid"] = False
            response["messages"].append("Es necesario un precio válido para la propiedad")
        try:
            float(Alquiler._precio)
        except ValueError:
            response["valid"] = False
            response["messages"].append("Es necesario un precio válido para la propiedad")

        if not Alquiler._fecha_inicio:
            response["valid"] = False
            response["messages"].append("Es necesaria una fecha de inicio para el alquiler")

        if not Alquiler._fecha_fin:
            response["valid"] = False
            response["messages"].append("Es necesaria una fecha de fin para el alquiler")

        try:
            registro = datetime.strptime(Alquiler._fecha_registro, '%d/%m/%Y')
            inicio = datetime.strptime(Alquiler._fecha_inicio, '%d/%m/%Y')
            fin = datetime.strptime(Alquiler._fecha_fin, '%d/%m/%Y')

            if registro > inicio or inicio >= fin:
                response["valid"] = False
                response["messages"].append("La relación entre fechas introducidas no es válida")

        except ValueError:
            response["valid"] = False

        return response