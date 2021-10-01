import os
import re
import PyPDF2

class Entity:
    def __init__(self, name_entity, temperatures, months):
        self.name_entity = name_entity
        self.temperatures = temperatures
        self.months = months
        self.data_temp = {months:temperatures}
        

entities = ['Aguascalientes', 'Baja California','Baja California Sur','Campeche']
months = ('Enero','Febrero','Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Agosto', 'Octubre', 'Noviembre', 'Diciembre')
all_data = []

def get_data(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        f_list = list(enumerate(f))
        
        for i, data in f_list:
            
            data_state = data[:len(data)-1]
            
            if data_state == 'Aguascalientes':
                print('Aguascalientes esta en la linea: '+ str(int(i)+1))
                
                
    print('Data has been gotten')
          
    

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


def run():
    print('Bienvenido\n')
    print(os.getcwd())
    files = os.listdir('./files')
    for file in files:
        print(file)
    

    # name_f = input('Ingresa el nombre del archivo que deseas graficar: ')
    file_path = './files/2020t.txt'#+name_f
    get_data(file_path)
    


if __name__ == "__main__":
    run()


