--
-- Table structure for table persons
--

DROP TABLE IF EXISTS persons;
CREATE TABLE persons (
  id bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255)   NOT NULL,
  slug varchar(255)   NOT NULL,
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY persons_name_unique (`name`)
) ;