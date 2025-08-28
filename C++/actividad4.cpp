#include <iostream>

int main () {
    double pi = 3.14159;
    double radio, area, resultado;

    std::cout << "Agregue el radio: ";
    std::cin >> radio;

    resultado = radio * radio;

    area = pi * resultado;

    std::cout << "El area es: " << area << std::endl;


    return 0;
}