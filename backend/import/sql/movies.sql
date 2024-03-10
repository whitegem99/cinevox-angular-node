--
-- Table structure for table movies
--

DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
  id bigint unsigned NOT NULL AUTO_INCREMENT,
  cinematek_number bigint DEFAULT NULL,
  cinematek_bib_id varchar(255) DEFAULT NULL,
  `title_original` varchar(255) NOT NULL,
  trailer varchar(255),
  slug varchar(255) NOT NULL,
  `month` int NOT NULL,
  release_date varchar(255)   NOT NULL,
  countries varchar(255)   NOT NULL DEFAULT 'Belgium',
  languages varchar(255)   NOT NULL DEFAULT 'nl',
  color tinyint(1) NOT NULL DEFAULT 1,
  color_raw varchar(4)   NOT NULL DEFAULT 'C',
  sound tinyint(1) NOT NULL DEFAULT 1,
  synopsis_nl text  ,
  synopsis_fr text  ,
  synopsis_en text  ,
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY movies_slug_unique (slug),
  UNIQUE KEY movies_cinematek_bib_id_unique (cinematek_bib_id)
) ;