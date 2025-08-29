#ifndef CIRCULO_H
#define CIRCULO_H

class Circulo {
private:
    double radio;

public:
   
    Circulo(double r);

    double calcularArea() const;
    double calcularCircunferencia() const;
};

#endif