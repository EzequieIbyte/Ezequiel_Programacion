#include <iostream>


int main () {
    int num;

    std::cout << "Agregue un numero: ";
    std::cin >> num;

    if(num % 2 == 0){
        std::cout << "El numero es positivo" << std::endl;
    }

    else{
        std::cout << "El numero es negativo" << std::endl;
    }

    return 0;
}