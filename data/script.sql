DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Assigment;
DROP TABLE IF EXISTS ProfessorNote;
DROP TABLE IF EXISTS StudentNote;


CREATE TABLE User(
  code VARCHAR(255) PRIMARY KEY NOT NULL,
  name VARCHAR(100) NOT NULL,
  role VARCHAR(5) NOT NULL
);


CREATE TABLE Assigment(
  code VARCHAR(255) PRIMARY KEY NOT NULL,
  name VARCHAR(100) NOT NULL  
);


CREATE TABLE ProfessorNote(
  id VARCHAR(255) PRIMARY KEY NOT NULL,
  assigment_name VARCHAR(255) NOT NULL,
  court_1 float,
  court_2 float,
  court_3 float,
  student_code VARCHAR(255) NOT NULL,
  FOREIGN KEY (student_code) REFERENCES User(code)
);


CREATE TABLE StudentNote(
  id VARCHAR(255) PRIMARY KEY NOT NULL,
  assigment_name VARCHAR(255) NOT NULL,
  court_1 float,
  court_2 float,
  court_3 float,
  assigment_code VARCHAR(255) NOT NULL,
  FOREIGN KEY (assigment_code) REFERENCES Assigment(code)
);
