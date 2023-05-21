DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Note;

CREATE TABLE User(
  code VARCHAR(255) PRIMARY KEY NOT NULL,
  name VARCHAR(100) NOT NULL,
  role VARCHAR(5) NOT NULL
);

CREATE TABLE Note(
  id VARCHAR(255) PRIMARY KEY NOT NULL,
  assigment_name VARCHAR(255) NOT NULL,
  court_1 float,
  court_2 float,
  court_3 float,
  student_code VARCHAR(255) NOT NULL,
  FOREIGN KEY (student_code) REFERENCES User(code)
);
