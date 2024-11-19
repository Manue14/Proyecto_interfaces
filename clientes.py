from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtCore

import clientes
import conexion_server
import var
import eventos
import conexion
import styles
from datetime import datetime

class Clientes:
    campos = {}

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

    def construir_cliente():
        cliente = {"dni": Clientes.campos["dni"].text(), "fecha_alta": Clientes.campos["fecha_alta"].text(), "apellido": Clientes.campos["apellido"].text(),
                    "nombre": Clientes.campos["nombre"].text(), "email": Clientes.campos["email"].text(), "movil": Clientes.campos["movil"].text(),
                    "direccion": Clientes.campos["direccion"].text(), "provincia": Clientes.campos["provincia"].currentText(),
                    "municipio": Clientes.campos["municipio"].currentText(), "fecha_baja": Clientes.campos["fecha_baja"].text()}
        return cliente

    def alta_cliente(self):
        Clientes.inicializar_campos()
        if not Clientes.validar_campos_cli():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
            return
        if Clientes.campos["fecha_baja"].text().strip() != "":
            eventos.Eventos.mensaje_error("Aviso", "Al dar de alta un cliente no puedes introducir una fecha de baja")
            return
        
        try:
            cliente = Clientes.construir_cliente()
            if conexion.Conexion.alta_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Alta cliente en la base de datos")
            else:
                eventos.Eventos.mensaje_error("Aviso", "El cliente ya existe")
            clientes.Clientes.cargar_cli_tab()
        except Exception as error:
            print("error alta cliente", error)

    def modificar_cliente(self):
        Clientes.inicializar_campos()
        if not Clientes.validar_campos_cli():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
            return
        
        try:
            cliente = Clientes.construir_cliente()
            if not Clientes.check_existe_cli(cliente["dni"]):
                eventos.Eventos.mensaje_error("Aviso", "El cliente que intentas modificar no existe")
                return
            if conexion.Conexion.modificar_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Datos cliente modificados correctamente")
                clientes.Clientes.cargar_cli_tab()
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error al modificar los datos del cliente")
            clientes.Clientes.cargar_cli_tab()
        except Exception as error:
            print("error modificar_cliente", error)

    def baja_cliente(self):
        try:
            cliente = Clientes.construir_cliente()
            if not Clientes.check_existe_cli(cliente["dni"]):
                eventos.Eventos.mensaje_error("Aviso", "El cliente que intentas dar de baja no existe")
                return
            if cliente["fecha_baja"].strip() == "":
                formato = '%d/%m/%Y'
                cliente["fecha_baja"] = datetime.strftime(datetime.now(), formato)
            
            if conexion.Conexion.baja_cliente(cliente):
                eventos.Eventos.mensaje_exito("Aviso", "Cliente dado de baja")
                clientes.Clientes.cargar_cli_tab()
            else:
                eventos.Eventos.mensaje_error("Aviso", "Error baja cliente: cliente no existe o dado de baja")
            clientes.Clientes.cargar_cli_tab()
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
        except Exception as error:
            print("error cargar_cliente", error)

    @staticmethod
    def cargar_cli_tab():
        try:
            clientes = conexion.Conexion.listar_clientes()
            #listado = conexionserver.ConexionServer.listar_clientes(self)
            index = 0
            var.ui.tab_cli.verticalHeader().setVisible(False)
            for cliente in clientes:
                var.ui.tab_cli.setRowCount(index + 1)
                var.ui.tab_cli.setItem(index, 0, QtWidgets.QTableWidgetItem(cliente["dni"]))
                var.ui.tab_cli.setItem(index, 1, QtWidgets.QTableWidgetItem(cliente["apellido"]))
                var.ui.tab_cli.setItem(index, 2, QtWidgets.QTableWidgetItem(cliente["nombre"]))
                var.ui.tab_cli.setItem(index, 3, QtWidgets.QTableWidgetItem("  " + cliente["movil"] + "  "))
                var.ui.tab_cli.setItem(index, 4, QtWidgets.QTableWidgetItem(cliente["provincia"]))
                var.ui.tab_cli.setItem(index, 5, QtWidgets.QTableWidgetItem(cliente["municipio"]))
                var.ui.tab_cli.setItem(index, 6, QtWidgets.QTableWidgetItem("  " + cliente["fecha_baja"] + "  "))

                '''
                var.ui.tab_cli.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tab_cli.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tab_cli.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tab_cli.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tab_cli.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tab_cli.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tab_cli.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                '''

                var.ui.tab_cli.item(index, 0)
                var.ui.tab_cli.item(index, 1)
                var.ui.tab_cli.item(index, 2)
                var.ui.tab_cli.item(index, 3)
                var.ui.tab_cli.item(index, 4)
                var.ui.tab_cli.item(index, 5)
                var.ui.tab_cli.item(index, 6)

                index += 1

        except Exception as e:
            print("error cargar_cli_tab", e)

    def set_historico_cliente(self):
        try:
            if var.ui.chk_cli_historico.isChecked():
                var.historico_cli = 0
            else:
                var.historico_cli = 1
            Clientes.cargar_cli_tab()
        except Exception as Error:
            print("checkbox histórico", Error)

    def check_existe_cli(dni):
        cliente = conexion.Conexion.get_cliente(dni)
        if (cliente["dni"] == ""):
            return False
        else:
            return True

    def validar_campos_cli():
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
        
        if (fecha_baja.strip() and not eventos.Eventos.validar_fecha(fecha_baja)):
            return False

        return True