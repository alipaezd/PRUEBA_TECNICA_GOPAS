CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL UNIQUE,
    fecha_registro TIMESTAMP DEFAULT NOW()
);

INSERT INTO usuarios (nombre, correo,fecha_registro) VALUES
('Ali Paez', 'ali@email.com','2023-05-01 12:00:00'),
('Josefino Gómez', 'josefino@email.com','2023-10-11 12:00:00'),
('Lucho Díaz', 'Lucho@emaiol.com', '2025-03-15 12:00:00'),
('Lucho Díaz2', 'Lucho2@emaiol.com', '2025-03-15 16:00:00');
