import var
import eventos
import conexion
import conexion_server
import mapper
from datetime import datetime

from facturas import Facturas


class Vendedores:
    campos = {}
    botones = {}
    _codigo, _dni, _fecha_alta, _fecha_baja, _nombre, _email, _movil, _provincia  = "", "", "", "", "", "", "", ""

    def inicializar_campos():
        Vendedores.campos = {
            "codigo": var.ui.lbl_ven_codigo,
            "dni": var.ui.txt_ven_dni,
            "fecha_alta": var.ui.txt_ven_alta,
            "fecha_baja": var.ui.txt_ven_baja,
            "nombre": var.ui.txt_ven_nombre,
            "email": var.ui.txt_ven_email,
            "movil": var.ui.txt_ven_movil,
            "provincia": var.ui.cmb_ven_provincia,
        }

    def inicializar_botones():
        Vendedores.botones = {
            "btn_grabar": var.ui.btn_ven_grabar,
            "btn_modificar": var.ui.btn_ven_modificar,
            "btn_eliminar": var.ui.btn_ven_eliminar,
            "btn_alta": var.ui.btn_ven_alta,
            "btn_baja": var.ui.btn_ven_baja
        }

    def inicializar_valores():
        Vendedores._codigo = var.ui.lbl_ven_codigo.text()
        Vendedores._dni = var.ui.txt_ven_dni.text()
        Vendedores._fecha_alta = var.ui.txt_ven_alta.text()
        Vendedores._fecha_baja = var.ui.txt_ven_baja.text()
        Vendedores._nombre = var.ui.txt_ven_nombre.text()
        Vendedores._email = var.ui.txt_ven_email.text()
        Vendedores._movil = var.ui.txt_ven_movil.text()
        Vendedores._provincia = var.ui.cmb_ven_provincia.currentText()

    def check_existe_ven(codigo):
        cliente = var.clase_conexion.get_vendedor_dni(codigo)
        if (not cliente["codigo"]):
            return False
        else:
            return True

    def check_existe_ven_dni(dni):
        cliente = var.clase_conexion.get_vendedor_dni(dni)
        if (cliente["dni"] == ""):
            return False
        else:
            return True

    def common_checks(response):
        if (not Vendedores._dni.strip() or not Vendedores._nombre.strip()
                or not Vendedores._movil.strip() or not Vendedores._provincia.strip()):
            response["valid"] = False
            response["messages"].append("Algún campo obligatorio no está cubierto")

        if (not eventos.Eventos.validar_dni(Vendedores._dni) or not eventos.Eventos.validar_movil(Vendedores._movil)
                or not eventos.Eventos.validar_fecha(Vendedores._fecha_alta)):
            response["valid"] = False
            response["messages"].append("Algún campo obligatorio no tiene el formato esperado")

        if (Vendedores._email.strip() and not eventos.Eventos.validar_email(Vendedores._email)):
            response["valid"] = False
            response["messages"].append("El email no está vacío y no tiene el formato esperado")


    def check_if_vendedor_valid_for_create():
        response = {
            "valid": True,
            "messages": []
        }

        Vendedores.inicializar_campos()
        Vendedores.inicializar_valores()

        Vendedores.common_checks(response)

        if (Vendedores.check_existe_ven(Vendedores._codigo)):
            response["valid"] = False
            response["messages"].append("El vendedor con código " + Vendedores._codigo + " ya existe")

        if (Vendedores.check_existe_ven_dni(Vendedores._dni)):
            response["valid"] = False
            response["messages"].append("El vendedor con dni " + Vendedores._dni + " ya existe")

        if (Vendedores._fecha_baja.strip()):
            response["valid"] = False
            response["messages"].append("Al dar de alta a un vendedor no puedes introducir una fecha de baja")

        return response

    def check_if_vendedor_valid_for_edit():
        response = {
            "valid": True,
            "messages": []
        }

        Vendedores.inicializar_campos()
        Vendedores.inicializar_valores()

        Vendedores.common_checks(response)

        if (var.clase_conexion.get_vendedor(Vendedores._codigo) == False):
            response["valid"] = False
            response["messages"].append("El vendedor con código " + Vendedores._codigo + " no existe")

        if (Vendedores._fecha_baja.strip()):  # Comprobamos que hay una fecha de baja porque si se deja en blanco usamos la actual
            if not eventos.Eventos.comparar_fechas(Vendedores._fecha_alta, Vendedores._fecha_baja):
                response["valid"] = False
                response["messages"].append("La fecha de baja no puede ser anterior a la fecha de alta")
        else:
            if not eventos.Eventos.comparar_fechas(Vendedores._fecha_alta,
                                                   str(datetime.now().date().strftime('%d/%m/%Y'))):
                response["valid"] = False
                response["messages"].append("La fecha de baja no puede ser anterior a la fecha de alta")

        return response

    def check_if_vendedor_valid_for_delete():
        response = {
            "valid": True,
            "messages": []
        }

        Vendedores.inicializar_campos()
        Vendedores.inicializar_valores()

        if (not Vendedores._codigo.strip()):
            response["valid"] = False
            response["messages"].append("Es necesario un código válido para dar de baja")

        if (var.clase_conexion.get_vendedor(Vendedores._codigo) == False):
            response["valid"] = False
            response["messages"].append("El vendedor con código " + Vendedores._codigo + " no existe")

        if (Vendedores._fecha_baja.strip()):  # Comprobamos que hay una fecha de baja porque si se deja en blanco usamos la actual
            if not eventos.Eventos.comparar_fechas(Vendedores._fecha_alta, Vendedores._fecha_baja):
                response["valid"] = False
                response["messages"].append("La fecha de baja no puede ser anterior a la fecha de alta")
        else:
            if not eventos.Eventos.comparar_fechas(Vendedores._fecha_alta,
                                                   str(datetime.now().date().strftime('%d/%m/%Y'))):
                response["valid"] = False
                response["messages"].append("La fecha de baja no puede ser anterior a la fecha de alta")
        return response

    def alta_vendedor(self):
        response = Vendedores.check_if_vendedor_valid_for_create()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            vendedor = mapper.Mapper.map_vendedor(Vendedores.campos)
            last_id = var.clase_conexion.alta_vendedor(vendedor)
            if last_id != -1:
                eventos.Eventos.mensaje_exito("Aviso", "Alta vendedor en la base de datos")
                var.state_manager.update_tabla_vendedores()
                vendedor_updated = var.clase_conexion.get_vendedor(vendedor["codigo"])
                Vendedores.populate_fields(vendedor_updated)
            else:
                eventos.Eventos.mensaje_error("Aviso", "El vendedor ya existe")
        except Exception as error:
            print("error alta vendedor", error)

    def modificar_vendedor(self):
        Vendedores.inicializar_campos()
        response = Vendedores.check_if_vendedor_valid_for_edit()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            vendedor = mapper.Mapper.map_vendedor(Vendedores.campos)
            if var.clase_conexion.modificar_vendedor(vendedor):
                eventos.Eventos.mensaje_exito("Aviso", "Datos vendedor modificados correctamente")
                var.state_manager.update_tabla_vendedores()
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error al modificar los datos del vendedor")
        except Exception as error:
            print("error modificar_vendedor", error)

    def baja_vendedor(self):
        Vendedores.inicializar_campos()
        response = Vendedores.check_if_vendedor_valid_for_delete()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            vendedor = mapper.Mapper.map_vendedor(Vendedores.campos)
            if vendedor["fecha_baja"].strip() == "":
                formato = '%d/%m/%Y'
                vendedor["fecha_baja"] = datetime.strftime(datetime.now(), formato)

            if var.clase_conexion.baja_vendedor(vendedor):
                eventos.Eventos.mensaje_exito("Aviso", "Vendedor dado de baja")
                var.state_manager.update_tabla_vendedores()
                eventos.Eventos.limpiar_panel()
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error al dar de baja al vendedor")
        except Exception as error:
            print("error baja_vendedor", error)

    def cargar_vendedor():
        Vendedores.inicializar_campos()
        try:
            fila = var.ui.tab_ven.selectedItems()
            vendedor = var.clase_conexion.get_vendedor(fila[0].text())
            Vendedores.populate_fields(vendedor)
            Facturas.populate_vendedor_fields(vendedor)
        except Exception as error:
            print("error cargar_vendedor", error)

    def populate_fields(vendedor):
        for key in vendedor:
            if key == "provincia":
                Vendedores.campos[key].setCurrentText(vendedor[key])
            else:
                Vendedores.campos[key].setText(vendedor[key])
        eventos.Eventos.observar_fecha_baja(Vendedores.campos["fecha_baja"])