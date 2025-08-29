<?php


function invertirCadena($cadena) {
 
  return strrev($cadena);
}


$textoOriginal = "Hola, mundo!";
$textoInvertido = invertirCadena($textoOriginal);


echo "Cadena original: " . $textoOriginal . "<br>";
echo "Cadena invertida: " . $textoInvertido;

?> 