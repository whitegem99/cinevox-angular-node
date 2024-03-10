--
-- Table structure for table link_movie
--

DROP TABLE IF EXISTS link_movie;
CREATE TABLE link_movie (
  `link_id` bigint unsigned NOT NULL,
  `movie_id` bigint unsigned NOT NULL,
  PRIMARY KEY (link_id,movie_id),
  KEY link_movie_movie_id_foreign (movie_id),
  CONSTRAINT link_movie_link_id_foreign FOREIGN KEY (link_id) REFERENCES links (id),
  CONSTRAINT link_movie_movie_id_foreign FOREIGN KEY (movie_id) REFERENCES movies (id)
) ;