import sys
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

    def cargarProv(self):
        var.ui.cmbProcli.clear()
        listado = conexion.Conexion.listProv(self)
        var.ui.cmbProcli.addItems(listado)

    def cargarMuni(self):
        var.ui.cmbMunicli.clear()
        listado = conexion.Conexion.listMuni(self)
        var.ui.cmbMunicli.addItems(listado)

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
            object.setStyleSheet(f"background-color: #90EE90;")
        else:
            if not dni:
                object.setStyleSheet(f"background-color: #FFFCDC;")
            else:
                object.setStyleSheet(f"background-color: #FFCCCB;")