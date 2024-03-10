from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from slugify import slugify
from mysql.connector import Error
import requests
import shutil
import mysql.connector
import os.path
import os

### Import movies from Movix

def getAllMoviesFromThisMonthToOneYearLater():
    token = getTokenFromMovix()

    current_year = datetime.now().year
    current_month = datetime.now().month

    movies = []

    for month in range(current_month, 13):
        new_movies = getMonthMoviesFromMovix(current_year, month, token)
        for movie in new_movies:
                movies.append(movie)
    for month in range(1, current_month):
        new_movies = getMonthMoviesFromMovix(current_year + 1, month, token)
        for movie in new_movies:
            movies.append(movie)    

    return movies

def getYearMoviesFromMovix(year, token):

    url = "https://movix.brightfish.be/api/movies/y" + str(year)
    headers = {'Authorization': "Bearer " + token}

    try:
        res = requests.get(url, headers=headers)
    except:
        print("Movies couldn\'t be retrieved")
        return
    return res.json()['data']

def getMonthMoviesFromMovix(year, month, token):
    url = "https://movix.brightfish.be/api/movies/" + str(year) + "/" + str(month)
    headers = {'Authorization': "Bearer " + token}

    try:
        res = requests.get(url, headers=headers)
    except:
        print("Movies couldn\'t be retrieved")
        return
    return res.json()['data']

def getTokenFromMovix():
    url = "https://movix.brightfish.be/api/user/login"
    email = "ljans@point-be.be"
    password = "jaP@HAd@O8qs"
    data = {
        'email' : email, 
        'password' : password
    }

    try:
        res = requests.post(url, json=data)
    except:
        print("The token couldn\'t be accessed")
        return
    
    token = res.json()['data']['token']
    
    return token


### Insert movies into DB

def parseMovies(jsonMovies):
    movies = []
    for movie in jsonMovies:
        dbMovie = {}

        dbMovie["movie"] = {
                "title_original": movie["title"],
                "slug": movie["slug"] + getReleaseDate(movie),
                "month": getMonth(movie),
                "trailer": getTrailer(movie),
                "release_date": getReleaseDate(movie),
                "countries": getCountries(movie),
                "languages": getLanguages(movie),
                "synopsis_nl": getSpecificSynopse(movie, "nl"),
                "synopsis_fr": getSpecificSynopse(movie, "fr"),
                "synopsis_en": getSpecificSynopse(movie, "en"),
                "created_at": movie["created_at"],
                "updated_at": movie["updated_at"],
            }


        splitedUrl = movie["poster"].split('/')
        fileName = splitedUrl[len(splitedUrl)-1]
        filePath = "./storage/posters/" + fileName
        dbMovie["posterUrl"] = movie["poster"]

        dbMovie["poster"] = {
            "path": filePath,
            "title": fileName,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        dbMovie["persons"] = []
        for person in movie["persons"]:
            dbMovie["persons"].append(
                {
                    "name": person["name"],
                    "slug": slugify(person["name"]),
                    "created_at": datetime.now(),
                    "updated_at": datetime.now()
                }
            )

        dbMovie["movie_person"] = []
        for person in movie["persons"]:
            dbMovie["movie_person"].append(
                {
                    "character": '-',
                    "credit": person["type"]
                }
            )
        
        dbMovie["titles"] = []
        for title in movie["titles"]:
            dbMovie["titles"].append(
                {
                    "title": title["title"],
                    "language": title["lang"] if title["lang"] != None else "Unknown",
                    "created_at": datetime.now(),
                    "updated_at": datetime.now()
                }
            )
        
        dbMovie["links"] = []
        linksTitle = list(dict(movie["links"]).keys())
        for i in range(len(linksTitle)):
            dbMovie["links"].append(
                {
                    "title": linksTitle[i],
                    "url": movie["links"][linksTitle[i]],
                    "created_at": datetime.now(),
                    "updated_at": datetime.now()
                }
            )

        movies.append(dbMovie)

    return movies

# Export specific info from dict

def getDate(movie):
    release_date = getYear(movie)
    return release_date.split('-')[0] + "-" + release_date.split('-')[1]

def getMonth(movie):
    release_date = getReleaseDate(movie)
    
    if (release_date != ""):
        month = release_date.split('-')[1]
        return  month
    return 0

def getReleaseDate(movie):
    release_date = ""
    if (movie["re_release_date"] != None):
        release_date = movie["re_release_date"]
    elif (movie["release_date"] != None):
        release_date = movie["release_date"]
    
    if (release_date != ""):
        # splitted_release_date = release_date.split('-')
        # year = splitted_release_date[0]
        # month = splitted_release_date[1]
        # day = splitted_release_date[2]
        # return day + "/" + month + "/" + year
        return release_date
    
    return 0

def getTrailer(movie):
    if (movie["trailers"] != None ):
        for trailer in movie["trailers"] :
            if (trailer["embed"]):
                return trailer["url"] 
    return None

def getCountries(movie):
    countries = ""
    for country in movie["countries"]:
        if (countries == ""):
            countries+= country["name"]
        else:
            countries += ", " + country["name"] 
    
    return countries

def getLanguages(movie):
    languages = ""
    for language in movie["languages"]:
        languages += language + " # "

    return languages

def getSpecificSynopse(movie, lang):
    if (movie["synopses"] == None):
        return ""
    for synopse in movie["synopses"]:
        if (synopse["lang"] == lang):
            return synopse["text"]
    return ""

### Insert into DB

def connectToDB():
    host = os.getenv('BK_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    try:
        connection = mysql.connector.connect(host=host,
                                            user=user,
                                            password=password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def connectToDBCinevox():
    host = os.getenv('BK_HOST')
    database = os.getenv('DB_DATABASE')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
        return connection

    except Error as e:
        print("Error while connecting to MySQL", e)

# Initialisation

def initDB():
    print("-- -- Init Database --")
    initDatabase()

    print("-- -- Init Tables --")
    initTables()

def initDatabase():
    sqlStatement = getSqlStatementFromFile('./sql/database.sql')

    connection = connectToDB()
    
    cursor = connection.cursor()

    try:
        cursor.execute(sqlStatement)
    except Error as e:
        print("Error while creating the database : ", e)
    
    cursor.close()
   
    connection.close()
    
    return

def initTables():
    tables = ["movies", "links", "persons", "posters", "titles", "movie_person", "link_movie"]

    for table in tables:
        print(f"-- -- -- Init {table} --")
        executeSqlStatement(f'./sql/{table}.sql')

def executeSqlStatement(fileName):
    connection = connectToDBCinevox()
    cursor = connection.cursor()

    sqlStatement = getSqlStatementFromFile(fileName)

    try:
        cursor.execute(sqlStatement)
    except Error as e:
        print("Error : ", e)
    
    cursor.close()
    connection.close()
   
def getSqlStatementFromFile(fileName):
    filedesc = open(fileName, 'r')
    sqlStatement = filedesc.read()
    filedesc.close()

    return sqlStatement

# Statements

# - Insert

def insertStatement(connection, object, table):
    placeholders = ', '.join(['%s'] * len(object))
    columns = ', '.join(object.keys())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)

    cursor = connection.cursor()
    cursor.execute(sql, list(object.values()))
    id = cursor.lastrowid
    cursor.close()

    connection.commit()

    return id

def insertWithoutNamedParam(connection, object, table):
    placeholders = ', '.join(['%s'] * len(object))
    sql = "INSERT INTO %s VALUES ( %s )" % (table, placeholders)

    cursor = connection.cursor()
    cursor.execute(sql, list(object.values()))
    id = cursor.lastrowid
    cursor.close()

    connection.commit()

    return id

# - Select

def getPersonByName(connection, name):
    cursor = connection.cursor()
    sql = "SELECT * FROM persons pers WHERE pers.name = %(name)s"

    cursor.execute(sql, {'name': name})
    
    result = cursor.fetchall()
    
    cursor.close()

    return result


# Insert movies

def insertAllMovies(movies):
    connection = connectToDBCinevox()
    fillMoviesInDB(connection, movies)

    connection.close()
    return

def fillMoviesInDB(connection, movies):
    for movie in movies:
        insertAllMovie(connection, movie)

    return

def insertAllMovie(connection, movie):
    movieId = insertMovie(connection, movie["movie"])

    insertPoster(connection, movie["poster"], movie["posterUrl"], movieId)
    
    insertTitles(connection, movie["titles"], movieId)

    personsIds = insertPersons(connection, movie["persons"])

    insertMoviePerson(connection, movie["movie_person"], movieId, personsIds)

    linksId = insertLinks(connection, movie["links"])

    insertMovieLink(connection, movieId, linksId)

    connection.commit()

    return

def insertMovie(connection, movie):
    try:
        movieId = insertStatement(connection, movie, "movies")

        return movieId

    except mysql.connector.Error as error:
        print("Failed to insert movie in MySQL: {}".format(error))

def insertPoster(connection, poster, url, movieId):
    downloadImage(url, poster["path"])

    poster["movie_id"] = movieId
    poster["path"] = "posters/" + poster["title"]
    insertStatement(connection, poster, "posters")

def insertTitles(connection, titles, movieId):
    for title in titles:
        title["movie_id"] = movieId
        try:
            insertStatement(connection, title, "titles")

        except mysql.connector.Error as error:
            print("Failed to insert title in MySQL: {}".format(error))
    return

def insertPersons(connection, persons):
    ids = []
    for person in persons:
        result = ""

        try: 
            result = getPersonByName(connection, person["name"])
        except mysql.connector.Error as error:
            print("Failed to get person name in MySQL: {}".format(error))

        if (len(result) == 0):
            try:
                id = insertStatement(connection, person, "persons")
                ids.append(id)

            except mysql.connector.Error as error:
                print("Failed to insert person in MySQL: {}".format(error))
        else:
            ids.append(result[0][0])

    return ids

def insertMoviePerson(connection, moviePersons, movieId, personsIds):
    for i in range(len(moviePersons)):
        moviePerson = moviePersons[i]
        moviePerson["person_id"] = personsIds[i]
        moviePerson["movie_id"] = movieId
        try:
            insertWithoutNamedParam(connection, moviePerson, "movie_person")

        except mysql.connector.Error as error:
            print("Failed to insert movie_person in MySQL: {}".format(error))

def insertLinks(connection, links):
    ids = []
    for link in links:
        try:
            id = insertStatement(connection, link, "links")
            ids.append(id)

        except mysql.connector.Error as error:
            print("Failed to insert link in MySQL: {}".format(error))
    return ids

def insertMovieLink(connection, movieId, LinksId):
    for linkId in LinksId:
        ids = {
            "link_id": linkId,
            "movie_id": movieId
        }
        try:
            insertStatement(connection, ids, "link_movie")
        except mysql.connector.Error as error:
            print("Failed to insert movie_link in MYSQL: {}".format(error))

# Download images

def downloadImage(url, path):
    if (os.path.isfile(path)):
        return

    try:
        res = requests.get(url, stream = True)
    except:
        print("The image couldn\'t be downloaded")
        return
    
    if res.status_code == 200:
        with open(path,'wb') as f:
            shutil.copyfileobj(res.raw, f)
    else:
        print('Image Couldn\'t be retrieved')

# Setup .env
dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

print("-- Retrieving movies from Movix --")

movies = getAllMoviesFromThisMonthToOneYearLater()

print("-- Parse movies --")

movies = parseMovies(movies)

print("-- Init DB --")

initDB()

print("-- Insert all Movies in DB --")

insertAllMovies(movies)

print("-- Done --")
