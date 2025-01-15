import var
import conexion
import eventos

class Facturas:

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