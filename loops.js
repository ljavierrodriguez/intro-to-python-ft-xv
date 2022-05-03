/* 

for(iterador; condition; incremento){
    sentences
}
for( index in object){

}
for ( valor of object){

}

while(condition){
    senteces
}

do {
    sentences
} while(condition)

*/

let nombres = ["Hugo", "Paco", "Luis"];

for (let i = 1; i <= 10; i++) {
    console.log(i)
}

for (let i = 0; i < nombres.length; i++) {
    console.log(nombres[i]);
}

for (index in nombres) {
    console.log(nombres[index]);
}

for(valor of nombres){
    console.log(valor)
}