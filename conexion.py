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
    def list_prov(self):
        listaprov = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias;")
        if query.exec():
            while query.next():
                listaprov.append([query.value(0), query.value(1)])
        return listaprov

    def list_mun_by_prov(prov_id):
        mun_list = []
        query = QtSql.QSqlQuery()
        query.prepare(f"SELECT * FROM municipios where idprov = {prov_id};")
        if query.exec():
            while query.next():
                mun_list.append([query.value(1), query.value(2)])
        return mun_list

    @staticmethod
    def altaCliente(nuevocli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into clientes (dnicli, altacli, apelcli, nomecli, emailcli, movilcli, "
                          "dircli, procli, municli) VALUES (:dnicli, :altacli, :apelcli, :nomecli, :emailcli, "
                          " :movilcli, :dircli, :procli, :municli)")
            query.bindValue(":dnicli", nuevocli[0])
            query.bindValue(":altacli", nuevocli[1])
            query.bindValue(":apelcli", nuevocli[2])
            query.bindValue(":nomecli", nuevocli[3])
            query.bindValue(":emailcli", nuevocli[4])
            query.bindValue(":movilcli", nuevocli[5])
            query.bindValue(":dircli", nuevocli[6])
            query.bindValue(":procli", nuevocli[7])
            query.bindValue(":municli", nuevocli[8])
            if query.exec():
                return True
            else:
                return False
        except sqlite3.IntegrityError:
            return False
        except Exception as error:
            print("error alta cliente", error)
            return False

    def listadoClientes(self):
        try:
            list_cli = []
            if var.historico == 1:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM clientes WHERE bajacli is NULL ORDER BY nomecli, apelcli ASC;")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        list_cli.append(fila)
            elif var.historico == 0:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM clientes ORDER BY nomecli, apelcli ASC;")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        list_cli.append(fila)
            return list_cli
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("error listado clientes", error)
            return []

    def datosOneCliente(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM clientes WHERE dnicli = :dni;")
            query.bindValue(":dni", dni)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
                return registro
        except Exception as error:
            print("error datos un cliente", error)

    def modifCliente(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from clientes where dnicli = :dni")
            query.bindValue(":dni", str(registro[0]))
            
            if query.exec() and query.next() and query.value(0) > 0:
                query.prepare("UPDATE clientes SET altacli = :altacli, apelcli = :apelcli, nomecli = :nomecli, "
                            "emailcli = :emailcli, movilcli = :movilcli, dircli = :dircli, procli = :provcli, "
                            "municli = :municli, bajacli = :bajacli WHERE dnicli = :dni")

                query.bindValue(":dni", str(registro[0]))
                query.bindValue(":altacli", str(registro[1]))
                query.bindValue(":apelcli", str(registro[2]))
                query.bindValue(":nomecli", str(registro[3]))
                query.bindValue(":emailcli", str(registro[4]))
                query.bindValue(":movilcli", str(registro[5]))
                query.bindValue(":dircli", str(registro[6]))
                query.bindValue(":provcli", str(registro[7]))
                query.bindValue(":municli", str(registro[8]))
                
                if registro[9] == "":
                    query.bindValue(":bajacli", None)
                else:
                    query.bindValue(":bajacli", str(registro[9]))

                if query.exec():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print("error modificar cliente", error)

    def bajaCliente(datos):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE clientes SET bajacli = :bajacli WHERE dnicli = :dnicli")
            query.bindValue(":bajacli", str(datos[0]))
            query.bindValue(":dnicli", str(datos[1]))
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error baja cliente", error)

    def altaTipoprop(tipo):
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

    def cargarTipoprop(self):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT tipo FROM tipopropiedad ASC")
        if query.exec():
            registro = []
            while query.next():
                registro.append(query.value(0))
            return registro

    def bajaTipoprop(tipo):
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