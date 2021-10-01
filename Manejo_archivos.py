import os
import re
import PyPDF2



def get_data(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        f_list = list(enumerate(f))
        
        print(f_list)
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



    
        

    #with open(path_file, 'w', encoding = 'utf-8') as f:
        
            


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


