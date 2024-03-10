import { getAllActorsFromMovieId, getAllDirectorsFromMovieId } from '../controllers/persons.js'
import { getAllMovies, getMovieInfoFromId } from '../controllers/movies.js'

export async function getAllMoviesService(){
    const movies = await getAllMovies()
    var moviesSorted = {}
    
    movies.map(movie => {
        if (! (movie.month in moviesSorted)) moviesSorted[movie.month] = []
        moviesSorted[movie.month].push(movie)
    });
    return moviesSorted
}

export async function getMovieInfoFromIdService(id){
    const movie = await getMovieInfoFromId(id)
    const actors = await getAllActorsFromMovieId(id)
    const directors = await getAllDirectorsFromMovieId(id)

    movie["actors"] = actors
    movie["directors"] = directors

    return movie
}