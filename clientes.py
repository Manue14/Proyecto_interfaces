from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtCore
from datetime import datetime

import var
import eventos
import conexion
import conexion_server
import mapper

class Clientes:
    campos = {}
    botones = {}
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

    def alta_cliente(self):
        Clientes.inicializar_campos()
        if not Clientes.validar_campos_cli():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
            return
        if Clientes.campos["fecha_baja"].text().strip() != "":
            eventos.Eventos.mensaje_error("Aviso", "Al dar de alta un cliente no puedes introducir una fecha de baja")
            return
        
        try:
            cliente = mapper.Mapper.map_cliente(Clientes.campos)
            if conexion.Conexion.alta_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Alta cliente en la base de datos")
                var.state_manager.change_state("cliente_query_object", conexion.Conexion.listar_clientes())
            else:
                eventos.Eventos.mensaje_error("Aviso", "El cliente ya existe")
        except Exception as error:
            print("error alta cliente", error)

    def modificar_cliente(self):
        Clientes.inicializar_campos()
        if not Clientes.validar_campos_cli():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
            return
        
        try:
            cliente = mapper.Mapper.map_cliente(Clientes.campos)
            if not Clientes.check_existe_cli(cliente["dni"]):
                eventos.Eventos.mensaje_error("Aviso", "El cliente que intentas modificar no existe")
                return
            if conexion.Conexion.modificar_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Datos cliente modificados correctamente")
                var.state_manager.change_state("cliente_query_object", conexion.Conexion.listar_clientes())
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error al modificar los datos del cliente")
        except Exception as error:
            print("error modificar_cliente", error)

    def baja_cliente(self):
        try:
            cliente = mapper.Mapper.map_cliente(Clientes.campos)
            if not Clientes.check_existe_cli(cliente["dni"]):
                eventos.Eventos.mensaje_error("Aviso", "El cliente que intentas dar de baja no existe")
                return
            if cliente["fecha_baja"].strip() == "":
                formato = '%d/%m/%Y'
                cliente["fecha_baja"] = datetime.strftime(datetime.now(), formato)
            
            if conexion.Conexion.baja_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Cliente dado de baja")
                var.state_manager.change_state("cliente_query_object", conexion.Conexion.listar_clientes())
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error baja cliente: cliente no existe o dado de baja")
        except Exception as error:
            print("error baja_cliente", error)

    def cargar_cliente(self):
        Clientes.inicializar_campos()
        try:
            fila = var.ui.tab_cli.selectedItems()
            datos = [dato.text() for dato in fila]
            cliente = conexion.Conexion.get_cliente(str(datos[0]))
            for key in cliente:
                if key == "provincia" or key == "municipio":
                    Clientes.campos[key].setCurrentText(cliente[key])
                else:
                    Clientes.campos[key].setText(cliente[key])
            eventos.Eventos.observar_fecha_baja(Clientes.campos["fecha_baja"])
        except Exception as error:
            print("error cargar_cliente", error)

    def buscar_cliente():
        Clientes.inicializar_campos()
        try:
            dni = Clientes.campos["dni"].text()
            cliente = conexion.Conexion.get_cliente(dni)
            for key in cliente:
                if key == "provincia" or key == "municipio":
                    Clientes.campos[key].setCurrentText(cliente[key])
                else:
                    Clientes.campos[key].setText(cliente[key])
            eventos.Eventos.observar_fecha_baja(Clientes.campos["fecha_baja"])
        except Exception as error:
            print("Error al buscar cliente", error)

    def check_existe_cli(dni):
        cliente = conexion.Conexion.get_cliente(dni)
        if (cliente["dni"] == ""):
            return False
        else:
            return True

    def check_if_cliente_valid_for_create():
        Clientes.inicializar_campos()
        dni = Clientes.campos["dni"].text()
        apellido = Clientes.campos["apellido"].text()
        email = Clientes.campos["email"].text()
        direccion = Clientes.campos["direccion"].text()
        fecha_alta = Clientes.campos["fecha_alta"].text()
        nombre = Clientes.campos["nombre"].text()
        movil = Clientes.campos["movil"].text()
        provincia = Clientes.campos["provincia"].currentText()
        municipio = Clientes.campos["municipio"].currentText()
        fecha_baja = Clientes.campos["fecha_baja"].text()

        if (not dni.strip() or not apellido.strip() or not direccion.strip() or not fecha_alta.strip()
        or not nombre.strip() or not movil.strip() or not provincia.strip() or not municipio.strip()):
            return False
        
        if (not eventos.Eventos.validar_dni(dni) or not eventos.Eventos.validar_movil(movil)
            or not eventos.Eventos.validar_fecha(fecha_alta)):
            return False

        if (email.strip() and not eventos.Eventos.validar_email(email)):
            return False

        if (conexion.Conexion.get_cliente(dni)):
            return False

        if (fecha_baja.strip()):
            return False

        return True