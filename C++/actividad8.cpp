#include <iostream>

int main() {
    
    int numeros[] = {10, 20, 30, 40, 50};
    int tamano = sizeof(numeros) / sizeof(numeros[0]); 
    int suma = 0; 

    std::cout << "Array: { ";
    for (int i = 0; i < tamano; i++) {
        suma += numeros[i]; 
        std::cout << numeros[i] << " ";
    }
    std::cout << "}" << std::endl;

    std::cout << "La suma total de los elementos es: " << suma << std::endl;

    return 0;
}