function calcularBalance(transacciones) {
  return transacciones.reduce((balanceActual, transaccion) => {
    if (transaccion.tipo === 'ingreso') {
      return balanceActual + transaccion.monto;
    } else if (transaccion.tipo === 'gasto') {
      return balanceActual - transaccion.monto;
    }
    return balanceActual;
  }, 0); 
}

const transacciones = [
  { tipo: 'ingreso', monto: 500 },
  { tipo: 'gasto', monto: 150 },
  { tipo: 'ingreso', monto: 100 },
  { tipo: 'gasto', monto: 75 }
];

const balanceFinal = calcularBalance(transacciones);
console.log(`El balance final es: ${balanceFinal}`); 

