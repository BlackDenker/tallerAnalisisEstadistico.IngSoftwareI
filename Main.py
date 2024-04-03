from Model.File import File
from Controller.Numbers import Numbers
import os

path = input('Escriba la ruta del archivo: ')
if os.path.exists(path):
    if path[-4:] == '.txt':
        file = File(path)
        file.read()
        if len(file.numbers) == 0:
            print('No hay números en el archivo.')
        else:
            file.view()
            if len(file.numbers) == 1:
                print('No se puede calcular la varianza o la mediana de un solo número.')
            else:
                print('La varianza de los números es: ', Numbers.variance(file.numbers))
                print('La mediana de los números es: ', Numbers.median(file.numbers))
    else: 
        print('El archivo no es un .txt o no esta llamando un arhivo')
else:
    print("El archivo o ruta no existe.")