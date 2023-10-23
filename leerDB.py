import pandas as pd
import sys
import random

with open(F"database.txt", "w") as archivo:
    sys.stdout = archivo
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    
    datos = pd.read_csv("entrenamiento.csv")
    
    #print(datos)
        
    df_0 = datos[datos['ca_cervix'] == 0]
    
    print(f"Contienen 0: no cervical cancer #{len(df_0)}")
   
    moda = df_0['behavior_sexualRisk'].value_counts()
    print(moda)
    
    
    #print(df_0)
    print("**********************************************")
    df_1 = datos[datos['ca_cervix'] == 1]
    print(f"Contienen 1: has cervical cancer #{len(df_1)}")
    
    moda = df_1['behavior_sexualRisk'].value_counts()
    print(moda)
    #print(df_1)
        
    '''random.seed(42)  # Esto establece una semilla para que los números aleatorios sean reproducibles.
    indices_seleccionados = random.sample(range(len(datos)), 58)
    entrenamiento = datos.loc[indices_seleccionados]

    # Los elementos restantes se guardarán en otro DataFrame llamado 'prueba'.
    prueba = datos.drop(indices_seleccionados)

    # Finalmente, puedes guardar estos DataFrames en archivos CSV.
    entrenamiento.to_csv('entrenamiento.csv', index=False)
    prueba.to_csv('prueba.csv', index=False)'''

    
