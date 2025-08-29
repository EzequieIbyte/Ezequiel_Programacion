<?php

$usuario = [
    'id' => 123,
    'nombre' => 'Juan Perez',
    'email' => 'juan.perez@example.com',
    'roles' => ['admin', 'editor']
];


$json_usuario = json_encode($usuario);

echo $json_usuario;

?>