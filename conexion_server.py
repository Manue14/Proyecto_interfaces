import mysql.connector
from mysql.connector import Error
import os
from PyQt6 import QtSql, QtWidgets

import mapper
import var

'''
IMPORTANTE TO-DOs:
    Comprobar que municipios y provincias funcionan
    Comprobar que funcionan los dict
    Comprobar que la fecha de baja en el ternario de modificar_cliente no da error
    Comprobar que cursor.execute() efectivamente devuelve el número de filas afectadas
'''
class ConexionServer():
    @staticmethod
    def db_conexion():

        try:
            conexion = mysql.connector.connect(
            host='192.168.10.66', # Cambia esto a la IP de tu servidor user='dam', # Usuario creado
            user='dam',
            password='dam2425',
            database='bbdd'
            # Contraseña del usuario database='bbdd' # Nombre de la base de datos
            )
            if conexion.is_connected():
                pass
                #print("Conexión exitosa a la base de datos")
            return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    @staticmethod
    def listar_provincias():
        listaprov = []
        conexion = ConexionServer().db_conexion()

        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM provincias")
                resultados = cursor.fetchall()
                for fila in resultados:
                    listaprov.append([fila[0], fila[1]])  # Asumiendo que el nombre de la provincia está en la segunda columna
                cursor.close()
                conexion.close()
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
        return listaprov

    @staticmethod
    def listar_municipios(prov_id):
        try:
            conexion = ConexionServer().db_conexion()
            listamunicipios = []
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM municipios WHERE idprov = %s",
                (prov_id,)
            )
            resultados = cursor.fetchall()
            for fila in resultados:
                listamunicipios.append([fila[1], fila[0]])  # Asumiendo que el nombre de la provincia está en la segunda columna
            cursor.close()
            conexion.close()
            return listamunicipios
        except Exception as error:
            print("error lista muni", error)

    def listar_clientes():
        try:
            clientes = []

            conexion = ConexionServer().db_conexion()
            cursor = conexion.cursor(dictionary=True)
            if not var.state_manager.state["historico_cli"]:
                cursor.execute("SELECT * FROM clientes WHERE bajacli IS NULL ORDER BY apelcli, nomecli ASC")
            else:
                cursor.execute("SELECT * FROM clientes ORDER BY apelcli, nomecli ASC")
            resultados = cursor.fetchall()

            # Procesar cada fila de los resultados
            for fila in resultados:
                clientes.append(mapper.Mapper.map_cliente_servidor_list(fila))

            # Cerrar el cursor y la conexión si no los necesitas más
            cursor.close()
            conexion.close()
            print(clientes)
            return clientes
        except Exception as e:
            print("error listado en conexion", e)
            return []
    
    @staticmethod
    def alta_cliente(cliente):
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            add_cliente = ("INSERT INTO clientes "
            "(dnicli, altacli, apelcli, nomecli, emailcli, movilcli, dircli, provcli, municli) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            mapper.Mapper.bind_cliente_create_query_servidor(cursor, add_cliente, cliente)
            affected_files = cursor.rowcount
            last_id = cursor.lastrowid
            conexion.commit()
            cursor.close()
            conexion.close()
            if affected_files >= 1:
                return last_id
            else:
                return -1
        except Exception as e:
            print("Error al dar de alta el cliente en el servidor", e)
            return -1
        
    @staticmethod
    def get_cliente(dni):
        try:
            cliente = mapper.Mapper.initialize_cliente()
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor(dictionary=True)
            query = ("SELECT dnicli, altacli, apelcli, nomecli, emailcli, movilcli, dircli, provcli, municli, bajacli "
                     "FROM clientes "
                     "WHERE dnicli = %s")
            cursor.execute(query, (dni,))
            resultados = cursor.fetchall()
            for fila in resultados:
                cliente = mapper.Mapper.map_cliente_servidor_list(fila)
            cursor.close()
            conexion.close()
            return cliente
        except Exception as e:
            print("Error al obtener cliente del servidor", e)
            return {}
        
    @staticmethod
    def modificar_cliente(cliente):
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            update_cliente = ("UPDATE clientes "
                     "SET altacli = %s, apelcli = %s, nomecli = %s, emailcli = %s, movilcli = %s, dircli = %s, provcli = %s, municli = %s, bajacli = %s "
                     "WHERE dnicli = %s")
            mapper.Mapper.bind_cliente_update_query_servidor(cursor, update_cliente, cliente)
            affected_files = cursor.rowcount
            conexion.commit()
            cursor.close()
            conexion.close()
            if affected_files >= 1:
                return True
            else:
                return False
        except Exception as e:
            print("Error al modificar cliente en el servidor", e)
            return False
        
    @staticmethod
    def baja_cliente(cliente):
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            delete_cliente = ("UPDATE clientes "
                              "SET bajacli = %s "
                              "WHERE dnicli = %s")
            cursor.execute(delete_cliente, (cliente["fecha_baja"], cliente["dni"]))
            affected_files = cursor.rowcount
            conexion.commit()
            cursor.close()
            if affected_files >= 1:
                return True
            else:
                return False
        except Exception as e:
            print("Error al dar de baja cliente en el servidor", e)
            return False
        
    @staticmethod
    def alta_propiedad_tipo(tipo):
        try:
            if (ConexionServer.check_if_tipo_propiedad_existe(tipo)):
                return False
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            insert_tipo = ("INSERT INTO tipopropiedad (tipo) "
                           "VALUES (%s)")
            cursor.execute(insert_tipo, (tipo,))
            affected_files = cursor.rowcount
            conexion.commit()
            cursor.close()
            if affected_files >= 1:
                return True
            else:
                return False
        except Exception as e:
            print("Error al dar de alta tipo de propiedad en el servidor", e)
            return False
        
    @staticmethod
    def cargar_propiedad_tipos():
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            query = ("SELECT tipo FROM tipopropiedad ORDER BY tipo ASC")
            cursor.execute(query)
            resultados = cursor.fetchall()
            tipos = []
            for tipo in resultados:
                tipos.append(tipo)
            return tipos
        except Exception as e:
            print("Error al cargar tipos de propiedad desde el servidor", e)
            return []
        
    @staticmethod
    def baja_propiedad_tipo(tipo):
        try:
            if (not ConexionServer.check_if_tipo_propiedad_existe(tipo)):
                return False
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            delete_tipo = ("DELETE FROM tipopropiedad "
                           "WHERE tipo = %s")
            cursor.execute(delete_tipo, (tipo,))
            affected_files = cursor.rowcount
            conexion.commit()
            cursor.close()
            if affected_files >= 1:
                return True
            else:
                return False
        except Exception as e:
            print("Error al dar de baja tipo de propiedad en el servidor", e)
            return False
        
    @staticmethod
    def check_if_tipo_propiedad_existe(tipo):
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            query = ("SELECT * FROM tipopropiedad "
                           "WHERE tipo = %s")
            cursor.execute(query, (tipo,))
            resultado = cursor.fetchall()
            conexion.commit()
            cursor.close()
            if resultado:
                return True
            else:
                return False
        except Exception as e:
            print("Error al comprobar si el tipo de propiedad existe en el servidor", e)
            return False
        
    @staticmethod
    def alta_propiedad(propiedad):
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            add_propiedad = ("INSERT INTO propiedades "
            "(altaprop, dirprop, provprop, muniprop, tipoprop, habprop, banprop, superprop, prealquiprop, prevenprop, "
            "cpprop, obserprop, tipooper, estadoprop, nomeprop, movilprop) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            mapper.Mapper.bind_propiedad_create_query_servidor(cursor, add_propiedad, propiedad)
            affected_files = cursor.rowcount
            last_id = cursor.lastrowid
            conexion.commit()
            cursor.close()
            conexion.close()
            if affected_files >= 1:
                return last_id
            else:
                return -1
        except Exception as e:
            print("Error dar de alta propiedad en el servidor", e)
            return -1
        
    @staticmethod
    def modificar_propiedad(propiedad):
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            update_propiedad = ("UPDATE propiedades "
                                "SET altaprop = %s, dirprop = %s, provprop = %s, muniprop = %s, tipoprop = %s, habprop = %s, banprop = %s, superprop = %s, "
                                "prealquiprop = %s, prevenprop = %s, cpprop = %s, obserprop = %s, tipooper = %s, estadoprop = %s, "
                                "nomeprop = %s, movilprop = %s, bajaprop = %s "
                                "WHERE codigo = %s")
            mapper.Mapper.bind_propiedad_update_query_servidor(cursor, update_propiedad, propiedad)
            affected_files = cursor.rowcount
            conexion.commit()
            cursor.close()
            conexion.close()
            if affected_files >= 1:
                return True
            else:
                return False
        except Exception as e:
            print("Error al modificar propiedad en el servidor", e)
            return False
        
    @staticmethod
    def eliminar_propiedad(propiedad):
        try:
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor()
            delete_propiedad = ("UPDATE propiedades "
                                "SET bajaprop = %s, estadoprop = %s "
                                "WHERE codigo = %s")
            cursor.execute(delete_propiedad, (propiedad["fecha_baja"], propiedad["estado"], propiedad["codigo"]))
            affected_files = cursor.rowcount
            conexion.commit()
            cursor.close()
            conexion.close()
            if affected_files >= 1:
                return True
            else:
                return False
        except Exception as e:
            print("Error al dar de baja propiedad en el servidor", e)
            return False
        
    @staticmethod
    def listar_propiedades(to_export = False):
        try:
            propiedades = []
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor(dictionary=True)
            if not var.state_manager.state["historico_pro"] and not to_export:
                query = ("SELECT * FROM propiedades WHERE bajaprop IS NULL ORDER BY muniprop ASC")
            else:
                query = ("SELECT * FROM propiedades ORDER BY muniprop ASC")
            cursor.execute(query)
            resultados = cursor.fetchall()
            for fila in resultados:
                propiedades.append(mapper.Mapper.map_propiedad_servidor_list(fila))
            cursor.close()
            conexion.close()
            return propiedades
        except Exception as e:
            print("Error al listar propiedades desde el servidor", e)
            return []
        
    @staticmethod
    def get_propiedad(codigo):
        try:
            propiedad = mapper.Mapper.initialize_propiedad()
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor(dictionary=True)
            query = ("SELECT * FROM propiedades "
                     "WHERE codigo = %s")
            cursor.execute(query, (codigo,))
            resultados = cursor.fetchall()
            for fila in resultados:
                propiedad = mapper.Mapper.map_propiedad_servidor_list(fila)
            cursor.close()
            conexion.close()
            return propiedad
        except Exception as e:
            print("Error al obtener propiedad desde el servidor", e)
            return {}
        
    @staticmethod
    def filtrar_propiedades(tipo, municipio):
        try:
            propiedades = []
            conexion = ConexionServer.db_conexion()
            cursor = conexion.cursor(dictionary=True)
            query = ("SELECT * FROM propiedades "
                     "WHERE tipoprop = %s AND muniprop = %s " 
                     "ORDER BY muniprop ASC")
            cursor.execute(query, (tipo, municipio))
            resultados = cursor.fetchall()
            for fila in resultados:
                propiedades.append(mapper.Mapper.map_propiedad_servidor_list(fila))
            cursor.close()
            conexion.close()
            return propiedades
        except Exception as e:
            print("Error al filtrar propiedades desde el servidor", e)
            return []