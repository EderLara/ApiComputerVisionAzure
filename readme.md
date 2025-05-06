# Api Computer Vision AZURE

En este archivo encontraremos una api que usa Computer Vision de Azure para predecir imagenes.
Asegurate de tener un archivo .env con las credenciales de azure.

## Instalación y uso

### Pasos de instalación
1. Clona este repositorio:
   ```
   git clone https://github.com/EderLara/ApiComputerVisionAzure.git
   cd azureapi
   ```

2. Instala los requerimientos:
    ```
    pip install -r requeriments.txt
    ```

### Uso
* Desde el ide o colab, ejecutar
* Asegurate de tener una imagen en la raiz del proyecto 
    ```
        # Cargar y mostrar la imagen original
        image_path = ".\ps.webp"
    ```
* Se conectará a azure con las credenciales: clave 1 y el externo
* Consulta los resultados en la terminal:

```
    Objetos detectados:

    Etiquetas generales:
    - panel solar: 99.94%
    - energía solar: 97.74%
    - exterior: 91.89%
    - tenis: 90.89%
    - raqueta: 61.83%
    - solar: 53.46%

```