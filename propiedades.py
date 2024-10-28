import var
import dlgGestipoprop

class Propiedades():
    def altaTipopropiedad(self):
        tipo = var.dlggestion.txtGestipoprop.text()
        print(tipo)

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