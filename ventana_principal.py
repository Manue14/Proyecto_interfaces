# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolBar, QVBoxLayout, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(2153, 1210)
        VentanaPrincipal.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"img/house.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        VentanaPrincipal.setWindowIcon(icon)
        self.action_archivo_salir = QAction(VentanaPrincipal)
        self.action_archivo_salir.setObjectName(u"action_archivo_salir")
        self.action_archivo_backup_crear = QAction(VentanaPrincipal)
        self.action_archivo_backup_crear.setObjectName(u"action_archivo_backup_crear")
        self.action_archivo_backup_restaurar = QAction(VentanaPrincipal)
        self.action_archivo_backup_restaurar.setObjectName(u"action_archivo_backup_restaurar")
        self.action_tool_salir = QAction(VentanaPrincipal)
        self.action_tool_salir.setObjectName(u"action_tool_salir")
        icon1 = QIcon()
        icon1.addFile(u"../img/exit-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_tool_salir.setIcon(icon1)
        self.action_tool_limpiar = QAction(VentanaPrincipal)
        self.action_tool_limpiar.setObjectName(u"action_tool_limpiar")
        icon2 = QIcon()
        icon2.addFile(u"../img/clear-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_tool_limpiar.setIcon(icon2)
        self.action_tool_gestionar_tipos_propiedad = QAction(VentanaPrincipal)
        self.action_tool_gestionar_tipos_propiedad.setObjectName(u"action_tool_gestionar_tipos_propiedad")
        icon3 = QIcon()
        icon3.addFile(u"../img/gear-building-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_tool_gestionar_tipos_propiedad.setIcon(icon3)
        self.action_gestion_propiedades_tipo = QAction(VentanaPrincipal)
        self.action_gestion_propiedades_tipo.setObjectName(u"action_gestion_propiedades_tipo")
        self.action_tool_filtrar_propiedades = QAction(VentanaPrincipal)
        self.action_tool_filtrar_propiedades.setObjectName(u"action_tool_filtrar_propiedades")
        icon4 = QIcon()
        icon4.addFile(u"../img/search-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_tool_filtrar_propiedades.setIcon(icon4)
        self.action_exportar_propiedades_CSV = QAction(VentanaPrincipal)
        self.action_exportar_propiedades_CSV.setObjectName(u"action_exportar_propiedades_CSV")
        self.action_exportar_propiedades_JSON = QAction(VentanaPrincipal)
        self.action_exportar_propiedades_JSON.setObjectName(u"action_exportar_propiedades_JSON")
        self.action_abrir_about = QAction(VentanaPrincipal)
        self.action_abrir_about.setObjectName(u"action_abrir_about")
        self.action_listado_clientes = QAction(VentanaPrincipal)
        self.action_listado_clientes.setObjectName(u"action_listado_clientes")
        self.action_listado_propiedades = QAction(VentanaPrincipal)
        self.action_listado_propiedades.setObjectName(u"action_listado_propiedades")
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.panel_principal = QTabWidget(self.centralwidget)
        self.panel_principal.setObjectName(u"panel_principal")
        self.panel_principal.setMinimumSize(QSize(0, 0))
        self.panel_principal.setMaximumSize(QSize(16777215, 1500))
        self.panel_principal.setStyleSheet(u"")
        self.pestana_clientes = QWidget()
        self.pestana_clientes.setObjectName(u"pestana_clientes")
        self.gridLayout_3 = QGridLayout(self.pestana_clientes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.btn_cli_grabar = QPushButton(self.pestana_clientes)
        self.btn_cli_grabar.setObjectName(u"btn_cli_grabar")
        self.btn_cli_grabar.setMinimumSize(QSize(80, 25))
        self.btn_cli_grabar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout.addWidget(self.btn_cli_grabar)

        self.btn_cli_modificar = QPushButton(self.pestana_clientes)
        self.btn_cli_modificar.setObjectName(u"btn_cli_modificar")
        self.btn_cli_modificar.setMinimumSize(QSize(80, 25))
        self.btn_cli_modificar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout.addWidget(self.btn_cli_modificar)

        self.btn_cli_eliminar = QPushButton(self.pestana_clientes)
        self.btn_cli_eliminar.setObjectName(u"btn_cli_eliminar")
        self.btn_cli_eliminar.setMinimumSize(QSize(80, 25))
        self.btn_cli_eliminar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout.addWidget(self.btn_cli_eliminar)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.line = QFrame(self.pestana_clientes)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.pestana_clientes)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_9.addWidget(self.label_5)

        self.lbl_cli_nombre = QLabel(self.pestana_clientes)
        self.lbl_cli_nombre.setObjectName(u"lbl_cli_nombre")
        self.lbl_cli_nombre.setMinimumSize(QSize(0, 0))
        self.lbl_cli_nombre.setMaximumSize(QSize(70, 16777215))
        self.lbl_cli_nombre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lbl_cli_nombre)


        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 3, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_8 = QSpacerItem(85, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.label_6 = QLabel(self.pestana_clientes)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_10.addWidget(self.label_6)

        self.lbl_cli_movil = QLabel(self.pestana_clientes)
        self.lbl_cli_movil.setObjectName(u"lbl_cli_movil")
        self.lbl_cli_movil.setMaximumSize(QSize(45, 16777215))
        self.lbl_cli_movil.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lbl_cli_movil)


        self.gridLayout.addLayout(self.horizontalLayout_10, 6, 3, 1, 1)

        self.lbl_cli_baja = QLabel(self.pestana_clientes)
        self.lbl_cli_baja.setObjectName(u"lbl_cli_baja")
        self.lbl_cli_baja.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_cli_baja, 2, 10, 1, 1)

        self.cmb_cli_provincia = QComboBox(self.pestana_clientes)
        self.cmb_cli_provincia.setObjectName(u"cmb_cli_provincia")
        self.cmb_cli_provincia.setMinimumSize(QSize(350, 0))
        self.cmb_cli_provincia.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.cmb_cli_provincia, 8, 6, 1, 5)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.txt_cli_alta = QLineEdit(self.pestana_clientes)
        self.txt_cli_alta.setObjectName(u"txt_cli_alta")
        self.txt_cli_alta.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_cli_alta.sizePolicy().hasHeightForWidth())
        self.txt_cli_alta.setSizePolicy(sizePolicy)
        self.txt_cli_alta.setMinimumSize(QSize(115, 0))
        self.txt_cli_alta.setMaximumSize(QSize(115, 16777215))
        self.txt_cli_alta.setAlignment(Qt.AlignCenter)
        self.txt_cli_alta.setReadOnly(False)

        self.horizontalLayout_15.addWidget(self.txt_cli_alta)

        self.btn_cli_alta = QPushButton(self.pestana_clientes)
        self.btn_cli_alta.setObjectName(u"btn_cli_alta")
        self.btn_cli_alta.setMinimumSize(QSize(30, 30))
        self.btn_cli_alta.setMaximumSize(QSize(30, 30))
        self.btn_cli_alta.setStyleSheet(u"background-color: transparent; border: none;")
        icon5 = QIcon()
        icon5.addFile(u"../img/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cli_alta.setIcon(icon5)
        self.btn_cli_alta.setIconSize(QSize(30, 30))

        self.horizontalLayout_15.addWidget(self.btn_cli_alta)


        self.gridLayout.addLayout(self.horizontalLayout_15, 2, 4, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_4 = QLabel(self.pestana_clientes)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_8.addWidget(self.label_4)

        self.lbl_cli_alta = QLabel(self.pestana_clientes)
        self.lbl_cli_alta.setObjectName(u"lbl_cli_alta")
        self.lbl_cli_alta.setMinimumSize(QSize(0, 0))
        self.lbl_cli_alta.setMaximumSize(QSize(100, 16777215))
        self.lbl_cli_alta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lbl_cli_alta)


        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 7, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_cli_dni = QLineEdit(self.pestana_clientes)
        self.txt_cli_dni.setObjectName(u"txt_cli_dni")
        sizePolicy.setHeightForWidth(self.txt_cli_dni.sizePolicy().hasHeightForWidth())
        self.txt_cli_dni.setSizePolicy(sizePolicy)
        self.txt_cli_dni.setMinimumSize(QSize(90, 0))
        self.txt_cli_dni.setMaximumSize(QSize(90, 16777215))
        self.txt_cli_dni.setStyleSheet(u"")
        self.txt_cli_dni.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_cli_dni, 0, Qt.AlignLeft)

        self.btn_cli_buscar = QPushButton(self.pestana_clientes)
        self.btn_cli_buscar.setObjectName(u"btn_cli_buscar")
        self.btn_cli_buscar.setMaximumSize(QSize(30, 16777215))
        self.btn_cli_buscar.setStyleSheet(u"background-color: transparent; border: none;")
        self.btn_cli_buscar.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_cli_buscar, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.pestana_clientes)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_5.addWidget(self.label)

        self.lbl_cli_dni = QLabel(self.pestana_clientes)
        self.lbl_cli_dni.setObjectName(u"lbl_cli_dni")
        self.lbl_cli_dni.setMinimumSize(QSize(0, 0))
        self.lbl_cli_dni.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_cli_dni.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.lbl_cli_dni)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.chk_cli_historico = QCheckBox(self.pestana_clientes)
        self.chk_cli_historico.setObjectName(u"chk_cli_historico")

        self.gridLayout.addWidget(self.chk_cli_historico, 2, 13, 1, 1)

        self.txt_cli_direccion = QLineEdit(self.pestana_clientes)
        self.txt_cli_direccion.setObjectName(u"txt_cli_direccion")
        self.txt_cli_direccion.setMinimumSize(QSize(350, 0))
        self.txt_cli_direccion.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.txt_cli_direccion, 8, 1, 1, 3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.txt_cli_baja = QLineEdit(self.pestana_clientes)
        self.txt_cli_baja.setObjectName(u"txt_cli_baja")
        self.txt_cli_baja.setEnabled(True)
        sizePolicy.setHeightForWidth(self.txt_cli_baja.sizePolicy().hasHeightForWidth())
        self.txt_cli_baja.setSizePolicy(sizePolicy)
        self.txt_cli_baja.setMinimumSize(QSize(115, 0))
        self.txt_cli_baja.setMaximumSize(QSize(115, 16777215))
        self.txt_cli_baja.setAlignment(Qt.AlignCenter)
        self.txt_cli_baja.setReadOnly(False)

        self.horizontalLayout_14.addWidget(self.txt_cli_baja)

        self.btn_cli_baja = QPushButton(self.pestana_clientes)
        self.btn_cli_baja.setObjectName(u"btn_cli_baja")
        self.btn_cli_baja.setMinimumSize(QSize(30, 30))
        self.btn_cli_baja.setMaximumSize(QSize(30, 30))
        self.btn_cli_baja.setStyleSheet(u"background-color: transparent; border: none;")
        self.btn_cli_baja.setIcon(icon5)
        self.btn_cli_baja.setIconSize(QSize(29, 29))

        self.horizontalLayout_14.addWidget(self.btn_cli_baja)


        self.gridLayout.addLayout(self.horizontalLayout_14, 2, 11, 1, 1)

        self.txt_cli_movil = QLineEdit(self.pestana_clientes)
        self.txt_cli_movil.setObjectName(u"txt_cli_movil")
        self.txt_cli_movil.setMinimumSize(QSize(115, 0))
        self.txt_cli_movil.setMaximumSize(QSize(115, 16777215))
        self.txt_cli_movil.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cli_movil, 6, 4, 1, 1)

        self.txt_cli_apellido = QLineEdit(self.pestana_clientes)
        self.txt_cli_apellido.setObjectName(u"txt_cli_apellido")
        self.txt_cli_apellido.setMinimumSize(QSize(200, 0))
        self.txt_cli_apellido.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.txt_cli_apellido, 4, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.label_8 = QLabel(self.pestana_clientes)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_12.addWidget(self.label_8)

        self.lbl_cli_provincia = QLabel(self.pestana_clientes)
        self.lbl_cli_provincia.setObjectName(u"lbl_cli_provincia")
        self.lbl_cli_provincia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lbl_cli_provincia)


        self.gridLayout.addLayout(self.horizontalLayout_12, 8, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 13, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.pestana_clientes)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lbl_cli_direccion = QLabel(self.pestana_clientes)
        self.lbl_cli_direccion.setObjectName(u"lbl_cli_direccion")
        self.lbl_cli_direccion.setMinimumSize(QSize(0, 0))
        self.lbl_cli_direccion.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.lbl_cli_direccion)


        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 13, 1, 1)

        self.txt_cli_email = QLineEdit(self.pestana_clientes)
        self.txt_cli_email.setObjectName(u"txt_cli_email")
        self.txt_cli_email.setMinimumSize(QSize(250, 0))
        self.txt_cli_email.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.txt_cli_email, 6, 1, 1, 1)

        self.cmb_cli_municipio = QComboBox(self.pestana_clientes)
        self.cmb_cli_municipio.setObjectName(u"cmb_cli_municipio")
        self.cmb_cli_municipio.setMinimumSize(QSize(350, 0))
        self.cmb_cli_municipio.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.cmb_cli_municipio, 8, 12, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_10 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.label_9 = QLabel(self.pestana_clientes)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_13.addWidget(self.label_9)

        self.lbl_cli_municipio = QLabel(self.pestana_clientes)
        self.lbl_cli_municipio.setObjectName(u"lbl_cli_municipio")
        self.lbl_cli_municipio.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.lbl_cli_municipio)


        self.gridLayout.addLayout(self.horizontalLayout_13, 8, 11, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 13, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_21)

        self.label_28 = QLabel(self.pestana_clientes)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_28)

        self.label_29 = QLabel(self.pestana_clientes)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_35.addWidget(self.label_29)

        self.label_30 = QLabel(self.pestana_clientes)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_30)


        self.gridLayout.addLayout(self.horizontalLayout_35, 0, 12, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.pestana_clientes)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.lbl_cli_apellido = QLabel(self.pestana_clientes)
        self.lbl_cli_apellido.setObjectName(u"lbl_cli_apellido")
        self.lbl_cli_apellido.setMinimumSize(QSize(0, 0))
        self.lbl_cli_apellido.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_cli_apellido)


        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

        self.txt_cli_nombre = QLineEdit(self.pestana_clientes)
        self.txt_cli_nombre.setObjectName(u"txt_cli_nombre")
        self.txt_cli_nombre.setMinimumSize(QSize(200, 0))
        self.txt_cli_nombre.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.txt_cli_nombre, 4, 4, 1, 3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.pestana_clientes)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lbl_cli_email = QLabel(self.pestana_clientes)
        self.lbl_cli_email.setObjectName(u"lbl_cli_email")
        self.lbl_cli_email.setMinimumSize(QSize(0, 0))
        self.lbl_cli_email.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.lbl_cli_email)


        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 12, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.line_2 = QFrame(self.pestana_clientes)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 8, 0, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_24)

        self.btn_cli_anterior = QPushButton(self.pestana_clientes)
        self.btn_cli_anterior.setObjectName(u"btn_cli_anterior")
        sizePolicy.setHeightForWidth(self.btn_cli_anterior.sizePolicy().hasHeightForWidth())
        self.btn_cli_anterior.setSizePolicy(sizePolicy)
        self.btn_cli_anterior.setMinimumSize(QSize(80, 25))
        self.btn_cli_anterior.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_37.addWidget(self.btn_cli_anterior)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_26)

        self.lbl_cli_pagina = QLabel(self.pestana_clientes)
        self.lbl_cli_pagina.setObjectName(u"lbl_cli_pagina")

        self.horizontalLayout_37.addWidget(self.lbl_cli_pagina)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_30)

        self.btn_cli_siguiente = QPushButton(self.pestana_clientes)
        self.btn_cli_siguiente.setObjectName(u"btn_cli_siguiente")
        sizePolicy.setHeightForWidth(self.btn_cli_siguiente.sizePolicy().hasHeightForWidth())
        self.btn_cli_siguiente.setSizePolicy(sizePolicy)
        self.btn_cli_siguiente.setMinimumSize(QSize(80, 25))
        self.btn_cli_siguiente.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_37.addWidget(self.btn_cli_siguiente)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_25)


        self.gridLayout_3.addLayout(self.horizontalLayout_37, 9, 0, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_28 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_28)

        self.tab_cli = QTableWidget(self.pestana_clientes)
        if (self.tab_cli.columnCount() < 7):
            self.tab_cli.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_cli.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_cli.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_cli.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tab_cli.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tab_cli.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tab_cli.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tab_cli.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tab_cli.setObjectName(u"tab_cli")
        self.tab_cli.setMaximumSize(QSize(16777215, 600))
        self.tab_cli.setStyleSheet(u"")
        self.tab_cli.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_cli.setAlternatingRowColors(True)
        self.tab_cli.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab_cli.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_32.addWidget(self.tab_cli)

        self.horizontalSpacer_29 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_29)


        self.gridLayout_3.addLayout(self.horizontalLayout_32, 4, 0, 1, 1)

        self.panel_principal.addTab(self.pestana_clientes, "")
        self.pestana_propiedades = QWidget()
        self.pestana_propiedades.setObjectName(u"pestana_propiedades")
        self.gridLayout_4 = QGridLayout(self.pestana_propiedades)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.txt_pro_movil = QLineEdit(self.pestana_propiedades)
        self.txt_pro_movil.setObjectName(u"txt_pro_movil")
        self.txt_pro_movil.setMinimumSize(QSize(110, 0))
        self.txt_pro_movil.setMaximumSize(QSize(110, 16777215))
        self.txt_pro_movil.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_pro_movil, 8, 11, 1, 1)

        self.cmb_pro_tipo = QComboBox(self.pestana_propiedades)
        self.cmb_pro_tipo.setObjectName(u"cmb_pro_tipo")

        self.gridLayout_7.addWidget(self.cmb_pro_tipo, 4, 1, 1, 2)

        self.lbl_pro_baja = QLabel(self.pestana_propiedades)
        self.lbl_pro_baja.setObjectName(u"lbl_pro_baja")
        self.lbl_pro_baja.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_pro_baja, 0, 10, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.pestana_propiedades)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_18.addWidget(self.label_13)

        self.lbl_pro_tipo = QLabel(self.pestana_propiedades)
        self.lbl_pro_tipo.setObjectName(u"lbl_pro_tipo")

        self.horizontalLayout_18.addWidget(self.lbl_pro_tipo)


        self.gridLayout_7.addLayout(self.horizontalLayout_18, 4, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_14)

        self.label_17 = QLabel(self.pestana_propiedades)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_24.addWidget(self.label_17)

        self.lbl_pro_municipio = QLabel(self.pestana_propiedades)
        self.lbl_pro_municipio.setObjectName(u"lbl_pro_municipio")
        self.lbl_pro_municipio.setMinimumSize(QSize(70, 0))
        self.lbl_pro_municipio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.lbl_pro_municipio)


        self.gridLayout_7.addLayout(self.horizontalLayout_24, 2, 12, 1, 1)

        self.txt_pro_postal = QLineEdit(self.pestana_propiedades)
        self.txt_pro_postal.setObjectName(u"txt_pro_postal")
        self.txt_pro_postal.setMinimumSize(QSize(80, 0))
        self.txt_pro_postal.setMaximumSize(QSize(80, 16777215))
        self.txt_pro_postal.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_pro_postal, 2, 19, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_10, 3, 0, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_25 = QLabel(self.pestana_propiedades)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_25)

        self.label_26 = QLabel(self.pestana_propiedades)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_33.addWidget(self.label_26)

        self.label_27 = QLabel(self.pestana_propiedades)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_33.addWidget(self.label_27)


        self.gridLayout_7.addLayout(self.horizontalLayout_33, 0, 18, 1, 2)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_20 = QLabel(self.pestana_propiedades)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_27.addWidget(self.label_20)

        self.lbl_pro_habitaciones = QLabel(self.pestana_propiedades)
        self.lbl_pro_habitaciones.setObjectName(u"lbl_pro_habitaciones")
        self.lbl_pro_habitaciones.setMinimumSize(QSize(100, 0))
        self.lbl_pro_habitaciones.setMaximumSize(QSize(100, 16777215))
        self.lbl_pro_habitaciones.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.lbl_pro_habitaciones)


        self.gridLayout_7.addLayout(self.horizontalLayout_27, 4, 5, 1, 1)

        self.lbl_separator = QLabel(self.pestana_propiedades)
        self.lbl_separator.setObjectName(u"lbl_separator")
        self.lbl_separator.setMaximumSize(QSize(8, 16777215))
        self.lbl_separator.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lbl_separator, 4, 16, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_9 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_9)

        self.label_7 = QLabel(self.pestana_propiedades)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_23.addWidget(self.label_7)

        self.lbl_pro_provincia = QLabel(self.pestana_propiedades)
        self.lbl_pro_provincia.setObjectName(u"lbl_pro_provincia")
        self.lbl_pro_provincia.setMinimumSize(QSize(70, 0))
        self.lbl_pro_provincia.setMaximumSize(QSize(0, 16777215))
        self.lbl_pro_provincia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.lbl_pro_provincia)


        self.gridLayout_7.addLayout(self.horizontalLayout_23, 2, 7, 1, 1)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_19 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_19)

        self.label_24 = QLabel(self.pestana_propiedades)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_31.addWidget(self.label_24)

        self.lbl_pro_estado = QLabel(self.pestana_propiedades)
        self.lbl_pro_estado.setObjectName(u"lbl_pro_estado")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_pro_estado.sizePolicy().hasHeightForWidth())
        self.lbl_pro_estado.setSizePolicy(sizePolicy1)
        self.lbl_pro_estado.setMaximumSize(QSize(60, 16777215))
        self.lbl_pro_estado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.lbl_pro_estado)


        self.gridLayout_7.addLayout(self.horizontalLayout_31, 6, 14, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 50, -1, 50)
        self.rbt_pro_disponible = QRadioButton(self.pestana_propiedades)
        self.buttonGroup = QButtonGroup(VentanaPrincipal)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rbt_pro_disponible)
        self.rbt_pro_disponible.setObjectName(u"rbt_pro_disponible")
        self.rbt_pro_disponible.setChecked(True)

        self.verticalLayout_2.addWidget(self.rbt_pro_disponible)

        self.rbt_pro_alquilado = QRadioButton(self.pestana_propiedades)
        self.buttonGroup.addButton(self.rbt_pro_alquilado)
        self.rbt_pro_alquilado.setObjectName(u"rbt_pro_alquilado")

        self.verticalLayout_2.addWidget(self.rbt_pro_alquilado)

        self.rbt_pro_vendido = QRadioButton(self.pestana_propiedades)
        self.buttonGroup.addButton(self.rbt_pro_vendido)
        self.rbt_pro_vendido.setObjectName(u"rbt_pro_vendido")

        self.verticalLayout_2.addWidget(self.rbt_pro_vendido)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 6, 15, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_11, 7, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_14, 11, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_18 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_18)

        self.label_22 = QLabel(self.pestana_propiedades)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_29.addWidget(self.label_22)

        self.lbl_pro_superficie = QLabel(self.pestana_propiedades)
        self.lbl_pro_superficie.setObjectName(u"lbl_pro_superficie")
        self.lbl_pro_superficie.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.lbl_pro_superficie)


        self.gridLayout_7.addLayout(self.horizontalLayout_29, 4, 10, 1, 1)

        self.lbl_pro_codigo = QLabel(self.pestana_propiedades)
        self.lbl_pro_codigo.setObjectName(u"lbl_pro_codigo")
        self.lbl_pro_codigo.setMinimumSize(QSize(80, 0))
        self.lbl_pro_codigo.setMaximumSize(QSize(80, 20))
        self.lbl_pro_codigo.setStyleSheet(u"background-color: #f5f3e4; border: 1px solid black;")
        self.lbl_pro_codigo.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lbl_pro_codigo, 0, 1, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_16 = QLabel(self.pestana_propiedades)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_21.addWidget(self.label_16)

        self.lbl_pro_alta = QLabel(self.pestana_propiedades)
        self.lbl_pro_alta.setObjectName(u"lbl_pro_alta")
        self.lbl_pro_alta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.lbl_pro_alta)


        self.gridLayout_7.addLayout(self.horizontalLayout_21, 0, 6, 1, 1)

        self.line_3 = QFrame(self.pestana_propiedades)
        self.line_3.setObjectName(u"line_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy2)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_3, 12, 0, 1, 20)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.pestana_propiedades)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_16.addWidget(self.label_11)

        self.lbl_pro_direccion = QLabel(self.pestana_propiedades)
        self.lbl_pro_direccion.setObjectName(u"lbl_pro_direccion")

        self.horizontalLayout_16.addWidget(self.lbl_pro_direccion)


        self.gridLayout_7.addLayout(self.horizontalLayout_16, 2, 0, 1, 1)

        self.cmb_pro_provincia = QComboBox(self.pestana_propiedades)
        self.cmb_pro_provincia.setObjectName(u"cmb_pro_provincia")

        self.gridLayout_7.addWidget(self.cmb_pro_provincia, 2, 8, 1, 4)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_15 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_15)

        self.label_19 = QLabel(self.pestana_propiedades)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_26.addWidget(self.label_19)

        self.lbl_pro_movil = QLabel(self.pestana_propiedades)
        self.lbl_pro_movil.setObjectName(u"lbl_pro_movil")
        self.lbl_pro_movil.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.lbl_pro_movil)


        self.gridLayout_7.addLayout(self.horizontalLayout_26, 8, 10, 1, 1)

        self.txt_pro_propietario = QLineEdit(self.pestana_propiedades)
        self.txt_pro_propietario.setObjectName(u"txt_pro_propietario")

        self.gridLayout_7.addWidget(self.txt_pro_propietario, 8, 1, 1, 6)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.txt_pro_alta = QLineEdit(self.pestana_propiedades)
        self.txt_pro_alta.setObjectName(u"txt_pro_alta")
        self.txt_pro_alta.setEnabled(True)
        sizePolicy.setHeightForWidth(self.txt_pro_alta.sizePolicy().hasHeightForWidth())
        self.txt_pro_alta.setSizePolicy(sizePolicy)
        self.txt_pro_alta.setMinimumSize(QSize(110, 0))
        self.txt_pro_alta.setMaximumSize(QSize(110, 16777215))
        self.txt_pro_alta.setAlignment(Qt.AlignCenter)
        self.txt_pro_alta.setReadOnly(False)

        self.horizontalLayout_22.addWidget(self.txt_pro_alta)

        self.btn_pro_alta = QPushButton(self.pestana_propiedades)
        self.btn_pro_alta.setObjectName(u"btn_pro_alta")
        self.btn_pro_alta.setMinimumSize(QSize(35, 30))
        self.btn_pro_alta.setMaximumSize(QSize(35, 30))
        self.btn_pro_alta.setStyleSheet(u"background-color: transparent; border: none;")
        self.btn_pro_alta.setIcon(icon5)
        self.btn_pro_alta.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.btn_pro_alta)


        self.gridLayout_7.addLayout(self.horizontalLayout_22, 0, 7, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.txt_pro_baja = QLineEdit(self.pestana_propiedades)
        self.txt_pro_baja.setObjectName(u"txt_pro_baja")
        sizePolicy.setHeightForWidth(self.txt_pro_baja.sizePolicy().hasHeightForWidth())
        self.txt_pro_baja.setSizePolicy(sizePolicy)
        self.txt_pro_baja.setMinimumSize(QSize(110, 0))
        self.txt_pro_baja.setMaximumSize(QSize(110, 16777215))
        self.txt_pro_baja.setAlignment(Qt.AlignCenter)
        self.txt_pro_baja.setReadOnly(False)

        self.horizontalLayout_11.addWidget(self.txt_pro_baja)

        self.btn_pro_baja = QPushButton(self.pestana_propiedades)
        self.btn_pro_baja.setObjectName(u"btn_pro_baja")
        self.btn_pro_baja.setMinimumSize(QSize(30, 30))
        self.btn_pro_baja.setMaximumSize(QSize(30, 30))
        self.btn_pro_baja.setStyleSheet(u"background-color: transparent; border: none;")
        self.btn_pro_baja.setIcon(icon5)
        self.btn_pro_baja.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.btn_pro_baja)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 0, 11, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_20 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_20)

        self.label_18 = QLabel(self.pestana_propiedades)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_25.addWidget(self.label_18)

        self.lbl_pro_postal = QLabel(self.pestana_propiedades)
        self.lbl_pro_postal.setObjectName(u"lbl_pro_postal")
        self.lbl_pro_postal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.lbl_pro_postal)


        self.gridLayout_7.addLayout(self.horizontalLayout_25, 2, 18, 1, 1)

        self.chk_pro_historico = QCheckBox(self.pestana_propiedades)
        self.chk_pro_historico.setObjectName(u"chk_pro_historico")
        self.chk_pro_historico.setMinimumSize(QSize(60, 0))

        self.gridLayout_7.addWidget(self.chk_pro_historico, 8, 17, 1, 1)

        self.txt_pro_precio_alquiler = QLineEdit(self.pestana_propiedades)
        self.txt_pro_precio_alquiler.setObjectName(u"txt_pro_precio_alquiler")
        self.txt_pro_precio_alquiler.setMinimumSize(QSize(120, 0))
        self.txt_pro_precio_alquiler.setMaximumSize(QSize(120, 16777215))
        self.txt_pro_precio_alquiler.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.txt_pro_precio_alquiler, 4, 15, 1, 1)

        self.txt_pro_direccion = QLineEdit(self.pestana_propiedades)
        self.txt_pro_direccion.setObjectName(u"txt_pro_direccion")

        self.gridLayout_7.addWidget(self.txt_pro_direccion, 2, 1, 1, 6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 50, -1, 50)
        self.chk_pro_alquiler = QCheckBox(self.pestana_propiedades)
        self.chk_pro_alquiler.setObjectName(u"chk_pro_alquiler")

        self.verticalLayout.addWidget(self.chk_pro_alquiler)

        self.chk_pro_venta = QCheckBox(self.pestana_propiedades)
        self.chk_pro_venta.setObjectName(u"chk_pro_venta")

        self.verticalLayout.addWidget(self.chk_pro_venta)

        self.chk_pro_intercambio = QCheckBox(self.pestana_propiedades)
        self.chk_pro_intercambio.setObjectName(u"chk_pro_intercambio")

        self.verticalLayout.addWidget(self.chk_pro_intercambio)


        self.gridLayout_7.addLayout(self.verticalLayout, 6, 11, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.pestana_propiedades)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_17.addWidget(self.label_12)

        self.lbl_pro_codigo_name = QLabel(self.pestana_propiedades)
        self.lbl_pro_codigo_name.setObjectName(u"lbl_pro_codigo_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_pro_codigo_name.sizePolicy().hasHeightForWidth())
        self.lbl_pro_codigo_name.setSizePolicy(sizePolicy3)
        self.lbl_pro_codigo_name.setMinimumSize(QSize(60, 0))
        self.lbl_pro_codigo_name.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_17.addWidget(self.lbl_pro_codigo_name)


        self.gridLayout_7.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.spin_pro_habitaciones = QSpinBox(self.pestana_propiedades)
        self.spin_pro_habitaciones.setObjectName(u"spin_pro_habitaciones")
        self.spin_pro_habitaciones.setMinimumSize(QSize(50, 0))
        self.spin_pro_habitaciones.setMaximumSize(QSize(40, 16777215))
        self.spin_pro_habitaciones.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.spin_pro_habitaciones, 4, 6, 1, 1)

        self.lbl_pro_precio = QLabel(self.pestana_propiedades)
        self.lbl_pro_precio.setObjectName(u"lbl_pro_precio")
        self.lbl_pro_precio.setMinimumSize(QSize(155, 0))
        self.lbl_pro_precio.setMaximumSize(QSize(155, 16777215))
        self.lbl_pro_precio.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_pro_precio, 4, 14, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.btn_pro_grabar = QPushButton(self.pestana_propiedades)
        self.btn_pro_grabar.setObjectName(u"btn_pro_grabar")
        self.btn_pro_grabar.setMinimumSize(QSize(80, 25))
        self.btn_pro_grabar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_3.addWidget(self.btn_pro_grabar)

        self.btn_pro_modificar = QPushButton(self.pestana_propiedades)
        self.btn_pro_modificar.setObjectName(u"btn_pro_modificar")
        self.btn_pro_modificar.setMinimumSize(QSize(80, 25))
        self.btn_pro_modificar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_3.addWidget(self.btn_pro_modificar)

        self.btn_pro_eliminar = QPushButton(self.pestana_propiedades)
        self.btn_pro_eliminar.setObjectName(u"btn_pro_eliminar")
        self.btn_pro_eliminar.setMinimumSize(QSize(80, 25))
        self.btn_pro_eliminar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_3.addWidget(self.btn_pro_eliminar)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 10, 0, 1, 20)

        self.cmb_pro_municipio = QComboBox(self.pestana_propiedades)
        self.cmb_pro_municipio.setObjectName(u"cmb_pro_municipio")

        self.gridLayout_7.addWidget(self.cmb_pro_municipio, 2, 13, 1, 3)

        self.txt_pro_precio_venta = QLineEdit(self.pestana_propiedades)
        self.txt_pro_precio_venta.setObjectName(u"txt_pro_precio_venta")
        self.txt_pro_precio_venta.setMinimumSize(QSize(120, 0))
        self.txt_pro_precio_venta.setMaximumSize(QSize(120, 16777215))
        self.txt_pro_precio_venta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.txt_pro_precio_venta, 4, 17, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.pestana_propiedades)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_19.addWidget(self.label_14, 0, Qt.AlignTop)

        self.lbl_pro_descripcion = QLabel(self.pestana_propiedades)
        self.lbl_pro_descripcion.setObjectName(u"lbl_pro_descripcion")
        self.lbl_pro_descripcion.setMinimumSize(QSize(100, 0))
        self.lbl_pro_descripcion.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_pro_descripcion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.lbl_pro_descripcion, 0, Qt.AlignTop)


        self.gridLayout_7.addLayout(self.horizontalLayout_19, 6, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_13, 9, 0, 1, 1)

        self.areatxt_pro_descripcion = QTextEdit(self.pestana_propiedades)
        self.areatxt_pro_descripcion.setObjectName(u"areatxt_pro_descripcion")
        self.areatxt_pro_descripcion.setMaximumSize(QSize(16777215, 180))

        self.gridLayout_7.addWidget(self.areatxt_pro_descripcion, 6, 1, 1, 8)

        self.verticalSpacer_12 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_12, 5, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.pestana_propiedades)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_20.addWidget(self.label_15)

        self.lbl_pro_propietario = QLabel(self.pestana_propiedades)
        self.lbl_pro_propietario.setObjectName(u"lbl_pro_propietario")

        self.horizontalLayout_20.addWidget(self.lbl_pro_propietario)


        self.gridLayout_7.addLayout(self.horizontalLayout_20, 8, 0, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_23 = QLabel(self.pestana_propiedades)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_30.addWidget(self.label_23)

        self.lbl_pro_tipo_operacion = QLabel(self.pestana_propiedades)
        self.lbl_pro_tipo_operacion.setObjectName(u"lbl_pro_tipo_operacion")
        self.lbl_pro_tipo_operacion.setMinimumSize(QSize(140, 0))
        self.lbl_pro_tipo_operacion.setMaximumSize(QSize(95, 16777215))
        self.lbl_pro_tipo_operacion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.lbl_pro_tipo_operacion)


        self.gridLayout_7.addLayout(self.horizontalLayout_30, 6, 10, 1, 1)

        self.txt_pro_superficie = QLineEdit(self.pestana_propiedades)
        self.txt_pro_superficie.setObjectName(u"txt_pro_superficie")
        self.txt_pro_superficie.setMinimumSize(QSize(110, 0))
        self.txt_pro_superficie.setMaximumSize(QSize(110, 16777215))
        self.txt_pro_superficie.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.txt_pro_superficie, 4, 11, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_17 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_17)

        self.label_21 = QLabel(self.pestana_propiedades)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_28.addWidget(self.label_21)

        self.lbl_pro_banos = QLabel(self.pestana_propiedades)
        self.lbl_pro_banos.setObjectName(u"lbl_pro_banos")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lbl_pro_banos.sizePolicy().hasHeightForWidth())
        self.lbl_pro_banos.setSizePolicy(sizePolicy4)
        self.lbl_pro_banos.setMinimumSize(QSize(50, 0))
        self.lbl_pro_banos.setMaximumSize(QSize(50, 16777215))
        self.lbl_pro_banos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.lbl_pro_banos)


        self.gridLayout_7.addLayout(self.horizontalLayout_28, 4, 7, 1, 1)

        self.spin_pro_banos = QSpinBox(self.pestana_propiedades)
        self.spin_pro_banos.setObjectName(u"spin_pro_banos")
        sizePolicy2.setHeightForWidth(self.spin_pro_banos.sizePolicy().hasHeightForWidth())
        self.spin_pro_banos.setSizePolicy(sizePolicy2)
        self.spin_pro_banos.setMinimumSize(QSize(50, 0))
        self.spin_pro_banos.setMaximumSize(QSize(40, 16777215))
        self.spin_pro_banos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.spin_pro_banos, 4, 8, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(108, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_27, 5, 19, 1, 1)

        self.tab_pro = QTableWidget(self.pestana_propiedades)
        if (self.tab_pro.columnCount() < 9):
            self.tab_pro.setColumnCount(9)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tab_pro.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        self.tab_pro.setObjectName(u"tab_pro")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tab_pro.sizePolicy().hasHeightForWidth())
        self.tab_pro.setSizePolicy(sizePolicy5)
        self.tab_pro.setStyleSheet(u"")
        self.tab_pro.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_pro.setAlternatingRowColors(True)
        self.tab_pro.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab_pro.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_7.addWidget(self.tab_pro, 13, 1, 1, 18)


        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_16)

        self.btn_pro_anterior = QPushButton(self.pestana_propiedades)
        self.btn_pro_anterior.setObjectName(u"btn_pro_anterior")
        sizePolicy.setHeightForWidth(self.btn_pro_anterior.sizePolicy().hasHeightForWidth())
        self.btn_pro_anterior.setSizePolicy(sizePolicy)
        self.btn_pro_anterior.setMinimumSize(QSize(80, 25))
        self.btn_pro_anterior.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_36.addWidget(self.btn_pro_anterior)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_23)

        self.lbl_pro_pagina = QLabel(self.pestana_propiedades)
        self.lbl_pro_pagina.setObjectName(u"lbl_pro_pagina")

        self.horizontalLayout_36.addWidget(self.lbl_pro_pagina)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_31)

        self.btn_pro_siguiente = QPushButton(self.pestana_propiedades)
        self.btn_pro_siguiente.setObjectName(u"btn_pro_siguiente")
        sizePolicy.setHeightForWidth(self.btn_pro_siguiente.sizePolicy().hasHeightForWidth())
        self.btn_pro_siguiente.setSizePolicy(sizePolicy)
        self.btn_pro_siguiente.setMinimumSize(QSize(80, 25))
        self.btn_pro_siguiente.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_36.addWidget(self.btn_pro_siguiente)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_22)


        self.gridLayout_4.addLayout(self.horizontalLayout_36, 3, 0, 1, 1)

        self.line_4 = QFrame(self.pestana_propiedades)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 1, 0, 1, 1)

        self.panel_principal.addTab(self.pestana_propiedades, "")
        self.pestana_vendedores = QWidget()
        self.pestana_vendedores.setObjectName(u"pestana_vendedores")
        self.gridLayout_5 = QGridLayout(self.pestana_vendedores)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_40 = QLabel(self.pestana_vendedores)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_47.addWidget(self.label_40)

        self.lbl_ven_provincia_2 = QLabel(self.pestana_vendedores)
        self.lbl_ven_provincia_2.setObjectName(u"lbl_ven_provincia_2")
        self.lbl_ven_provincia_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.lbl_ven_provincia_2)


        self.gridLayout_6.addLayout(self.horizontalLayout_47, 6, 0, 1, 1)

        self.txt_ven_dni = QLineEdit(self.pestana_vendedores)
        self.txt_ven_dni.setObjectName(u"txt_ven_dni")
        self.txt_ven_dni.setMinimumSize(QSize(90, 0))
        self.txt_ven_dni.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_6.addWidget(self.txt_ven_dni, 4, 1, 1, 1)

        self.txt_ven_email = QLineEdit(self.pestana_vendedores)
        self.txt_ven_email.setObjectName(u"txt_ven_email")
        self.txt_ven_email.setMinimumSize(QSize(250, 0))
        self.txt_ven_email.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_6.addWidget(self.txt_ven_email, 8, 1, 1, 1)

        self.cmb_ven_provincia = QComboBox(self.pestana_vendedores)
        self.cmb_ven_provincia.setObjectName(u"cmb_ven_provincia")
        self.cmb_ven_provincia.setMinimumSize(QSize(350, 0))
        self.cmb_ven_provincia.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_6.addWidget(self.cmb_ven_provincia, 10, 1, 1, 1)

        self.txt_ven_nombre = QLineEdit(self.pestana_vendedores)
        self.txt_ven_nombre.setObjectName(u"txt_ven_nombre")
        self.txt_ven_nombre.setMinimumSize(QSize(200, 0))
        self.txt_ven_nombre.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.txt_ven_nombre, 6, 1, 1, 1)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_34 = QSpacerItem(330, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_34)

        self.label_37 = QLabel(self.pestana_vendedores)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_44.addWidget(self.label_37)

        self.lbl_ven_alta = QLabel(self.pestana_vendedores)
        self.lbl_ven_alta.setObjectName(u"lbl_ven_alta")

        self.horizontalLayout_44.addWidget(self.lbl_ven_alta)


        self.gridLayout_6.addLayout(self.horizontalLayout_44, 4, 2, 1, 1)

        self.lbl_ven_codigo = QLabel(self.pestana_vendedores)
        self.lbl_ven_codigo.setObjectName(u"lbl_ven_codigo")
        self.lbl_ven_codigo.setMinimumSize(QSize(80, 20))
        self.lbl_ven_codigo.setMaximumSize(QSize(80, 20))
        self.lbl_ven_codigo.setStyleSheet(u"background-color: #f5f3e4; border: 1px solid black;")

        self.gridLayout_6.addWidget(self.lbl_ven_codigo, 2, 1, 1, 1)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_42 = QLabel(self.pestana_vendedores)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_49.addWidget(self.label_42)

        self.lbl_ven_codigo_name = QLabel(self.pestana_vendedores)
        self.lbl_ven_codigo_name.setObjectName(u"lbl_ven_codigo_name")
        sizePolicy3.setHeightForWidth(self.lbl_ven_codigo_name.sizePolicy().hasHeightForWidth())
        self.lbl_ven_codigo_name.setSizePolicy(sizePolicy3)
        self.lbl_ven_codigo_name.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_49.addWidget(self.lbl_ven_codigo_name)


        self.gridLayout_6.addLayout(self.horizontalLayout_49, 2, 0, 1, 1)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_39 = QLabel(self.pestana_vendedores)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_46.addWidget(self.label_39)

        self.lbl_ven_provincia = QLabel(self.pestana_vendedores)
        self.lbl_ven_provincia.setObjectName(u"lbl_ven_provincia")
        self.lbl_ven_provincia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.lbl_ven_provincia)


        self.gridLayout_6.addLayout(self.horizontalLayout_46, 10, 0, 1, 1)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_43 = QLabel(self.pestana_vendedores)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_50.addWidget(self.label_43)

        self.lbl_ven_provincia_4 = QLabel(self.pestana_vendedores)
        self.lbl_ven_provincia_4.setObjectName(u"lbl_ven_provincia_4")
        self.lbl_ven_provincia_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.lbl_ven_provincia_4)


        self.gridLayout_6.addLayout(self.horizontalLayout_50, 4, 0, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.txt_ven_baja = QLineEdit(self.pestana_vendedores)
        self.txt_ven_baja.setObjectName(u"txt_ven_baja")
        self.txt_ven_baja.setEnabled(True)
        sizePolicy.setHeightForWidth(self.txt_ven_baja.sizePolicy().hasHeightForWidth())
        self.txt_ven_baja.setSizePolicy(sizePolicy)
        self.txt_ven_baja.setMinimumSize(QSize(115, 0))
        self.txt_ven_baja.setMaximumSize(QSize(115, 16777215))
        self.txt_ven_baja.setAlignment(Qt.AlignCenter)
        self.txt_ven_baja.setReadOnly(False)

        self.horizontalLayout_39.addWidget(self.txt_ven_baja)

        self.btn_ven_baja = QPushButton(self.pestana_vendedores)
        self.btn_ven_baja.setObjectName(u"btn_ven_baja")
        self.btn_ven_baja.setMinimumSize(QSize(35, 30))
        self.btn_ven_baja.setMaximumSize(QSize(35, 30))
        self.btn_ven_baja.setStyleSheet(u"background-color: transparent; border: none;")
        self.btn_ven_baja.setIcon(icon5)
        self.btn_ven_baja.setIconSize(QSize(30, 30))

        self.horizontalLayout_39.addWidget(self.btn_ven_baja)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_37)


        self.gridLayout_6.addLayout(self.horizontalLayout_39, 4, 5, 1, 1)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.txt_ven_alta = QLineEdit(self.pestana_vendedores)
        self.txt_ven_alta.setObjectName(u"txt_ven_alta")
        self.txt_ven_alta.setEnabled(True)
        sizePolicy.setHeightForWidth(self.txt_ven_alta.sizePolicy().hasHeightForWidth())
        self.txt_ven_alta.setSizePolicy(sizePolicy)
        self.txt_ven_alta.setMinimumSize(QSize(115, 0))
        self.txt_ven_alta.setMaximumSize(QSize(115, 16777215))
        self.txt_ven_alta.setAlignment(Qt.AlignCenter)
        self.txt_ven_alta.setReadOnly(False)

        self.horizontalLayout_38.addWidget(self.txt_ven_alta)

        self.btn_ven_alta = QPushButton(self.pestana_vendedores)
        self.btn_ven_alta.setObjectName(u"btn_ven_alta")
        self.btn_ven_alta.setMinimumSize(QSize(35, 30))
        self.btn_ven_alta.setMaximumSize(QSize(35, 30))
        self.btn_ven_alta.setStyleSheet(u"background-color: transparent; border: none;")
        self.btn_ven_alta.setIcon(icon5)
        self.btn_ven_alta.setIconSize(QSize(30, 30))

        self.horizontalLayout_38.addWidget(self.btn_ven_alta)


        self.gridLayout_6.addLayout(self.horizontalLayout_38, 4, 3, 1, 1)

        self.chk_ven_historico = QCheckBox(self.pestana_vendedores)
        self.chk_ven_historico.setObjectName(u"chk_ven_historico")

        self.gridLayout_6.addWidget(self.chk_ven_historico, 10, 5, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 5, 0, 1, 1)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_36 = QSpacerItem(330, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_36)

        self.label_38 = QLabel(self.pestana_vendedores)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_45.addWidget(self.label_38)

        self.lbl_ven_baja = QLabel(self.pestana_vendedores)
        self.lbl_ven_baja.setObjectName(u"lbl_ven_baja")

        self.horizontalLayout_45.addWidget(self.lbl_ven_baja)


        self.gridLayout_6.addLayout(self.horizontalLayout_45, 4, 4, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_32)

        self.btn_ven_grabar = QPushButton(self.pestana_vendedores)
        self.btn_ven_grabar.setObjectName(u"btn_ven_grabar")
        self.btn_ven_grabar.setMinimumSize(QSize(80, 25))
        self.btn_ven_grabar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_34.addWidget(self.btn_ven_grabar)

        self.btn_ven_modificar = QPushButton(self.pestana_vendedores)
        self.btn_ven_modificar.setObjectName(u"btn_ven_modificar")
        self.btn_ven_modificar.setMinimumSize(QSize(80, 25))
        self.btn_ven_modificar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_34.addWidget(self.btn_ven_modificar)

        self.btn_ven_eliminar = QPushButton(self.pestana_vendedores)
        self.btn_ven_eliminar.setObjectName(u"btn_ven_eliminar")
        self.btn_ven_eliminar.setMinimumSize(QSize(80, 25))
        self.btn_ven_eliminar.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_34.addWidget(self.btn_ven_eliminar)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_33)


        self.gridLayout_6.addLayout(self.horizontalLayout_34, 11, 0, 1, 6)

        self.verticalSpacer_6 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_35 = QLabel(self.pestana_vendedores)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_42.addWidget(self.label_35)

        self.lbl_ven_codigo_name_2 = QLabel(self.pestana_vendedores)
        self.lbl_ven_codigo_name_2.setObjectName(u"lbl_ven_codigo_name_2")

        self.horizontalLayout_42.addWidget(self.lbl_ven_codigo_name_2)


        self.gridLayout_6.addLayout(self.horizontalLayout_42, 8, 0, 1, 1)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_35 = QSpacerItem(330, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_35)

        self.label_36 = QLabel(self.pestana_vendedores)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(8, 16777215))

        self.horizontalLayout_43.addWidget(self.label_36)

        self.lbl_ven_dni_2 = QLabel(self.pestana_vendedores)
        self.lbl_ven_dni_2.setObjectName(u"lbl_ven_dni_2")

        self.horizontalLayout_43.addWidget(self.lbl_ven_dni_2)


        self.gridLayout_6.addLayout(self.horizontalLayout_43, 8, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 7, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_15, 9, 0, 1, 1)

        self.txt_ven_movil = QLineEdit(self.pestana_vendedores)
        self.txt_ven_movil.setObjectName(u"txt_ven_movil")
        self.txt_ven_movil.setMinimumSize(QSize(115, 0))
        self.txt_ven_movil.setMaximumSize(QSize(115, 16777215))
        self.txt_ven_movil.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.txt_ven_movil, 8, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer_38 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_38)

        self.tab_ven = QTableWidget(self.pestana_vendedores)
        if (self.tab_ven.columnCount() < 4):
            self.tab_ven.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tab_ven.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tab_ven.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tab_ven.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tab_ven.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        self.tab_ven.setObjectName(u"tab_ven")
        self.tab_ven.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab_ven.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_40.addWidget(self.tab_ven)

        self.horizontalSpacer_39 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_39)


        self.gridLayout_5.addLayout(self.horizontalLayout_40, 1, 0, 1, 1)

        self.panel_principal.addTab(self.pestana_vendedores, "")

        self.gridLayout_2.addWidget(self.panel_principal, 0, 0, 1, 1)

        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2153, 22))
        self.menu_archivo = QMenu(self.menubar)
        self.menu_archivo.setObjectName(u"menu_archivo")
        self.menu_herramientas = QMenu(self.menubar)
        self.menu_herramientas.setObjectName(u"menu_herramientas")
        self.menuExportar_Datos = QMenu(self.menu_herramientas)
        self.menuExportar_Datos.setObjectName(u"menuExportar_Datos")
        self.menu_ayuda = QMenu(self.menubar)
        self.menu_ayuda.setObjectName(u"menu_ayuda")
        self.menu_gestion = QMenu(self.menubar)
        self.menu_gestion.setObjectName(u"menu_gestion")
        self.menuInformes = QMenu(self.menubar)
        self.menuInformes.setObjectName(u"menuInformes")
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)
        self.toolbar = QToolBar(VentanaPrincipal)
        self.toolbar.setObjectName(u"toolbar")
        VentanaPrincipal.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
        QWidget.setTabOrder(self.txt_cli_apellido, self.txt_cli_nombre)
        QWidget.setTabOrder(self.txt_cli_nombre, self.txt_cli_email)
        QWidget.setTabOrder(self.txt_cli_email, self.txt_cli_movil)
        QWidget.setTabOrder(self.txt_cli_movil, self.txt_cli_direccion)
        QWidget.setTabOrder(self.txt_cli_direccion, self.btn_cli_grabar)
        QWidget.setTabOrder(self.btn_cli_grabar, self.btn_cli_modificar)
        QWidget.setTabOrder(self.btn_cli_modificar, self.btn_cli_eliminar)

        self.menubar.addAction(self.menu_archivo.menuAction())
        self.menubar.addAction(self.menu_gestion.menuAction())
        self.menubar.addAction(self.menu_herramientas.menuAction())
        self.menubar.addAction(self.menuInformes.menuAction())
        self.menubar.addAction(self.menu_ayuda.menuAction())
        self.menu_archivo.addAction(self.action_archivo_salir)
        self.menu_herramientas.addAction(self.action_archivo_backup_crear)
        self.menu_herramientas.addAction(self.action_archivo_backup_restaurar)
        self.menu_herramientas.addAction(self.menuExportar_Datos.menuAction())
        self.menuExportar_Datos.addAction(self.action_exportar_propiedades_CSV)
        self.menuExportar_Datos.addAction(self.action_exportar_propiedades_JSON)
        self.menu_ayuda.addAction(self.action_abrir_about)
        self.menu_gestion.addAction(self.action_gestion_propiedades_tipo)
        self.menuInformes.addAction(self.action_listado_clientes)
        self.menuInformes.addAction(self.action_listado_propiedades)
        self.toolbar.addAction(self.action_tool_limpiar)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_tool_gestionar_tipos_propiedad)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_tool_filtrar_propiedades)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_tool_salir)

        self.retranslateUi(VentanaPrincipal)

        self.panel_principal.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"InmoTeis", None))
        self.action_archivo_salir.setText(QCoreApplication.translate("VentanaPrincipal", u"Salir", None))
        self.action_archivo_backup_crear.setText(QCoreApplication.translate("VentanaPrincipal", u"Crear Backup", None))
#if QT_CONFIG(shortcut)
        self.action_archivo_backup_crear.setShortcut(QCoreApplication.translate("VentanaPrincipal", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.action_archivo_backup_restaurar.setText(QCoreApplication.translate("VentanaPrincipal", u"Restaurar Backup", None))
        self.action_tool_salir.setText(QCoreApplication.translate("VentanaPrincipal", u"barSalir", None))
#if QT_CONFIG(tooltip)
        self.action_tool_salir.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Salir", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_tool_salir.setShortcut(QCoreApplication.translate("VentanaPrincipal", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_tool_limpiar.setText(QCoreApplication.translate("VentanaPrincipal", u"barLimpiar", None))
#if QT_CONFIG(tooltip)
        self.action_tool_limpiar.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Limpiar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_tool_limpiar.setShortcut(QCoreApplication.translate("VentanaPrincipal", u"Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_tool_gestionar_tipos_propiedad.setText(QCoreApplication.translate("VentanaPrincipal", u"barTipoPro", None))
#if QT_CONFIG(tooltip)
        self.action_tool_gestionar_tipos_propiedad.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Gesti\u00f3n tipos propiedad", None))
#endif // QT_CONFIG(tooltip)
        self.action_gestion_propiedades_tipo.setText(QCoreApplication.translate("VentanaPrincipal", u"Gestionar tipos propiedades", None))
        self.action_tool_filtrar_propiedades.setText(QCoreApplication.translate("VentanaPrincipal", u"barFiltrarPro", None))
        self.action_exportar_propiedades_CSV.setText(QCoreApplication.translate("VentanaPrincipal", u"Exportar Propiedades CSV", None))
#if QT_CONFIG(tooltip)
        self.action_exportar_propiedades_CSV.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Exportar Propiedaes CSV", None))
#endif // QT_CONFIG(tooltip)
        self.action_exportar_propiedades_JSON.setText(QCoreApplication.translate("VentanaPrincipal", u"Exportar Propiedades JSON", None))
        self.action_abrir_about.setText(QCoreApplication.translate("VentanaPrincipal", u"Acerca de", None))
        self.action_listado_clientes.setText(QCoreApplication.translate("VentanaPrincipal", u"Listado Clientes", None))
        self.action_listado_propiedades.setText(QCoreApplication.translate("VentanaPrincipal", u"Listado Propiedades", None))
        self.btn_cli_grabar.setText(QCoreApplication.translate("VentanaPrincipal", u"Grabar", None))
        self.btn_cli_modificar.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar", None))
        self.btn_cli_eliminar.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
        self.label_5.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_5.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_nombre.setText(QCoreApplication.translate("VentanaPrincipal", u"Nombre:", None))
        self.label_6.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_6.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_movil.setText(QCoreApplication.translate("VentanaPrincipal", u"M\u00f3vil:", None))
        self.lbl_cli_baja.setText(QCoreApplication.translate("VentanaPrincipal", u"Fecha Baja:", None))
        self.btn_cli_alta.setText("")
        self.label_4.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_4.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_alta.setText(QCoreApplication.translate("VentanaPrincipal", u"Fecha de alta:", None))
        self.btn_cli_buscar.setText("")
        self.label.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_dni.setText(QCoreApplication.translate("VentanaPrincipal", u"DNI/CIF:", None))
        self.chk_cli_historico.setText(QCoreApplication.translate("VentanaPrincipal", u"Hist\u00f3rico", None))
        self.btn_cli_baja.setText("")
        self.txt_cli_apellido.setText("")
        self.label_8.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_8.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_provincia.setText(QCoreApplication.translate("VentanaPrincipal", u"Provincia:", None))
        self.label_3.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_3.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_direccion.setText(QCoreApplication.translate("VentanaPrincipal", u"Direci\u00f3n:", None))
        self.label_9.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_9.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_municipio.setText(QCoreApplication.translate("VentanaPrincipal", u"Municipio:", None))
        self.label_28.setText(QCoreApplication.translate("VentanaPrincipal", u"Los campos con", None))
        self.label_29.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_29.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.label_30.setText(QCoreApplication.translate("VentanaPrincipal", u"son obligatorios", None))
        self.label_2.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_2.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_cli_apellido.setText(QCoreApplication.translate("VentanaPrincipal", u"Apellidos:", None))
        self.label_10.setText("")
        self.lbl_cli_email.setText(QCoreApplication.translate("VentanaPrincipal", u"Email:", None))
        self.btn_cli_anterior.setText(QCoreApplication.translate("VentanaPrincipal", u"Anterior", None))
        self.lbl_cli_pagina.setText("")
        self.btn_cli_siguiente.setText(QCoreApplication.translate("VentanaPrincipal", u"Siguiente", None))
        ___qtablewidgetitem = self.tab_cli.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaPrincipal", u"DNI/NIE", None));
        ___qtablewidgetitem1 = self.tab_cli.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaPrincipal", u"Apellidos", None));
        ___qtablewidgetitem2 = self.tab_cli.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaPrincipal", u"Nombre", None));
        ___qtablewidgetitem3 = self.tab_cli.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaPrincipal", u"M\u00f3vil", None));
        ___qtablewidgetitem4 = self.tab_cli.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaPrincipal", u"Provincia", None));
        ___qtablewidgetitem5 = self.tab_cli.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VentanaPrincipal", u"Municipio", None));
        ___qtablewidgetitem6 = self.tab_cli.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VentanaPrincipal", u"Fecha de Baja", None));
        self.panel_principal.setTabText(self.panel_principal.indexOf(self.pestana_clientes), QCoreApplication.translate("VentanaPrincipal", u"Clientes", None))
        self.lbl_pro_baja.setText(QCoreApplication.translate("VentanaPrincipal", u"Fecha Baja:", None))
        self.label_13.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_13.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_tipo.setText(QCoreApplication.translate("VentanaPrincipal", u"Tipo:", None))
        self.label_17.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_17.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_municipio.setText(QCoreApplication.translate("VentanaPrincipal", u"Municipio:", None))
        self.label_25.setText(QCoreApplication.translate("VentanaPrincipal", u"Los campos con", None))
        self.label_26.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_26.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.label_27.setText(QCoreApplication.translate("VentanaPrincipal", u"son obligatorios", None))
        self.label_20.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_20.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_habitaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Habitaciones:", None))
        self.lbl_separator.setText(QCoreApplication.translate("VentanaPrincipal", u"/", None))
        self.label_7.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_7.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_provincia.setText(QCoreApplication.translate("VentanaPrincipal", u"Provincia:", None))
        self.label_24.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_24.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_estado.setText(QCoreApplication.translate("VentanaPrincipal", u"Estado:", None))
        self.rbt_pro_disponible.setText(QCoreApplication.translate("VentanaPrincipal", u"Disponible", None))
        self.rbt_pro_alquilado.setText(QCoreApplication.translate("VentanaPrincipal", u"Alquilado", None))
        self.rbt_pro_vendido.setText(QCoreApplication.translate("VentanaPrincipal", u"Vendido", None))
        self.label_22.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_22.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_superficie.setText(QCoreApplication.translate("VentanaPrincipal", u"Superficie:", None))
        self.lbl_pro_codigo.setText("")
        self.label_16.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_16.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_alta.setText(QCoreApplication.translate("VentanaPrincipal", u"Publicaci\u00f3n:", None))
        self.label_11.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_11.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_direccion.setText(QCoreApplication.translate("VentanaPrincipal", u"Direcci\u00f3n:", None))
        self.label_19.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_19.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_movil.setText(QCoreApplication.translate("VentanaPrincipal", u"M\u00f3vil:", None))
        self.btn_pro_alta.setText("")
        self.btn_pro_baja.setText("")
        self.label_18.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_18.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_postal.setText(QCoreApplication.translate("VentanaPrincipal", u"C\u00f3digo Postal:", None))
        self.chk_pro_historico.setText(QCoreApplication.translate("VentanaPrincipal", u"Hist\u00f3rico", None))
        self.txt_pro_precio_alquiler.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Precio Alquiler \u20ac", None))
        self.chk_pro_alquiler.setText(QCoreApplication.translate("VentanaPrincipal", u"Alquiler", None))
        self.chk_pro_venta.setText(QCoreApplication.translate("VentanaPrincipal", u"Venta", None))
        self.chk_pro_intercambio.setText(QCoreApplication.translate("VentanaPrincipal", u"Intercambio", None))
        self.label_12.setText("")
        self.lbl_pro_codigo_name.setText(QCoreApplication.translate("VentanaPrincipal", u"C\u00f3digo:", None))
        self.lbl_pro_precio.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio(Alquiler/Venta):", None))
        self.btn_pro_grabar.setText(QCoreApplication.translate("VentanaPrincipal", u"Grabar", None))
        self.btn_pro_modificar.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar", None))
        self.btn_pro_eliminar.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
        self.txt_pro_precio_venta.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Precio Venta \u20ac", None))
        self.label_14.setText("")
        self.lbl_pro_descripcion.setText(QCoreApplication.translate("VentanaPrincipal", u"Observaciones:", None))
        self.label_15.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_15.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_propietario.setText(QCoreApplication.translate("VentanaPrincipal", u"Propietario:", None))
        self.label_23.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_23.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_tipo_operacion.setText(QCoreApplication.translate("VentanaPrincipal", u"Tipo de Operaci\u00f3n:", None))
        self.txt_pro_superficie.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"m2", None))
        self.label_21.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_21.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_pro_banos.setText(QCoreApplication.translate("VentanaPrincipal", u"Ba\u00f1os:", None))
        ___qtablewidgetitem7 = self.tab_pro.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VentanaPrincipal", u"C\u00f3digo", None));
        ___qtablewidgetitem8 = self.tab_pro.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VentanaPrincipal", u"Municipio", None));
        ___qtablewidgetitem9 = self.tab_pro.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("VentanaPrincipal", u"Tipo Propiedad", None));
        ___qtablewidgetitem10 = self.tab_pro.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("VentanaPrincipal", u"Habitaciones", None));
        ___qtablewidgetitem11 = self.tab_pro.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("VentanaPrincipal", u"Ba\u00f1os", None));
        ___qtablewidgetitem12 = self.tab_pro.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio Alquiler", None));
        ___qtablewidgetitem13 = self.tab_pro.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio Venta", None));
        ___qtablewidgetitem14 = self.tab_pro.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("VentanaPrincipal", u"Tipo Operaci\u00f3n", None));
        ___qtablewidgetitem15 = self.tab_pro.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("VentanaPrincipal", u"Fecha Baja", None));
        self.btn_pro_anterior.setText(QCoreApplication.translate("VentanaPrincipal", u"Anterior", None))
        self.lbl_pro_pagina.setText("")
        self.btn_pro_siguiente.setText(QCoreApplication.translate("VentanaPrincipal", u"Siguiente", None))
        self.panel_principal.setTabText(self.panel_principal.indexOf(self.pestana_propiedades), QCoreApplication.translate("VentanaPrincipal", u"Propiedades", None))
        self.label_40.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_40.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_ven_provincia_2.setText(QCoreApplication.translate("VentanaPrincipal", u"Nombre", None))
        self.txt_ven_nombre.setText("")
        self.label_37.setText("")
        self.lbl_ven_alta.setText(QCoreApplication.translate("VentanaPrincipal", u"Alta:", None))
        self.lbl_ven_codigo.setText("")
        self.label_42.setText("")
        self.label_42.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_ven_codigo_name.setText(QCoreApplication.translate("VentanaPrincipal", u"C\u00f3digo:", None))
        self.label_39.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_39.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_ven_provincia.setText(QCoreApplication.translate("VentanaPrincipal", u"Provincia:", None))
        self.label_43.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_43.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_ven_provincia_4.setText(QCoreApplication.translate("VentanaPrincipal", u"DNI:", None))
        self.btn_ven_baja.setText("")
        self.btn_ven_alta.setText("")
        self.chk_ven_historico.setText(QCoreApplication.translate("VentanaPrincipal", u"Hist\u00f3rico", None))
        self.label_38.setText("")
        self.lbl_ven_baja.setText(QCoreApplication.translate("VentanaPrincipal", u"Baja:", None))
        self.btn_ven_grabar.setText(QCoreApplication.translate("VentanaPrincipal", u"Grabar", None))
        self.btn_ven_modificar.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar", None))
        self.btn_ven_eliminar.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
        self.label_35.setText("")
        self.lbl_ven_codigo_name_2.setText(QCoreApplication.translate("VentanaPrincipal", u"Email:", None))
        self.label_36.setText(QCoreApplication.translate("VentanaPrincipal", u"*", None))
        self.label_36.setProperty(u"qssClass", QCoreApplication.translate("VentanaPrincipal", u"asterisk", None))
        self.lbl_ven_dni_2.setText(QCoreApplication.translate("VentanaPrincipal", u"M\u00f3vil:", None))
        ___qtablewidgetitem16 = self.tab_ven.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("VentanaPrincipal", u"C\u00f3digo", None));
        ___qtablewidgetitem17 = self.tab_ven.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("VentanaPrincipal", u"M\u00f3vil", None));
        ___qtablewidgetitem18 = self.tab_ven.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("VentanaPrincipal", u"Nombre", None));
        ___qtablewidgetitem19 = self.tab_ven.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("VentanaPrincipal", u"Delegaci\u00f3n", None));
        self.panel_principal.setTabText(self.panel_principal.indexOf(self.pestana_vendedores), QCoreApplication.translate("VentanaPrincipal", u"Vendedores", None))
        self.menu_archivo.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Archivo", None))
        self.menu_herramientas.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Herramientas", None))
        self.menuExportar_Datos.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Exportar Datos", None))
        self.menu_ayuda.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Ayuda", None))
        self.menu_gestion.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Gesti\u00f3n", None))
        self.menuInformes.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Informes", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"toolBar", None))
    # retranslateUi

