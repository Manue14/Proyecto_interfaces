import csv
import json
import sys
import time
import re
from datetime import datetime
import os
from PyQt6 import QtWidgets, QtGui
import locale
import zipfile
import shutil

from reportlab.lib.testutils import setOutDir

import var
import clientes
import propiedades
import conexion
import conexion_server
import styles
import vendedores

#Establecer configuración regional
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos:
    def mensaje_salir(self=None):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
        mbox.setWindowTitle('Salir')
        mbox.setText("Desea usted salir")
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText("Sí")
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText("No")

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()

    def mensaje_exito(titulo, mensaje):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
        mbox.setWindowTitle(titulo)
        mbox.setText(mensaje)
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
        mbox.exec()

    def mensaje_error(titulo, mensaje):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
        mbox.setWindowTitle(titulo)
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")

        try:
            iter(mensaje)
            mensaje_total = ""
            for m in mensaje:
                mensaje_total = mensaje_total + m + "\n"
            mbox.setText(mensaje_total)
        except TypeError as te:
            mbox.setText(mensaje)
        mbox.exec()

    def cargar_provincias(widget):
        widget.clear()
        listado = var.clase_conexion.listar_provincias()
        #listado = conexionserver.ConexionServer.listar_provincias(self)
        for prov in listado:
            widget.addItem(prov[1], prov[0])

    def cargar_municipios(widget, provId = 1):
        widget.clear()
        listado = var.clase_conexion.listar_municipios(provId)
        for mun in listado:
            widget.addItem(str(mun[0]), mun[1])

    def observar_dni(widget):
        try:
            dni = widget.text()
            if Eventos.validar_dni(dni):
                styles.set_style(widget,"general_label")
                widget.setText(dni.upper())
            else:
                styles.set_style(widget,"general_label_error")
                widget.setText(None)
        except Exception as error:
            print("Error al validar el dni", error)

    def observar_email(widget):
        try:
            mail = widget.text()
            if Eventos.validar_email(mail) or mail == "":
                styles.set_style(widget, "general_label")
                widget.setText(mail.lower())
            else:
                styles.set_style(widget, "general_label_error")
                widget.setText(None)
                widget.setText("Email no válido")
                widget.setFocus()
        except Exception as error:
            print("Error al validar el email", error)

    def observar_movil(widget):
        try:
            movil = widget.text()
            if Eventos.validar_movil(movil):
                styles.set_style(widget, "general_label")
            else:
                styles.set_style(widget, "general_label_error")
                widget.setText(None)
                widget.setText("Móvil no válido")
                widget.setFocus()
        except Exception as error:
            print("Error al validar el móvil", error)

    def observar_fecha_alta(widget):
        try:
            fecha = widget.text()
            if Eventos.validar_fecha(fecha):
                styles.set_style(widget, "general_label")
            else:
                styles.set_style(widget, "general_label_error")
                widget.setText(None)
                widget.setText("Fecha no válida")
                widget.setFocus()
        except Exception as error:
            print("Error al validar la fecha de alta", error)

    def observar_fecha_baja(widget):
        try:
            fecha = widget.text()
            if Eventos.validar_fecha(fecha) or fecha == "":
                styles.set_style(widget, "general_label")
            else:
                styles.set_style(widget, "general_label_error")
                widget.setText(None)
                widget.setText("fecha no válida")
                widget.setFocus()
        except Exception as error:
            print("Error al validar la fecha de baja", error)

    def observar_codigo_postal(widget):
        try:
            postal = widget.text()
            if Eventos.validar_numero(postal):
                styles.set_style(widget, "general_label")
            else:
                styles.set_style(widget, "general_label_error")
                widget.setText(None)
                widget.setText("CP no válido")
                widget.setFocus()
        except Exception as error:
            print("Error al validar el código postal", error)

    def observar_superficie(widget):
        try:
            superficie = widget.text()
            if Eventos.validar_numero(superficie):
                styles.set_style(widget, "general_label")
            else:
                styles.set_style(widget, "general_label_error")
                widget.setText(None)
                widget.setText("Valor no válido")
                widget.setFocus()
        except Exception as error:
            print("Error al validar la superficie", error)

    def observar_precio(widget):
        try:
            precio = widget.text()
            nombre = widget.objectName()
            if Eventos.validar_numero(precio) or precio == "":
                styles.set_style(widget, "general_label")
                if Eventos.validar_numero(precio):
                    if (nombre == "txt_pro_precio_alquiler"):
                        var.state_manager.change_state("precio_alquiler_propiedad", True)
                    elif (nombre == "txt_pro_precio_venta"):
                        var.state_manager.change_state("precio_venta_propiedad", True)
                else:
                    if (nombre == "txt_pro_precio_alquiler"):
                        var.state_manager.change_state("precio_alquiler_propiedad", False)
                    elif (nombre == "txt_pro_precio_venta"):
                        var.state_manager.change_state("precio_venta_propiedad", False)
            else:
                styles.set_style(widget, "general_label_error")
                widget.setText(None)
                widget.setText("Valor no válido")
                widget.setFocus()
                if (nombre == "txt_pro_precio_alquiler"):
                    var.state_manager.change_state("precio_alquiler_propiedad", False)
                elif (nombre == "txt_pro_precio_venta"):
                    var.state_manager.change_state("precio_venta_propiedad", False)
        except Exception as error:
            print("Error al validar el precio", error)

    def observar_checkbox(widget):
        try:
            name = widget.objectName()
            if (name == "chk_pro_alquiler"):
                var.state_manager.change_state("check_alquiler_propiedad", widget.isChecked())
            elif (name == "chk_pro_venta"):
                var.state_manager.change_state("check_venta_propiedad", widget.isChecked())
        except Exception as error:
            print("Error al observar el checkbox", error)
    
        
    def validar_dni(dni):
        valid_letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9 :
            return False
        number_part = dni[0:8]
        if not number_part.isdigit() :
            return False
        correct_letter = valid_letters[int(number_part) % 23]
        if dni[8].upper() != correct_letter:
            return False
        return True

    def validar_email(mail):
        mail = mail.lower()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, mail):
            return True
        else:
            return False

    def validar_movil(phone):
        regex = r'(\+34|0034|34)?(6|7)([0-9]){8}'
        if re.match(regex, phone):
            return True
        else:
            return False
        
    def validar_fecha(fecha):
        formato = '%d/%m/%Y'
        try:
            datetime.strptime(fecha, formato)
            return True
        except ValueError:
            return False
        
    def validar_numero(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def abrir_calendar(btn):
        try:
            var.btn = btn
            var.ui_calendar.show()
        except Exception as error:
            print("error en abrir calendar ", error)

    def cargar_fecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.ui.panel_principal.currentIndex() == 0 and var.btn == 0:
                var.ui.txt_cli_alta.setText(str(data))
                Eventos.observar_fecha_alta(var.ui.txt_cli_alta)

            elif var.ui.panel_principal.currentIndex() == 0 and var.btn == 1:
                var.ui.txt_cli_baja.setText(str(data))
                Eventos.observar_fecha_baja(var.ui.txt_cli_baja)

            elif var.ui.panel_principal.currentIndex() == 1 and var.btn == 0:
                var.ui.txt_pro_alta.setText(str(data))
                Eventos.observar_fecha_alta(var.ui.txt_pro_alta)

            elif var.ui.panel_principal.currentIndex() == 1 and var.btn == 1:
                var.ui.txt_pro_baja.setText(str(data))
                Eventos.observar_fecha_baja(var.ui.txt_pro_baja)

            elif var.ui.panel_principal.currentIndex() == 2 and var.btn == 0:
                var.ui.txt_ven_alta.setText(str(data))
                Eventos.observar_fecha_alta(var.ui.txt_ven_alta)

            elif var.ui.panel_principal.currentIndex() == 2 and var.btn == 1:
                var.ui.txt_ven_baja.setText(str(data))
                Eventos.observar_fecha_baja(var.ui.txt_ven_baja)

            time.sleep(0.5)
            var.ui_calendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)

    def cargar_tabla_clientes():
        index = 0
        var.ui.tab_cli.verticalHeader().setVisible(False)
        clientes = var.state_manager.state["cliente_query_object"]

        start = var.state_manager.state["current_cli_pagina"] * var.state_manager.state["cliente_pagination"]
        end = var.state_manager.state["current_cli_pagina"] * var.state_manager.state["cliente_pagination"] + var.state_manager.state["cliente_pagination"]

        if (var.state_manager.state["current_cli_pagina"] > len(clientes) / var.state_manager.state["cliente_pagination"]):
            var.state_manager.change_state("current_cli_pagina", int(len(clientes) / var.state_manager.state["cliente_pagination"]))
        elif (var.state_manager.state["current_cli_pagina"] == len(clientes) / var.state_manager.state["cliente_pagination"] and len(clientes) != 0):
            var.state_manager.change_state("current_cli_pagina", 0)

        if (len(clientes) % var.state_manager.state["cliente_pagination"] == 0 and len(clientes) != 0):
            var.ui.lbl_cli_pagina.setText("Página " + str(var.state_manager.state["current_cli_pagina"] + 1) + " de "
                + str(int(len(clientes) / var.state_manager.state["cliente_pagination"]))) 
        else:
            var.ui.lbl_cli_pagina.setText("Página " + str(var.state_manager.state["current_cli_pagina"] + 1) + " de "
                + str(int(len(clientes) / var.state_manager.state["cliente_pagination"] + 1))) 

        for i in range(start, end):
            if (i < len(clientes)):
                cliente = clientes[i]
                Eventos.show_cli_on_table(cliente, index)
                index += 1

    def cargar_tabla_propiedades():
        index = 0
        var.ui.tab_pro.verticalHeader().setVisible(False)
        propiedades = var.state_manager.state["propiedad_query_object"]

        start = var.state_manager.state["current_pro_pagina"] * var.state_manager.state["propiedad_pagination"]
        end = var.state_manager.state["current_pro_pagina"] * var.state_manager.state["propiedad_pagination"] + var.state_manager.state["propiedad_pagination"]

        if (var.state_manager.state["current_pro_pagina"] > len(propiedades) / var.state_manager.state["propiedad_pagination"]):
            var.state_manager.change_state("current_pro_pagina", int(len(propiedades) / var.state_manager.state["propiedad_pagination"]))
        elif (var.state_manager.state["current_pro_pagina"] == len(propiedades) / var.state_manager.state["propiedad_pagination"] and len(propiedades) != 0):
            var.state_manager.change_state("current_pro_pagina", 0)

        if (len(propiedades) % var.state_manager.state["propiedad_pagination"] == 0 and len(propiedades) != 0):
            var.ui.lbl_pro_pagina.setText("Página " + str(var.state_manager.state["current_pro_pagina"] + 1) + " de "
                + str(int(len(propiedades) / var.state_manager.state["propiedad_pagination"]))) 
        else:
            var.ui.lbl_pro_pagina.setText("Página " + str(var.state_manager.state["current_pro_pagina"] + 1) + " de "
                + str(int(len(propiedades) / var.state_manager.state["propiedad_pagination"] + 1))) 

        if propiedades:
            for i in range(start, end):
                if (i < len(propiedades)):
                    propiedad = propiedades[i]
                    Eventos.show_pro_on_table(propiedad, index)
                    index += 1
        else:
            var.ui.tab_pro.setRowCount(index + 1)
            var.ui.tab_pro.setItem(index, 0, QtWidgets.QTableWidgetItem(""))
            var.ui.tab_pro.setItem(index, 1, QtWidgets.QTableWidgetItem(""))
            var.ui.tab_pro.setItem(index, 2, QtWidgets.QTableWidgetItem("No se encontraron propiedades"))
            var.ui.tab_pro.setItem(index, 3, QtWidgets.QTableWidgetItem(""))
            var.ui.tab_pro.setItem(index, 4, QtWidgets.QTableWidgetItem(""))
            var.ui.tab_pro.setItem(index, 5, QtWidgets.QTableWidgetItem(""))
            var.ui.tab_pro.setItem(index, 6, QtWidgets.QTableWidgetItem(""))
            var.ui.tab_pro.setItem(index, 7, QtWidgets.QTableWidgetItem(""))
            var.ui.tab_pro.setItem(index, 8, QtWidgets.QTableWidgetItem(""))

            var.ui.tab_pro.item(index, 0)
            var.ui.tab_pro.item(index, 1)
            var.ui.tab_pro.item(index, 2)
            var.ui.tab_pro.item(index, 3)
            var.ui.tab_pro.item(index, 4)
            var.ui.tab_pro.item(index, 5)
            var.ui.tab_pro.item(index, 6)
            var.ui.tab_pro.item(index, 7)
            var.ui.tab_pro.item(index, 8)

    def cargar_tabla_vendedores():
        index = 0
        var.ui.tab_ven.verticalHeader().setVisible(False)
        vendedores = var.state_manager.state["vendedor_query_object"]
        for i in range(0, len(vendedores)):
            vendedor = vendedores[i]
            Eventos.show_ven_on_table(vendedor, index)
            index += 1

    def show_cli_on_table(cliente, index):
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

    def show_pro_on_table(propiedad, index):
        var.ui.tab_pro.setRowCount(index + 1)
        var.ui.tab_pro.setItem(index, 0, QtWidgets.QTableWidgetItem(propiedad["codigo"]))
        var.ui.tab_pro.setItem(index, 1, QtWidgets.QTableWidgetItem(propiedad["municipio"]))
        var.ui.tab_pro.setItem(index, 2, QtWidgets.QTableWidgetItem(propiedad["tipo"]))
        var.ui.tab_pro.setItem(index, 3, QtWidgets.QTableWidgetItem(propiedad["habitaciones"]))
        var.ui.tab_pro.setItem(index, 4, QtWidgets.QTableWidgetItem(propiedad["banos"]))
        var.ui.tab_pro.setItem(index, 5, QtWidgets.QTableWidgetItem(
            propiedad["precio_alquiler"] + " €" if propiedad["precio_alquiler"] else "-"))
        var.ui.tab_pro.setItem(index, 6, QtWidgets.QTableWidgetItem(
            propiedad["precio_venta"] + " €" if propiedad["precio_venta"] else "-"))
        var.ui.tab_pro.setItem(index, 7, QtWidgets.QTableWidgetItem(propiedad["operaciones"]))
        var.ui.tab_pro.setItem(index, 8, QtWidgets.QTableWidgetItem(propiedad["fecha_baja"]))

        var.ui.tab_pro.item(index, 0)
        var.ui.tab_pro.item(index, 1)
        var.ui.tab_pro.item(index, 2)
        var.ui.tab_pro.item(index, 3)
        var.ui.tab_pro.item(index, 4)
        var.ui.tab_pro.item(index, 5)
        var.ui.tab_pro.item(index, 6)
        var.ui.tab_pro.item(index, 7)
        var.ui.tab_pro.item(index, 8)

    def show_ven_on_table(vendedor, index):
        var.ui.tab_ven.setRowCount(index + 1)

        var.ui.tab_ven.setItem(index, 0, QtWidgets.QTableWidgetItem(vendedor["codigo"]))
        var.ui.tab_ven.setItem(index, 1, QtWidgets.QTableWidgetItem(vendedor["nombre"]))
        var.ui.tab_ven.setItem(index, 2, QtWidgets.QTableWidgetItem(" " + vendedor["movil"] + " "))
        var.ui.tab_ven.setItem(index, 3, QtWidgets.QTableWidgetItem(vendedor["provincia"]))

        var.ui.tab_ven.item(index, 0)
        var.ui.tab_ven.item(index, 1)
        var.ui.tab_ven.item(index, 2)
        var.ui.tab_ven.item(index, 3)

    def resize_cli_tab(self):
        try:
            header = var.ui.tab_cli.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 2 or i == 4 or i == 5):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items = var.ui.tab_cli.horizontalHeaderItem(i)
                font = header_items.font()
                font.setBold(True)
                header_items.setFont(font)
        except Exception as error:
            print("error en resize tabla clientes: " + error)

    def resize_pro_tab(self):
        try:
            header = var.ui.tab_pro.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 2):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items = var.ui.tab_pro.horizontalHeaderItem(i)
                font = header_items.font()
                font.setBold(True)
                header_items.setFont(font)
        except Exception as error:
            print("error en resize tabla propiedades: " + error)

    def resize_ven_tab(self):
        try:
            header = var.ui.tab_ven.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 3):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items = var.ui.tab_ven.horizontalHeaderItem(i)
                font = header_items.font()
                font.setBold(True)
                header_items.setFont(font)
        except Exception as error:
            print("Error en resize tabla vendedores: " + error)

    def crear_backup(self):
        try:
            fecha = datetime.now()
            fecha = fecha.strftime('%Y_/%m_/%d_%H_%M_%S')
            copia = str(fecha) + "_backup.zip"
            directorio, fichero = var.dlg_abrir.getSaveFileName(None, "Guardar Copia Seguridad", copia, '.zip')
            if var.dlg_abrir.accept and fichero:
                fichzip = zipfile.ZipFile(fichero, 'w')
                fichzip.write('bbdd.sqlite', os.path.basename('bbdd.sqlite'), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(fichero, directorio)

                Eventos.mensaje_exito("Copia de Seguridad", "Copia de seguridad guardada")

        except Exception as error:
            print("error en crear backup: ", error)

    def restaurar_backup(self):
        try:
            filename = var.dlg_abrir.getOpenFileName(None, "Restaurar Copia Seguridad", '', "*.zip;;All Files(*)")
            file = filename[0]

            if file:
                with zipfile.ZipFile(file, 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()

                Eventos.mensaje_exito("Copia de Seguridad", "Copia de seguridad restaurada")

                var.clase_conexion.db_conexion(self)
                Eventos.cargar_provincias(self)
                clientes.Clientes.cargar_cli_tab(self)
        except Exception as error:
            print("error en restaurar backup: ", error)

    def limpiar_panel():
        if var.ui.panel_principal.currentIndex() == 0:
            clientes.Clientes.inicializar_campos()
            objetos_panel_cli = clientes.Clientes.campos

            for key, value in objetos_panel_cli.items():
                if key == "provincia":
                    Eventos.cargar_provincias(value)
                elif key == "municipio":
                    pass
                else:
                    value.setText("")
            var.state_manager.change_state("last_cliente_function", var.clase_conexion.listar_clientes)

        if var.ui.panel_principal.currentIndex() == 1:
            propiedades.Propiedades.inicializar_campos()
            objetos_panel_pro = propiedades.Propiedades.campos

            for key, value in objetos_panel_pro.items():
                if key == "provincia":
                    Eventos.cargar_provincias(value)
                elif key == "municipio":
                    pass
                elif (key == "tipo" or key == "check_alquiler" or key == "check_venta" or key == "check_intercambio"
                or key == "radio_disponible" or key == "radio_alquilado" or key == "radio_vendido"):
                    if key == "check_alquiler" or key == "check_venta" or key == "check_intercambio":
                        value.setChecked(False)
                    if key == "radio_disponible":
                        value.setChecked(True)
                    if key == "radio_alquilado" or key == "radio_vendido":
                        value.setChecked(False)
                elif (key == "banos" or key == "habitaciones"):
                    value.setValue(0)
                else:
                    value.setText("")
            
            Eventos.cargar_propiedad_tipos(propiedades.Propiedades.campos["tipo"])
            var.state_manager.change_state("last_propiedad_function", var.clase_conexion.listar_propiedades)
            var.state_manager.change_state("precio_alquiler_propiedad", False)
            var.state_manager.change_state("precio_venta_propiedad", False)
            var.state_manager.change_state("check_alquiler_propiedad", False)
            var.state_manager.change_state("check_venta_propiedad", False)

        if var.ui.panel_principal.currentIndex() == 2:
            vendedores.Vendedores.inicializar_campos()
            objetos_panel_ven = vendedores.Vendedores.campos

            for key, value in objetos_panel_ven.items():
                if key == "provincia":
                    Eventos.cargar_provincias(value)
                else:
                    value.setText("")
            var.state_manager.change_state("last_vendedor_function", var.clase_conexion.listar_vendedores)

    def abrir_dlg_propiedades_tipo():
        try:
            var.dlg_gestion_propiedad_tipo.show()
        except Exception as error:
            print("error en abrir gestión propiedades ", error)

    def cargar_propiedad_tipos(cmb):
        registro = var.clase_conexion.cargar_propiedad_tipos()
        cmb.clear()
        for tipo in registro:
            if (isinstance(tipo, tuple)):
                cmb.addItem(tipo[0])
            else:
                cmb.addItem(tipo)

    def exportar_propiedades_csv(self):
        try:
            fecha = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
            file = (str(fecha) + '_DatosPropiedades.csv')
            directorio, fichero = var.dlg_abrir.getSaveFileName(None, "Exportar Datos en CSV", file, ".csv")

            if fichero:
                registros = var.clase_conexion.listar_propiedades(True)
                with open(fichero, 'w', newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(registros[0].keys())
                    for registro in registros:
                        writer.writerow(registro.values())

                shutil.move(fichero, directorio)

                Eventos.mensaje_exito("Aviso", "Fichero guardado")
            else:
                Eventos.mensaje_error("Aviso","Error al exportar las propiedades")
        except Exception as error:
            print("Error al exportar las propiedades ", error)

    def exportar_propiedades_json(self):
        try:
            fecha = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
            file = (str(fecha) + '_DatosPropiedades.json')
            directorio, fichero = var.dlg_abrir.getSaveFileName(None, "Exportar Datos en JSON", file, ".json")

            if fichero:
                registros = var.clase_conexion.listar_propiedades(True)
                with open(fichero, 'w', newline='', encoding="utf-8") as jsonfile:
                    json.dump(registros, jsonfile, ensure_ascii=False, indent=4)

                shutil.move(fichero, directorio)

                Eventos.mensaje_exito("Aviso", "Fichero guardado")
            else:
                Eventos.mensaje_error("Aviso", "Error al exportar las propiedades")
        except Exception as error:
            print("Error al exportar las propiedades ", error)

    def abrir_dlg_about():
        try:
            var.dlg_about.show()
        except Exception as error:
            print("Error al abrir la ventana de acerca de ", error)

    def avanzar_pagina_cliente():
        if var.state_manager.state["current_cli_pagina"] < len(var.state_manager.state["cliente_query_object"]) / var.state_manager.state["cliente_pagination"]:
            var.state_manager.change_state("current_cli_pagina", var.state_manager.state["current_cli_pagina"] + 1)
        else:
            pass

    def retroceder_pagina_cliente():
        if var.state_manager.state["current_cli_pagina"] > 0:
            var.state_manager.change_state("current_cli_pagina", var.state_manager.state["current_cli_pagina"] - 1)
        else:
            pass

    def avanzar_pagina_propiedad():
        if var.state_manager.state["current_pro_pagina"] < len(var.state_manager.state["propiedad_query_object"]) / var.state_manager.state["propiedad_pagination"]:
            var.state_manager.change_state("current_pro_pagina", var.state_manager.state["current_pro_pagina"] + 1)
        else:
            pass

    def retroceder_pagina_propiedad():
        if var.state_manager.state["current_pro_pagina"] > 0:
            var.state_manager.change_state("current_pro_pagina", var.state_manager.state["current_pro_pagina"] - 1)
        else:
            pass

    def comparar_fechas(fecha_alta, fecha_baja):
        formato = '%d/%m/%Y'
        if(not fecha_alta):
            return False
        if datetime.strptime(fecha_alta, formato) <= datetime.strptime(fecha_baja, formato):
            return True
        else:
            return False

    def abrir_dlg_buscar_propiedades():
        try:
            var.dlg_buscar_propiedad.show()
        except Exception as error:
            print("Error al abrir la ventana de acerca de ", error)