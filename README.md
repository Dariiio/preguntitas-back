# Proyecto Flask con Docker

Este proyecto es una aplicación Flask que utiliza Docker para su ejecución. Permite realizar operaciones CRUD en una base de datos SQLite y tiene una API que proporciona acceso a estas operaciones.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)
- Python 3.x (opcional, solo si necesitas modificar la aplicación)

## Cómo ejecutar la aplicación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tuusuario/tu-proyecto-flask-docker.git
   cd tu-proyecto-flask-docker

2. Construye la imagen Docker:

    >docker build -t preguntitas-back .

3. Ejecuta la aplicación en un contenedor Docker:

    >docker run -p 5000:5000 preguntitas-back

Uso de la API

La API de esta aplicación Flask ofrece las siguientes rutas:

    GET /preguntas: Obtiene todas las preguntas.
    POST /preguntas: Crea una nueva pregunta (requiere datos JSON en la solicitud).
    PUT /preguntas/<id>: Actualiza una pregunta existente por su ID (requiere datos JSON en la solicitud).
    DELETE /preguntas/<id>: Elimina una pregunta por su ID.
    GET /preguntas/random: Obtiene una pregunta aleatoria de la base de datos.

Puedes utilizar herramientas como Postman o cURL para interactuar con la API.