CREATE DATABASE pytocrudphp;

CREATE TABLE person (
  pid int(11) NOT NULL AUTO_INCREMENT,
  name varchar(50),
  description varchar(50),
  mjid int(11),
  mnid int(11),
  sjid varchar(100),
  sex varchar(10),
  blood varchar(10),
  color varchar(100),
  biography text,
  PRIMARY KEY (pid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE major (
  mjid int(11) NOT NULL AUTO_INCREMENT,
  mjname varchar(50),
  PRIMARY KEY (mjid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE minor (
  mnid int(11) NOT NULL AUTO_INCREMENT,
  mnname varchar(50),
  PRIMARY KEY (mnid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE subject (
  sjid int(11) NOT NULL AUTO_INCREMENT,
  sjname varchar(50),
  PRIMARY KEY (sjid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO person (pid, name, description, mjid, mnid, sjid, sex, blood, color, biography) VALUES
(1, 'John', 'A ME student.', 2, 4, '1,2,5', '1', 'o', 'green,blue', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
(2, 'Jane', 'An ART student.', 3, 5, '3,4', '2', 'ab', 'red,green', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.');

INSERT INTO major (mjname) VALUES
('Science and Technology'),
('Engineering'),
('Arts');

INSERT INTO minor (mnname) VALUES
('Computer Science'),
('Information Technology'),
('Industrial Engineering'),
('Mechanical Engineering'),
('Philosophy'),
('History');

INSERT INTO subject (sjname) VALUES
('Mathematics'),
('Science'),
('Art'),
('English'),
('Computer');
