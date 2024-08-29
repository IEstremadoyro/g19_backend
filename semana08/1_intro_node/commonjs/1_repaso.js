//asi se debe de realizar la importacion de otros archivos en nuestro proyecto con CommonJs
const funciones = require('./2_funciones')
const x = 'eduardo'

x = 'ramiro'

function sumar(numero1, numero2) {
    const resultado = numero1 + numero2
    return resultado
}
const sumatoria = sumar(12,23)

console.log(sumatoria)

const resta = funciones.restar(10,20)
console.log(resta)