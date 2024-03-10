import { getAllMoviesForAPersonForACredit } from "../controllers/movies.js";

export async function getAllMoviesForAPerson(person_id){
    const moviesDirector = await getAllMoviesForAPersonForACredit(person_id, 'director')
    const moviesActor = await getAllMoviesForAPersonForACredit(person_id, 'actor')

    const movies = {
        "actor": moviesActor,
        "director": moviesDirector
    }

    return movies
}