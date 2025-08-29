<?php


function esPrimo(int $numero): bool
{
    
    if ($numero <= 1) {
        return false;
    }
    
    if ($numero === 2) {
        return true;
    }
   
    if ($numero % 2 === 0) {
        return false;
    }


    $limite = sqrt($numero);
    for ($i = 3; $i <= $limite; $i += 2) {
        if ($numero % $i === 0) {
            return false; 
        }
    }

   
    return true;
}


echo "El número 7 es primo: " . (esPrimo(7) ? 'Sí' : 'No') . "\n";       
echo "El número 10 es primo: " . (esPrimo(10) ? 'Sí' : 'No') . "\n";      
?>
