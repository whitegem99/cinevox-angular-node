import { connection } from '../config/access.js'


export async function getPersonSearched(search){
    const query = 'SELECT id, name FROM persons WHERE name LIKE ?'

    const persons = await connection.execute(query, ["%"+search+"%"])

    return persons[0]
}

export async function getMoviesSearched(search){
    const query = 'SELECT id, title_original FROM movies WHERE title_original LIKE ?'

    const movies = await connection.execute(query, ["%"+search+"%"])

    return movies[0]
}
