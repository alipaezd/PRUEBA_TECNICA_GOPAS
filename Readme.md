
#  Proyecto de Automatización, PostgreSQL y Linux

---

## 1.  Automatización con Python

Ejecutar el script de automatización:

```bash
python app/automatizacion_archivos.py
```

---

## 2.  PostgreSQL y Python

###  Levantar el entorno con Docker:
```bash
docker-compose up --build -d
```

###  Ver los logs de inicialización de PostgreSQL:
```bash
docker logs -f postgres_db
```

### Ejecutar el script de base de datos en Python:

1. Ingresar al contenedor:
   ```bash
   docker exec -it prueba_tecnica_gopas-app-1 bash
   ```
2. Dentro del bash, ejecutar:
   ```bash
   python /app/app/base_datos_postgres.py
   ```

---

## 3.  Administración Linux

###  Entrar al contenedor:
```bash
docker exec -it prueba_tecnica_gopas-app-1 bash
```

###  Ejecutar script de respaldo:
```bash
./app/scripts/respaldo.sh
```

---

##  RESPUESTAS ENUNCIADO

### 1. Acciones básicas en Linux (respuestas breves):

####  Ver los 5 procesos que más memoria consumen:

```bash
ps aux --sort=-%mem | head -n 6
```

- `ps aux`: lista todos los procesos
- `--sort=-%mem`: ordena por consumo de memoria (descendente)
- `head -n 6`: muestra el encabezado + los 5 procesos más consumidores

---

#### 👤 Agregar un nuevo usuario al sistema:

```bash
sudo adduser nuevo_usuario
```

---

####  Cambiar los permisos de un archivo para que solo el dueño pueda leer y escribir:

```bash
chmod 600 archivo.txt
```

- `6`: permisos de lectura y escritura para el dueño
- `0`: sin permisos para grupo ni otros

---

####  Ver el estado del servicio `ssh`:

```bash
systemctl status ssh
```
