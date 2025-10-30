function maiorABC(a, b, c) {
    maiorEntreAB = (a + b + Math.abs(a - b)) / 2;
    // abs() retorna o valor absoluto de um numero, ou seja,
    // a distancia que ele tem ate o zero. Ex: abs(-5) é 5 e de abs(5) é 5 tbm
   
    if(maiorEntreAB < c){
        console.log( c , "eh o maior") 
    } else {
        console.log( maiorEntreAB, "eh o maior" ) 
    }
    
}

maiorABC(7, 14 , 106)