import var
import conexion
import eventos

class Facturas:
    campos = {}
    botones = {}

    @staticmethod
    def inicializar_campos():
        Facturas.campos = {
            "numero": var.ui.txt_fac_numero,
            "fecha_registro": var.ui.txt_fac_alta,
            "dni_cliente": var.ui.txt_fac_cli_dni,
            "apellidos_cliente": var.ui.txt_fac_cli_apellidos,
            "nombre_cliente": var.ui.txt_fac_cli_nombre,
            "codigo_propiedad": var.ui.txt_fac_pro_codigo,
            "tipo_propiedad": var.ui.txt_fac_pro_tipo,
            "precio_propiedad": var.ui.txt_fac_pro_precio,
            "direccion_propiedad": var.ui.txt_fac_pro_direccion,
            "localidad_propiedad": var.ui.txt_fac_pro_localidad,
            "id_vendedor": var.ui.txt_fac_ven_id
        }

    def inicializar_botones(self):
        Facturas.botones = {
            "btn_grabar": var.ui.btn_fac_grabar,
            "btn_grabar_ven": var.ui.btn_fac_ven_grabar
        }

    @staticmethod
    def populate_cliente_fields(cliente):
        Facturas.inicializar_campos()
        Facturas.campos["dni_cliente"].setText(cliente["dni"])
        Facturas.campos["apellidos_cliente"].setText(cliente["apellido"])
        Facturas.campos["nombre_cliente"].setText(cliente["nombre"])

    @staticmethod
    def populate_propiedad_fields(propiedad):
        Facturas.inicializar_campos()
        Facturas.campos["codigo_propiedad"].setText(propiedad["codigo"])
        Facturas.campos["tipo_propiedad"].setText(propiedad["tipo"])
        Facturas.campos["precio_propiedad"].setText("34")
        Facturas.campos["direccion_propiedad"].setText(propiedad["direccion"])
        Facturas.campos["localidad_propiedad"].setText(propiedad["municipio"])

    @staticmethod
    def populate_vendedor_fields(vendedor):
        Facturas.inicializar_campos()
        Facturas.campos["id_vendedor"].setText(vendedor["codigo"])

    def alta_factura(self):
        try:
            nueva_factura = [var.ui.lbl_fac_codigo.text(), var.ui.txt_fac_fecha.text(), var.ui.txt_fac_dni.text()]
            print(nueva_factura)
            if (conexion.Conexion.alta_factura(nueva_factura)):
                eventos.Eventos.mensaje_exito("Aviso", "Alta factura en la base de datos")
                #var.state_manager.update_tabla_facturas()
            else:
                eventos.Eventos.mensaje_error("Aviso", "La factura ya existe")
        except Exception as error:
            print("factura", error)