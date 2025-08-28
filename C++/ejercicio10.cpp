#include <iostream>


int main () {
    char respuesta;
    float num1, num2;
    float suma, resta, multiplicacion, division;
    
    std::cout << "Agrega un numero: ";
    std::cin >> num1;

    std::cout << "Agrega un numero: ";
    std::cin >> num2;

    std::cout << "Escoga una operacion[+,-,*,/]: ";
    std::cin >> respuesta;

    switch (respuesta)
    {
    case '+':
        suma = num1 + num2;
        std::cout << "La suma de los numeros es: " << suma << std::endl;

        break;

    case '-':
        resta = num1 - num2;
        std::cout << "La resta de los numeros es: " << resta << std::endl;

        break;

    case '*':
        multiplicacion = num1 * num2;
        std::cout << "La multiplicacion de los numeros es: " << multiplicacion << std::endl;

        break;

    case '/':

        if(num2 == 0){
            std::cout << "No se puede dividir por 0 " << std::endl;
        }

        else{
            division = num1 / num2;
            std::cout << "La division de los numeros es: " << division << std::endl;
        }
        
        break;
    
    default:
        std::cout << "Error vuelva a intentarlo" << std::endl;

        break;
    }

 
    return 0;

}