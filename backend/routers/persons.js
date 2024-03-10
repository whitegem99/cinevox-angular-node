import express from 'express'
import { getAllMoviesForAPerson } from '../services/persons.js'

export const personsRouter = express.Router()

personsRouter.get('/:id', async (request, response) =>{
    var id = request.params['id']

    const movies = await getAllMoviesForAPerson(id)

    response.json(movies)
    response.end()
})
