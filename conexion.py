import os
from PyQt6 import QtSql, QtWidgets
from PyQt6.uic.properties import QtGui


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

    def altaCliente(nuevocli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into clientes (dnicli, altacli, apelcli, nomecli, emailcli, movilcli, "
                          "dircli, provcli, municli) VALUES (:dnicli, :altacli, :apelcli, :nomecli, :emailcli, "
                          " :movilcli, :dircli, :provcli, :municli)")
            query.bindValue(":dnicli", nuevocli[0])
            query.bindValue(":altacli", nuevocli[1])
            query.bindValue(":apelcli", nuevocli[2])
            query.bindValue(":nomecli", nuevocli[3])
            query.bindValue(":emailcli", nuevocli[4])
            query.bindValue(":movilcli", nuevocli[5])
            query.bindValue(":dircli", nuevocli[6])
            query.bindValue(":provcli", nuevocli[7])
            query.bindValue(":municli", nuevocli[8])
            if query.exec():
                return True
            else:
                QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo dar de alta el cliente en la base de datos.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
        except Exception as error:
            print("error alta cliente", error)