import os
from PyQt6 import QtSql, QtWidgets
from PyQt6.uic.properties import QtGui
import sqlite3

import var
import mapper

class Conexion:

    '''

    método de una clase que no depende de una instancia específica de esa clase. 
    Se puede llamarlo directamente a través de la clase, sin necesidad de crear un objeto de esa clase. 
    Es útil en comportamientos o funcionalidades que son más a una clase en general que a una instancia en particular.
    
    '''

    @staticmethod
    def db_conexion():
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
    def listar_provincias():
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
            mapper.Mapper.bind_cliente_query(query, cliente)
            if query.exec():
                return query.lastInsertId()
            else:
                return -1
        except sqlite3.IntegrityError:
            return -1
        except Exception as error:
            print("error alta cliente", error)
            return -1

    def listar_clientes():
        try:
            clientes = []
            cliente = mapper.Mapper.initialize_cliente()
            keys = list(cliente.keys())

            query = QtSql.QSqlQuery()
            if not var.state_manager.state["historico_cli"]:
                query.prepare("SELECT * FROM clientes WHERE bajacli IS NULL ORDER BY nomecli, apelcli ASC;")
            else:
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
            cliente = mapper.Mapper.initialize_cliente()
            keys = list(cliente.keys())

            query = QtSql.QSqlQuery()
            if not var.state_manager.state["historico_cli"]:
                query.prepare("SELECT * FROM clientes WHERE dnicli = :dni AND bajacli IS NULL;")
            else:
                query.prepare("SELECT * FROM clientes WHERE dnicli = :dni;")

            query.bindValue(":dni", dni)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        cliente[keys[i]] = str(query.value(i))
                return cliente
        except Exception as error:
            print("error datos un cliente", error)
            return {}

    def modificar_cliente(cliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from clientes where dnicli = :dni")
            query.bindValue(":dni", str(cliente["dni"]))

            if query.exec() and query.next() and query.value(0) > 0:
                query.prepare("UPDATE clientes SET altacli = :altacli, apelcli = :apelcli, nomecli = :nomecli, "
                            "emailcli = :emailcli, movilcli = :movilcli, dircli = :dircli, procli = :procli, "
                            "municli = :municli, bajacli = :bajacli WHERE dnicli = :dnicli")

                mapper.Mapper.bind_cliente_query(query, cliente)

                if query.exec():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print("error modificar cliente", error)
            return False

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
            return False

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
                    return True
            else:
                return False
        except Exception as error:
            print("error alta tipo propiedad", error)
            return False

    def cargar_propiedad_tipos():
        query = QtSql.QSqlQuery()
        query.prepare("SELECT tipo FROM tipopropiedad ORDER BY tipo ASC")
        if query.exec():
            registro = []
            while query.next():
                registro.append(query.value(0))
            return registro
        else:
            return []

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
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into propiedades (altaprop, dirprop, provprop, muniprop, tipoprop, habprop, "
                          "banprop, superprop, prealquiprop, prevenprop, cpprop, obserprop, tipooper, estadoprop, "
                          "nomeprop, movilprop) VALUES (:altaprop, :dirprop, :provprop, :muniprop, :tipoprop, :habprop, "
                          ":banprop, :superprop, :prealquiprop, :prevenprop, :cpprop, :obserprop, :tipooper, :estadoprop, "
                          ":nomeprop, :movilprop)")
            mapper.Mapper.bind_propiedad_create_query(query, propiedad)

            if query.exec():
                return query.lastInsertId()
            else:
                return -1
        except Exception as error:
            print("error al dar de alta la propiedad en la base de datos", error)
            return -1

    def modificar_propiedad(propiedad):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades SET altaprop = :altaprop, dirprop = :dirprop, provprop = :provprop, "
                          "muniprop = :muniprop, tipoprop = :tipoprop, habprop = :habprop, banprop = :banprop, "
                          "superprop = :superprop, prealquiprop = :prealquiprop, prevenprop = :prevenprop, "
                          "cpprop = :cpprop, obserprop = :obserprop, tipooper = :tipooper, estadoprop = :estadoprop, "
                          "nomeprop = :nomeprop, movilprop = :movilprop, bajaprop = :bajaprop WHERE codigo = :codigo")

            mapper.Mapper.bind_propiedad_update_query(query, propiedad)

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al modificar la propiedad en la base de datos", error)
            return False

    def eliminar_propiedad(propiedad):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades SET bajaprop = :bajaprop, estadoprop = :estadoprop WHERE codigo = :codigo")

            query.bindValue(":bajaprop", str(propiedad["fecha_baja"]))
            query.bindValue(":estadoprop", str(propiedad["estado"]))
            query.bindValue(":codigo", propiedad["codigo"])

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al dar de baja la propiedad en la base de datos", error)
            return False

    def listar_propiedades(to_export = False):
        try:
            propiedades = []
            propiedad = mapper.Mapper.initialize_propiedad()
            keys = list(propiedad.keys())

            query = QtSql.QSqlQuery()
            if not var.state_manager.state["historico_pro"] and not to_export:
                query.prepare("SELECT * FROM propiedades WHERE bajaprop IS NULL ORDER BY muniprop ASC;")
            else:
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
            propiedad = mapper.Mapper.initialize_propiedad()

            keys = list(propiedad.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades WHERE codigo = :codigo;")
            query.bindValue(":codigo", codigo)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        propiedad[keys[i]] = str(query.value(i))
                return propiedad
            else:
                return {}
        except Exception as error:
            print("error al obtener la propiedad de la base de datos", error)
            return {}

    def filtrar_propiedades(tipo, municipio):
        try:
            propiedades = []
            propiedad = mapper.Mapper.initialize_propiedad()
            keys = list(propiedad.keys())

            query = QtSql.QSqlQuery()
            if not var.state_manager.state["historico_pro"]:
                query.prepare("SELECT * FROM propiedades WHERE tipoprop = :tipoprop AND muniprop = :muniprop AND bajaprop IS NULL ORDER BY muniprop ASC;")
            else:
                query.prepare("SELECT * FROM propiedades WHERE tipoprop = :tipoprop AND muniprop = :muniprop ORDER BY muniprop ASC;")

            query.bindValue(":tipoprop", tipo)
            query.bindValue(":muniprop", municipio)

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        propiedad[keys[i]] = str(query.value(i))
                    propiedades.append(propiedad.copy())
            return propiedades
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("Error al filtrar propiedades en la base de datos", error)
            return []


    def alta_vendedor(vendedor):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into vendedores (dniVendedor, nombreVendedor, altaVendedor, "
                          "movilVendedor, mailVendedor, delegacionVendedor) VALUES (:dniven, :nomven, :altaven, "
                          ":movilven, :mailven, :delven)")
            mapper.Mapper.bind_vendedor_create_query(query, vendedor)

            if query.exec():
                return query.lastInsertId()
            else:
                return -1
        except Exception as error:
            print("error al dar de alta al vendedor en la base de datos", error)
            return -1

    def modificar_vendedor(vendedor):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE vendedores SET dniVendedor = :dniven, nombreVendedor = :nomven, altaVendedor = :altaven, bajaVendedor = :bajaven, "
                          "movilVendedor = :movilven, mailVendedor = :mailven, delegacionVendedor = :delven WHERE idVendedor = :idven")

            mapper.Mapper.bind_vendedor_update_query(query, vendedor)

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al modificar el vendedor en la base de datos", error)
            return False

    def baja_vendedor(vendedor):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE vendedores SET bajaVendedor = :bajaven WHERE idVendedor = :idven")

            query.bindValue(":bajaprop", str(vendedor["fecha_baja"]))
            query.bindValue(":idven", vendedor["codigo"])

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al dar de baja la propiedad en la base de datos", error)
            return False

    def listar_vendedores():
        try:
            vendedores = []
            vendedor = mapper.Mapper.initialize_vendedor()
            keys = list(vendedor.keys())

            query = QtSql.QSqlQuery()
            if not var.state_manager.state["historico_ven"]:
                query.prepare("SELECT * FROM vendedores WHERE bajaVendedor IS NULL ORDER BY idVendedor ASC;")
            else:
                query.prepare("SELECT * FROM vendedores ORDER BY idVendedor ASC;")

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        vendedor[keys[i]] = str(query.value(i))
                    vendedores.append(vendedor.copy())
            return vendedores
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("error listado clientes", error)
            return []

    def get_vendedor(codigo):
        try:
            vendedor = mapper.Mapper.initialize_vendedor()
            keys = list(vendedor.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM vendedores WHERE idVendedor = :codigo;")

            query.bindValue(":codigo", codigo)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        vendedor[keys[i]] = str(query.value(i))
                return vendedor
        except Exception as error:
            print("error datos un vendedor", error)
            return {}

    def get_vendedor_dni(dni):
        try:
            vendedor = mapper.Mapper.initialize_vendedor()
            keys = list(vendedor.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM vendedores WHERE dniVendedor = :dni;")

            query.bindValue(":dni", dni)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        vendedor[keys[i]] = str(query.value(i))
                return vendedor
        except Exception as error:
            print("error datos un vendedor", error)
            return {}