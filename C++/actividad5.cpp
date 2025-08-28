#include <iostream>


int main () {
    int num;

    std::cout << "Agregar numero: ";
    std::cin >> num;

    if(num > 0){
        std::cout << "El numero es positivo: " << std::endl;
    }
    else if(num < 0){
        std::cout << "El numero es negativo: " << std::endl;
    }

    else{
        std::cout << "El numero es neutral es decir 0." << std::endl;
    }


    return 0;
}