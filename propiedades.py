from PyQt6.uic.properties import QtWidgets, QtGui
from PyQt6 import QtWidgets

import conexion
import eventos
import var
import dlg_gestion_propiedad_tipo

class Propiedades():
    campos = {}

    def inicializar_campos():
        Propiedades.campos = {
            "codigo": var.ui.lbl_pro_codigo,
            "fecha_alta": var.ui.txt_pro_alta,
            "fecha_baja": var.ui.txt_pro_baja,
            "direccion": var.ui.txt_pro_direccion,
            "provincia": var.ui.cmb_pro_provincia,
            "municipio": var.ui.cmb_pro_municipio,
            "postal": var.ui.txt_pro_postal,
            "tipo": var.ui.cmb_pro_tipo,
            "habitaciones": var.ui.spin_pro_habitaciones,
            "banos": var.ui.spin_pro_banos,
            "superficie": var.ui.txt_pro_superficie,
            "precio_alquiler": var.ui.txt_pro_precio_alquiler,
            "precio_venta": var.ui.txt_pro_precio_venta,
            "descripcion": var.ui.areatxt_pro_descripcion,
            "check_alquiler": var.ui.chk_pro_alquiler,
            "check_venta": var.ui.chk_pro_venta,
            "check_intercambio": var.ui.chk_pro_intercambio,
            "radio_disponible": var.ui.rbt_pro_disponible,
            "radio_alquilado": var.ui.rbt_pro_alquilado,
            "radio_vendido": var.ui.rbt_pro_vendido,
            "propietario": var.ui.txt_pro_propietario,
            "movil": var.ui.txt_pro_movil
        }

    def construir_propiedad():
        propiedad = {"codigo": Propiedades.campos["codigo"].text(), "fecha_alta": Propiedades.campos["fecha_alta"].text(),
                     "fecha_baja": Propiedades.campos["fecha_baja"].text(), "direccion": Propiedades.campos["direccion"].text(),
                     "provincia": Propiedades.campos["provincia"].currentText(), "municipio": Propiedades.campos["municipio"].currentText(),
                     "postal": Propiedades.campos["postal"].text(), "tipo": Propiedades.campos["tipo"].currentText(),
                     "habitaciones": Propiedades.campos["habitaciones"].text(), "banos": Propiedades.campos["banos"].text(),
                     "superficie": Propiedades.campos["superficie"].text(), "precio_alquiler": Propiedades.campos["precio_alquiler"].text(),
                     "precio_venta": Propiedades.campos["precio_venta"].text(), "descripcion": Propiedades.campos["descripcion"].toPlainText(),
                     "propietario": Propiedades.campos["propietario"].text(), "movil": Propiedades.campos["movil"].text(),
                     "operaciones": "", "estado": ""}
        
        if Propiedades.campos["check_alquiler"].isChecked():
            propiedad["operaciones"] = propiedad["operaciones"] + "-" + Propiedades.campos["check_alquiler"].text()
        if Propiedades.campos["check_venta"].isChecked():
            propiedad["operaciones"] = propiedad["operaciones"] + "-" + Propiedades.campos["check_venta"].text()
        if Propiedades.campos["check_intercambio"].isChecked():
            propiedad["operaciones"] = propiedad["operaciones"] + "-" + Propiedades.campos["check_intercambio"].text()

        propiedad["operaciones"] = propiedad["operaciones"][1:]

        if Propiedades.campos["radio_disponible"].isChecked():
                propiedad["estado"] = Propiedades.campos["radio_disponible"].text()
        elif Propiedades.campos["radio_alquilado"].isChecked():
                propiedad["estado"] = Propiedades.campos["radio_alquilado"].text()
        elif Propiedades.campos["radio_vendido"].isChecked():
                propiedad["estado"] = Propiedades.campos["radio_vendido"].text()

        return propiedad

    def alta_tipo_propiedad(self):
        try:
            tipo = var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.text()
            registro = conexion.Conexion.alta_propiedad_tipo(tipo)
            if registro:
                eventos.Eventos.cargar_propiedad_tipos(self)
                eventos.Eventos.mensaje_exito("Aviso", "Tipo de propiedad registrado con éxito")
            else:
                eventos.Eventos.mensaje_error("Aviso", "Ese tipo de propieda ya existe")
            var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.setText("")
        except Exception as e:
            print(f"Error: {e}")

    def baja_tipo_propiedad(self):
        try:
            tipo = var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.text()
            if conexion.Conexion.baja_propiedad_tipo(tipo):
                eventos.Eventos.cargar_propiedad_tipos(self)
                eventos.Eventos.mensaje_exito("Aviso", "Tipo de propiedad dado de baja")
            else:
                eventos.Eventos.mensaje_error("Aviso", "Ese tipo de propieda no existe")
            var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.setText("")
        except Exception as e:
            print(f"Error: {e}")


    def alta_propiedad(self):
        Propiedades.inicializar_campos()
        if not Propiedades.validar_campos_pro():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
            return

        try:
            propiedad = Propiedades.construir_propiedad()
            conexion.Conexion.alta_propiedad(propiedad)
            eventos.Eventos.mensaje_exito("Aviso", "Propiedad dada de alta con éxito")
            Propiedades.cargar_pro_tab()
        except Exception as e:
            print("error en en alta de una propiedad")

    def baja_propiedad(self):
        print("a")

    @staticmethod
    def cargar_pro_tab():
        try:
            propiedades = conexion.Conexion.listar_propiedades()
            index = 0
            var.ui.tab_pro.verticalHeader().setVisible(False)

            for propiedad in propiedades:
                var.ui.tab_pro.setRowCount(index + 1)
                var.ui.tab_pro.setItem(index, 0, QtWidgets.QTableWidgetItem(propiedad["codigo"]))
                var.ui.tab_pro.setItem(index, 1, QtWidgets.QTableWidgetItem(propiedad["municipio"]))
                var.ui.tab_pro.setItem(index, 2, QtWidgets.QTableWidgetItem(propiedad["tipo"]))
                var.ui.tab_pro.setItem(index, 3, QtWidgets.QTableWidgetItem(propiedad["habitaciones"]))
                var.ui.tab_pro.setItem(index, 4, QtWidgets.QTableWidgetItem(propiedad["banos"]))
                var.ui.tab_pro.setItem(index, 5, QtWidgets.QTableWidgetItem(
                    propiedad["precio_alquiler"] + " €" if propiedad["precio_alquiler"] else "-"))
                var.ui.tab_pro.setItem(index, 6, QtWidgets.QTableWidgetItem(
                    propiedad["precio_venta"] + " €" if propiedad["precio_venta"] else "-"))
                var.ui.tab_pro.setItem(index, 7, QtWidgets.QTableWidgetItem(propiedad["operaciones"]))
                var.ui.tab_pro.setItem(index, 8, QtWidgets.QTableWidgetItem(propiedad["fecha_baja"]))

                var.ui.tab_pro.item(index, 0)
                var.ui.tab_pro.item(index, 1)
                var.ui.tab_pro.item(index, 2)
                var.ui.tab_pro.item(index, 3)
                var.ui.tab_pro.item(index, 4)
                var.ui.tab_pro.item(index, 5)
                var.ui.tab_pro.item(index, 6)
                var.ui.tab_pro.item(index, 7)
                var.ui.tab_pro.item(index, 8)

                index += 1
        except Exception as error:
            print("error al cargar la tabal de propiedades", error)

    def cargar_propiedad(self):
        Propiedades.inicializar_campos()
        try:
            codigo = var.ui.tab_pro.selectedItems()[0].text()
            propiedad = conexion.Conexion.get_cliente(codigo)
            print(propiedad)
        except Exception as error:
            print("error al cargar el cliente", error)

    def validar_campos_pro():
        Propiedades.inicializar_campos()

        fecha_alta = Propiedades.campos["fecha_alta"].text()
        fecha_baja = Propiedades.campos["fecha_baja"].text()
        direccion = Propiedades.campos["direccion"].text()
        provincia = Propiedades.campos["provincia"].currentText()
        municipio = Propiedades.campos["municipio"].currentText()
        postal = Propiedades.campos["postal"].text()
        tipo = Propiedades.campos["tipo"].currentText()
        habitaciones = Propiedades.campos["habitaciones"].text()
        banos = Propiedades.campos["banos"].text()
        superficie = Propiedades.campos["superficie"].text()
        precio_alquiler = Propiedades.campos["precio_alquiler"].text()
        precio_venta = Propiedades.campos["precio_venta"].text()
        descripcion = Propiedades.campos["descripcion"].toPlainText()
        check_alquiler = Propiedades.campos["check_alquiler"].isChecked()
        check_venta = Propiedades.campos["check_venta"].isChecked()
        check_intercambio = Propiedades.campos["check_intercambio"].isChecked()
        radio_disponible = Propiedades.campos["radio_disponible"].isChecked()
        radio_alquilado = Propiedades.campos["radio_alquilado"].isChecked()
        radio_vendido = Propiedades.campos["radio_vendido"].isChecked()
        propietario = Propiedades.campos["propietario"].text()
        movil = Propiedades.campos["movil"].text()

        if (not fecha_alta.strip() or not direccion.strip() or not provincia.strip() or not municipio.strip() or not postal.strip() or not tipo.strip()
            or not habitaciones.strip() or not banos.strip() or not superficie.strip() or not propietario.strip() or not movil.strip()):
            return False
        
        if (not eventos.Eventos.validar_fecha(fecha_alta) or not eventos.Eventos.validar_movil(movil)
            or not eventos.Eventos.validar_numero(postal) or not eventos.Eventos.validar_numero(habitaciones)
            or not eventos.Eventos.validar_numero(banos) or not eventos.Eventos.validar_numero(superficie)):
            return False
        
        if (not radio_disponible and not radio_alquilado and not radio_vendido):
            return False
        
        if (not precio_alquiler.strip() and not precio_venta.strip()):
            return False
        
        if (precio_alquiler.strip() and not eventos.Eventos.validar_numero(precio_alquiler)):
            return False
        
        if (precio_venta.strip() and not eventos.Eventos.validar_numero(precio_venta)):
            return False
        
        if (fecha_baja.strip() and not eventos.Eventos.validar_fecha(fecha_baja)):
            return False
        
        if (not check_alquiler and not check_venta and not check_intercambio):
            return False

        return True
    
    @staticmethod
    def validar_movil():
        Propiedades.inicializar_campos()
        try:
            phone = str(Propiedades.campos["movil"].text())

            if eventos.Eventos.validar_movil(phone):
                Propiedades.campos["movil"].setStyleSheet('''QLineEdit#txt_pro_movil {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_pro_movil:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            else:
                Propiedades.campos["movil"].setStyleSheet('''QLineEdit#txt_pro_movil {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_pro_movil:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Propiedades.campos["movil"].setText(None)
                Propiedades.campos["movil"].setText("móvil no válido")
                Propiedades.campos["movil"].setFocus()
        except Exception as error:
            print("error check propiedad", error)

    @staticmethod
    def validar_fecha_alta():
        Propiedades.inicializar_campos()
        try:
            fecha = Propiedades.campos["fecha_alta"].text()

            if eventos.Eventos.validar_fecha(fecha):
                Propiedades.campos["fecha_alta"].setStyleSheet('''QLineEdit#txt_pro_alta {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_pro_alta:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            else:
                Propiedades.campos["fecha_alta"].setStyleSheet('''QLineEdit#txt_pro_alta {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_pro_alta:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Propiedades.campos["fecha_alta"].setText(None)
                Propiedades.campos["fecha_alta"].setText("fecha no válida")
                Propiedades.campos["fecha_alta"].setFocus()
        except Exception as error:
            print("Error al validar la fecha de alta", error)

    @staticmethod
    def validar_postal():
        Propiedades.inicializar_campos()
        try:
            postal = Propiedades.campos["postal"].text()

            if eventos.Eventos.validar_numero(postal):
                Propiedades.campos["postal"].setStyleSheet('''QLineEdit#txt_pro_postal {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_pro_postal:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            else:
                Propiedades.campos["postal"].setStyleSheet('''QLineEdit#txt_pro_postal {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_pro_postal:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Propiedades.campos["postal"].setText(None)
                Propiedades.campos["postal"].setText("CP no válido")
                Propiedades.campos["postal"].setFocus()
        except Exception as error:
            print("Error al validar el código postal", error)

    @staticmethod
    def validar_superficie():
        Propiedades.inicializar_campos()
        try:
            superficie = Propiedades.campos["superficie"].text()

            if eventos.Eventos.validar_numero(superficie):
                Propiedades.campos["superficie"].setStyleSheet('''QLineEdit#txt_pro_superficie {border-bottom: 1px solid #fdba74;
                                                                                background-color: #ffedd5;}
                                                        QLineEdit#txt_pro_superficie:focus {border-bottom: 1.5px solid #ea580c;
                                                                                        background-color: #fed7aa;}''')
            else:
                Propiedades.campos["superficie"].setStyleSheet('''QLineEdit#txt_pro_superficie {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_pro_superficie:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Propiedades.campos["superficie"].setText(None)
                Propiedades.campos["superficie"].setText("Valor no válido")
                Propiedades.campos["superficie"].setFocus()
        except Exception as error:
            print("Error al validar la superficie", error)

    @staticmethod
    def validar_fecha_baja():
        Propiedades.inicializar_campos()
        try:
            fecha = Propiedades.campos["fecha_baja"].text()

            if eventos.Eventos.validar_fecha(fecha) or fecha == "":
                Propiedades.campos["fecha_baja"].setStyleSheet('''QLineEdit#txt_pro_baja {border-bottom: 1px solid #93c5fd;
                                                                                background-color: #dbeafe;}
                                                        QLineEdit#txt_pro_baja:focus {border-bottom: 1.5px solid #2563eb;
                                                                                        background-color: #bfdbfe;}''')
            else:
                Propiedades.campos["fecha_baja"].setStyleSheet('''QLineEdit#txt_pro_baja {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_pro_baja:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Propiedades.campos["fecha_baja"].setText(None)
                Propiedades.campos["fecha_baja"].setText("fecha no válida")
                Propiedades.campos["fecha_baja"].setFocus()
        except Exception as error:
            print("Error al validar la fecha de baja", error)

    @staticmethod
    def validar_precio_alquiler():
        Propiedades.inicializar_campos()
        try:
            precio_alquiler = Propiedades.campos["precio_alquiler"].text()

            if eventos.Eventos.validar_numero(precio_alquiler) or precio_alquiler == "":
                Propiedades.campos["precio_alquiler"].setStyleSheet('''QLineEdit#txt_pro_precio_alquiler {border-bottom: 1px solid #93c5fd;
                                                                                background-color: #dbeafe;}
                                                        QLineEdit#txt_pro_precio_alquiler:focus {border-bottom: 1.5px solid #2563eb;
                                                                                        background-color: #bfdbfe;}''')
            else:
                Propiedades.campos["precio_alquiler"].setStyleSheet('''QLineEdit#txt_pro_precio_alquiler {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_pro_precio_alquiler:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Propiedades.campos["precio_alquiler"].setText(None)
                Propiedades.campos["precio_alquiler"].setText("Valor no válido")
                Propiedades.campos["precio_alquiler"].setFocus()
        except Exception as error:
            print("Error al validar el precio de alquiler", error)

    @staticmethod
    def validar_precio_venta():
        Propiedades.inicializar_campos()
        try:
            precio_venta = Propiedades.campos["precio_venta"].text()

            if eventos.Eventos.validar_numero(precio_venta) or precio_venta == "":
                Propiedades.campos["precio_venta"].setStyleSheet('''QLineEdit#txt_pro_precio_venta {border-bottom: 1px solid #93c5fd;
                                                                                background-color: #dbeafe;}
                                                        QLineEdit#txt_pro_precio_venta:focus {border-bottom: 1.5px solid #2563eb;
                                                                                        background-color: #bfdbfe;}''')
            else:
                Propiedades.campos["precio_venta"].setStyleSheet('''QLineEdit#txt_pro_precio_venta {border-bottom: 1px solid #f87171;
                                                                                background-color: #fecaca;}
                                                        QLineEdit#txt_pro_precio_venta:focus {border-bottom: 1.5px solid #dc2626;
                                                                                        background-color: #fca5a5;}''')
                Propiedades.campos["precio_venta"].setText(None)
                Propiedades.campos["precio_venta"].setText("Valor no válido")
                Propiedades.campos["precio_venta"].setFocus()
        except Exception as error:
            print("Error al validar el precio de venta", error)