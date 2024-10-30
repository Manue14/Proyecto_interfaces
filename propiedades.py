from PyQt6.uic.properties import QtWidgets, QtGui

import conexion
import eventos
import var
import dlgGestipoprop

class Propiedades():
    def altaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text()
            registro = conexion.Conexion.altaTipoprop(tipo)
            if registro:
                eventos.Eventos.cargarTipoprop(self)
            else:
                print("Ya existe")
            var.dlggestion.ui.txtGestipoprop.setText("")
        except Exception as e:
            print(f"Error: {e}")

    def bajaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text()
            if conexion.Conexion.bajaTipoprop(tipo):
                eventos.Eventos.cargarTipoprop(self)
                print("baja")
            else:
                print("No existe")
            var.dlggestion.ui.txtGestipoprop.setText("")
        except Exception as e:
            print(f"Error: {e}")


    def altaPropiedad(self):
        try:
            propiedad = [var.ui.txtFechaprop.text(),var.ui.txtFechabajaprop.text(), var.ui.txtDirprop.text(), var.ui.cmbProvprop.currentText(),
                         var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(), var.ui.spinHabprop.text(),
                         var.ui.spinBanosprop.text(), var.ui.txtSuperprop.text(), var.ui.txtPrecioalquilerprop.text(),
                         var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(), var.ui.areatxtDescriprop.toPlainText()]
            tipooper = []
            if var.ui.chkAlquiprop.isChecked():
                tipooper.append(var.ui.chkAlquiprop.text())
            if var.ui.chkVentaprop.isChecked():
                tipooper.append(var.ui.chkVentaprop.text())
            if var.ui.chkInterprop.isChecked():
                tipooper.append(var.ui.chkInterprop.text())
            propiedad.append(tipooper)

            if var.ui.rbtDisprop.isChecked():
                propiedad.append(var.ui.rbtDisprop.text())
            elif var.ui.rbtAlquiprop.isChecked():
                propiedad.append(var.ui.rbtAlquiprop.text())
            elif var.ui.rbtVendiprop.isChecked():
                propiedad.append(var.ui.rbtVendiprop.text())

            propiedad.append(var.ui.txtNomeprop.text())
            propiedad.append(var.ui.txtMovilprop.text())
            conexion.Conexion.altaPropiedad(propiedad)
        except Exception as e:
            print("error en en alta de una propiedad")

    def bajaPropiedad(self):
        print("a")