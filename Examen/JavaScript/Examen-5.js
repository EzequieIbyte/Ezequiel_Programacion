function concatenarArrays(array1, array2) {
  
  return [...array1, ...array2];
}


const listaNumeros = [1, 2, 3];
const listaLetras = ['a', 'b', 'c'];

const listaCombinada = concatenarArrays(listaNumeros, listaLetras);

console.log("Array 1 original:", listaNumeros);
console.log("Array 2 original:", listaLetras);
console.log("Array concatenado:", listaCombinada);
