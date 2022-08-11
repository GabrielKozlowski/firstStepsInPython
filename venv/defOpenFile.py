
def openFileFunkcion(path):
    try:
        with open(path,"r",encoding="UTF-8") as file:
            return file.read()

    except FileNotFoundError:
        print("File not existed")

inputNameFile = input("Please write a name of file with you wanna read : ")
fileSerch = openFileFunkcion(inputNameFile)