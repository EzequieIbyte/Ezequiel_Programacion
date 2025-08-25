<?php
// Desarrolla un script que determine si un número almacenado en una variable es positivo, negativo o cero, y muestre el resultado correspondiente.

$num = readline("Ingresar el numero: ");
if($num > 0){
    echo "El numero es positivo";
}elseif($num < 0){
    echo "El numero es negativo";
}else{
    echo "El numero es 0";
}
?>