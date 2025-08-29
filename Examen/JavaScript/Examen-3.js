
function encontrarMaximo(numeros) {
 
  if (numeros.length === 0) {
    return null;
  }
  
  let maximo = numeros[0]; 
  
 
  for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] > maximo) {
      maximo = numeros[i]; 
    }
  }
  
  return maximo;
}


const listaNumeros = [15, 8, 25, 4, 30, 12];
console.log(`El número más alto en [${listaNumeros}] es: ${encontrarMaximo(listaNumeros)}`);


