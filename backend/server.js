import express, { query } from 'express'
import cors from 'cors'
import { PORT } from './config.js'
import { moviesRouter } from './routers/movies.js'
import { personsRouter } from './routers/persons.js'
import { searchRouter } from './routers/search.js'

const app = express()

var __dirname = './import/storage'


app.use(cors({
    origin: ('http://localhost')
}))

app.get('/api/test', (request, response) => {
    response.send("You're online")
})

app.use('/images', express.static(__dirname));

app.use('/api/movies', moviesRouter)
app.use('/api/persons', personsRouter)
app.use('/api/search', searchRouter)



app.listen(PORT)
console.log(`Server running on port ${PORT}`)
