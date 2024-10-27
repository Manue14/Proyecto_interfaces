from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.uic.properties import QtCore

import clientes
import conexionserver
import var
import eventos
import conexion

class Clientes:
    @staticmethod
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

    @staticmethod
    def checkEmail():
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('''QLineEdit#txtEmailcli {background-color: #dbeafe;}
                                                 QLineEdit#txtEmailcli:focus {background-color: #bfdbfe;}''')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setText("correo no válido")
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)

    @staticmethod
    def checkPhone():
        try:
            phone = str(var.ui.txtMovilcli.text())

            if eventos.Eventos.validarPhone(phone):
                var.ui.txtMovilcli.setStyleSheet('background-color: rgb(255, 255, 255);')
            else:
                var.ui.txtMovilcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMovilcli.setText(None)
                var.ui.txtMovilcli.setText("móvil no válido")
                var.ui.txtMovilcli.setFocus()
        except Exception as error:
            print("error check cliente", error)

    def altaCliente(self):
        try:
            nuevocli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(), var.ui.txtNomcli.text(),
                    var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProcli.currentText(),
                    var.ui.cmbMunicli.currentText()]
            if conexion.Conexion.altaCliente(nuevocli):

                '''
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
                '''

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

    @staticmethod
    def cargaTablaClientes(self):
        try:
            listado = conexion.Conexion.listadoClientes(self)
            #listado = conexionserver.ConexionServer.listadoClientes(self)
            index = 0
            var.ui.tabClientes.verticalHeader().setVisible(False)
            for registro in listado:
                var.ui.tabClientes.setRowCount(index + 1)
                var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[3]))
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem("  " + registro[5] + "  "))
                var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(registro[7]))
                var.ui.tabClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(registro[8]))
                var.ui.tabClientes.setItem(index, 6, QtWidgets.QTableWidgetItem("  " + registro[9] + "  "))

                '''
                var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tabClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tabClientes.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                '''

                var.ui.tabClientes.item(index, 0)
                var.ui.tabClientes.item(index, 1)
                var.ui.tabClientes.item(index, 2)
                var.ui.tabClientes.item(index, 3)
                var.ui.tabClientes.item(index, 4)
                var.ui.tabClientes.item(index, 5)
                var.ui.tabClientes.item(index, 6)

                index += 1

        except Exception as e:
            print("error cargaTablaClientes", e)

    def cargaOneCliente(self):
        try:
            fila = var.ui.tabClientes.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneCliente(str(datos[0]))
            listado = [var.ui.txtDnicli, var.ui.txtAltacli, var.ui.txtApelcli,
                        var.ui.txtNomcli,
                        var.ui.txtEmailcli, var.ui.txtMovilcli, var.ui.txtDircli,
                        var.ui.cmbProcli,
                        var.ui.cmbMunicli]
            for i in range(len(listado)):
                if i == 7 or i == 8:
                    listado[i].setCurrentText(registro[i])
                else:
                    listado[i].setText(registro[i])
        except Exception as error:
            print("error cargaOneCliente", error)

    def modifCliente(self):
        try:
            modifcli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(), var.ui.txtNomcli.text(),
                    var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProcli.currentText(),
                    var.ui.cmbMunicli.currentText(), var.ui.txtBajacli.text()]
            if conexion.Conexion.modifCliente(modifcli):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Datos cliente modificados correctamente")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                mbox.exec()
                clientes.Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Error al modificar los datos del cliente")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                mbox.exec()
        except Exception as error:
            print("error modifCliente", error)

    def bajaCliente(self):
        try:
            datos = [var.ui.txtBajacli.text(), var.ui.txtDnicli.text()]
            if conexion.Conexion.bajaCliente(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Cliente dado de baja")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                mbox.exec()
                clientes.Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon("img/house.ico"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Error baja cliente: cliente no existe o dado de baja")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText("Aceptar")
                mbox.exec()
        except Exception as error:
            print("error bajaCliente", error)

    def historicoCli(self):
        try:
            if var.ui.chkHistoriacli.isChecked():
                var.historico = 0
            else:
                var.historico = 1
            Clientes.cargaTablaClientes(self)
        except Exception as Error:
            print("checkbox histórico", Error)

    def checkCampos(self):
        dni = var.ui.txtDnicli.text()
        apellido = var.ui.txtApelcli.text()
        email = var.ui.txtEmailcli.text()
        direccion = var.ui.txtDircli.tetx()
        fechaAlta = var.ui.txtAltacli.text()
        nombre = var.ui.txtNomcli.text()
        movil = var.ui.txtMovilcli.text()
        provincia = var.ui.cmbProcli.currentText()
        municipio = var.ui.cmbMunicli.currentText()

        if (not eventos.Eventos.checkDNI(dni) or not
        eventos.Eventos.validarMail(email) or not eventos.Eventos.validarPhone(movil)):
            return False

        if (not dni.strip() or not apellido.strip() or not direccion.strip() or not fechaAlta.strip()
        or not nombre.strip() or not movil.strip() or not provincia.strip() or not municipio.strip()):
            return False

        return True