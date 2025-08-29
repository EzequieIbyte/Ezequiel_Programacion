function filtrar(arraysobjetos, propiedad, valor) {
    return arraysobjetos.filter(objeto => objeto[propiedad] === valor);
}

const lenguajes = [
    { programacion: "C++", Creador: "Bjarne Stroustrup", anio: 1979 },
    { programacion: "Java", Creador: "James Gosling", anio: 1995 },
    { programacion: "Python", Creador: "Guido van", anio: 1991 }
];


const lenguajePython = filtrar(lenguajes, 'programacion', 'Python');
console.log("Lenguaje de programacion:");
console.log(lenguajePython);


console.log('--------------------');


const lenguaje_1979 = filtrar(lenguajes, 'anio', 1979);
console.log("Lenguajes Creado en 1979:");
console.log(lenguaje_1979);









