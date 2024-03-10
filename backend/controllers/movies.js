import { connection } from '../config/access.js'


export async function getAllMovies(){
    const query = 'SELECT mv.id, mv.title_original, ps.path, mv.month FROM movies mv, posters ps WHERE ps.movie_id = mv.id'

    let movies = await connection.execute(query)

    return movies[0]
}

export async function getMovieInfoFromId(movie_id){
    const query = "SELECT mv.id, mv.title_original, mv.trailer, mv.release_date, mv.countries, mv.synopsis_nl, mv.synopsis_fr, mv.synopsis_en, ps.path FROM movies mv, posters ps WHERE mv.id = ? AND ps.movie_id = mv.id"

    let movie = await connection.execute(query, [movie_id])

    return movie[0][0]
}

export async function getAllMoviesForAPersonForACredit(person_id, credit){
    const query = "SELECT mv.id, mv.title_original FROM movies mv, movie_person mp WHERE mp.person_id = ? AND mp.movie_id = mv.id AND mp.credit = ?"

    let movies = await connection.execute(query, [person_id, credit])

    return movies[0]
}
