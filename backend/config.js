import { config } from 'dotenv'
import { fileURLToPath } from 'url'
import { dirname } from 'path'
import path from 'path'

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
config({path: path.resolve(__dirname, '.env')})

export const PORT = process.env.BK_PORT
export const HOST = process.env.BK_HOST
export const USER = process.env.DB_USER
export const PASSWORD = process.env.DB_PASSWORD
export const DATABASE = process.env.DB_DATABASE