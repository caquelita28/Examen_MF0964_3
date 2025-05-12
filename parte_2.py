import requests
import random

servidor ="192.168.1.17:5101"


def main():
    # Realizar la petición GET a la API
    respuesta = requests.get("https://api.ejemplo.com/estado usando request")
    datos = respuesta.text
    print(datos)
    return datos


def comprobar_estado():
    for i in range(200):
        if i == 200:
            print("OK")
        else:
            "ERROR"

if __name__ == '__main__':
    main()