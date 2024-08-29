import express from 'express'

const servidor = express()

servidor.use(express.json())
servidor.get('/', (req, res) => {
    res.json({
        message: 'bienvenido a mi API de express'
    })
})
servidor.post('/registro', (req, res) => {
    console.log(req.body)
    res.json({
        message: 'Registro exitoso'
    })
})
servidor.listen(3000, ()=> {
    console.log('Servidor corriendo en el puerto 3000')
})