<?php
//Crea un script que genere y muestre en la terminal la tabla de multiplicar
//completa del número 8, desde el 8×1 hasta el 8×10.
echo "Tablas de Multiplicar del 8\n";

for ($i = 1; $i <= 10; $i++) {
    echo "8 x " . $i . " = " . (8 * $i) . "\n";
}
echo "\n";
?>