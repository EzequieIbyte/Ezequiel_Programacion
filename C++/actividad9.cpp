#include <iostream>


int main (){
    int num, i;
    long long factorial = 1;

    std::cout << "Agregue un numero: ";
    std::cin >> num;


    if(num < 1){
        std::cout << "Los numeros negativos y el 0 no tiene valor factorial";
    }

    else{

        for (i = num; i >= 1; i--){
        
        factorial = factorial * i;
        
        }

        std::cout << "El factorial del numero " << num << " = " << factorial << std::endl;
    }


    return 0;
}