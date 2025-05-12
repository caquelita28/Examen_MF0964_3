import requests
import json



def comprobar_estado():
    try:
        # Realizar la petición GET a la API
        respuesta = requests.get("https://api.ejemplo.com/estado usando request")

        # Verificar si la petición fue exitosa
        respuesta.raise_for_status()

        # Obtener y mostrar los datos en formato JSON
        datos = respuesta.json()
        print("Respuesta de la API:")
        print(f"Mensaje: {datos['OK']}")
        print(f"Estado: {datos['estado']}")

    except requests.exceptions.ConnectionError:
        print("ERROR: FALLO DE CONEXION")
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {e}")


if __name__ == '__main__':
    comprobar_estado()