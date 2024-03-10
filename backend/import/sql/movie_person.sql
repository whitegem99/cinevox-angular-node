--
-- Table structure for table movie_person
--

DROP TABLE IF EXISTS movie_person;
CREATE TABLE movie_person (
  `character` varchar(255)   NOT NULL DEFAULT '-',
  credit varchar(10)   NOT NULL DEFAULT 'actor',
  `person_id` bigint unsigned NOT NULL,
  `movie_id` bigint unsigned NOT NULL,
  PRIMARY KEY (person_id,movie_id,credit,`character`),
  KEY movie_person_movie_id_foreign (movie_id),
  CONSTRAINT movie_person_movie_id_foreign FOREIGN KEY (movie_id) REFERENCES movies (id),
  CONSTRAINT movie_person_person_id_foreign FOREIGN KEY (person_id) REFERENCES persons (id)
) ;