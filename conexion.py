import os
from PyQt6 import QtSql, QtWidgets
from PyQt6.uic.properties import QtGui
import sqlite3
import var

class Conexion:

    '''

    método de una clase que no depende de una instancia específica de esa clase. 
    Se puede llamarlo directamente a través de la clase, sin necesidad de crear un objeto de esa clase. 
    Es útil en comportamientos o funcionalidades que son más a una clase en general que a una instancia en particular.
    
    '''

    @staticmethod
    def db_conexion(self):
        # Verifica si el archivo de base de datos existe
        if not os.path.isfile('bbdd.sqlite'):
            QtWidgets.QMessageBox.critical(None, 'Error', 'El archivo de la base de datos no existe.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        # Crear la conexión con la base de datos SQLite
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')

        if db.open():
            # Verificar si la base de datos contiene tablas
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table';")

            if not query.next():  # Si no hay tablas
                QtWidgets.QMessageBox.critical(None, 'Error', 'Base de datos vacía o no válida.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
                return False
            else:
                QtWidgets.QMessageBox.information(None, 'Aviso', 'Conexión Base de Datos realizada',
                                               QtWidgets.QMessageBox.StandardButton.Ok)
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

    @staticmethod
    def listar_provincias(self):
        listaprov = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias;")
        if query.exec():
            while query.next():
                listaprov.append([query.value(0), query.value(1)])
        return listaprov

    def listar_municipios(prov_id):
        mun_list = []
        query = QtSql.QSqlQuery()
        query.prepare(f"SELECT * FROM municipios where idprov = {prov_id};")
        if query.exec():
            while query.next():
                mun_list.append([query.value(1), query.value(2)])
        return mun_list

    @staticmethod
    def alta_cliente(cliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into clientes (dnicli, altacli, apelcli, nomecli, emailcli, movilcli, "
                          "dircli, procli, municli, bajacli) VALUES (:dnicli, :altacli, :apelcli, :nomecli, :emailcli, "
                          " :movilcli, :dircli, :procli, :municli, :bajacli)")
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
            if query.exec():
                return True
            else:
                return False
        except sqlite3.IntegrityError:
            return False
        except Exception as error:
            print("error alta cliente", error)
            return False

    def listar_clientes():
        try:
            clientes = []
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
            keys = list(cliente.keys())

            query = QtSql.QSqlQuery()
            if var.historico == 1:
                query.prepare("SELECT * FROM clientes WHERE bajacli is NULL ORDER BY nomecli, apelcli ASC;")
                
            elif var.historico == 0:
                query.prepare("SELECT * FROM clientes ORDER BY nomecli, apelcli ASC;")

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        cliente[keys[i]] = str(query.value(i))
                    clientes.append(cliente.copy())
            return clientes
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("error listado clientes", error)
            return []

    def get_cliente(dni):
        try:
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
            keys = list(cliente.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM clientes WHERE dnicli = :dni;")
            query.bindValue(":dni", dni)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        cliente[keys[i]] = str(query.value(i))
                return cliente
        except Exception as error:
            print("error datos un cliente", error)

    def modificar_cliente(cliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from clientes where dnicli = :dni")
            query.bindValue(":dni", str(cliente["dni"]))

            if query.exec() and query.next() and query.value(0) > 0:
                query.prepare("UPDATE clientes SET altacli = :altacli, apelcli = :apelcli, nomecli = :nomecli, "
                            "emailcli = :emailcli, movilcli = :movilcli, dircli = :dircli, procli = :procli, "
                            "municli = :municli, bajacli = :bajacli WHERE dnicli = :dni")

                query.bindValue(":dni", cliente["dni"])
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
                    print(cliente["fecha_baja"])
                    query.bindValue(":bajacli", cliente["fecha_baja"])

                if query.exec():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print("error modificar cliente", error)

    def baja_cliente(cliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE clientes SET bajacli = :bajacli WHERE dnicli = :dnicli")
            query.bindValue(":bajacli", str(cliente["fecha_baja"]))
            query.bindValue(":dnicli", str(cliente["dni"]))
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error baja cliente", error)

    def alta_propiedad_tipo(tipo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into tipopropiedad (TIPO) VALUES (:tipo) ")
            query.bindValue(":tipo", str(tipo))
            if query.exec():
                query = QtSql.QSqlQuery()
                query.prepare("SELECT tipo FROM tipopropiedad")
                if query.exec():
                    registro = []
                    while query.next():
                        registro.append(query.value(0))
                    return registro
            else:
                return False
        except Exception as error:
            print("error alta tipo propiedad", error)

    def cargar_propiedad_tipos(self):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT tipo FROM tipopropiedad ASC")
        if query.exec():
            registro = []
            while query.next():
                registro.append(query.value(0))
            return registro

    def baja_propiedad_tipo(tipo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE from tipopropiedad WHERE tipo = :tipo")
            query.bindValue(":tipo", str(tipo))
            if query.exec():
                if query.numRowsAffected() > 0:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print("error baja tipo propiedad", error)

    def alta_propiedad(propiedad):
        print(propiedad)
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into propiedades (altaprop, dirprop, provprop, muniprop, tipoprop, habprop, "
                          "banprop, superprop, prealquiprop, prevenprop, cpprop, obserprop, tipooper, estadoprop, "
                          "nomeprop, movilprop) VALUES (:altaprop, :dirprop, :provprop, :muniprop, :tipoprop, :habprop, "
                          ":banprop, :superprop, :prealquiprop, :prevenprop, :cpprop, :obserprop, :tipooper, :estadoprop, "
                          ":nomeprop, :movilprop)")
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

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error al dar de alta la propiedad en la base de datos", error)

    def modificar_propiedad(propiedad):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades SET altaprop = :altaprop, dirprop = :dirprop, provprop = :provprop, "
                          "muniprop = :muniprop, tipoprop = :tipoprop, habprop = :habprop, banprop = :banprop, "
                          "superprop = :superprop, prealquiprop = :prealquiprop, prevenprop = :prevenprop, "
                          "cpprop = :cpprop, obserprop = :obserprop, tipooper = :tipooper, estadoprop = :estadoprop, "
                          "nomeprop = :nomeprop, movilprop = :movilprop WHERE codigo = :codigo")
            query.bindValue(":codigo", propiedad["codigo"])
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

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al modificar la propiedad en la base de datos", error)

    def eliminar_propiedad(propiedad):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades SET bajaprop = :bajaprop WHERE codigo = :codigo")

            query.bindValue(":bajaprop", str(propiedad["fecha_baja"]))
            query.bindValue(":codigo", propiedad["codigo"])

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al dar de baja la propiedad en la base de datos", error)

    def listar_propiedades():
        try:
            propiedades = []
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
            keys = list(propiedad.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades ORDER BY muniprop ASC;")

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        propiedad[keys[i]] = str(query.value(i))
                    propiedades.append(propiedad.copy())
            return propiedades
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("error listado propiedades", error)
            return []

    def get_propiedad(codigo):
        try:
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

            keys = list(propiedad.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades WHERE codigo = :codigo;")
            query.bindValue(":codigo", codigo)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        propiedad[keys[i]] = str(query.value(i))
                return propiedad
        except Exception as error:
            print("error al obtener la propiedad de la base de datos", error)