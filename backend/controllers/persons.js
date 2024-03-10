import { connection } from '../config/access.js'


export async function getAllActorsFromMovieId(movie_id){
    const query = 'SELECT ps.id, ps.name FROM persons ps, movie_person mp WHERE mp.movie_id = ? AND mp.person_id = ps.id AND credit = \'actor\''

    let actors = await connection.execute(query, [movie_id])

    return actors[0]
}

export async function getAllDirectorsFromMovieId(movie_id){
    const query = 'SELECT ps.id, ps.name FROM persons ps, movie_person mp WHERE mp.movie_id = ? AND mp.person_id = ps.id AND credit = \'director\''

    let directors = await connection.execute(query, [movie_id])

    return directors[0]
}