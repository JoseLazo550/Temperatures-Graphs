import os
import PyPDF2
from Grafica import plot_data

# mexico_entities = ('Aguascalientes', 'Baja California','Baja California Sur','Campeche','Coahuila','Colima','Chiapas','Chihuahua','Ciudad de México',
#     'Durango','Guanajuato','Guerrero','Hidalgo','Jalisco','Estado de México','Michoacán','Morelos','Nayarit','Nuevo León','Oaxaca','Puebla','Querétaro',
#     'Quintana Roo','San Luis Potosí','Sinaloa','Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz','Yucatán','Zacatecas')

mexico_entities: tuple = ('Oaxaca','Baja California','Tabasco')
months: tuple = ('Enero','Febrero','Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

class Entity:
    def __init__(self, name_entity, temperatures, months):
        self.name_entity = name_entity
        self.temperatures = temperatures
        self.months = months
        self.data_temp = {months:temperatures}
        

def get_data(path: str):
    '''
        This function save information from a txt into Dictionary of States
        Each state has a  dictionary, keys = Months, values = temperatures
        returns a nested dictionary
    '''
    all_state_temperatures = {}
    with open(path, 'r', encoding = 'utf-8') as f:
        f_list = list(enumerate(f))

    data_location = {}
    for i, data in f_list:#Search in a enumerate list
            state = data.strip()
            if state in mexico_entities:#For each entity in list, do:
                begin = int(i)+1#Where data begins 
                end = begin+11#Where data ends
                data_range = (begin,end)
                data_location.setdefault(state,data_range)

    for entity in mexico_entities:
        only_temperatures = [float(t.strip()) for i, t in f_list if i in range(data_location[entity][0],data_location[entity][1]+1)] #Extract temperatures for each state from file enumerate
        monthly_temperatures = dict(zip(months, only_temperatures))#save temperatures for each month
        all_state_temperatures.setdefault(entity, monthly_temperatures)#Save all entitys with its own data

    return all_state_temperatures    
 
              
def extract_pdf(path_pdf: str) -> str:#Not yet
    '''
        This function extracts temperature information from a PDF (SMN)
        Then save it in a txt file 
        returns the txt file's path
    '''
    try:
        pdfFileObj = open(path_pdf, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        text: str = pageObj.extractText()

        path_file: str = path_pdf[:12]+'temperatures.txt'
        with open(path_file, 'w', encoding ='utf-8') as f:
            f.write(text) 

        return path_file
    except:
        print("Error al abrir el archivo")
    finally:
        pdfFileObj.close()


def interfaz():
    print('Bienvenido\n')
    print('Estos son los archivos disponibles: \n')
    print(os.getcwd())
    files = os.listdir('./files')
    for file in files:
        print(file)


def run():
    interfaz()
    path_pdf: str = './files/2019.pdf'#Select file
    data_path = extract_pdf(path_pdf)
    temperatures = get_data(data_path)
    year: str = path_pdf[8:]#Year in string
    year = year[:4]
    plot_data(temperatures, months, year)

if __name__ == "__main__":
    run()


