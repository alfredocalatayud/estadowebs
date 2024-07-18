import pandas as pd

df = pd.read_csv('ayuntamientos.csv', delimiter=';')

comunidad_autonoma = df['ComunidadAutonoma'].tolist()
provincia = df['Provincia'].tolist()
nombre_ayuntamiento = df['NombreAyuntamiento'].tolist()
web_ayuntamiento = df['WebAyuntamiento'].tolist()
sede_electronica = df['SedeElectronica'].tolist()

print("Número de elementos en ComunidadAutonoma:", len(comunidad_autonoma))
print("Número de elementos en Provincia:", len(provincia))
print("Número de elementos en NombreAyuntamiento:", len(nombre_ayuntamiento))
print("Número de elementos en WebAyuntamiento:", len(web_ayuntamiento))
print("Número de elementos en SedeElectronica:", len(sede_electronica))