import sys
import time

import var
from PyQt6 import QtWidgets, QtGui

import conexion


class Eventos():
    def mensajeSalir(self=None):
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

    def cargar_muni_cli(self, provId = 1):
        var.ui.cmbMunicli.clear()
        listado = conexion.Conexion.list_mun_by_prov(provId)
        for mun in listado:
            var.ui.cmbMunicli.addItem(mun[0], mun[1])

    def cargarProv(self):
        var.ui.cmbProcli.clear()
        listado = conexion.Conexion.list_prov(self)
        for prov in listado:
            var.ui.cmbProcli.addItem(prov[1], prov[0])

    def dniTextBoxChecker(self):
        var.ui.txtDnicli.textChanged.connect(lambda: Eventos.changeStyleDNI(Eventos, var.ui.txtDnicli.text(), var.ui.txtDnicli))

    @staticmethod
    def checkDNI(cls, dni: str):
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

    @staticmethod
    def changeStyleDNI(cls, dni: str, object):
        if cls.checkDNI(cls, dni):
            object.setStyleSheet("background-color: #90EE90;")
        else:
            if not dni:
                object.setStyleSheet("background-color: #FFFCDC;")
            else:
                object.setStyleSheet("background-color: #FFCCCB;")

    def abrirCalendar(op):
        try:
            var.panel = op
            var.uicalendar.show()
        except Exception as error:
            print("error en abrir calendar ", error)

    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.panel == var.ui.panPrincipal.currentIndex():
                var.ui.txtAltacli.setText(str(data))
            time.sleep(0.5)
            var.uicalendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)
