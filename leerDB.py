import pandas as pd
import sys

with open(F"database.txt", "w") as archivo:
    sys.stdout = archivo
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    
    datos = pd.read_csv("sobar-72.csv")
    
    #print(datos)
    
    for column in datos.columns :
        moda = datos[column].value_counts()
        print(moda)

    
