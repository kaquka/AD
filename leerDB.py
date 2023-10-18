import pandas as pd
import sys
import random

with open(F"database.txt", "w") as archivo:
    sys.stdout = archivo
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    
    datos = pd.read_csv("sobar-72.csv")
    
    #print(datos)
    
    for column in datos.columns :
        moda = datos[column].value_counts()
        print(moda)
        
    random.seed(42)  # Esto establece una semilla para que los números aleatorios sean reproducibles.
    indices_seleccionados = random.sample(range(len(datos)), 58)
    entrenamiento = datos.loc[indices_seleccionados]

    # Los elementos restantes se guardarán en otro DataFrame llamado 'prueba'.
    prueba = datos.drop(indices_seleccionados)

    # Finalmente, puedes guardar estos DataFrames en archivos CSV.
    entrenamiento.to_csv('entrenamiento.csv', index=False)
    prueba.to_csv('prueba.csv', index=False)   

    
