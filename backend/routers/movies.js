import express from 'express'
import { getAllMoviesService, getMovieInfoFromIdService } from '../services/movies.js'

export const moviesRouter = express.Router()

moviesRouter.get('/', async (request, response) => {
    const movies = await getAllMoviesService()

    response.json(movies)
    response.end()
})

moviesRouter.get('/:id', async (request, resposne) => {
    var id = request.params['id']

    const movie = await getMovieInfoFromIdService(id)

    resposne.json(movie)
    resposne.end()
})
