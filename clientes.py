from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtCore
from datetime import datetime

import facturas
import var
import eventos
import conexion
import conexion_server
import mapper
from facturas import Facturas


class Clientes:
    campos = {}
    botones = {}
    _dni, _fecha_alta, _apellido, _nombre, _email, _movil, _direccion, _provincia, _municipio, _fecha_baja = "", "", "", "", "", "", "", "", "", ""

    def inicializar_campos():
        Clientes.campos = {
            "dni": var.ui.txt_cli_dni,
            "fecha_alta": var.ui.txt_cli_alta,
            "apellido": var.ui.txt_cli_apellido,
            "nombre": var.ui.txt_cli_nombre,
            "email": var.ui.txt_cli_email,
            "movil": var.ui.txt_cli_movil, 
            "direccion": var.ui.txt_cli_direccion,
            "provincia": var.ui.cmb_cli_provincia,
            "municipio": var.ui.cmb_cli_municipio,
            "fecha_baja": var.ui.txt_cli_baja
        }

    def inicializar_botones():
        Clientes.botones = {
            "btn_grabar": var.ui.btn_cli_grabar,
            "btn_modificar": var.ui.btn_cli_modificar,
            "btn_eliminar": var.ui.btn_cli_eliminar,
            "btn_alta": var.ui.btn_cli_alta,
            "btn_baja": var.ui.btn_cli_baja,
            "btn_buscar": var.ui.btn_cli_buscar
        }

    def inicializar_valores():
        Clientes._dni = var.ui.txt_cli_dni.text()
        Clientes._fecha_alta = var.ui.txt_cli_alta.text()
        Clientes._apellido = var.ui.txt_cli_apellido.text()
        Clientes._nombre = var.ui.txt_cli_nombre.text()
        Clientes._email = var.ui.txt_cli_email.text()
        Clientes._movil = var.ui.txt_cli_movil.text()
        Clientes._direccion = var.ui.txt_cli_direccion.text()
        Clientes._provincia = var.ui.cmb_cli_provincia.currentText()
        Clientes._municipio = var.ui.cmb_cli_municipio.currentText()
        Clientes._fecha_baja = var.ui.txt_cli_baja.text()

    def alta_cliente(self):
        Clientes.inicializar_campos()
        response = Clientes.check_if_cliente_valid_for_create()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return
        
        try:
            cliente = mapper.Mapper.map_cliente(Clientes.campos)
            last_id = var.clase_conexion.alta_cliente(cliente)
            if last_id != -1:
                eventos.Eventos.mensaje_exito("Aviso", "Alta cliente en la base de datos")
                var.state_manager.update_tabla_clientes()
                cliente_updated = var.clase_conexion.get_cliente(cliente["dni"])
                Clientes.populate_fields(cliente_updated)
            else:
                eventos.Eventos.mensaje_error("Aviso", "El cliente ya existe")
        except Exception as error:
            print("error alta cliente", error)

    def modificar_cliente(self):
        Clientes.inicializar_campos()
        response = Clientes.check_if_cliente_valid_for_edit()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return
        
        try:
            cliente = mapper.Mapper.map_cliente(Clientes.campos)
            if var.clase_conexion.modificar_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Datos cliente modificados correctamente")
                var.state_manager.update_tabla_clientes()
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error al modificar los datos del cliente")
        except Exception as error:
            print("error modificar_cliente", error)

    def baja_cliente(self):
        Clientes.inicializar_campos()
        response = Clientes.check_if_cliente_valid_for_delete()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return
        
        try:
            cliente = mapper.Mapper.map_cliente(Clientes.campos)
            if cliente["fecha_baja"].strip() == "":
                formato = '%d/%m/%Y'
                cliente["fecha_baja"] = datetime.strftime(datetime.now(), formato)
            
            if var.clase_conexion.baja_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Cliente dado de baja")
                var.state_manager.update_tabla_clientes()
                eventos.Eventos.limpiar_panel()
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error al dar de baja al cliente")
        except Exception as error:
            print("error baja_cliente", error)

    def cargar_cliente():
        Clientes.inicializar_campos()
        try:
            fila = var.ui.tab_cli.selectedItems()
            datos = [dato.text() for dato in fila]
            cliente = var.clase_conexion.get_cliente(str(datos[0]))
            Clientes.populate_fields(cliente)
            facturas.Facturas.populate_cliente_fields(cliente)
        except Exception as error:
            print("error cargar_cliente", error)

    def populate_fields(cliente):
        for key in cliente:
            if key == "provincia" or key == "municipio":
                Clientes.campos[key].setCurrentText(cliente[key])
            else:
                Clientes.campos[key].setText(cliente[key])
        eventos.Eventos.observar_fecha_baja(Clientes.campos["fecha_baja"])

    def buscar_cliente():
        Clientes.inicializar_campos()
        try:
            dni = Clientes.campos["dni"].text()
            cliente = var.clase_conexion.get_cliente(dni)
            for key in cliente:
                if key == "provincia" or key == "municipio":
                    Clientes.campos[key].setCurrentText(cliente[key])
                else:
                    Clientes.campos[key].setText(cliente[key])
            eventos.Eventos.observar_fecha_baja(Clientes.campos["fecha_baja"])
        except Exception as error:
            print("Error al buscar cliente", error)

    def check_existe_cli(dni):
        cliente = var.clase_conexion.get_cliente(dni)
        if (cliente["dni"] == ""):
            return False
        else:
            return True
        
    def common_checks(response):
        if (not Clientes._dni.strip() or not Clientes._apellido.strip() or not Clientes._direccion.strip() or not Clientes._fecha_alta.strip()
        or not Clientes._nombre.strip() or not Clientes._movil.strip() or not Clientes._provincia.strip() or not Clientes._municipio.strip()):
            response["valid"] = False
            response["messages"].append("Algún campo obligatorio no está cubierto")
        
        if (not eventos.Eventos.validar_dni(Clientes._dni) or not eventos.Eventos.validar_movil(Clientes._movil)
            or not eventos.Eventos.validar_fecha(Clientes._fecha_alta)):
            response["valid"] = False
            response["messages"].append("Algún campo obligatorio no tiene el formato esperado")

        if (Clientes._email.strip() and not eventos.Eventos.validar_email(Clientes._email)):
            response["valid"] = False
            response["messages"].append("El email no está vacío y no tiene el formata esperado")


    def check_if_cliente_valid_for_create():
        response = {
            "valid": True,
            "messages": []
        }

        Clientes.inicializar_campos()
        Clientes.inicializar_valores()

        Clientes.common_checks(response)

        if (Clientes.check_existe_cli(Clientes._dni)):
            response["valid"] = False
            response["messages"].append("El cliente con dni " + Clientes._dni + " ya existe")

        if (Clientes._fecha_baja.strip()):
            response["valid"] = False
            response["messages"].append("Al dar de alta a un cliente no puedes introducir una fecha de baja")

        return response
    
    def check_if_cliente_valid_for_edit():
        response = {
            "valid": True,
            "messages": []
        }

        Clientes.inicializar_campos()
        Clientes.inicializar_valores()

        Clientes.common_checks(response)

        if (var.clase_conexion.get_cliente(Clientes._dni) == False):
            response["valid"] = False
            response["messages"].append("El cliente con dni " + Clientes._dni + " no existe")

        return response

    def check_if_cliente_valid_for_delete():
        response = {
            "valid": True,
            "messages": []
        }

        Clientes.inicializar_campos()
        Clientes.inicializar_valores()

        if (not Clientes._dni.strip() or not eventos.Eventos.validar_dni(Clientes._dni)):
            response["valid"] = False
            response["messages"].append("Es necesario un dni válido para dar de baja")

        if (var.clase_conexion.get_cliente(Clientes._dni) == False):
            response["valid"] = False
            response["messages"].append("El cliente con dni " + Clientes._dni + " no existe")

        '''if (not Clientes._fecha_baja.strip() or not eventos.Eventos.validar_fecha(Clientes._fecha_baja)):
            response["valid"] = False
            response["messages"].append("Es necesaria una fecha de baja para dar de baja a un cliente")'''
        #Si no introducimos una fecha de baja se coge automáticamente la fecha actual
            
        if (Clientes._fecha_baja.strip()):  #Comprobamos que hay una fecha de baja porque si se deja en blanco usamos la actual
            if not eventos.Eventos.comparar_fechas(Clientes._fecha_alta, Clientes._fecha_baja):
                response["valid"] = False
                response["messages"].append("La fecha de baja no puede ser anterior a la fecha de alta")
        else:
            if not eventos.Eventos.comparar_fechas(Clientes._fecha_alta, str(datetime.now().date().strftime('%d/%m/%Y'))):
                response["valid"] = False
                response["messages"].append("La fecha de baja no puede ser anterior a la fecha de alta")
        return response