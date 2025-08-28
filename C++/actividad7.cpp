#include <iostream>

int main (){
    int num, i, resultado;

    std::cout << "Agregue un numero: ";
    std::cin >> num;

    for (i = 1; i <= 10; i++){
        
        std::cout << num << "x" << i << "=" << num * i << std::endl;
    }


    return 0;
}