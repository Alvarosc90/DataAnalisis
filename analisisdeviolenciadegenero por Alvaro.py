# -*- coding: utf-8 -*-
"""Analisisdeviolenciadegenero.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vRHWi7qm_5CYzkp8GoTPJ9wwU6iiZaBO
"""

from google.colab import drive
import io
import os
import pandas as pd

#montar drive
drive.mount('/content/gdrive/')

bd_22 = pd.read_csv('/content/gdrive/MyDrive/Bases de datos/linea144-enero-diciembre-2022.csv')
bd_22.head(10)

bd_22.info()

bd_22.value_counts('prov_residencia_persona_en_situacion_violencia')

#ViolenciaEdad= bd_22['edad_persona_en_situacion_de_violencia'].groupby
bd_22.value_counts('edad_persona_en_situacion_de_violencia')

plt.figure(figsize=(10,8))
ax=sns.histplot(data= bd_22 , x ='edad_persona_en_situacion_de_violencia')
ax.tick_params(axis='x', rotation=45)

plt.figure(figsize=(10,8))
ax=sns.boxplot(data= bd_22 , x ='edad_persona_en_situacion_de_violencia',y='prov_residencia_persona_en_situacion_violencia') #claramente el grafico muestra errores de tipeo

bd_22=bd_22.query('edad_persona_en_situacion_de_violencia > 18 & edad_persona_en_situacion_de_violencia < 62') #realizamos una consulta para acotar la edad evitando outliers
bd_22.value_counts('edad_persona_en_situacion_de_violencia')

plt.figure(figsize=(10,8))
sns.boxplot(data= bd_22 , x ='edad_persona_en_situacion_de_violencia',y='prov_residencia_persona_en_situacion_violencia')

plt.figure(figsize=(10,8))
ax=sns.histplot(data= bd_22 , x ='pais_nacimiento_persona_en_situacion_de_violencia')
ax.tick_params(axis='x', rotation=90)

bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Varon Trans','Varon_Trans')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Transgenero','5')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Varon trans','6')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Mujer Trans','Mujer_Trans')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Travesti','8')

bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Mujer_Trans','7')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Varon_Trans','4')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Varon_trans','6')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Varon','1')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Mujer','2')
bd_22['genero_de_la_persona_agresora']=bd_22['genero_de_la_persona_agresora'].str.replace('Otro','3')
bd_22['genero_de_la_persona_agresora'].value_counts()

bd_22.sample(5)

bd_22 = bd_22.drop ('Unnamed: 19', axis = 1)# borro columna con error

bd_22

estadisticaviolencia = bd_22['genero_de_la_persona_agresora'].value_counts()/21541 #sacamos la probabilidad del genero q sea el q ejerza violencia
estadisticaviolencia

bd_22['genero_de_la_persona_agresora']=bd_22.genero_de_la_persona_agresora.astype('float')
bd_22.info()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,8))
ax=sns.histplot(data= bd_22 , x ='genero_de_la_persona_agresora',hue='genero_persona_en_situacion_de_violencia') #Grafico de barras de la consulta de los primeros 10 Barrios
ax.tick_params(axis='x', rotation=45) #Indicadores de cada punto (Los nombres de los label rotan en 45 grados)

plt.figure(figsize=(10,8))
ax=sns.histplot(data= bd_22 , x ='prov_residencia_persona_en_situacion_violencia')
ax.tick_params(axis='x', rotation=90)

#Procedo a comparar la probabilidad de un caso de violencia en argentina, comparando la cantidad de casos denunciados con la poblacion total y poblacion provincial
Arg_pob = pd.read_csv('/content/gdrive/MyDrive/Bases de datos/PoblacionArgentinaprovisorio.csv - Hoja 1.csv')
Arg_pob.info()

Arg_pob['Jurisdicción']=Arg_pob['Jurisdicción'].str.replace('Santiago del Estero','Santiago Del Estero')
Arg_pob['Jurisdicción']=Arg_pob['Jurisdicción'].str.replace('Córdoba','Cordoba')
Arg_pob['Jurisdicción']=Arg_pob['Jurisdicción'].str.replace('Tierra del Fuego, Antártida e Islas del Atlántico Sur (2)','Tierra del Fuego, Antártida e Islas del Atlántico Sur')

Arg_pob.head(27)

bd_22['prov_residencia_persona_en_situacion_violencia'].value_counts() #cantidad por provincia
Total_violencia = bd_22.loc[:,['prov_residencia_persona_en_situacion_violencia','genero_de_la_persona_agresora']]
Total_violencia

Arg_pob = Arg_pob.drop(4)
Arg_pob = Arg_pob.drop(3)

Arg_pob.reset_index(inplace=True, drop=False)

Arg_pob = Arg_pob.drop('index', axis=1) #borre el indice viejo
Arg_pob

Arg_pob.sort_values('Jurisdicción',inplace=True)
Arg_pob = Arg_pob.drop(0)
Arg_pob = Arg_pob.drop(1)

Arg_pob

pobtot = Arg_pob.loc[:,['Jurisdicción','Total de población']]
pobtot

Total_violencia

TotalPro=Total_violencia.value_counts('prov_residencia_persona_en_situacion_violencia')
TotalPro

pd.Series(TotalPro)
totalProv = TotalPro.to_frame()

totalprov=totalProv.sort_values('prov_residencia_persona_en_situacion_violencia',inplace=True)

totalprov

concatbd= pd.merge( totalProv, pobtot, left_on ='prov_residencia_persona_en_situacion_violencia',right_on='Jurisdicción')
concatbd.info()

concatbd.set_index(0, inplace=True)

concatbd

concatbd = concatbd.reset_index()

concatbd['Total de población']=concatbd['Total de población'].str.replace('.','',regex=True) #convierto de sting a entero para poder dividir luego
concatbd['Total de población']=concatbd['Total de población'].astype('int64')

concatbd.rename(columns={0:'TotalCasos'})

Arg_pob = Arg_pob.drop(4)

Promedio=(concatbd['Total de población'] / concatbd[0]).mean()

Promedio  #promedio de casos por dia

#concatbd= ( totalProv, pobtot, left_on ='prov_residencia_persona_en_situacion_violencia',right_on='Jurisdicción')
concatbd['Probabilidad']= concatbd[0]/concatbd['Total de población'] #probabilidad de que haya un caso de violencia por provincia

concatbd

concatbd[0].sum()/concatbd['Total de población'].sum() #probabilidad que haya un caso de violencia de genero en argentina sin contar valores nulos

Total = 24558/46044703 #Probabilidad de tener un caso de violencia, numero de casos por el total de poblacion
Total