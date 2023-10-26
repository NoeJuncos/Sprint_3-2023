import os

class Inicializar():
# Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../../"))

    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

# JsonData
    Json = basedir + "\Pages"

    Environment = 'Dev'

    NAVEGADOR = 'CHROME'

# DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'
# HOJA DE DATOS EXCEL
    Excel = basedir + '/data/DataTest.xlsx'
    if Environment == 'Dev':

        URL = 'https://shop.thonet-vander.com/login'
        User = 'automationtestsNoe@outlook.com'
        Password = 'testautomation'
