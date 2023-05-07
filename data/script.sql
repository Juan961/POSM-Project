DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Professor;
DROP TABLE IF EXISTS Assigment;
DROP TABLE IF EXISTS Note;
DROP TABLE IF EXISTS StudentAssigment;

CREATE TABLE Student (
  id VARCHAR(255) PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);


CREATE TABLE Professor (
  id VARCHAR(255) PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);


CREATE TABLE Assigment (
  id VARCHAR(255) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  professor_id VARCHAR(255) NOT NULL,
  FOREIGN KEY (professor_id) REFERENCES Professor(id)
);


CREATE TABLE Note (
  id VARCHAR(255) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  professor_id VARCHAR(255) NOT NULL,
  FOREIGN KEY (professor_id) REFERENCES Professor(id)
);


CREATE TABLE StudentAssigment (
  id VARCHAR(255) PRIMARY KEY,
  student_id VARCHAR(255) NOT NULL,
  assigment_id VARCHAR(255) NOT NULL,
  FOREIGN KEY (student_id) REFERENCES Student(id),
  FOREIGN KEY (assigment_id) REFERENCES Assigment(id)
);
