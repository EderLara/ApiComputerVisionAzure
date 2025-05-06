import requests
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from io import BytesIO
import os
import json
from dotenv import load_dotenv

load_dotenv()

 # Configuración de la API de Azure
subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")                # Usar la clave de suscripción correcta, por lo general la clave 1
region = "eastus"  # Reemplaza con tu región de Azure
endpoint = os.getenv("AZURE_ENDPOINT")                                                    # Reemplaza con tu extremo de Azure
# URL para el análisis de imágenes
analyze_url = endpoint + "vision/v3.1/analyze"

# Función para cargar y mostrar una imagen
def load_and_show_image(image_path):
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    return image

def analyze_image(image_path):
    try:
        # Leer la imagen
        image = open(image_path, "rb").read()
        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/octet-stream'
        }
        params = {
            'visualFeatures': 'Objects,Tags',
            'language': 'es'
        }

        # Hacer la petición a la API
        response = requests.post(analyze_url, headers=headers, params=params, data=image)
        response.raise_for_status()
        analysis = response.json()

        # Mostrar predicciones
        print("\nObjetos detectados:")
        if 'objects' in analysis:
            for obj in analysis['objects']:
                print(f"- {obj['object']}: {obj['confidence']:.2%}")

        print("\nEtiquetas generales:")
        if 'tags' in analysis:
            for tag in analysis['tags']:
                print(f"- {tag['name']}: {tag['confidence']:.2%}")

        # Visualizar la imagen con las detecciones
        original_image = Image.open(image_path)
        image_array = np.array(original_image)

        fig, ax = plt.subplots(1, figsize=(12, 8))
        ax.imshow(image_array)

        if 'objects' in analysis:
            for obj in analysis['objects']:
                rect = obj['rectangle']
                # Dibujar rectángulo
                ax.add_patch(plt.Rectangle(
                    (rect['x'], rect['y']),
                    rect['w'], rect['h'],
                    fill=False,
                    edgecolor='red',
                    linewidth=2
                ))
                # Añadir etiqueta con confianza
                plt.text(
                    rect['x'], rect['y'] - 10,
                    f"{obj['object']} ({obj['confidence']:.2%})",
                    color='white',
                    bbox={'facecolor': 'red', 'alpha': 0.5}
                )

        plt.axis('off')
        plt.title("Análisis de Imagen")
        plt.show()

        return analysis

    except Exception as e:
        print(f"Error: {e}")
        return None

# Cargar y mostrar la imagen original
image_path = ".\ps.webp"
# Analizar la imagen
image_path = image_path                  # Cambia esto a la ruta de tu imagen
results = analyze_image(image_path)
# Obtener y mostrar la detección de objetos
result_image = analyze_image(image_path)
plt.axis('off')
plt.title("Detección de Objetos")
plt.show()