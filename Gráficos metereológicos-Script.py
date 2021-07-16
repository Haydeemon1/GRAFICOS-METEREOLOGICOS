import pandas as pd
import matplotlib.pyplot as plt
#"estaciones" es un Data.Frame con la informacion de cada estación.
estaciones = pd.read_csv('codigoss.txt', delimiter = ',', index_col = [0])
print(estaciones['estacion'])
def graf():  #Función para graficar la temperatura y/o precipitacion de cada estación.
    fig, ax = plt.subplots()  #Nos permite tener dos gráficas.
    ax.set_xlabel('Año')  #Subtítulo del eje "x".
    if n==2: #gráfica para la temperatura 
        ax.plot(izq, color = 'green') #Uso de "izq" para graficar 
        ax.set_ylabel(F'{datos.columns[-1]}', color='green') #Subtítulo del eje "y".
        ax.tick_params(axis='y', labelcolor= 'green') #Propiedades del eje "y".
        ax.axhline(izq.mean(), color = 'green', ls = '--') #Media de  la temperatura y propiedades
        ax.legend([F'{datos.columns[-1]}','Media'],loc = 'upper left')
    elif n==1: #gráfica para  precipitación
        ax.plot(der, color = '#998ec3') #Uso de "der" para graficar 
        ax.set_ylabel(F'{datos.columns[-1]}', color='#998ec3')
        ax.tick_params(axis='y', labelcolor= '#998ec3',)
        ax.yaxis.tick_right()
        ax.yaxis.set_label_position("right")
        ax.axhline(der.mean(), color = '#998ec3', ls = '--') 
        ax.legend([F'{datos.columns[-1]}','Media'],loc = 'upper right')  
    elif n == 0: #Gráfica para la temperatura y la precipitación
        #"a" Es una lista para el valor mínimo y maximo del eje "y".
        a = [datos[datos.columns[-2]].mean() - datos[datos.columns[-2]].std() + 3.5, datos[datos.columns[-2]].max()]
        ax.plot(izq, color = 'green')
        ax.set_ylim(a[0],a[1])  #Límites del eje "y".
        ax.set_ylabel(F'{datos.columns[-2]}', color = 'green')
        ax.tick_params(axis='y', labelcolor = 'green')
        ax.axhline(izq.mean(), color = 'green', ls = '--')
        ax.legend([F'{datos.columns[-2]}','Media'],loc = 'upper left')
        
        b = [datos[datos.columns[-1]].min()-40, datos[datos.columns[-1]].mean() + datos[datos.columns[-1]].std()+55]
        ax2 = ax.twinx() #Crea ejes gemelos compartiendo el eje x.
        ax2.plot(der,color = '#998ec3')
        ax2.set_ylim(b[0],b[1]) #Límites del eje "y".
        ax2.set_ylabel(F'{datos.columns[-1]}', color = '#998ec3')
        ax2.tick_params(axis = 'y', labelcolor = '#998ec3')
        ax2.axhline(der.mean(), color = '#998ec3', ls = '--')
        ax2.legend([F'{datos.columns[-1]}','Media'],loc = 'upper right')
    plt.title(F'{st[0]} | {codigo_observatorio} | {st[1]} m.s.n.m.| {st[2]}',weight='bold')  #T'itulo de la gráfica
    plt.show()

while True:  #Bucle para graficar las estaciones.
    print('\n\nIngrese "cancel" para terminar la visualización') #"codigo_observatorio" es lo que ingresa el usuario.
    codigo_observatorio = input('Ingrese el codigo de la estacion: ') # Ingreso del código
    if codigo_observatorio == 'cancel':  #Control para terminar de graficar.
        break
    elif  F'{codigo_observatorio}' in str(estaciones.index[0:]):  #Lectura Temperatura y/o Precipitación.
        lectura = pd.read_fwf(F'homog_mo_{codigo_observatorio}.txt') #"lectura" es un Data.Frame con una sola columna
        for i in range(18):  #Identificacion la linea en donde estan los datos Temperatura y/o Precipitación.
            if 'Year' in lectura.iloc[i][0]:
                #"datos" es un Data.Frame con columnas y filas manejables.
                datos = pd.read_csv(F'homog_mo_{codigo_observatorio}.txt', header = i + 1, delimiter = '\s+')
        #"st" es un lista con la información de la estacion ingresada.
        st = [estaciones['estacion'][codigo_observatorio], estaciones['altitud'][codigo_observatorio], estaciones['region'][codigo_observatorio]]   
        if 'Precipitation' in datos.columns and 'Temperature' in datos.columns:            
            izq = datos.groupby('Year')[datos.columns[-2]].mean()  #"izq" Es una serie de la Temperatura de la estación
            der = datos.groupby('Year')[datos.columns[-1]].mean()  #"der" Es una serie de la Precipitación de la estación 
            n = 0  #"n" es un controlador al tener Temperatura y/o precipitación.
            graf() #Para graficar los datos de la estación ingresada.
        elif 'Precipitation' in datos.columns or 'Temperature' in datos.columns:
            if 'Precipitation' in datos.columns:
                der = datos.groupby('Year')[datos.columns[-1]].mean() #"der" Es una serie de la Precipitación de la estación 
                n = 1  #"n" es un controlador al tener la precipitación.
                graf() #Para graficar los datos de la estación ingresada. 
            elif 'Temperature' in datos.columns:
                izq = datos.groupby('Year')[datos.columns[-1]].mean()
                n = 2  #"n" es un controlador al tener Temperatura 
                graf() #Para graficar los datos de la estación ingresada. 
    else:
        print('\n\nCodigo de estacion incorrecto. Reintente!!')
