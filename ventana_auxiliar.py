from datetime import datetime
from dlg_calendar import *
from dlg_gestion_propiedad_tipo import *
from dlg_about import *
import var
import eventos
import propiedades
import styles

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.ui_calendar = Ui_DlgCalendar()
        var.ui_calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

        var.ui_calendar.Calendar.setSelectedDate((QtCore.QDate(ano,mes,dia)))
        var.ui_calendar.Calendar.clicked.connect(eventos.Eventos.cargar_fecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()

class DlgGestionPropiedadTipo(QtWidgets.QDialog):
    def __init__(self):
        super(DlgGestionPropiedadTipo, self).__init__()
        self.ui = Ui_DlgGestionPropiedadTipo()
        self.ui.setupUi(self)
        self.setStyleSheet(styles.load_stylesheet())
        self.ui.btn_pro_tipo_alta.clicked.connect(propiedades.Propiedades.alta_tipo_propiedad)
        self.ui.btn_pro_tipo_eliminar.clicked.connect(propiedades.Propiedades.baja_tipo_propiedad)

class DlgAbout(QtWidgets.QDialog):
    def __init__(self):
        super(DlgAbout, self).__init__()
        self.ui = Ui_DlgAbout()
        self.ui.setupUi(self)
        self.setStyleSheet(styles.load_stylesheet())
        self.ui.btn_cerrar_about.clicked.connect(self.close)
