# Form implementation generated from reading ui file '/home/manu/Proyecto_interfaces/templates/dlgCalendar.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgCalendar(object):
    def setupUi(self, dlgCalendar):
        dlgCalendar.setObjectName("dlgCalendar")
        dlgCalendar.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgCalendar.resize(500, 185)
        dlgCalendar.setMinimumSize(QtCore.QSize(500, 185))
        dlgCalendar.setMaximumSize(QtCore.QSize(500, 185))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/manu/Proyecto_interfaces/templates/../img/house.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgCalendar.setWindowIcon(icon)
        dlgCalendar.setModal(True)
        self.Calendar = QtWidgets.QCalendarWidget(parent=dlgCalendar)
        self.Calendar.setGeometry(QtCore.QRect(0, 0, 500, 183))
        self.Calendar.setMinimumSize(QtCore.QSize(500, 183))
        self.Calendar.setMaximumSize(QtCore.QSize(500, 183))
        self.Calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.Calendar.setObjectName("Calendar")

        self.retranslateUi(dlgCalendar)
        QtCore.QMetaObject.connectSlotsByName(dlgCalendar)

    def retranslateUi(self, dlgCalendar):
        _translate = QtCore.QCoreApplication.translate
        dlgCalendar.setWindowTitle(_translate("dlgCalendar", "Selecciona fecha"))
