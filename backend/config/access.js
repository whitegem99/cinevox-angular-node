import mysql from 'mysql2/promise.js'
import { HOST, USER, PASSWORD, DATABASE } from '../config.js'

export const connection = await createConnection()

export async function createConnection(){
    console.log(HOST)
    const connection = await mysql.createConnection({
        host: HOST,
        user: USER,
        password: PASSWORD,
        database: DATABASE
    })

    return connection
}