from datetime import datetime, timedelta

from reportlab.rl_settings import eps_ttf_embed

from PyQt6.QtCore import Qt

import conexion
import eventos
import mapper
import var

class Alquiler:
    campos = {}
    botones = {}
    _id, _fecha_firma, _dni_cliente, _id_propiedad, _id_vendedor = "", "", "", "", ""
    _precio, _fecha_inicio, _fecha_fin = "", "", ""

    @staticmethod
    def inicializar_campos():
        Alquiler.campos = {
            "id": var.ui.txt_alq_id,
            "fecha_firma": var.ui.txt_alq_alta,
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
        Alquiler._fecha_firma = Alquiler.campos["fecha_firma"].text()
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
    def populate_cliente_fields(cliente):
        if cliente["fecha_baja"] != "":
            Alquiler.campos["dni_cliente"].setText("")
            return

        Alquiler.campos["dni_cliente"].setText(cliente["dni"])

    @staticmethod
    def populate_vendedor_fields(vendedor):
        if vendedor["fecha_baja"] != "":
            Alquiler.campos["id_vendedor"].setText("")
            return

        Alquiler.campos["id_vendedor"].setText(vendedor["codigo"])

    @staticmethod
    def populate_propiedad_fields(propiedad):
        if propiedad["fecha_baja"] != "":
            Alquiler.campos["id_propiedad"].setText("")
            Alquiler.campos["precio"].setText("")

            Alquiler.campos["precio"].setAlignment(Qt.AlignmentFlag.AlignRight)
            eventos.Eventos.observar_non_editable(Alquiler.campos["precio"], True)
            return

        Alquiler.campos["id_propiedad"].setText(propiedad["codigo"])

        if "Alquiler" not in propiedad["operaciones"]:
            Alquiler.campos["precio"].setText("Propiedad no en alquiler")
            Alquiler.campos["precio"].setAlignment(Qt.AlignmentFlag.AlignCenter)
            eventos.Eventos.observar_non_editable(Alquiler.campos["precio"], False)
        else:
            Alquiler.campos["precio"].setText(propiedad["precio_alquiler"])
            Alquiler.campos["precio"].setAlignment(Qt.AlignmentFlag.AlignRight)
            eventos.Eventos.observar_non_editable(Alquiler.campos["precio"], True)

    @staticmethod
    def populate_alquiler_fields(alquiler):
        Alquiler.campos["id"].setText(alquiler["id"])
        Alquiler.campos["fecha_firma"].setText(alquiler["fecha_firma"])
        Alquiler.campos["dni_cliente"].setText(alquiler["dni_cliente"])
        Alquiler.campos["id_propiedad"].setText(alquiler["id_propiedad"])
        Alquiler.campos["id_vendedor"].setText(alquiler["id_vendedor"])
        Alquiler.campos["precio"].setText(alquiler["precio"])
        Alquiler.campos["fecha_inicio"].setText(alquiler["fecha_inicio"])
        Alquiler.campos["fecha_fin"].setText(alquiler["fecha_fin"])

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

        mensualidades_map = {}

        for date in date_range:
            month = date.strftime("%B")
            year = str(date.year)
            key = month + year

            if key not in mensualidades_map.keys():
                date_list = []
                date_list.append(date.strftime('%d/%m/%Y'))
                date_list.append((month + "-" + year).capitalize())
                mensualidades_map[key] = date_list

        return mensualidades_map.values()
    
    @staticmethod
    def aaaa():
        mensualidades = Alquiler.calcular_mensualidades("01/01/2025", "01/11/2026")
        for mensualidad in mensualidades:
            print(mensualidad)

    @staticmethod
    def alta_alquiler():
        response = Alquiler.check_if_alquiler_valid_for_create()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            alquiler = mapper.Mapper.map_alquiler(Alquiler.campos)
            alquiler["fecha_firma"] = Alquiler._fecha_firma

            last_inserted_id = conexion.Conexion.alta_alquiler(alquiler)

            if last_inserted_id == -1:
                eventos.Eventos.mensaje_error("Aviso", "El alquiler ya existe")
                return
            
            mensualidades = Alquiler.calcular_mensualidades(alquiler["fecha_inicio"], alquiler["fecha_fin"])

            for mensualidad in mensualidades:
                recibo = mapper.Mapper.initialize_recibo()
                recibo["alquiler_id"] = last_inserted_id
                recibo["propiedad_id"] = alquiler["id_propiedad"]
                recibo["mensualidad"] = mensualidad[1]
                recibo["fecha"] = mensualidad[0]
                recibo["importe"] = alquiler["precio"]
                recibo["pagado"] = 0
                conexion.Conexion.alta_recibo(recibo)

            eventos.Eventos.mensaje_exito("Aviso", "Alta del contrato de alquiler en la base de datos")

            Alquiler.populate_alquiler_fields(conexion.Conexion.get_alquiler(last_inserted_id))
            recibos = conexion.Conexion.listar_recibos_by_alquiler(last_inserted_id)

            propiedad = conexion.Conexion.get_propiedad(alquiler["id_propiedad"])
            propiedad["estado"] = "Alquilado"
            propiedad["fecha_baja"] = alquiler["fecha_firma"]
            conexion.Conexion.modificar_propiedad(propiedad)
            var.state_manager.update_tabla_propiedades()
            eventos.Eventos.limpiar_panel_propiedades()

            eventos.Eventos.cargar_tabla_recibos(recibos)
            var.state_manager.update_tabla_alquileres()

        except Exception as error:
            print("Error al dar de alta el alquiler", error)

    @staticmethod
    def eliminar_alquiler(id_alquiler):
        try:

            if conexion.Conexion.eliminar_alquiler(id_alquiler):
                eventos.Eventos.mensaje_exito("Aviso", "Alquiler eliminado con éxito")
                var.state_manager.update_tabla_alquileres()
                recibos = conexion.Conexion.listar_recibos_by_alquiler(id_alquiler)
                eventos.Eventos.cargar_tabla_recibos(recibos)
            else:
                eventos.Eventos.mensaje_error("Aviso", "No se pudo eliminar el alquiler")

        except Exception as error:
            print("Error al eliminar alquiler", error)

    @staticmethod
    def cargar_alquiler():
        Alquiler.inicializar_campos()
        try:
            fila = var.ui.tab_alq.selectedItems()
            datos = [dato.text() for dato in fila]
            alquiler = conexion.Conexion.get_alquiler(str(datos[0]))
            Alquiler.populate_alquiler_fields(alquiler)
            recibos = conexion.Conexion.listar_recibos_by_alquiler(str(alquiler["id"]))
            eventos.Eventos.cargar_tabla_recibos(recibos)
        except Exception as error:
            print("error cargar_alquiler", error)

    @staticmethod
    def toogle_recibo_pagado(id_recibo, checkbox):
        recibo = conexion.Conexion.get_recibo(id_recibo)
        if int(recibo["pagado"]) == 0:
            recibo["pagado"] = 1
        else:
            recibo["pagado"] = 0

        if conexion.Conexion.update_recibo(recibo):
            if int(recibo["pagado"]) == 0:
                checkbox.setChecked(False)
            else:
                checkbox.setChecked(True)


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

        if Alquiler._fecha_firma:
            if not eventos.Eventos.validar_fecha(Alquiler._fecha_firma):
                response["valid"] = False
                response["messages"].append("Debes introducir una fecha válida")
        else:
            Alquiler._fecha_firma = datetime.strftime(datetime.now(), '%d/%m/%Y')

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
            registro = datetime.strptime(Alquiler._fecha_firma, '%d/%m/%Y')
            inicio = datetime.strptime(Alquiler._fecha_inicio, '%d/%m/%Y')
            fin = datetime.strptime(Alquiler._fecha_fin, '%d/%m/%Y')

            if registro > inicio or inicio >= fin:
                response["valid"] = False
                response["messages"].append("La relación entre fechas introducidas no es válida")

        except ValueError:
            response["valid"] = False

        return response