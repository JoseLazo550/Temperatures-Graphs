from os import error
import re
import PyPDF2



def read_file(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        for line in f:
            
            if line.startswith('G'):#Find line that starts with 'G'
                print(line.rstrip())#Erase \n
            

def read_pdf():
    try:
        pdfFileObj = open('./files/2020.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        texto = pageObj.extractText()
        return texto
    except error as e:
        print(e)
    finally:
        pdfFileObj.close()
def run():
    file_path = './files/file_1.txt'
    read_file(file_path)

    textFile = read_pdf()
    print(textFile)


if __name__ == "__main__":
    run()


