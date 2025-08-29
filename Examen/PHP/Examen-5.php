<?php

function generarContrasena($longitud, $incluirCaracteresEspeciales = false) {
   
    $caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    $caracteresEspeciales = '!@#$%^&*()-_+=~`[]{}|:;"<>,./?';


    if ($incluirCaracteresEspeciales) {
        $caracteres .= $caracteresEspeciales;
    }

    $contrasena = '';
    $longitudCaracteres = strlen($caracteres);

 
    for ($i = 0; $i < $longitud; $i++) {
      
        $contrasena .= $caracteres[rand(0, $longitudCaracteres - 1)];
    }

    return $contrasena;
}


echo "Contraseña generada (sin caracteres especiales): " . generarContrasena(10) . "<br>";


echo "Contraseña generada (con caracteres especiales): " . generarContrasena(12, true) . "<br>";

?>