CREATE TABLE [studenttable] (
  [student_Id] Varchar(255),
  [student_name] Varchar(255),
  PRIMARY KEY ([student_Id])
);

CREATE TABLE [professor] (
  [professor_id] Varchar(255),
  [professor_name] Varchar(255),
  [department] Varchar(255),
  PRIMARY KEY ([professor_id])
);

CREATE TABLE [Course] (
  [course_id] Varchar(255),
  [course_name] Varchar(255),
  [professor_id] Varchar(255),
  PRIMARY KEY ([course_id]),
  Foreign key([professor_id]) references professor([professor_id])
  --ON DELETE CASCADE --Prof - delete course deletes
);

CREATE TABLE [Enrollment] (
  [enroll_id] Varchar(255),
  [student_id] Varchar(255),
  [course_id] Varchar(255),
  PRIMARY KEY ([enroll_id]),
  Foreign key([course_id]) references Course([course_id]),
  Foreign key([student_id]) references studenttable([student_Id])
);

insert into professor values ('P001','Dr. Brown','Mathematics'),
('P002','Dr. Smith','Physics');

insert into studenttable values ('S001','Alice'),
('S002','Bob'),
('S003','Charlie');

select * from professor;
select * from studenttable;

insert into Course values ('C001','Math 101','P001'),
('C002','Physics 101','P002');

INSERT INTO Enrollment (enroll_id, course_id, student_id)
VALUES ('E001', 'C001', 'S001'),
       ('E002', 'C002', 'S002'),
       ('E003', 'C002', 'S001'),
       ('E004', 'C001', 'S003');

