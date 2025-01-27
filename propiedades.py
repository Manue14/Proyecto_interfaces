from tabnanny import check
from PyQt6.uic.properties import QtWidgets, QtGui
from PyQt6 import QtWidgets

import var
import eventos
import conexion
import mapper
import facturas


class Propiedades():
    campos = {}
    _codigo, _fecha_alta, _fecha_baja, _direccion, _provincia, _municipio = "", "", "" , "", "", ""
    _postal, _tipo, _habitaciones, _banos, _superficie = "", "", "", "", ""
    _precio_alquiler, _precio_venta, _descripcion, _propietario, _movil = "", "", "", "", ""
    _check_alquiler, _check_venta, _check_intercambio = False, False, False
    _radio_disponible, _radio_alquilado, _radio_vendido = False, False, False

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

    def inicializar_valores():
        Propiedades._codigo = Propiedades.campos["codigo"].text()
        Propiedades._fecha_alta = Propiedades.campos["fecha_alta"].text()
        Propiedades._fecha_baja = Propiedades.campos["fecha_baja"].text()
        Propiedades._direccion = Propiedades.campos["direccion"].text()
        Propiedades._provincia = Propiedades.campos["provincia"].currentText()
        Propiedades._municipio = Propiedades.campos["municipio"].currentText()
        Propiedades._postal = Propiedades.campos["postal"].text()
        Propiedades._tipo = Propiedades.campos["tipo"].currentText()
        Propiedades._habitaciones = Propiedades.campos["habitaciones"].text()
        Propiedades._banos = Propiedades.campos["banos"].text()
        Propiedades._superficie = Propiedades.campos["superficie"].text()
        Propiedades._precio_alquiler = Propiedades.campos["precio_alquiler"].text()
        Propiedades._precio_venta = Propiedades.campos["precio_venta"].text()
        Propiedades._descripcion = Propiedades.campos["descripcion"].toPlainText()
        Propiedades._check_alquiler = Propiedades.campos["check_alquiler"].isChecked()
        Propiedades._check_venta = Propiedades.campos["check_venta"].isChecked()
        Propiedades._check_intercambio = Propiedades.campos["check_intercambio"].isChecked()
        Propiedades._radio_disponible = Propiedades.campos["radio_disponible"].isChecked()
        Propiedades._radio_alquilado = Propiedades.campos["radio_alquilado"].isChecked()
        Propiedades._radio_vendido = Propiedades.campos["radio_vendido"].isChecked()
        Propiedades._propietario = Propiedades.campos["propietario"].text()
        Propiedades._movil = Propiedades.campos["movil"].text()

    def alta_tipo_propiedad(self):
        Propiedades.inicializar_campos()
        try:
            tipo = var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.text()
            exito = var.clase_conexion.alta_propiedad_tipo(tipo)
            if exito:
                eventos.Eventos.mensaje_exito("Aviso", "Tipo de propiedad registrado con éxito")
            else:
                eventos.Eventos.mensaje_error("Aviso", "Ese tipo de propieda ya existe")
            var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.setText("")
            eventos.Eventos.cargar_propiedad_tipos(Propiedades.campos["tipo"])
        except Exception as e:
            print(f"Error: {e}")

    def baja_tipo_propiedad(self):
        Propiedades.inicializar_campos()
        try:
            tipo = var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.text()
            if var.clase_conexion.baja_propiedad_tipo(tipo):
                eventos.Eventos.mensaje_exito("Aviso", "Tipo de propiedad dado de baja")
            else:
                eventos.Eventos.mensaje_error("Aviso", "Ese tipo de propieda no existe")
            var.dlg_gestion_propiedad_tipo.ui.txt_pro_gestion_tipo.setText("")
            eventos.Eventos.cargar_propiedad_tipos(Propiedades.campos["tipo"])
        except Exception as e:
            print(f"Error: {e}")


    def alta_propiedad(self):
        response = Propiedades.check_if_propiedad_valid_for_create()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            propiedad = mapper.Mapper.map_propiedad(Propiedades.campos)
            last_id = var.clase_conexion.alta_propiedad(propiedad)
            if last_id != -1:
                eventos.Eventos.mensaje_exito("Aviso", "Propiedad dada de alta con éxito")
                propiedad_updated = var.clase_conexion.get_propiedad(last_id)
                Propiedades.populate_fields(propiedad_updated)
            else:
                eventos.Eventos.mensaje_error("Aviso", "No se pudo dar de alta la propiedad")
            var.state_manager.update_tabla_propiedades()
        except Exception as e:
            print("error en en alta de una propiedad")

    def modificar_propiedad(self):
        response = Propiedades.check_if_propiedad_valid_for_edit()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            propiedad = mapper.Mapper.map_propiedad(Propiedades.campos)
            if var.clase_conexion.modificar_propiedad(propiedad):
                eventos.Eventos.mensaje_exito("Aviso", "Propiedad modificada con éxito")
            else:
                eventos.Eventos.mensaje_error("Aviso", "No se pudo modificar la propiedad")
            var.state_manager.update_tabla_propiedades()
        except Exception as e:
            print("Error al modificar la propiedad", e)

    def baja_propiedad(self):
        response = Propiedades.check_if_propiedad_valid_for_delete()
        if not response["valid"]:
            eventos.Eventos.mensaje_error("Aviso", response["messages"])
            return

        try:
            propiedad = mapper.Mapper.map_propiedad(Propiedades.campos)
            if var.clase_conexion.eliminar_propiedad(propiedad):
                eventos.Eventos.mensaje_exito("Aviso", "Propiedad dada de baja con éxito")
            else:
                eventos.Eventos.mensaje_error("Aviso", "No se pudo dar de baja la propiedad")
            var.state_manager.update_tabla_propiedades()
            eventos.Eventos.limpiar_panel()
        except Exception as e:
            print("Error al dar de baja la propiedad", e)

    def filtrar_propiedades():
        try:
            tipo = Propiedades.campos["tipo"].currentText()
            municipio = Propiedades.campos["municipio"].currentText()
            propiedades = var.clase_conexion.filtrar_propiedades(tipo, municipio)
            var.state_manager.change_state("last_propiedad_params", [tipo, municipio])
            var.state_manager.change_state("last_propiedad_function", var.clase_conexion.filtrar_propiedades)
        except Exception as error:
            print("Error al filtrar las propiedades", error)

    def cargar_propiedad(self):
        Propiedades.inicializar_campos()
        try:
            codigo = var.ui.tab_pro.selectedItems()[0].text()
            propiedad = var.clase_conexion.get_propiedad(codigo)
            Propiedades.populate_fields(propiedad)
            facturas.Facturas.populate_propiedad_fields(propiedad)
        except Exception as error:
            print("error al cargar el cliente", error)

    def populate_fields(propiedad):
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
                    var.state_manager.change_state("check_alquiler_propiedad", True)
                if "Venta" in propiedad[key]:
                    Propiedades.campos["check_venta"].setChecked(True)
                    var.state_manager.change_state("check_venta_propiedad", True)
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
                var.state_manager.change_state("precio_alquiler_propiedad", eventos.Eventos.validar_numero(propiedad["precio_alquiler"]))
                var.state_manager.change_state("precio_venta_propiedad", eventos.Eventos.validar_numero(propiedad["precio_venta"]))
        eventos.Eventos.observar_fecha_baja(Propiedades.campos["fecha_baja"])

    def common_checks(response):
        if (not Propiedades._fecha_alta.strip() or not Propiedades._direccion.strip() or not Propiedades._provincia.strip()
            or not Propiedades._municipio.strip() or not Propiedades._postal.strip() or not Propiedades._tipo.strip()
            or not Propiedades._habitaciones.strip() or not Propiedades._banos.strip() or not Propiedades._superficie.strip()
            or not Propiedades._propietario.strip() or not Propiedades._movil.strip()):
            response["valid"] = False
            response["messages"].append("Algún campo obligatorio no está cubierto")
        
        if (not eventos.Eventos.validar_fecha(Propiedades._fecha_alta) or not eventos.Eventos.validar_movil(Propiedades._movil)
            or not eventos.Eventos.validar_numero(Propiedades._postal) or not eventos.Eventos.validar_numero(Propiedades._habitaciones)
            or not eventos.Eventos.validar_numero(Propiedades._banos) or not eventos.Eventos.validar_numero(Propiedades._superficie)):
            response["valid"] = False
            response["messages"].append("Algún campo obligatorio no tiene el formato correcto")

        if (not Propiedades._check_alquiler and not Propiedades._check_venta and not Propiedades._check_intercambio):
            response["valid"] = False
            response["messages"].append("Al menos un tipo de operación tiene que estar seleccionado")

        if (Propiedades._check_alquiler and (not Propiedades._precio_alquiler.strip() or not eventos.Eventos.validar_numero(Propiedades._precio_alquiler))):
            response["valid"] = False
            response["messages"].append("Si el tipo de operación 'Alquiler' está seleccionado es necesario un precio de alquiler válido")

        if (Propiedades._precio_alquiler.strip() and eventos.Eventos.validar_numero(Propiedades._precio_alquiler) and not Propiedades._check_alquiler):
            response["valid"] = False
            response["messages"].append("Si introduces un precio de alquiler el tipo de operación 'Alquiler' debe de estar seleccionado")

        if (Propiedades._check_venta and (not Propiedades._precio_venta.strip() or not eventos.Eventos.validar_numero(Propiedades._precio_venta))):
            response["valid"] = False
            response["messages"].append("Si el tipo de operación 'Venta' está seleccionado es necesario un precio de venta válido")

        if (Propiedades._precio_venta.strip() and eventos.Eventos.validar_numero(Propiedades._precio_venta) and not Propiedades._check_venta):
            response["valid"] = False
            response["messages"].append("Si introduces un precio de venta el tipo de operación 'Venta' debe de estar seleccionado")

    def check_if_propiedad_valid_for_create():
        response = {
            "valid": True,
            "messages": []
        }

        Propiedades.inicializar_campos()
        Propiedades.inicializar_valores()

        Propiedades.common_checks(response)

        if (var.clase_conexion.get_propiedad(Propiedades._codigo) and Propiedades._codigo != ""):
            response["valid"] = False
            response["messages"].append("La propiedad con código " + Propiedades._codigo + " ya existe")

        if (Propiedades._fecha_baja.strip()):
            response["valid"] = False
            response["messages"].append("Al dar de alta una propiedad no puedes introducir una fecha de baja")

        if (not Propiedades._radio_disponible or Propiedades._radio_alquilado or Propiedades._radio_vendido):
            response["valid"] = False
            response["messages"].append("Al dar de alta una propiedad su estado debe ser 'Disponible'")

        return response
    
    def check_if_propiedad_valid_for_edit():
        response = {
            "valid": True,
            "messages": []
        }

        Propiedades.inicializar_campos()
        Propiedades.inicializar_valores()

        Propiedades.common_checks(response)

        if (not Propiedades._codigo.strip() or not var.clase_conexion.get_propiedad(Propiedades._codigo)):
            response["valid"] = False
            response["messages"].append("La propiedad con código " + Propiedades._codigo + " no existe")

        if (Propiedades._fecha_baja.strip()):
            if not eventos.Eventos.validar_fecha(Propiedades._fecha_baja):
                response["valid"] = False
                response["messages"].append("La fecha de baja introducida no tiene el formato correcto")

            if Propiedades._radio_disponible:
                response["valid"] = False
                response["messages"].append("Con una fecha de baja el estado no puede ser 'Disponible'")

            if Propiedades._radio_alquilado:
                if not Propiedades._check_alquiler:
                    response["valid"] = False
                    response["messages"].append("Con el estado 'Alquilado' seleccionado el tipo de operación 'Alquiler' debe de estar seleccionado")
                else:
                    if not Propiedades._precio_alquiler.strip() or not eventos.Eventos.validar_numero(Propiedades._precio_alquiler):
                        response["valid"] = False
                        response["messages"].append("Con el tipo de operación 'Alquiler' seleccionado debe introducirse un precio de alquiler válido")

            if Propiedades._radio_vendido:
                if not Propiedades._check_venta:
                    response["valid"] = False
                    response["messages"].append("Con el estado 'Vendido' seleccionado el tipo de operación 'Venta' debe de estar seleccionado")
                else:
                    if not Propiedades._precio_venta.strip() or not eventos.Eventos.validar_numero(Propiedades._precio_venta):
                        response["valid"] = False
                        response["messages"].append("Con el tipo de operación 'Venta' seleccionado debe introducirse un precio de venta válido")

        if (not Propiedades._fecha_baja.strip()):
            if not Propiedades._radio_disponible:
                response["valid"] = False
                response["messages"].append("Sin una fecha de baja el estado debe de ser 'Disponible'")
            
        return response
    
    def check_if_propiedad_valid_for_delete():
        response = {
            "valid": True,
            "messages": []
        }

        Propiedades.inicializar_campos()
        Propiedades.inicializar_valores()

        if (not Propiedades._codigo.strip() or not var.clase_conexion.get_propiedad(Propiedades._codigo)):
            response["valid"] = False
            response["messages"].append("La propiedad con código " + Propiedades._codigo + " no existe")

        if (not Propiedades._fecha_baja.strip() or not eventos.Eventos.validar_fecha(Propiedades._fecha_baja)):
            response["valid"] = False
            response["messages"].append("Para dar de baja es necesaria una fecha de baja válida")
        else:
            if not eventos.Eventos.comparar_fechas(Propiedades._fecha_alta.strip(), Propiedades._fecha_baja.strip()):
                response["valid"] = False
                response["messages"].append("La fecha de baja no puede ser anterior a la fecha de alta")

        if Propiedades._radio_disponible:
                response["valid"] = False
                response["messages"].append("Para dar de baja el estado no puede ser 'Disponible'")

        if Propiedades._radio_alquilado:
            if not Propiedades._check_alquiler:
                response["valid"] = False
                response["messages"].append("Con el estado 'Alquilado' seleccionado el tipo de operación 'Alquiler' debe de estar seleccionado")
            else:
                if not Propiedades._precio_alquiler.strip() or not eventos.Eventos.validar_numero(Propiedades._precio_alquiler):
                    response["valid"] = False
                    response["messages"].append("Con el tipo de operación 'Alquiler' seleccionado debe introducirse un precio de alquiler válido")

        if Propiedades._radio_vendido:
            if not Propiedades._check_venta:
                response["valid"] = False
                response["messages"].append("Con el estado 'Vendido' seleccionado el tipo de operación 'Venta' debe de estar seleccionado")
            else:
                if not Propiedades._precio_venta.strip() or not eventos.Eventos.validar_numero(Propiedades._precio_venta):
                    response["valid"] = False
                    response["messages"].append("Con el tipo de operación 'Venta' seleccionado debe introducirse un precio de venta válido")

        return response