# Aplicación Web - Sistema de Recomendación
Este proyecto hace uso de un sistema de recomendación, que se encuentra en este [repositorio](https://github.com/X4Zero/SISTEMAS_DE_RECOMENDACION).

Para la aplicación desplegada se usa un subset porque debido a la cantidad de películas y la matriz que se genera con los puntajes entre las películas genera un problema con la memoria ram.

Proyecto de la Segunda Semana en Hackspace.

## Inicio

### Pasos
Los pasos para el desarrollo de este proyecto son:
- Ejecutar el archivo languages.py para generar un diccionario con los lenguajes que se ven en el notebook de la implementación del sistema de recomendación.
- Ejecutar el notebook en este [repositorio](https://github.com/X4Zero/SISTEMAS_DE_RECOMENDACION), en la última sección se explica como se prepara uno de los sistemas de recomendación para incrustarlo en una aplicación web.
- Luego en base al archivo metadata_prod_final.csv cargamos los datos para realizar las recomendaciones.

### Requisitos
Todos los requerimientos para que el proyecto funcione se encuentran el archivo requirements.txt, ejecutar el siguiente comando para instalar las librerías necesarias.
```
pip install -r requirements.txt
```

Para levantar el proyecto ejecutar:
```
python app.py
```

### Despliegue
El sistema se encuentra desplegado en heroku en el siguiente [enlace](https://sis-recomendacion-peliculas.herokuapp.com/)