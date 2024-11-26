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
        query.bindValue(":bajaprop", str(propiedad["fecha_baja"]))