import psycopg2
from psycopg2 import errors, OperationalError, IntegrityError

nombre = "Pepito Pérez21312"
correo = "pepito312@email.com"

try:
    conexion = psycopg2.connect(
        dbname="mi_db",
        user="postgres",
        password="postgres",
        host="db_postgres",
        port="5432"
    )
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)", (nombre, correo))
        conexion.commit()
        print("✅ Usuario insertado correctamente.")

    except errors.UniqueViolation:
        conexion.rollback()
        print(" Error: El correo ya existe en la base de datos.")

    except IntegrityError as e:
        conexion.rollback()
        print(f" Error  de datos: {e}")

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print("\n Todos los usuarios:")
    [print(u) for u in usuarios]

    cursor.execute("SELECT * FROM usuarios WHERE fecha_registro >= NOW() - INTERVAL '7 days'")
    recientes = cursor.fetchall()
    print("\n Usuarios registrados en los últimos 7 días:")
    [print(r) for r in recientes]

    cursor.close()
    conexion.close()

except OperationalError as e:
    print(f" Error de conexión con la base de datos: {e}")

except Exception as e:
    print(f"Error inesperado: {e}")
