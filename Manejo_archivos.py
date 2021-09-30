import re

def read_file(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        for line in f:
            
            if line.startswith('G'):#Find line that starts with 'G'
                print(line.rstrip())#Erase \n
            


def run():
    file_path = './files/file_1.txt'
    read_file(file_path)


if __name__ == "__main__":
    run()


