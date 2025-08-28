#include <iostream>
#include <conio.h>

int main () {
    int age;

    std::cout << "Ingrese su edad: ";
    std::cin >> age;
     
    if(age < 18){
        std::cout << "Eres menor de edad" << std::endl;
    }

    else if(age >= 18 && age <= 65){
        std::cout << "Eres menor de edad" << std::endl;
    }

    else{
        std::cout << "Eres un adulto mayor" << std::endl;
    }

    getch();
}