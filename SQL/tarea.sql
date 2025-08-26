CREATE TABLE Estudiantes (
first_name VARCHAR (100),
last_name VARCHAR (100),
age INT,
number INT
);

ALTER TABLE Estudiantes
ADD COLUMN status VARCHAR(120);

ALTER TABLE Estudiantes
DROP COLUMN status;

INSERT INTO Estudiantes (first_name, last_name, age, number)

VALUES
('Ezequiel', 'García', 18, 04127770031),
('Victor', 'Rodriguez', 19, 04248765400),
('Carlos', 'Bruzual', 56, 04326780983),
('Jose', 'Colina', 34, 0412447658953),
('Miguel', 'Gomez', 50, 04123256478),
('Eliezer', 'Zambrano', 23, 04215647823),
('Jean', 'Cefala', 20, 0437986453),
('Jaiver', 'Camacho', 40, 0433623571),
('Diego', 'Hernandez', 78, 0853712334),
('Nestor', 'Nuñez', 45, 02413237489),
('Sebastian', 'Medina', 30, 04123245637),
('Roque', 'Oviedo', 43, 04146788263);