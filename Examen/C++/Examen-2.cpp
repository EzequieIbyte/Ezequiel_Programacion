#ifndef ESTUDIANTE_H
#define ESTUDIANTE_H

#include <string>
#include <vector>

class Estudiante {
private:
    std::string nombre;
    std::vector<int> calificaciones;

public:
 
    Estudiante(const std::string& nombreEstudiante);

    void agregarCalificacion(int calificacion);
    double calcularPromedio() const;
};

#endif