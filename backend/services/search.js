import { getMoviesSearched, getPersonSearched } from "../controllers/search.js";


export async function getPersonOrMovieSearched(search){
    const persons = await getPersonSearched(search)
    const movies = await getMoviesSearched(search)

    const searched = {
        "persons": persons,
        "movies": movies
    }

    return searched
}