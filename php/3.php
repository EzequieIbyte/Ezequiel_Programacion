<?php
echo "Descubre el numero del 1 al 10\n";

$intentos = 0;
$in = false;

do {
    $intentos++;
    $num = readline("Ingresar el numero:");
    echo "Intento #" . $intentos . "\n";

    if ($num == 7) {
        $in = true;
        echo "Bien hecho\n";
    }

} while ($in == false);
echo "\n";
?>