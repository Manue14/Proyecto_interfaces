from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
import var
import eventos
import conexion

class Clientes:
    def checkDni():
        try:
            dni = str(var.ui.txtDnicli.text())
            if eventos.Eventos.checkDNI(dni):
                var.ui.txtDnicli.setStyleSheet("background-color: #90EE90;")
                var.ui.txtDnicli.setText(dni.upper())
            else:
                var.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtDnicli.setText(None)
        except Exception as error:
            print("error check dni cliente", error)

    def checkEmail(mail):
        try:
            mail = str(var.ui.txtEmailCli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailCli.setStyleSheet('background-color: rgb(255, 255, 255);')
                var.ui.txtEmailCli.setText(mail.lower())

            else:
                var.ui.txtEmailCli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailCli.setText(None)
                var.ui.txtEmailCli.setText("correo no válido")
                var.ui.txtEmailCli.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def altaCliente(self):
        try:
            nuevocli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(), var.ui.txtNomcli.text(),
                    var.ui.txtEmailCli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProcli.currentText(),
                    var.ui.cmbMunicli.currentText()]
            if conexion.Conexion.altaCliente(nuevocli):
                var.ui.tabClientes.clear()
                var.ui.tabClientes.setRowCount(1)
                var.ui.tabClientes.setColumnCount(len(nuevocli))
                var.ui.tabClientes.setHorizontalHeaderLabels(("DNI", "Fecha Alta", "Apellidos", "Nombre", "Email", "Móvil", "Dirección", "Provincia", "Municipio"))
                columna = 0
                tableWidth = var.ui.tabClientes.viewport().width()
                for value in nuevocli:
                    item = QTableWidgetItem(value)
                    var.ui.tabClientes.setColumnWidth(columna, tableWidth // len(nuevocli))
                    var.ui.tabClientes.setItem(0, columna, item)
                    columna += 1

                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Alta cliente en la base de datos")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Error faltan datos o el cliente existe")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()

        except Exception as error:
            print("error alta cliente", error)