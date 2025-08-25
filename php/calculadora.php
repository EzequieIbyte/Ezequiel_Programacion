<?php
function calculadora(){
do{
$num1 = readline("Ingresar la número: ");
$num2 = readline("Ingresar la número: ");
$op = readline("Ingresar operador[+,-,*,/]: ");

switch ($op) {
    case "+":
        $resultado = $num1 + $num2;
        echo "La suma es:$resultado.\n";
        break; 
        
    case "-":
        $resultado = $num1 - $num2;
        echo "La suma es:$resultado.\n";
        break; 
        
    case "*":
        $resultado = $num1 * $num2;
        echo "La suma es:$resultado.\n";
        break; 
        
    case "/":
        if($num2 != 0){
        $resultado = $num1 / $num2;
        echo "La suma es:$resultado.\n";
        }else{
        echo "Error no se puede dividir por cero\n"; 
        }
        break; 
        
    default:
        echo "Operador no válido. Por favor, ingresa uno de los siguientes: +, -, *, /.\n";
        break;
}

$res = readline("Quiere seguir con el programa? precione S para seguir: ");
}while($res == 'S' || $res == 's');

echo "Programa terminado \n";
}

calculadora();
?>