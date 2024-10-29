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
                         var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(), var.ui.areatxtDescriprop.toPlainText(),
                         var.ui.txtNomeprop.text(), var.ui.txtMovilprop.text()]
            print(propiedad)
        except Exception as e:
            print(e)

    def bajaPropiedad(self):
        print("a")