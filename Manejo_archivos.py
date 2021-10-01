import os
import re
import PyPDF2
from Grafica import plot_data
mexico_entities = ['Aguascalientes', 'Baja California','Baja California Sur','Campeche']
months = ('Enero','Febrero','Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

class Entity:
    def __init__(self, name_entity, temperatures, months):
        self.name_entity = name_entity
        self.temperatures = temperatures
        self.months = months
        self.data_temp = {months:temperatures}
        

def get_data(path):
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
 
              
def extract_pdf():#Not yet
    try:
        pdfFileObj = open('./files/2020.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        texto = pageObj.extractText()

        return texto
    except:
        print("Error al abrir el archivo")
    finally:
        pdfFileObj.close()


def save_data(text):#Not yet
    
    path_file = './files/2020t.txt'
    with open(path_file, 'w', encoding ='utf-8') as f:
        f.write(text)   


def interfaz():
    print('Bienvenido\n')
    print(os.getcwd())
    files = os.listdir('./files')
    for file in files:
        print(file)


def run():
    interfaz()
    # name_f = input('Ingresa el nombre del archivo que deseas graficar: ')
    file_path = './files/2020t.txt'
    temperatures = get_data(file_path)
    print(temperatures['Aguascalientes'])
    plot_data(temperatures['Aguascalientes'])

if __name__ == "__main__":
    run()


