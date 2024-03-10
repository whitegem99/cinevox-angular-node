--
-- Table structure for table links
--

DROP TABLE IF EXISTS links;
CREATE TABLE links (
  id bigint unsigned NOT NULL AUTO_INCREMENT,
  title varchar(255) NOT NULL,
  `type` varchar(10) NOT NULL DEFAULT 'trailer',
  `url` varchar(255) NOT NULL,
  `language` varchar(10) NOT NULL DEFAULT 'en',
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL,
  PRIMARY KEY (id)
) ;