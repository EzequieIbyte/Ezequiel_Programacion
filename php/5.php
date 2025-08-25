<?php
//Crea un programa que verifique si una persona puede obtener una licencia de conducir. 
//La condición es que debe tener al menos 18 años y no más de 65 años. 
//Define una variable para la edad y muestra si cumple los requisitos o no.

echo "## 2. Ejemplo de if / else ##\n";

$edad = readline("Ingresar el numero:");

if ($edad >= 18 && $edad < 65) {
    echo "Puedes tener licencia de conducir.\n";
    
} elseif($edad >= 65) {
    echo "Eres muy viejo para tener licencia de conducir.\n";
} elseif($edad < 18 && $edad > 0){
    echo "Eres muy joven para tener licencia.\n";
} else{
    echo "Numero invalido.\n";
}
echo "\n";
?>