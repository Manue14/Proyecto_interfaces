import os
from PyQt6 import QtSql, QtWidgets
from PyQt6.uic.properties import QtGui
import sqlite3

import var
import mapper

class Conexion:

    '''

    Método de una clase que no depende de una instancia específica de esa clase.
    Se puede llamarlo directamente a través de la clase, sin necesidad de crear un objeto de esa clase. 
    Es útil en comportamientos o funcionalidades que son más a una clase en general que a una instancia en particular.
    
    '''

    @staticmethod
    def db_conexion():
        """

        :param None: None
        :type None: None
        :return:False or True
        :rtype: bool

        Módulo para establecer conexión con la base de datos.
        Si éxito devuelve true, en caso contrario devuelve false

        """
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
        """

        :param None: None
        :type None: None
        :return: lista provincias
        :rtype: bytearray

        Método que obtiene listado de provincias de la base de datos

        """
        listaprov = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias;")
        if query.exec():
            while query.next():
                listaprov.append([query.value(0), query.value(1)])
        return listaprov

    def listar_municipios(prov_id):
        """

        :param prov_id: id provincia
        :type prov_id: int
        :return: lista de municipios de la provincia con el id pasado por parámetro
        :rtype: list

        Método que obtiene listado de municipios de una provincia de la base de datos

        """
        mun_list = []
        query = QtSql.QSqlQuery()
        query.prepare(f"SELECT * FROM municipios where idprov = {prov_id};")
        if query.exec():
            while query.next():
                mun_list.append([query.value(1), query.value(2)])
        return mun_list

    @staticmethod
    def listar_all_municipios():
        """

        :param none: none
        :type: none
        :return: lista de todas las provincias existentes en la base de datos
        :rtype: list

        Método que obtiene un listado de todas los municipios existentes en la base de datos

        """
        mun_list = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios;")
        if query.exec():
            while query.next():
                mun_list.append(query.value(1))
        return mun_list

    @staticmethod
    def alta_cliente(cliente):
        """

        :param cliente: cliente a dar de alta
        :type cliente: dict
        :return: id del cliente registrado o -1
        :rtype: int

        Método que inserta a la base de datos el cliente
        Si éxito devuelve el id del cliente, en caso contrario devuelve -1

        """
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
        """

        :param None: None
        :type None: None
        :return: listado clientes
        :rtype: list

        Método que devuelve una lista con los clientes de la base de datos

        """
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
        """

        :param dni: DNI del cliente que se quiere obtener de la base de datos
        :type dni: str
        :return: cliente correspondiente al dni pasado por parametro
        :rtype: dict

        Método que a partir de un DNI obtiene el usuario de la base de datos

        """
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
        """

        :param cliente: cliente a modificar
        :type cliente: dict
        :return: True o False
        :rtype: bool

        Método que actualiza un cliente en la base de datos
        Si éxito devuelve True, en caso contrario devuelve False

        """
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
        """

        :param cliente: cliente a dar de baja
        :type cliente: dict
        :return: True o False
        :rtype: bool

        Método que da de baja un cliente en la base de datos (lo oculta añadiéndole una fecha de baja)
        Si éxito devuelve True, en caso contrario devuelve False

        """
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
        """

        :param tipo: tipo de propiedad a dar de alta
        :type tipo: str
        :return: True o False
        :rtype: bool

        Método para registrar un tipo de propiedad en la base de datos
        Si éxito devuelve True, en caso contrario devuelve False

        """
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
        """

        :param None: None
        :type None: None
        :return: listado de tipos de propiedad de la base de datos
        :rtype: list

        Método que devuelve un listado con todos los tipos de propiedades en la base de datos

        """
        query = QtSql.QSqlQuery()
        query.prepare("SELECT tipo FROM tipopropiedad ORDER BY tipo ASC")
        if query.exec():
            tipos = []
            while query.next():
                tipos.append(query.value(0))
            return tipos
        else:
            return []

    def baja_propiedad_tipo(tipo):
        """

        :param None: None
        :type None: None
        :return: True o False
        :rtype: bool

        Método que elimina de la base de datos el tipo de propiedad pasado por parametro
        Si éxito devuelve True, en caso contrario False

        """
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
        """

        :param propiedad: propiedad a registrar en la base de datos
        :type propiedad: dict
        :return: id de la última propiedad registrada o -1
        :rtype: int

        Método que registra en la base de datos la propiedad pasada por parámetro
        Si éxito devuelve id de la última propiedad registrada, en caso contrario -1

        """
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
        """

        :param propiedad: propiedad a modificar en la base de datos
        :type propiedad: dict
        :return: True o False
        :rtype: bool

        Método que actualiza una propiedad en la base de datos
        Si éxito devuelve True, en caso contrario False

        """
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
        """

        :param propiedad: propiedad a dar de baja en la base de datos
        :type propiedad: dict
        :return: True o False
        :rtype: bool

        Método que da de baja una propiedad en la base de datos (la oculta añadiéndole una fecha de baja)
        Si éxito devuelve True, en caso contrario False

        """
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
        """

        :param to_export: bandera para controlar si el listado de propiedades es para realizar una exportación
        :type to_export: bool
        :return: listado de propiedades existentes en la base de datos
        :rtype: list

        Método que devuelve una lista con las propiedades existentes en la base de datos

        """
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
        """

        :param codigo: código de la propiedad a obtener desde la base de datos
        :type codigo: int
        :return: propiedad correspondiente al código pasado por parámetro
        :rtype: dict

        Método que obtiene una propiedad de la base de datos a partir de su código

        """
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
        """

        :param tipo: tipo de propiedad para filtrar
        :type tipo: str
        :param municipio: municipio para filtrar
        :type municipio: str
        :return: listado de propiedades filtradas
        :rtype: list

        Método que devuelve una lista de propiedades filtradas

        """
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
        """

        :param vendedor: vendedor a dar de alta en la base de datos
        :type vendedor: dict
        :return: id del último vendedor registrado o -1
        :rtype: int

        Método que registra un vendedor en la base de datos
        Si éxito devuelve el id del vendedor registrado, en caso contrario -1

        """
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
        """

        :param vendedor: vendedor a actualizar en la base de datos
        :type vendedor: dict
        :return: True o False
        :rtype: bool

        Método que actualiza un vendedor en la base de datos
        Si éxito devuelve True, en caso contrario False

        """
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
        """

        :param vendedor: vendedor a dar de baja en la base de datos
        :type vendedor: dict
        :return: True o False
        :rtype: bool

        Método que da de baja un vendedor en la base de datos (lo oculta añadiéndole una fecha de baja)
        Si éxito devuelve True, en caso contrario devuelve False

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE vendedores SET bajaVendedor = :bajaven WHERE idVendedor = :idven")

            query.bindValue(":bajaven", str(vendedor["fecha_baja"]))
            query.bindValue(":idven", vendedor["codigo"])

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al dar de baja la propiedad en la base de datos", error)
            return False

    def listar_vendedores():
        """

        :param None: None
        :type None: None
        :return: listado de vendedores existentes en la base de datos
        :rtype: list

        Método que devuelve un listado de los vendedores existentes en la base de datos

        """
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
        """

        :param codigo: código del vendedor a obtener desde la base de datos
        :type codigo: int
        :return: vendedor correspondiente al código pasado por parámetro
        :rtype: dict

        Método que devuelve desde la base de datos un vendedor a partir de su código

        """
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
        """

        :param dni: dni del vendedor a obtener desde la base de datos
        :type dni: str
        :return: vendedor correspondiente al dni pasado por parámetro
        :rtype: dict

        Método que devuelve desde la base de datos un vendedor a partir de su dni

        """
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

    def alta_factura(factura):
        """

        :param factura: factura a almacenar en la base de datos
        :type factura: dict
        :return: id de la última factura registrada o -1
        :rtype: int

        Método que registra una factura en la base de datos
        Si éxito devuelve el id de la factura registrada, en caso contrario -1

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO facturas (fechafac, dnicli) VALUES (:fechafac, :dnicli)")
            mapper.Mapper.bind_factura_create_query(query, factura)
            if query.exec():
                return query.lastInsertId()
            else:
                return -1
        except Exception as error:
            print("error alta_factura", error)

    def listar_facturas():
        """

        :param None: None
        :type None: None
        :return: listado de facturas existentes en la base de datos
        :rtype: list

        Método que devuelve un listado de las facturas existentes en la base de datos

        """
        try:
            facturas = []
            factura = mapper.Mapper.initialize_factura()
            keys = list(factura.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas ORDER BY id ASC;")

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        factura[keys[i]] = str(query.value(i))
                    facturas.append(factura.copy())
            return facturas
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("error listado facturas", error)
            return []
        
    def get_factura(factura_id):
        """

        :param id: ID de la factura a obtener desde la base de datos
        :type codigo: int
        :return: factura correspondiente al ID pasado por parámetro
        :rtype: dict

        Método que devuelve desde la base de datos una factura a partir de su ID

        """
        try:
            factura = mapper.Mapper.initialize_factura()
            keys = list(factura.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas WHERE id = :id;")

            query.bindValue(":id", factura_id)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        factura[keys[i]] = str(query.value(i))
                return factura
        except Exception as error:
            print("error datos una factura", error)
            return {}

    @staticmethod
    def eliminar_factura(factura):
        """

        :param factura: factura a borrar en la base de datos
        :type factura: dict
        :return: True o False
        :rtype: bool

        Método que borra una factura de la base de datos
        Devuelve True si la factura de borró con éxito y False en caso contrario

        """
        try:
            ventas = Conexion.listar_ventas_by_factura(factura["id"])
            for venta in ventas:
                if not Conexion.eliminar_venta(venta):
                    raise Exception("No se pudieron elminar todas las ventas asociadas a la factura")

            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM facturas WHERE id = :id;")
            query.bindValue(":id", str(factura["id"]))

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al eliminar factura", error)

    @staticmethod
    def alta_venta(venta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO ventas (facventa, codprop, codagente, precioventa) "
                          "VALUES (:id_factura, :codigo_propiedad, :codigo_vendedor, :precio);")
            mapper.Mapper.bind_venta_create_query(query, venta)
            if query.exec():
                return query.lastInsertId()
            else:
                return -1
        except Exception as error:
            print("Error al dar de alta la venta", error)

    @staticmethod
    def listar_ventas_by_factura(factura_id):
        try:
            ventas = []
            venta = mapper.Mapper.initialize_venta()
            keys = list(venta.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM ventas WHERE facventa = :id;")
            query.bindValue(":id", str(factura_id))

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        venta[keys[i]] = str(query.value(i))
                    ventas.append(venta.copy())
            return ventas
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("Error al listar ventas de factura", error)

    @staticmethod
    def get_venta(venta_id):
        try:
            venta = mapper.Mapper.initialize_venta()
            keys = list(venta.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM ventas WHERE idventa = :venta_id;")

            query.bindValue(":venta_id", venta_id)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        venta[keys[i]] = str(query.value(i))
                return venta
        except Exception as error:
            print("Error al obtener venta desde la base de datos", error)

    @staticmethod
    def eliminar_venta(venta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM ventas WHERE idventa = :id;")
            query.bindValue(":id", str(venta["id"]))

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al eliminar venta", error)
            return False

    @staticmethod
    def alta_alquiler(alquiler):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO alquileres (dni_cli, propiedad_id, agente_id, fecha_firma, fecha_inicio, fecha_fin, precio_alquiler) "
                          "VALUES (:dni_cliente, :id_propiedad, :id_vendedor, :fecha_firma, :fecha_inicio, :fecha_fin, :precio);")
            mapper.Mapper.bind_alquiler_create_query(query, alquiler)
            if query.exec():
                return query.lastInsertId()
            else:
                return -1
        except Exception as error:
            print("Error al dar de alta el alquiler", error)

    @staticmethod
    def get_alquiler(alquiler_id):
        try:
            alquiler = mapper.Mapper.initialize_alquiler()
            keys = list(alquiler.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM alquileres WHERE id = :id;")

            query.bindValue(":id", alquiler_id)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        alquiler[keys[i]] = str(query.value(i))
                return alquiler
        except Exception as error:
            print("Error al obtener venta desde la base de datos", error)

    @staticmethod
    def listar_alquileres():
        try:
            alquileres = []
            alquiler = mapper.Mapper.initialize_alquiler()
            keys = list(alquiler.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM alquileres ORDER BY id ASC;")

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        alquiler[keys[i]] = str(query.value(i))
                    alquileres.append(alquiler.copy())
            return alquileres
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("error listado alquileres", error)
            return []
        
    @staticmethod
    def eliminar_alquiler(alquiler_id):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM alquileres WHERE id = :id;")
            query.bindValue(":id", alquiler_id)

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al eliminar alquiler", error)
            return False

    @staticmethod
    def alta_recibo(recibo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO recibos (alquiler_id, propiedad_id, mensualidad, importe, pagado) "
                          "VALUES (:alquiler_id, :propiedad_id, :mensualidad, :importe, :pagado);")
            mapper.Mapper.bind_recibo_create_query(query, recibo)
            if query.exec():
                return query.lastInsertId()
            else:
                return -1
        except Exception as error:
            print("Error al dar de alta el recibo", error)

    @staticmethod
    def listar_recibos_by_alquiler(alquiler_id):
        try:
            recibos = []
            recibo = mapper.Mapper.initialize_recibo()
            keys = list(recibo.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM recibos WHERE alquiler_id = :id;")
            query.bindValue(":id", str(alquiler_id))

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        recibo[keys[i]] = str(query.value(i))
                    recibos.append(recibo.copy())
            return recibos
        except sqlite3.IntegrityError:
            return []
        except Exception as error:
            print("Error al listar recibos de alquiler", error)

    @staticmethod
    def get_recibo(recibo_id):
        try:
            recibo = mapper.Mapper.initialize_recibo()
            keys = list(recibo.keys())

            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM recibos WHERE id = :recibo_id;")

            query.bindValue(":recibo_id", recibo_id)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        recibo[keys[i]] = str(query.value(i))
                return recibo
        except Exception as error:
            print("Error al obtener recibo desde la base de datos", error)

    @staticmethod
    def update_recibo(recibo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE recibos SET pagado = :pagado WHERE id = :id")

            query.bindValue(":pagado", int(recibo["pagado"]))
            query.bindValue(":id", int(recibo["id"]))

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al actualizar recibo en la base de datos")
            return False
        
    @staticmethod
    def eliminar_recibo(recibo_id):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM recibos WHERE id = :id;")
            query.bindValue(":id", recibo_id)

            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("Error al eliminar recibo", error)
            return False