<?php

    
$tem = readline("Ingresar la temperatura: ");
if($tem < 10){
    echo "Fria";
    
}elseif($tem >= 10 && $tem <= 25){
    echo "Templado";
    
}elseif($tem > 25){
    echo "Caluroso";
    
}else{
    echo "Temperatura invalida";
}
?>