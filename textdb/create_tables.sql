CREATE TABLE PUBLICATIONS (
  PID int NOT NULL,
  AUTHOR varchar(100) DEFAULT NULL,
  TITLE varchar(100) DEFAULT NULL,
  PUBDATE date DEFAULT NULL,
  ISBN varchar(14) DEFAULT NULL,
  URL varchar(100) DEFAULT NULL,
  PRIMARY KEY (PID)
);

CREATE TABLE TEXTS (
  BODY mediumtext,
  PUBID int DEFAULT NULL,
  KEY PUBID (PUBID),
  FULLTEXT KEY BODY (BODY),
  CONSTRAINT TEXTS_ibfk_1 FOREIGN KEY (PUBID) REFERENCES PUBLICATIONS (PID)
);