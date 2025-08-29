SELECT u.nombre, p.producto
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id;