import sys
import time
import re
from datetime import datetime
import os

import clientes
import propiedades
import var
from PyQt6 import QtWidgets, QtGui
import conexion
import locale
import zipfile
import shutil
import conexion_server
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
        mbox.setText(mensaje)
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
        mbox.exec()

    def cargar_municipios_cli(self, provId = 1):
        var.ui.cmb_cli_municipio.clear()
        listado = conexion.Conexion.listar_municipios(provId)
        #listado = conexionserver.ConexionServer.listar_municipios(provId)
        for mun in listado:
            var.ui.cmb_cli_municipio.addItem(mun[0], mun[1])

    def cargar_municipios_pro(self, provId = 1):
        var.ui.cmb_pro_municipio.clear()
        listado = conexion.Conexion.listar_municipios(provId)
        #listado = conexionserver.ConexionServer.listar_municipios(provId)
        for mun in listado:
            var.ui.cmb_pro_municipio.addItem(mun[0], mun[1])

    def cargar_municipios_pro_filtrar(self, provId = 1):
        var.dlg_filtrar_propiedades.ui.cmb_pro_municipio_filtrar.clear()
        listado = conexion.Conexion.listar_municipios(provId)
        #listado = conexionserver.ConexionServer.listar_municipios(provId)
        for mun in listado:
            var.dlg_filtrar_propiedades.ui.cmb_pro_municipio_filtrar.addItem(mun[0], mun[1])

    def cargar_provincias(self):
        var.ui.cmb_cli_provincia.clear()
        var.ui.cmb_pro_provincia.clear()
        var.dlg_filtrar_propiedades.ui.cmb_pro_provincia_filtrar.clear()
        listado = conexion.Conexion.listar_provincias(self)
        #listado = conexionserver.ConexionServer.listar_provincias(self)
        for prov in listado:
            var.ui.cmb_cli_provincia.addItem(prov[1], prov[0])
            var.ui.cmb_pro_provincia.addItem(prov[1], prov[0])
            var.dlg_filtrar_propiedades.ui.cmb_pro_provincia_filtrar.addItem(prov[1], prov[0])

    def validar_dni(dni: str):
        valid_letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9 :
            return False
        number_part = dni[0:8]
        if not number_part.isdigit() :
            return False
        correct_letter = valid_letters[int(number_part) % 23]
        if dni[8] != correct_letter:
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
                var.ui.txt_cli_alta.setStyleSheet('''QLineEdit#txt_cli_alta {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_cli_alta:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            elif var.ui.panel_principal.currentIndex() == 0 and var.btn == 1:
                var.ui.txt_cli_baja.setText(str(data))
                var.ui.txt_cli_baja.setStyleSheet('''QLineEdit#txt_cli_baja {border-bottom: 1px solid #93c5fd;
                                                                                background-color: #dbeafe;}
                                                        QLineEdit#txt_cli_baja:focus {border-bottom: 1.5px solid #2563eb;
                                                                                        background-color: #bfdbfe;}''')
            elif var.ui.panel_principal.currentIndex() == 1 and var.btn == 0:
                var.ui.txt_pro_alta.setText(str(data))
                var.ui.txt_pro_alta.setStyleSheet('''QLineEdit#txt_pro_alta {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_pro_alta:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            elif var.ui.panel_principal.currentIndex() == 1 and var.btn == 1:
                var.ui.txt_pro_baja.setText(str(data))
                var.ui.txt_pro_baja.setStyleSheet('''QLineEdit#txt_pro_baja {border-bottom: 1px solid #93c5fd;
                                                                                background-color: #dbeafe;}
                                                        QLineEdit#txt_pro_baja:focus {border-bottom: 1.5px solid #2563eb;
                                                                                        background-color: #bfdbfe;}''')
            time.sleep(0.5)
            var.ui_calendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)
        
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

                conexion.Conexion.db_conexion(self)
                Eventos.cargar_provincias(self)
                clientes.Clientes.cargar_cli_tab(self)
        except Exception as error:
            print("error en restaurar backup: ", error)

    def limpiar_panel(self):
        if var.ui.panel_principal.currentIndex() == 0:
            clientes.Clientes.inicializar_campos()
            objetos_panel_cli = clientes.Clientes.campos

            for key, value in objetos_panel_cli.items():
                if key == "provincia" or key == "municipio":
                    pass
                else:
                    value.setText("")

        if var.ui.panel_principal.currentIndex() == 1:
            propiedades.Propiedades.inicializar_campos()
            objetos_panel_pro = propiedades.Propiedades.campos

            for key, value in objetos_panel_pro.items():
                if (key == "provincia" or key == "municipio" or key == "tipo"
                or key == "check_alquiler" or key == "check_venta" or key == "check_intercambio"
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
            Eventos.cargar_propiedad_tipos(var.dlg_filtrar_propiedades.ui.cmb_pro_tipo_filtrar)

        Eventos.limpiar_provincias_municipios(self)
        propiedades.Propiedades.cargar_pro_tab()

    def limpiar_provincias_municipios(self):
        listado = conexion.Conexion.listar_provincias(self)
        #listado = conexionserver.ConexionServer.listar_provincias(self)

        if var.ui.panel_principal.currentIndex() == 0:
            var.ui.cmb_cli_provincia.clear()
            for prov in listado:
                var.ui.cmb_cli_provincia.addItem(prov[1], prov[0])

        if var.ui.panel_principal.currentIndex() == 1:
            var.ui.cmb_pro_provincia.clear()
            var.dlg_filtrar_propiedades.ui.cmb_pro_provincia_filtrar.clear()
            for prov in listado:
                var.ui.cmb_pro_provincia.addItem(prov[1], prov[0])
                var.dlg_filtrar_propiedades.ui.cmb_pro_provincia_filtrar.addItem(prov[1], prov[0])

    def abrir_dlg_propiedades_tipo():
        try:
            var.dlg_gestion_propiedad_tipo.show()
        except Exception as error:
            print("error en abrir gestión propiedades ", error)

    def abrir_dlg_filtrar_propiedades():
        try:
            var.dlg_filtrar_propiedades.show()
        except Exception as error:
            print("error en abrir filtrado propiedades ", error)

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

    def cargar_propiedad_tipos(cmb):
        registro = conexion.Conexion.cargar_propiedad_tipos()
        cmb.clear()
        cmb.addItems(registro)