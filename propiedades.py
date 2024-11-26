from tabnanny import check
from PyQt6.uic.properties import QtWidgets, QtGui
from PyQt6 import QtWidgets

import var
import eventos
import conexion
import mapper

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

    def alta_tipo_propiedad(self):
        Propiedades.inicializar_campos()
        try:
            tipo = var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.text()
            registro = conexion.Conexion.alta_propiedad_tipo(tipo)
            if registro:
                eventos.Eventos.mensaje_exito("Aviso", "Tipo de propiedad registrado con éxito")
            else:
                eventos.Eventos.mensaje_error("Aviso", "Ese tipo de propieda ya existe")
            var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.setText("")
            eventos.Eventos.cargar_propiedad_tipos(Propiedades.campos["tipo"])
            eventos.Eventos.cargar_propiedad_tipos(var.dlg_filtrar_propiedades.ui.cmb_pro_tipo_filtrar)
        except Exception as e:
            print(f"Error: {e}")

    def baja_tipo_propiedad(self):
        Propiedades.inicializar_campos()
        try:
            tipo = var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.text()
            if conexion.Conexion.baja_propiedad_tipo(tipo):
                eventos.Eventos.mensaje_exito("Aviso", "Tipo de propiedad dado de baja")
            else:
                eventos.Eventos.mensaje_error("Aviso", "Ese tipo de propieda no existe")
            var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.setText("")
            eventos.Eventos.cargar_propiedad_tipos(Propiedades.campos["tipo"])
            eventos.Eventos.cargar_propiedad_tipos(var.dlg_filtrar_propiedades.ui.cmb_pro_tipo_filtrar)
        except Exception as e:
            print(f"Error: {e}")


    def alta_propiedad(self):
        Propiedades.inicializar_campos()
        if not Propiedades.validar_campos_pro():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
            return
        if Propiedades.check_fecha_baja_prop():
            eventos.Eventos.mensaje_error("Aviso", "No introduzcas una fecha de baja al dar de alta una propiedad")
            return
        if not Propiedades.campos["radio_disponible"].isChecked():
            eventos.Eventos.mensaje_error("Aviso", "Al dar de alta una propiedad su estado tiene que estar en disponible")
            return

        try:
            propiedad = mapper.Mapper.map_propiedad(Propiedades.campos)
            if conexion.Conexion.alta_propiedad(propiedad):
                eventos.Eventos.mensaje_exito("Aviso", "Propiedad dada de alta con éxito")
            else:
                eventos.Eventos.mensaje_error("Aviso", "No se pudo dar de alta la propiedad")
            var.state_manager.change_state("propiedad_query_object", conexion.Conexion.listar_propiedades())
        except Exception as e:
            print("error en en alta de una propiedad")

    def modificar_propiedad(self):
        Propiedades.inicializar_campos()
        if not Propiedades.validar_campos_pro():
            eventos.Eventos.mensaje_error("Aviso", "Faltan datos por introducir")
            return
        if not Propiedades.check_dar_baja_prop():
            eventos.Eventos.mensaje_error("Aviso", "Si quieres dar de baja una propiedad tienes que introducir"
                                                   " una fecha de baja y ponder su estado a alquilado o vendido")
            return

        codigo = Propiedades.campos["codigo"].text()
        if (codigo):

            try:
                propiedad = mapper.Mapper.map_propiedad(Propiedades.campos)
                if conexion.Conexion.modificar_propiedad(propiedad):
                    eventos.Eventos.mensaje_exito("Aviso", "Propiedad modificada con éxito")
                else:
                    eventos.Eventos.mensaje_error("Aviso", "No se pudo modificar la propiedad")
                var.state_manager.change_state("propiedad_query_object", conexion.Conexion.listar_propiedades())
            except Exception as e:
                print("Error al modificar la propiedad", e)

        else:
            eventos.Eventos.mensaje_error("Aviso", "Seleccione una propiedad a modificar")

    def baja_propiedad(self):
        if (not Propiedades.campos["fecha_baja"].text() or not Propiedades.check_dar_baja_prop()
            or not eventos.Eventos.validar_fecha(Propiedades.campos["fecha_baja"].text())):
            eventos.Eventos.mensaje_error("Aviso", "Si quieres dar de baja una propiedad tienes que introducir"
                                                   " una fecha de baja y ponder su estado a alquilado o vendido")
            return

        codigo = Propiedades.campos["codigo"].text()
        if (codigo):

            try:
                propiedad = mapper.Mapper.map_propiedad(Propiedades.campos)
                if conexion.Conexion.eliminar_propiedad(propiedad):
                    eventos.Eventos.mensaje_exito("Aviso", "Propiedad dada de baja con éxito")
                else:
                    eventos.Eventos.mensaje_error("Aviso", "No se pudo dar de baja la propiedad")
                var.state_manager.change_state("propiedad_query_object", conexion.Conexion.listar_propiedades())
            except Exception as e:
                print("Error al dar de baja la propiedad", e)

        else:
            eventos.Eventos.mensaje_error("Aviso", "Seleccione una propiedad a dar de baja")
        return

    def filtrar_propiedades():
        try:
            tipo = Propiedades.campos["tipo"].currentText()
            municipio = Propiedades.campos["municipio"].currentText()
            propiedades = conexion.Conexion.filtrar_propiedades(tipo, municipio)

            var.state_manager.change_state("propiedad_query_object", propiedades)
        except Exception as error:
            print("Error al filtrar las propiedades", error)

    def cargar_propiedad(self):
        Propiedades.inicializar_campos()
        try:
            codigo = var.ui.tab_pro.selectedItems()[0].text()
            propiedad = conexion.Conexion.get_propiedad(codigo)
            for key in propiedad:
                if key == "provincia" or key == "municipio" or key == "tipo":
                    Propiedades.campos[key].setCurrentText(propiedad[key])
                elif key == "habitaciones" or key == "banos":
                    Propiedades.campos[key].setValue(int(propiedad[key]))
                elif key == "operaciones":
                    Propiedades.campos["check_alquiler"].setChecked(False)
                    Propiedades.campos["check_venta"].setChecked(False)
                    Propiedades.campos["check_intercambio"].setChecked(False)
                    if "Alquiler" in propiedad[key]:
                        Propiedades.campos["check_alquiler"].setChecked(True)

                    if "Venta" in propiedad[key]:
                        Propiedades.campos["check_venta"].setChecked(True)

                    if "Intercambio" in propiedad[key]:
                        Propiedades.campos["check_intercambio"].setChecked(True)

                elif key == "estado":
                    Propiedades.campos["radio_disponible"].setChecked(False)
                    Propiedades.campos["radio_alquilado"].setChecked(False)
                    Propiedades.campos["radio_vendido"].setChecked(False)

                    if propiedad[key] == "Disponible":
                        Propiedades.campos["radio_disponible"].setChecked(True)

                    if propiedad[key] == "Alquilado":
                        Propiedades.campos["radio_alquilado"].setChecked(True)

                    if propiedad[key] == "Vendido":
                        Propiedades.campos["radio_vendido"].setChecked(True)

                else:
                    Propiedades.campos[key].setText(propiedad[key])
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

        if ((not precio_venta.strip() and check_venta) or (precio_venta.strip() and not check_venta)):
            return False

        if ((not precio_alquiler.strip() and check_alquiler) or (precio_alquiler.strip() and not check_alquiler)):
            return False
        
        if (fecha_baja.strip() and not eventos.Eventos.validar_fecha(fecha_baja)):
            return False
        
        if (not check_alquiler and not check_venta and not check_intercambio):
            return False

        return True

    def check_fecha_baja_prop():
        Propiedades.inicializar_campos()
        if (Propiedades.campos["fecha_baja"].text().strip()):
            return True
        return False

    def check_dar_baja_prop():
        Propiedades.inicializar_campos()
        if (Propiedades.check_fecha_baja_prop()
                and Propiedades.campos["radio_disponible"].isChecked()):
            return False

        if (not Propiedades.check_fecha_baja_prop()
                and not Propiedades.campos["radio_disponible"].isChecked()):
            return False

        return True