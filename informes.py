from PyQt6 import QtSql
from reportlab.pdfgen import canvas
from datetime import datetime
from PIL import Image
import os, shutil, sys, subprocess

import conexion
import var

class Informes:
    separator = os.sep
    registros_por_pagina = 22

    @staticmethod
    def reportClientes():
        """

        :param None: None
        :type None: None
        :return: None
        :rtype: None

        Método que genera un informe .pdf con datos de los clientes presentes en la base de datos en la carpeta /informes de la aplicación

        """
        try:
            rootPath = '.' + Informes.separator + 'informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfcli = fecha + "_listadoclientes.pdf"
            pdf_path = os.path.join(rootPath, nomepdfcli)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Clientes"
            
            query = QtSql.QSqlQuery()
            query.prepare("SELECT dnicli, apelcli, nomecli, movilcli, procli, municli FROM "
                          "clientes ORDER BY apelcli")
            numberOfRows = 0
            query.exec()
            if(query.last()):
                numberOfRows =  query.at() + 1
                query.first()
                query.previous()
            total_pages = round(numberOfRows/Informes.registros_por_pagina) + 1

            Informes.clientes_decoration(titulo, total_pages)
            
            query = QtSql.QSqlQuery()
            query.prepare("SELECT dnicli, apelcli, nomecli, movilcli, procli, municli FROM "
                          "clientes ORDER BY apelcli")
            if query.exec():
                x = 55
                y = 625

                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=8)
                        var.report.drawString(450, 80, 'Página siguiente...')
                        var.report.showPage() #crea una página nueva
                        
                        Informes.clientes_decoration(titulo, total_pages)

                        x = 55
                        y = 625

                    var.report.setFont('Helvetica', size=7)
                    dni = '***' + str(query.value(0)[4:7] + '***')
                    var.report.drawCentredString(x + 10, y, str(dni))
                    var.report.drawString(x + 40, y, str(query.value(1)))
                    var.report.drawString(x + 120, y, str(query.value(2)))
                    var.report.drawString(x + 190, y, str(query.value(3)))
                    var.report.drawString(x + 260, y, str(query.value(4)))
                    var.report.drawString(x + 340, y, str(query.value(5)))

                    y -= 25
            totalPageCount = var.report.getPageNumber()
            print(totalPageCount)
            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdfcli):
                    if sys.platform == "win32":
                        os.startfile(pdf_path)
                    elif sys.platform == "linux":
                        subprocess.call([pdf_path])

        except Exception as error:
            print(error)

    @staticmethod
    def reportPropiedades(municipio):
        """

        :param municipio: Nombre del municipio del que queremos obtener datos sobre las propiedades que en él se encuentren
        :type municipio: str
        :return: None
        :rtype: None

        Método que genera un informe .pdf con datos de las propiedades del municipio pasado por parámetro presentes en la base de datos en la carpeta /informes de la aplicación

        """
        try:
            rootPath = '.' + Informes.separator + 'informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfprop = fecha + "_listadopropiedades" + municipio + ".pdf"
            pdf_path = os.path.join(rootPath, nomepdfprop)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Propiedades en " + municipio
            propiedades = conexion.Conexion.filtrar_propiedades_by_municipio(municipio)
            total_pages = round(len(propiedades)/Informes.registros_por_pagina) + 1

            Informes.propiedades_decoration(titulo, total_pages)

            x = 55
            y = 625
            for propiedad in propiedades:
                if y <= 90:
                    var.report.setFont('Helvetica-Oblique', size=8)
                    var.report.drawString(450, 80, 'Página siguiente...')
                    var.report.showPage()
                    
                    Informes.propiedades_decoration(titulo, total_pages)

                    x = 55
                    y = 625

                var.report.setFont('Helvetica', size=9)
                var.report.drawCentredString(x + 13, y, propiedad["codigo"])
                var.report.drawString(x + 52, y, propiedad["direccion"])
                var.report.drawString(x + 125, y, propiedad["tipo"])
                var.report.drawString(x + 190, y, propiedad["operaciones"])
                if propiedad["precio_alquiler"]:
                    var.report.drawString(x + 305, y, propiedad["precio_alquiler"] + "€")
                if propiedad["precio_venta"]:
                    var.report.drawString(x + 410, y, propiedad["precio_venta"] + "€")
                y -= 25

            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdfprop):
                    if sys.platform == "win32":
                        os.startfile(pdf_path)
                    elif sys.platform == "linux":
                        subprocess.call([pdf_path])

        except Exception as error:
            print(error)

    @staticmethod
    def reportFactura(factura_id, subtotal, impuestos, total):
        """

        :param factura_id: id de la factura que queremos ver
        :type factura_id: int
        :param subtotal: importe de la factura sin impuestos
        :type subtotal: float
        :param impuestos: % de impuestos a pagar a mayores
        :type impuestos: float
        :param total: importe de la factura con impuestos
        :type total: float
        :return: None
        :rtype: None

        Método que genera un informe .pdf con datos de una factura presente en la base de datos en la carpeta /informes de la aplicación

        """
        try:
            rootPath = '.' + Informes.separator + 'informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)

            factura = conexion.Conexion.get_factura(factura_id)
            ventas = conexion.Conexion.listar_ventas_by_factura(factura_id)
            total_pages = round(len(ventas)/Informes.registros_por_pagina) + 1

            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            titulo = "Factura " + factura_id + " del cliente: " + factura["dni_cliente"]
            fecha = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
            nomepdffac = fecha+"_factura"+factura_id+".pdf"
            pdf_path = os.path.join(rootPath, nomepdffac)
            var.report = canvas.Canvas(pdf_path)

            Informes.facturas_decoration(titulo, total_pages)

            x = 55
            y = 625
            for venta in ventas:
                if y <= 90:
                    var.report.setFont('Helvetica-Oblique', size=8)
                    var.report.drawString(450, 80, 'Página siguiente...')
                    var.report.showPage()
                    
                    Informes.facturas_decoration(titulo, total_pages)

                    x = 55
                    y = 625   

                propiedad = conexion.Conexion.get_propiedad(venta["codigo_propiedad"])
                var.report.setFont('Helvetica', size=9)
                var.report.drawCentredString(x + 13, y, venta["id"])
                var.report.drawString(x + 65, y, venta["codigo_propiedad"])
                var.report.drawString(x + 125, y, propiedad["direccion"])
                var.report.drawString(x + 255, y, propiedad["municipio"])
                var.report.drawString(x + 355, y, propiedad["tipo"])
                var.report.drawString(x + 420, y, venta["precio"] + "€")
                y -= 25

            var.report.setFont('Helvetica', size=12)

            if y <= 90:
                y = 625
            var.report.drawString(400, y, "Subtotal: " + subtotal)
            y = y - 25

            if y <= 90:
                y = 625
            var.report.drawString(400, y, "Impuestos: " + impuestos)
            y = y - 25

            if y <= 90:
                y = 625
            var.report.drawString(400, y, "Total: " + total)

            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdffac):
                    if sys.platform == "win32":
                        os.startfile(pdf_path)
                    elif sys.platform == "linux":
                        subprocess.call([pdf_path])

        except Exception as error:
            print(error)

    @staticmethod
    def report_mensualidad(id_mensualidad):
        """

        :param mensalidad_id: id de la mensualidad que queremos ver
        :type mensualidad_id: int
        :return: None
        :rtype: None

        Método que genera un informe .pdf con datos de una mensualidad presente en la base de datos en la carpeta /informes de la aplicación

        """
        try:
            rootPath = '.' + Informes.separator + 'informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfmen = fecha + "_mensualidad" + id_mensualidad + ".pdf"
            pdf_path = os.path.join(rootPath, nomepdfmen)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Mensualidad"
            mensualidad = conexion.Conexion.get_recibo(id_mensualidad)
            alquiler = conexion.Conexion.get_alquiler(mensualidad["alquiler_id"])
            cliente = conexion.Conexion.get_cliente(alquiler["dni_cliente"])
            propiedad = conexion.Conexion.get_propiedad(mensualidad["propiedad_id"])
            total_pages = 1

            Informes.mensualidad_decoration(titulo, total_pages, cliente)

            var.report.setFont('Helvetica-Bold', size = 10)
            var.report.drawString(70, 620, 'Propiedad:')
            var.report.drawString(180, 620, '2')

            var.report.setFont('Helvetica', size = 10)
            var.report.drawString(70, 600, 'Calle:')
            var.report.drawString(180, 600, propiedad["direccion"])
            var.report.drawString(70, 580, 'Localidad:')
            var.report.drawString(180, 580, propiedad["municipio"])
            var.report.drawString(70, 560, 'Provincia:')
            var.report.drawString(180, 560, propiedad["provincia"])


            var.report.setFont('Helvetica-Bold', size = 10)
            var.report.drawString(70, 460, 'Contrato:')
            var.report.drawString(180, 460, mensualidad["alquiler_id"])

            var.report.setFont('Helvetica', size = 10)
            var.report.drawString(70, 440, 'Fecha Mensualidad:')
            var.report.drawString(180, 440, mensualidad["mensualidad"])
            var.report.drawString(70, 420, 'Recibo número:')
            var.report.drawString(180, 420, mensualidad["id"])
            var.report.drawString(70, 400, 'Precio Alquiler:')
            var.report.drawString(180, 400, str(mensualidad["importe"]) + "€")
            var.report.drawString(70, 380, 'Estado:')
            if (mensualidad["pagado"] == '0'):
                var.report.drawString(180, 380, 'No pagado')
            else:
                var.report.setFont('Helvetica-Bold', size = 10)
                var.report.drawString(180, 380, 'Pagado')

            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdfmen):
                    if sys.platform == "win32":
                        os.startfile(pdf_path)
                    elif sys.platform == "linux":
                        subprocess.call([pdf_path])

        except Exception as error:
            print(error)

    @staticmethod
    def clientes_decoration(titulo, total_pages):
        """

        :param titulo: titulo de la cabecera del pdf
        :type titulo: str
        :param total_pages: número total de páginas del pdf
        :type subtotal: int
        :return: None
        :rtype: None

        Método que genera la cabecera y el footer del informe .pdf de clientes

        """
        Informes.topInforme(titulo)
        Informes.footInforme(titulo, total_pages)
        items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
        size = 10
        initial_x = 55

        var.report.setFont('Helvetica-Bold', size=size)
        var.report.drawString(initial_x, 650, str(items[0]))
        var.report.drawString(initial_x + size * 4, 650, str(items[1]))
        var.report.drawString(initial_x + size * 12, 650, str(items[2]))
        var.report.drawString(initial_x + size * 19, 650, str(items[3]))
        var.report.drawString(initial_x + size * 25, 650, str(items[4]))
        var.report.drawString(initial_x + size * 34, 650, str(items[5]))
        var.report.line(50, 645, 525, 645)

    @staticmethod
    def propiedades_decoration(titulo, total_pages):
        """

        :param titulo: titulo de la cabecera del pdf
        :type titulo: str
        :param total_pages: número total de páginas del pdf
        :type subtotal: int
        :return: None
        :rtype: None

        Método que genera la cabecera y el footer del informe .pdf de propiedades

        """
        Informes.topInforme(titulo)
        Informes.footInforme(titulo, total_pages)
        items = ['CÓDIGO', 'DIRECCIÓN', 'TIPO', 'OPERACIÓN', 'PRECIO ALQUILER', 'PRECIO COMPRA']
        size = 10
        initial_x = 55
        var.report.setFont('Helvetica-Bold', size=size)
        var.report.drawString(initial_x, 650, str(items[0]))
        var.report.drawString(initial_x + size * 5, 650, str(items[1]))
        var.report.drawString(initial_x + size * 13, 650, str(items[2]))
        var.report.drawString(initial_x + size * 20, 650, str(items[3]))
        var.report.drawString(initial_x + size * 28, 650, str(items[4]))
        var.report.drawString(initial_x + size * 38, 650, str(items[5]))
        var.report.line(50, 645, 525, 645)

    @staticmethod
    def facturas_decoration(titulo, total_pages):
        """

        :param titulo: titulo de la cabecera del pdf
        :type titulo: str
        :param total_pages: número total de páginas del pdf
        :type subtotal: int
        :return: None
        :rtype: None

        Método que genera la cabecera y el footer del informe .pdf de facturas

        """
        Informes.topInforme(titulo)
        Informes.footInforme(titulo, total_pages)

        items = ['VENTA', 'PROPIEDAD', 'DIRECCIÓN', 'MUNICIPIO', 'TIPO', 'PRECIO']
        size = 10
        initial_x = 55
        var.report.setFont('Helvetica-Bold', size=size)
        var.report.drawString(initial_x, 650, str(items[0]))
        var.report.drawString(initial_x + size * 5, 650, str(items[1]))
        var.report.drawString(initial_x + size * 14, 650, str(items[2]))
        var.report.drawString(initial_x + size * 24, 650, str(items[3]))
        var.report.drawString(initial_x + size * 35, 650, str(items[4]))
        var.report.drawString(initial_x + size * 42, 650, str(items[5]))
        var.report.line(50, 645, 525, 645)

    @staticmethod
    def mensualidad_decoration(titulo, total_pages, cliente):
        """

        :param titulo: titulo de la cabecera del pdf
        :type titulo: str
        :param total_pages: número total de páginas del pdf
        :type subtotal: int
        :param cliente: cliente relacionado al alquiler de la mensualidad que estamos viendo
        :type cliente: dict
        :return: None
        :rtype: None

        Método que genera la cabecera y el footer del informe .pdf de clientes

        """
        Informes.topInforme(titulo)
        Informes.footInforme(titulo, total_pages)

        var.report.setFont('Helvetica-Bold', size=10)
        var.report.drawString(280, 775, 'DNI CLiente:')
        var.report.drawString(280, 755, 'Nombre:')
        var.report.drawString(280, 735, 'Dirección:')
        var.report.drawString(280, 715, 'Localidad:')

        var.report.setFont('Helvetica', size=10)
        var.report.drawString(350, 775, cliente["dni"])
        var.report.drawString(350, 755, cliente["nombre"] + " " + cliente["apellido"])
        var.report.drawString(350, 735, cliente["direccion"])
        var.report.drawString(350, 715, cliente["provincia"] + "-" + cliente["municipio"])

    @staticmethod
    def topInforme(titulo):
        """

        :param titulo: titulo de la cabecera del pdf
        :type titulo: str
        :return: None
        :rtype: None

        Método que genera la cabecera común a todos los informes

        """
        try:
            ruta_logo = '.' + Informes.separator + 'img' + Informes.separator + 'house.ico'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Inmobiliaria Teis')
                var.report.drawString(230, 675, titulo)
                var.report.line(50, 665, 525, 665)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 755, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)

    @staticmethod
    def footInforme(titulo, total_pages):
        """

        :param titulo: titulo del pdf
        :type titulo: str
        :param total_pages: número total de páginas del pdf
        :type total_pages: int
        :return: None
        :rtype: None

        Método que genera el footer común a todos los informes

        """
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()) + " / " +
                                  str(total_pages))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)