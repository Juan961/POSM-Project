DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Professor;
DROP TABLE IF EXISTS Assigment;
DROP TABLE IF EXISTS Note;
DROP TABLE IF EXISTS StudentAssigment;


CREATE TABLE User (
  code VARCHAR(255) PRIMARY KEY,
  name VARCHAR(100) NOT NULL
  role VARCHAR(5) NOT NULL
);


CREATE TABLE Assigment (
  id VARCHAR(255) PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  professor_id VARCHAR(255) NOT NULL,
  FOREIGN KEY (professor_id) REFERENCES User(code)
);


CREATE TABLE StudentAssigment (
  id VARCHAR(255) PRIMARY KEY AUTO_INCREMENT,
  student_id VARCHAR(255) NOT NULL,
  assigment_id VARCHAR(255) NOT NULL,
  FOREIGN KEY (student_id) REFERENCES User(code),
  FOREIGN KEY (assigment_id) REFERENCES Assigment(id)
);

CREATE TABLE Note (
  id VARCHAR(255) PRIMARY KEY AUTO_INCREMENT,
  court_1 float,
  court_2 float,
  court_3 float,
  student_id VARCHAR(255) NOT NULL,
  FOREIGN KEY (student_id) REFERENCES User(code),
  assigment_id VARCHAR(255) NOT NULL,
  FOREIGN KEY (assigment_id) REFERENCES Assigment(id),
);
