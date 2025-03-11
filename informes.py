from PyQt6 import QtSql
from reportlab.pdfgen import canvas
from datetime import datetime
from PIL import Image
import os, shutil, sys, subprocess

import conexion
import var

class Informes:
    separator = os.sep
    @staticmethod
    def reportClientes(self):
        try:
            rootPath = '.' + Informes.separator + 'informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfcli = fecha + "_listadoclientes.pdf"
            pdf_path = os.path.join(rootPath, nomepdfcli)   #también esto
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Clientes"
            #query0 = QtSql.Query() ¿query para el número de páginas?
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(105, 650, str(items[1]))
            var.report.drawString(200, 650, str(items[2]))
            var.report.drawString(285, 650, str(items[3]))
            var.report.drawString(390, 650, str(items[4]))
            var.report.drawString(460, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)
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
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)

                        items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 650, str(items[0]))
                        var.report.drawString(105, 650, str(items[1]))
                        var.report.drawString(200, 650, str(items[2]))
                        var.report.drawString(285, 650, str(items[3]))
                        var.report.drawString(390, 650, str(items[4]))
                        var.report.drawString(460, 650, str(items[5]))
                        var.report.line(50, 645, 525, 645)

                        x = 55
                        y = 625

                    var.report.setFont('Helvetica', size=9)
                    dni = '***' + str(query.value(0)[4:7] + '***')
                    var.report.drawCentredString(x + 10, y, str(dni))
                    var.report.drawString(x + 29, y, str(query.value(1))) #1 letra = 19
                    var.report.drawString(x + 48, y, str(query.value(2)))
                    var.report.drawString(x + 220, y, str(query.value(3)))
                    var.report.drawString(x + 305, y, str(query.value(4)))
                    var.report.drawString(x + 390, y, str(query.value(5)))
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
    def reportPropiedades(municipio):  #código, dirección, tipo propiedad, tipo operación, precio alquiler, precio compra
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
            #query0 = QtSql.Query() ¿query para el número de páginas?
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = ['CÓDIGO', 'DIRECCIÓN', 'TIPO', 'OPERACIÓN', 'PRECIO ALQUILER', 'PRECIO COMPRA']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(95, 650, str(items[1]))
            var.report.drawString(200, 650, str(items[2]))
            var.report.drawString(285, 650, str(items[3]))
            var.report.drawString(390, 650, str(items[4]))
            var.report.drawString(460, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)

            propiedades = conexion.Conexion.filtrar_propiedades_by_municipio(municipio)

            x = 55
            y = 625
            for propiedad in propiedades:
                if y <= 90:
                    var.report.setFont('Helvetica-Oblique', size=8)
                    var.report.drawString(450, 80, 'Página siguiente...')
                    var.report.showPage()  # crea una página nueva
                    Informes.topInforme(titulo)
                    Informes.footInforme(titulo)

                    items = ['CÓDIGO', 'DIRECCIÓN', 'TIPO', 'OPERACIÓN', 'PRECIO ALQUILER', 'PRECIO COMPRA']
                    var.report.setFont('Helvetica-Bold', size=10)
                    var.report.drawString(55, 650, str(items[0]))
                    var.report.drawString(95, 650, str(items[1]))
                    var.report.drawString(200, 650, str(items[2]))
                    var.report.drawString(285, 650, str(items[3]))
                    var.report.drawString(390, 650, str(items[4]))
                    var.report.drawString(460, 650, str(items[5]))
                    var.report.line(50, 645, 525, 645)

                    x = 55
                    y = 625

                var.report.setFont('Helvetica', size=9)
                var.report.drawCentredString(x + 10, y, propiedad["codigo"])
                var.report.drawString(x + 50, y, propiedad["direccion"])
                var.report.drawString(x + 140, y, propiedad["tipo"])
                var.report.drawString(x + 220, y, propiedad["operaciones"])
                var.report.drawString(x + 305, y, propiedad["precio_alquiler"])
                var.report.drawString(x + 390, y, propiedad["precio_venta"])
                y -= 25

            totalPageCount = var.report.getPageNumber()
            print(totalPageCount)
            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nomepdfprop):
                    if sys.platform == "win32":
                        os.startfile(pdf_path)
                    elif sys.platform == "linux":
                        subprocess.call([pdf_path])

        except Exception as error:
            print(error)

    def topInforme(titulo):
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
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

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

    def footInforme(titulo):
        try:
            total_pages = 0
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()) + " / " +
                                  "x")

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)