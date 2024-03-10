--
-- Table structure for table posters
--

DROP TABLE IF EXISTS posters;
CREATE TABLE posters (
  id bigint unsigned NOT NULL AUTO_INCREMENT,
  title varchar(255)   NOT NULL,
  `path` varchar(255)   NOT NULL,
  `type` varchar(255)   NOT NULL DEFAULT 'poster',
  aspect double(4,2) NOT NULL DEFAULT 1.00,
  movie_id bigint unsigned NOT NULL,
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL,
  PRIMARY KEY (id),
  KEY posters_movie_id_foreign (movie_id),
  CONSTRAINT posters_movie_id_foreign FOREIGN KEY (movie_id) REFERENCES movies (id)
) ;