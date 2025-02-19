import var

class Alquiler:
    campos = {}
    botones = {}
    _numero, _fecha_registro, _dni_cliente = "", "", ""
    _id_contrato, _id_propiedad, _fecha_inicio, _fecha_fin = "", "", "", ""

    @staticmethod
    def inicializar_campos():
        Alquiler.campos = {
            "numero": var.ui.txt_alq_numero,
            "fecha_registro": var.ui.txt_alq_alta,
            "dni_cliente": var.ui.txt_alq_cli_dni,
            "id_contrato": var.ui.txt_alq_contrato_id,
            "id_propiedad": var.ui.txt_alq_propiedad_id,
            "fecha_inicio": var.ui.txt_alq_inicio,
            "fecha_fin": var.ui.txt_alq_fin
        }

    @staticmethod
    def inicializar_valores():
        Alquiler._numero = Alquiler.campos["numero"].text()
        Alquiler._fecha_registro = Alquiler.campos["fecha_registro"].text()
        Alquiler._dni_cliente = Alquiler.campos["dni_cliente"].text()
        Alquiler._id_contrato = Alquiler.campos["id_contrato"].text()
        Alquiler._id_propiedad = Alquiler.campos["id_propiedad"].text()
        Alquiler._fecha_inicio = Alquiler.campos["mensualidad_fecha_inicio"].text()
        Alquiler._fecha_fin = Alquiler.campos["mensualidad_fecha_fin"].text()

    @staticmethod
    def inicializar_botones():
        Alquiler.botones = {
            "btn_grabar": var.ui.btn_alq_grabar,
            "btn_cargar_mensualidades": var.ui.btn_alq_cargar_mensualidades
        }