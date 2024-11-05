from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtCore

import clientes
import conexion_server
import var
import eventos
import conexion

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
    
    @staticmethod
    def validar_dni():
        Clientes.inicializar_campos()
        try:
            dni = str(Clientes.campos["dni"].text())
            if eventos.Eventos.validar_dni(dni):
                Clientes.campos["dni"].setStyleSheet('''QLineEdit#txt_cli_dni {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_cli_dni:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
                Clientes.campos["dni"].setText(dni.upper())
            else:
                Clientes.campos["dni"].setStyleSheet('''QLineEdit#txt_cli_dni {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_cli_dni:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Clientes.campos["dni"].setText(None)
        except Exception as error:
            print("error check dni cliente", error)

    @staticmethod
    def validar_email():
        Clientes.inicializar_campos()
        try:
            mail = str(Clientes.campos["email"].text())
            if eventos.Eventos.validar_email(mail) or mail == "":
                Clientes.campos["email"].setStyleSheet('''QLineEdit#txt_cli_email {border-bottom: 1px solid #93c5fd;
                                                                                background-color: #dbeafe;}
                                                        QLineEdit#txt_cli_email:focus {border-bottom: 1.5px solid #2563eb;
                                                                                        background-color: #bfdbfe;}''')
                Clientes.campos["email"].setText(mail.lower())

            else:
                Clientes.campos["email"].setStyleSheet('''QLineEdit#txt_cli_email {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_cli_email:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Clientes.campos["email"].setText(None)
                Clientes.campos["email"].setText("correo no válido")
                Clientes.campos["email"].setFocus()

        except Exception as error:
            print("error check cliente", error)

    @staticmethod
    def validar_movil():
        Clientes.inicializar_campos()
        try:
            phone = str(Clientes.campos["movil"].text())

            if eventos.Eventos.validar_movil(phone):
                Clientes.campos["movil"].setStyleSheet('''QLineEdit#txt_cli_movil {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_cli_movil:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            else:
                Clientes.campos["movil"].setStyleSheet('''QLineEdit#txt_cli_movil {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_cli_movil:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Clientes.campos["movil"].setText(None)
                Clientes.campos["movil"].setText("móvil no válido")
                Clientes.campos["movil"].setFocus()
        except Exception as error:
            print("error check cliente", error)

    @staticmethod
    def validar_fecha_alta():
        Clientes.inicializar_campos()
        try:
            fecha = Clientes.campos["fecha_alta"].text()

            if eventos.Eventos.validar_fecha(fecha):
                Clientes.campos["fecha_alta"].setStyleSheet('''QLineEdit#txt_cli_alta {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_cli_alta:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            else:
                Clientes.campos["fecha_alta"].setStyleSheet('''QLineEdit#txt_cli_alta {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_cli_alta:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Clientes.campos["fecha_alta"].setText(None)
                Clientes.campos["fecha_alta"].setText("fecha no válida")
                Clientes.campos["fecha_alta"].setFocus()
        except Exception as error:
            print("Error al validar la fecha de alta", error)

    @staticmethod
    def validar_fecha_baja():
        Clientes.inicializar_campos()
        try:
            fecha = Clientes.campos["fecha_baja"].text()

            if eventos.Eventos.validar_fecha(fecha) or fecha == "":
                Clientes.campos["fecha_baja"].setStyleSheet('''QLineEdit#txt_cli_baja {border-bottom: 1px solid #93c5fd;
                                                                                background-color: #dbeafe;}
                                                        QLineEdit#txt_cli_baja:focus {border-bottom: 1.5px solid #2563eb;
                                                                                        background-color: #bfdbfe;}''')
            else:
                Clientes.campos["fecha_baja"].setStyleSheet('''QLineEdit#txt_cli_baja {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_cli_baja:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Clientes.campos["fecha_baja"].setText(None)
                Clientes.campos["fecha_baja"].setText("fecha no válida")
                Clientes.campos["fecha_baja"].setFocus()
        except Exception as error:
            print("Error al validar la fecha de baja", error)

    def alta_cliente(self):
        Clientes.inicializar_campos()
        if not Clientes.validar_campos_cli():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
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
                eventos.Eventos.mensaje_error("Aviso", "Para dar de baja al cliente es necesario introducir una fecha de baja")
                return 
            
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
                var.historico = 0
            else:
                var.historico = 1
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