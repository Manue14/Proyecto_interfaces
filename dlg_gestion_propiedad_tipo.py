# Form implementation generated from reading ui file '/home/manu/Proyecto_interfaces/templates/DlgGestionPropiedadTipo.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DlgGestionPropiedadTipo(object):
    def setupUi(self, DlgGestionPropiedadTipo):
        DlgGestionPropiedadTipo.setObjectName("DlgGestionPropiedadTipo")
        DlgGestionPropiedadTipo.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        DlgGestionPropiedadTipo.resize(400, 300)
        DlgGestionPropiedadTipo.setMinimumSize(QtCore.QSize(400, 300))
        DlgGestionPropiedadTipo.setMaximumSize(QtCore.QSize(400, 300))
        DlgGestionPropiedadTipo.setModal(True)
        self.frame = QtWidgets.QFrame(parent=DlgGestionPropiedadTipo)
        self.frame.setGeometry(QtCore.QRect(10, 20, 371, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 342, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/manu/Proyecto_interfaces/templates/../img/house.ico"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_pro_gestion_tipo = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lbl_pro_gestion_tipo.setMinimumSize(QtCore.QSize(280, 30))
        self.lbl_pro_gestion_tipo.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_pro_gestion_tipo.setFont(font)
        self.lbl_pro_gestion_tipo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pro_gestion_tipo.setObjectName("lbl_pro_gestion_tipo")
        self.horizontalLayout_3.addWidget(self.lbl_pro_gestion_tipo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txt_pro_gestion_tipo = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txt_pro_gestion_tipo.setMinimumSize(QtCore.QSize(150, 20))
        self.txt_pro_gestion_tipo.setMaximumSize(QtCore.QSize(150, 20))
        self.txt_pro_gestion_tipo.setObjectName("txt_pro_gestion_tipo")
        self.horizontalLayout_4.addWidget(self.txt_pro_gestion_tipo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_pro_tipo_alta = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_pro_tipo_alta.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_pro_tipo_alta.setMaximumSize(QtCore.QSize(80, 25))
        self.btn_pro_tipo_alta.setObjectName("btn_pro_tipo_alta")
        self.horizontalLayout.addWidget(self.btn_pro_tipo_alta)
        self.btn_pro_tipo_eliminar = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_pro_tipo_eliminar.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_pro_tipo_eliminar.setMaximumSize(QtCore.QSize(80, 25))
        self.btn_pro_tipo_eliminar.setObjectName("btn_pro_tipo_eliminar")
        self.horizontalLayout.addWidget(self.btn_pro_tipo_eliminar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DlgGestionPropiedadTipo)
        QtCore.QMetaObject.connectSlotsByName(DlgGestionPropiedadTipo)

    def retranslateUi(self, DlgGestionPropiedadTipo):
        _translate = QtCore.QCoreApplication.translate
        DlgGestionPropiedadTipo.setWindowTitle(_translate("DlgGestionPropiedadTipo", "Gestión Tipo Propiedades"))
        self.lbl_pro_gestion_tipo.setText(_translate("DlgGestionPropiedadTipo", "Introduzca tipo de propiedad a crear o eliminar"))
        self.btn_pro_tipo_alta.setText(_translate("DlgGestionPropiedadTipo", "Alta"))
        self.btn_pro_tipo_eliminar.setText(_translate("DlgGestionPropiedadTipo", "Eliminar"))