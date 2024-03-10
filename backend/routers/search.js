import express from 'express'
import { getPersonOrMovieSearched } from '../services/search.js'


export const searchRouter = express.Router()

searchRouter.get('/:search', async (request, response) => {
    var search = request.params["search"]

    const searched = await getPersonOrMovieSearched(search)

    response.json(searched)
    response.end()
})