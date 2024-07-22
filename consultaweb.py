import pandas as pd
import requests
from tqdm import tqdm

# Función para leer el archivo CSV
def read_csv(filename):
    return pd.read_csv(filename, delimiter=';')

# Función para obtener el estado HTTP de una URL
def get_http_status(url):
    try:
        response = requests.get(url, timeout=5, stream=True)
        return response.status_code
    except requests.RequestException as e:
        return str(e)

# Función para ver los resultados
def view_results(df):
    print(df.head(20))

# Función para comprobar el fichero de webs
def check_webs(df):
    tqdm.pandas(desc="Consultando webs")
    df['HttpStatus'] = df['WebAyuntamiento'].progress_apply(get_http_status)
    df.to_csv('ayuntamientos_con_estado_http.csv', index=False)
    print("Comprobación completada y guardada en 'ayuntamientos_con_estado_http.csv'")

# Función principal del menú
def main_menu():
    filename = 'ayuntamientos.csv'
    df = read_csv(filename)

    while True:
        print("\nMenú:")
        print("1. Comprobar el fichero de webs")
        print("2. Ver los resultados")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            check_webs(df)
        elif choice == '2':
            view_results(df)
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    main_menu()