--
-- Table structure for table titles
--

DROP TABLE IF EXISTS titles;
CREATE TABLE titles (
  id bigint unsigned NOT NULL AUTO_INCREMENT,
  title varchar(255)   NOT NULL,
  `language` varchar(20)   NOT NULL DEFAULT 'nl',
  movie_id bigint unsigned NOT NULL,
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL,
  PRIMARY KEY (id),
  KEY titles_movie_id_foreign (movie_id),
  CONSTRAINT titles_movie_id_foreign FOREIGN KEY (movie_id) REFERENCES movies (id)
) ;