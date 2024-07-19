import pandas as pd
import requests
from tqdm import tqdm

df = pd.read_csv('ayuntamientos.csv', delimiter=';')

# Seleccionar las primeras 5 filas
#df_subset = df.head(10)

# Función para obtener el estado HTTP de una URL
def get_http_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.RequestException as e:
        return str(e)

tqdm.pandas(desc="Consultando webs")
df['HttpStatus'] = df['WebAyuntamiento'].progress_apply(get_http_status)

#df.to_csv('ayuntamientos_con_estado_http.csv', index=False)

print(df.head(20))