# Form implementation generated from reading ui file '/home/manu/Proyecto_interfaces/templates/dlg_about.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DlgAbout(object):
    def setupUi(self, DlgAbout):
        DlgAbout.setObjectName("DlgAbout")
        DlgAbout.resize(400, 300)
        DlgAbout.setMinimumSize(QtCore.QSize(400, 300))
        DlgAbout.setMaximumSize(QtCore.QSize(400, 300))
        DlgAbout.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/manu/Proyecto_interfaces/templates/../img/house.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        DlgAbout.setWindowIcon(icon)
        DlgAbout.setModal(True)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=DlgAbout)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 9, 381, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/manu/Proyecto_interfaces/templates/../img/house.ico"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.btn_cerrar_about = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_cerrar_about.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_cerrar_about.setMaximumSize(QtCore.QSize(80, 25))
        self.btn_cerrar_about.setObjectName("btn_cerrar_about")
        self.gridLayout_4.addWidget(self.btn_cerrar_about, 5, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(DlgAbout)
        QtCore.QMetaObject.connectSlotsByName(DlgAbout)

    def retranslateUi(self, DlgAbout):
        _translate = QtCore.QCoreApplication.translate
        DlgAbout.setWindowTitle(_translate("DlgAbout", "Acerca de"))
        self.label_4.setText(_translate("DlgAbout", "v. 0.0.1"))
        self.label_2.setText(_translate("DlgAbout", "InmoTeis"))
        self.label_3.setText(_translate("DlgAbout", "Manuel Álvarez Gómez"))
        self.label_5.setText(_translate("DlgAbout", "©"))
        self.btn_cerrar_about.setText(_translate("DlgAbout", "Cerrar"))