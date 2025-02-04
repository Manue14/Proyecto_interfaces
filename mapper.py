class Mapper:

    @staticmethod
    def initialize_cliente():
        cliente = {"dni": "",
                   "fecha_alta": "",
                   "apellido": "",
                   "nombre": "",
                   "email": "",
                   "movil": "",
                   "direccion": "",
                   "provincia": "",
                   "municipio": "",
                   "fecha_baja": ""}
        return cliente

    @staticmethod
    def map_cliente(campos):
        cliente = {"dni": campos["dni"].text(), "fecha_alta": campos["fecha_alta"].text(), "apellido": campos["apellido"].text(),
                    "nombre": campos["nombre"].text(), "email": campos["email"].text(), "movil": campos["movil"].text(),
                    "direccion": campos["direccion"].text(), "provincia": campos["provincia"].currentText(),
                    "municipio": campos["municipio"].currentText(), "fecha_baja": campos["fecha_baja"].text()}
        return cliente
    
    @staticmethod
    def bind_cliente_query(query, cliente):
        query.bindValue(":dnicli", cliente["dni"])
        query.bindValue(":altacli", cliente["fecha_alta"])
        query.bindValue(":apelcli", cliente["apellido"])
        query.bindValue(":nomecli", cliente["nombre"])
        query.bindValue(":emailcli", cliente["email"])
        query.bindValue(":movilcli", cliente["movil"])
        query.bindValue(":dircli", cliente["direccion"])
        query.bindValue(":procli", cliente["provincia"])
        query.bindValue(":municli", cliente["municipio"])

        if cliente["fecha_baja"] == "":
            query.bindValue(":bajacli", None)
        else:
            query.bindValue(":bajacli", cliente["fecha_baja"])

    @staticmethod
    def initialize_propiedad():
       propiedad = {"codigo": "",
            "fecha_alta": "",
            "fecha_baja": "",
            "direccion": "",
            "provincia": "",
            "municipio": "",
            "tipo": "",
            "habitaciones": "",
            "banos": "",
            "superficie": "",
            "precio_alquiler": "",
            "precio_venta": "",
            "postal": "",
            "descripcion": "",
            "operaciones": "",
            "estado": "",
            "propietario": "",
            "movil": ""}
       return propiedad

    @staticmethod
    def map_propiedad(campos):
        propiedad = {"codigo": campos["codigo"].text(),
                     "fecha_alta": campos["fecha_alta"].text(),
                     "fecha_baja": campos["fecha_baja"].text(),
                     "direccion": campos["direccion"].text(),
                     "provincia": campos["provincia"].currentText(),
                     "municipio": campos["municipio"].currentText(),
                     "postal": campos["postal"].text(), "tipo": campos["tipo"].currentText(),
                     "habitaciones": campos["habitaciones"].text(),
                     "banos": campos["banos"].text(),
                     "superficie": campos["superficie"].text(),
                     "precio_alquiler": campos["precio_alquiler"].text(),
                     "precio_venta": campos["precio_venta"].text(),
                     "descripcion": campos["descripcion"].toPlainText(),
                     "propietario": campos["propietario"].text(),
                     "movil": campos["movil"].text(),
                     "operaciones": "", "estado": ""}

        if campos["check_alquiler"].isChecked():
            propiedad["operaciones"] = propiedad["operaciones"] + "-" + campos["check_alquiler"].text()
        if campos["check_venta"].isChecked():
            propiedad["operaciones"] = propiedad["operaciones"] + "-" + campos["check_venta"].text()
        if campos["check_intercambio"].isChecked():
            propiedad["operaciones"] = propiedad["operaciones"] + "-" + campos["check_intercambio"].text()

        propiedad["operaciones"] = propiedad["operaciones"][1:]

        if campos["radio_disponible"].isChecked():
            propiedad["estado"] = campos["radio_disponible"].text()
        elif campos["radio_alquilado"].isChecked():
            propiedad["estado"] = campos["radio_alquilado"].text()
        elif campos["radio_vendido"].isChecked():
            propiedad["estado"] = campos["radio_vendido"].text()

        return propiedad

    @staticmethod
    def bind_propiedad_create_query(query, propiedad):
        query.bindValue(":altaprop", str(propiedad["fecha_alta"]))
        query.bindValue(":dirprop", str(propiedad["direccion"]))
        query.bindValue(":provprop", str(propiedad["provincia"]))
        query.bindValue(":muniprop", str(propiedad["municipio"]))
        query.bindValue(":tipoprop", str(propiedad["tipo"]))
        query.bindValue(":habprop", int(propiedad["habitaciones"]))
        query.bindValue(":banprop", int(propiedad["banos"]))
        query.bindValue(":superprop", str(propiedad["superficie"]))

        if (propiedad["precio_alquiler"] == ""):
            query.bindValue(":prealquiprop", None)
        else:
            query.bindValue(":prealquiprop", str(propiedad["precio_alquiler"]))

        if (propiedad["precio_venta"] == ""):
            query.bindValue(":prevenprop", None)
        else:
            query.bindValue(":prevenprop", str(propiedad["precio_venta"]))

        query.bindValue(":cpprop", str(propiedad["postal"]))

        if (propiedad["descripcion"] == ""):
            query.bindValue(":obserprop", None)
        else:
            query.bindValue(":obserprop", str(propiedad["descripcion"]))

        query.bindValue(":tipooper", str(propiedad["operaciones"]))
        query.bindValue(":estadoprop", str(propiedad["estado"]))
        query.bindValue(":nomeprop", str(propiedad["propietario"]))
        query.bindValue(":movilprop", str(propiedad["movil"]))

    @staticmethod
    def bind_propiedad_update_query(query, propiedad):
        Mapper.bind_propiedad_create_query(query, propiedad)
        query.bindValue(":codigo", propiedad["codigo"])
        if propiedad["fecha_baja"] == "":
            query.bindValue(":bajaprop", None)
        else:
            query.bindValue(":bajaprop", str(propiedad["fecha_baja"]))

    @staticmethod
    def map_cliente_servidor_list(fila):
        cliente = {"dni": fila["dnicli"], "fecha_alta": fila["altacli"], "apellido": fila["apelcli"],
                    "nombre": fila["nomecli"], "email": ("" if fila["emailcli"] == None else fila["emailcli"]), "movil": fila["movilcli"],
                    "direccion": fila["dircli"], "provincia": fila["provcli"],
                    "municipio": fila["municli"], "fecha_baja": ("" if fila["bajacli"] == None else fila["bajacli"])}
        return cliente
    
    @staticmethod
    def map_propiedad_servidor_list(fila):
        propiedad = {"codigo": fila["codigo"], "fecha_alta": fila["altaprop"], "fecha_baja": fila["bajaprop"], "direccion": fila["dirprop"],
            "provincia": fila["provprop"], "municipio": fila["muniprop"], "tipo": fila["tipoprop"], "habitaciones": fila["habprop"],
            "banos": fila["banprop"], "superficie": fila["superprop"], "precio_alquiler": fila["prealquiprop"], "precio_venta": fila["prevenprop"],
            "postal": fila["cpprop"], "descripcion": fila["obserprop"], "operaciones": fila["tipooper"], "estado": fila["estadoprop"],
            "propietario": fila["nomeprop"], "movil": fila["movilprop"]}
        return propiedad

    @staticmethod
    def bind_cliente_create_query_servidor(cursor, query, cliente):
        cursor.execute(query, (cliente["dni"], cliente["fecha_alta"], cliente["apellido"], cliente["nombre"], cliente["email"], cliente["movil"],
                               cliente["direccion"], cliente["provincia"], cliente["municipio"]))
        
    @staticmethod
    def bind_cliente_update_query_servidor(cursor, query, cliente):
        cursor.execute(query, (cliente["fecha_alta"], cliente["apellido"], cliente["nombre"], cliente["email"], cliente["movil"],
                                cliente["direccion"], cliente["provincia"], cliente["municipio"],
                                (None if cliente["fecha_baja"] == "" else cliente["fecha_baja"]), cliente["dni"]))
        
    @staticmethod
    def bind_propiedad_create_query_servidor(cursor, query, propiedad):
        cursor.execute(query, (propiedad["fecha_alta"], propiedad["direccion"], propiedad["provincia"], propiedad["municipio"], propiedad["tipo"],
                               propiedad["habitaciones"], propiedad["banos"], propiedad["superficie"],
                               (None if propiedad["precio_alquiler"] == "" else propiedad["precio_alquiler"]),
                               (None if propiedad["precio_venta"] == "" else propiedad["precio_venta"]), propiedad["postal"],
                               (None if propiedad["descripcion"] == "" else propiedad["descripcion"]), propiedad["operaciones"],
                               propiedad["estado"], propiedad["propietario"], propiedad["movil"]))
        
    @staticmethod
    def bind_propiedad_update_query_servidor(cursor, query, propiedad):
        cursor.execute(query, (propiedad["fecha_alta"], propiedad["direccion"], propiedad["provincia"], propiedad["municipio"], propiedad["tipo"],
                               propiedad["habitaciones"], propiedad["banos"], propiedad["superficie"],
                               (None if propiedad["precio_alquiler"] == "" else propiedad["precio_alquiler"]),
                               (None if propiedad["precio_venta"] == "" else propiedad["precio_venta"]), propiedad["postal"],
                               (None if propiedad["descripcion"] == "" else propiedad["descripcion"]), propiedad["operaciones"],
                               propiedad["estado"], propiedad["propietario"], propiedad["movil"],
                               (None if propiedad["fecha_baja"] == "" else propiedad["fecha_baja"]), propiedad["codigo"]))

    @staticmethod
    def initialize_vendedor():
        vendedor = {"codigo": "",
                   "dni": "",
                   "nombre": "",
                   "fecha_alta": "",
                   "fecha_baja": "",
                   "movil": "",
                   "email": "",
                   "provincia": ""}
        return vendedor

    @staticmethod
    def map_vendedor(campos):
        vendedor = {"codigo": campos["codigo"].text(), "dni": campos["dni"].text(), "fecha_alta": campos["fecha_alta"].text(), "fecha_baja": campos["fecha_baja"].text(),
                   "nombre": campos["nombre"].text(), "email": campos["email"].text(), "movil": campos["movil"].text(),
                   "provincia": campos["provincia"].currentText()}
        return vendedor

    @staticmethod
    def bind_vendedor_create_query(query, vendedor):
        query.bindValue(":dniven", str(vendedor["dni"]))
        query.bindValue(":nomven", str(vendedor["nombre"]))
        query.bindValue(":altaven", str(vendedor["fecha_alta"]))
        query.bindValue(":movilven", str(vendedor["movil"]))
        query.bindValue(":mailven", str(vendedor["email"]))
        query.bindValue(":delven", str(vendedor["provincia"]))

    @staticmethod
    def bind_vendedor_update_query(query, vendedor):
        Mapper.bind_vendedor_create_query(query, vendedor)
        query.bindValue(":idven", vendedor["codigo"])
        if vendedor["fecha_baja"] == "":
            query.bindValue(":bajaven", None)
        else:
            query.bindValue(":bajaven", str(vendedor["fecha_baja"]))

    @staticmethod
    def initialize_factura():
        factura = {
            "id": "",
            "fecha_registro": "",
            "dni_cliente": ""
        }
        return factura

    @staticmethod
    def map_factura(campos):
        factura = {"id": campos["numero"].text(), "fecha_registro": campos["fecha_registro"].text(),
                   "dni_cliente": campos["dni_cliente"].text()}
        return factura

    @staticmethod
    def bind_factura_create_query(query, factura):
        query.bindValue(":fechafac", factura["fecha_registro"])
        query.bindValue(":dnicli", factura["dni_cliente"])

    @staticmethod
    def initialize_venta():
        venta = {
            "id": "",
            "id_factura": "",
            "codigo_propiedad": "",
            "codigo_vendedor": "",
            "precio": ""
        }
        return venta

    @staticmethod
    def map_venta(campos):
        venta = {"id_factura": campos["numero"].text(), "codigo_propiedad": campos["codigo_propiedad"].text(),
                 "codigo_vendedor": campos["id_vendedor"].text(), "precio": campos["precio_propiedad"].text()}
        return venta

    @staticmethod
    def bind_venta_create_query(query, venta):
        query.bindValue(":id_factura", int(venta["id_factura"]))
        query.bindValue(":codigo_propiedad", int(venta["codigo_propiedad"]))
        query.bindValue(":codigo_vendedor", int(venta["codigo_vendedor"]))
        query.bindValue(":precio", float(venta["precio"]))