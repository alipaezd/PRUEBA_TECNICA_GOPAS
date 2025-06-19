# Proyecto de Automatización, PostgreSQL y Linux

## 1. Automatización con Python
    Ejecutar:
    python app/automatizacion_archivos.py
## 2. PostgreSQL y Python
    ## Levantemos el entorno:
        docker-compose up --build -d
    ## Miramos los logs para ver la ejecucion incial del slq:
        docker logs -f postgres_db  
    ## Para correr el python base_datos_postgres:
        -entramos al bash linux:
         docker exec -it prueba_tecnica_gopas-app-1 bash
        - ya dentro  ejecutamos :
            python /app/app/base_datos_postgres.py  

## 3. Administración Linux
 ## Entramos al bash 
  -docker exec -it prueba_tecnica_gopas-app-1 bash
 ## Correr el script:
   ./app/scripts/respaldo.sh

## RESPUESTAS ENUNCIADO 

Enunciado:
1. Responde brevemente cómo realizarías las siguientes acciones (no es necesario ejecutarlas):
- Ver los 5 procesos que más memoria consumen.

ps aux --sort=-%mem | head -n 5

ps aux: lista todos los procesos
--sort=-%mem: Ordena los procesos por el uso de memoria
| head -n 5: Muestra  las primeras 5 líneas del resultado.


- Agregar un nuevo usuario al sistema.
    sudo adduser nuevo_usuario
- Cambiar los permisos de un archivo para que solo el dueño pueda leer y escribir.
 chmod 600 archivo.txt

 el 6 permite leer y escribir  a nivel de usuario dueño.

- Ver el estado del servicio `ssh`.
systemctl status ssh