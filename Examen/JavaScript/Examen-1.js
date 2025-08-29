function calculadora(num1, num2, operador){
    switch(operador){
        case '+':
            return  num1 + num2;
            
        case '-':
            return  num1 - num2;

        case '*':
            return num1 * num2;

        case '/':

            if(num2 === 0){
                return "Error: Division por Cero"
            }

            default:
                return num1 / num2;
            
    }   

}

console.log(`2 + 3 = ${calculadora(2, 3, '+')}`);   
console.log(`10 - 5 = ${calculadora(10, 5, '-')}`);  
console.log(`4 * 6 = ${calculadora(4, 6, '*')}`);    
console.log(`10 / 2 = ${calculadora(10, 2, '/')}`);  
console.log(`5 / 0 = ${calculadora(5, 0, '/')}`); 