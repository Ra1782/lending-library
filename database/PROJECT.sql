USE project;
CREATE TABLE Admin
(
	AdminId INT AUTO_INCREMENT PRIMARY KEY,
    AName varchar(30),
    Passwd VARCHAR(30)
);
CREATE TABLE Student
(
	StudentId INT AUTO_INCREMENT PRIMARY KEY,
    Passwd VARCHAR(30),
    SName VARCHAR(30),
    Class VARCHAR(7)
);
Alter table book add column AvailableCopies int default 5;
CREATE TABLE Book 
(
	BookId INT AUTO_INCREMENT PRIMARY KEY,
    BName VARCHAR(300),
    Author VARCHAR(30),
    Category VARCHAR(30),
    AvailableCopies int default 5
);
CREATE TABLE Lending
(
	OrderId INT AUTO_INCREMENT PRIMARY KEY,
    SId INT,
    BId INT,
    CONSTRAINT fk_category FOREIGN KEY (SId) REFERENCES Student(StudentId),
    CONSTRAINT fk_categry FOREIGN KEY (BId) REFERENCES Book(BookId),
    BDate DATE,
    RDate DATE,
    Fine INT,
    IsReturned BOOLEAN DEFAULT 0
);
insert into Student(Passwd,SName,Class)
VALUES('bhavesh','Bhavesh','D10');

insert into Student(Passwd,SName,Class)
VALUES('jayesh','Jayesh','D10');

insert into Student(Passwd,SName,Class)
VALUES('dev','Dev','D5');

insert into Student(Passwd,SName,Class)
VALUES('hitesh','Hitesh','D10');

insert into Student(Passwd,SName,Class)
VALUES('megha','Megha','D20');

insert into Student(Passwd,SName,Class)
VALUES('rohit','Rohit','D15');

insert into Student(Passwd,SName,Class)
VALUES('dharkan','Dharkan','D10');

insert into Student(Passwd,SName,Class)
VALUES('dinesh','Dinesh','D10');

insert into Student(Passwd,SName,Class)
VALUES('dhiraj','Dhiraj','D10');

insert into Student(Passwd,SName,Class)
VALUES('ravishankar','Ravishankar','D20');

insert into Book(BName,Author,Category) values('Engineering Mechanics','Prof.M.D. Dayal','SEM-I');
insert into Book(BName,Author,Category) values('Basic Electrical & Electronics Engineering','Ravish Singh','SEM-I');
insert into Book(BName,Author,Category) values('Applied Mathematics 1','Prof.G.V. Kumbhojkar','SEM-I');
insert into Book(BName,Author,Category) values('Applied Physics 1','Dr. I.A.Shaikh(Techmax)','SEM-I');
insert into Book(BName,Author,Category) values('Applied Chemistry','Prof. Keni Sir','SEM-I');
insert into Book(BName,Author,Category) values('Environmental Studies','Parikh J.A','SEM-I');

insert into Book(BName,Author,Category) values('Engineering Drawing','N.H.Dubey','SEM-II');
insert into Book(BName,Author,Category) values('Structured Programming Approach','Prof.Makrand Sir','SEM-II');
insert into Book(BName,Author,Category) values('Applied Mathematics 2','Prof.G.V. Kumbhojkar','SEM-II');
insert into Book(BName,Author,Category) values('Applied Physics 2','Prof. Keni Sir','SEM-II');
insert into Book(BName,Author,Category) values('Applied Chemistry','Prof.V.M. Balsaraf','SEM-II');
insert into Book(BName,Author,Category) values('Communication Skills','Sanyukta Shah Neb','SEM-II');

insert into Book(BName,Author,Category) values('Applied Mathematics 3','Prof.G.V. Kumbhojkar','SEM-III');
insert into Book(BName,Author,Category) values('Data Structure & Algorithm Analysis','Ellis horowitz','SEM-III');
insert into Book(BName,Author,Category) values('Object Oriented Programming Methodology','James Rumbaugh','SEM-III');
insert into Book(BName,Author,Category) values('Logic Design','Anil K. Mani','SEM-III');
insert into Book(BName,Author,Category) values('Database Management System','Korth','SEM-III');
insert into Book(BName,Author,Category) values('Principles of Communication','McGraw Hill','SEM-III');

insert into Book(BName,Author,Category) values('Applied Mathematics 4','Prof.G.V. Kumbhojkar','SEM-IV');
insert into Book(BName,Author,Category) values('Computer Networks','Peterson & Davie','SEM-IV');
insert into Book(BName,Author,Category) values('Computer Organization & Architecture','William Stallings','SEM-IV');
insert into Book(BName,Author,Category) values('Automata Theory','Michael Sipser','SEM-IV');
insert into Book(BName,Author,Category) values('Operating Systom','Vivek V. Jog','SEM-IV');
insert into Book(BName,Author,Category) values('Python','Nageshwar Rao','SEM-IV');

insert into Book(BName,Author,Category) values('Computer Graphics & Virtual Reality','R.K. Maurya','SEM-V');
insert into Book(BName,Author,Category) values('Operating System','Achyut S. Godbole','SEM-V');
insert into Book(BName,Author,Category) values('Microcontroller & Embedded System','Shibu K.V McGraw','SEM-V');
insert into Book(BName,Author,Category) values('Advanced Database Management Systems','Elmasri and Navathe','SEM-V');
insert into Book(BName,Author,Category) values('Open Source Technologies','Ambavade-Dreamtech','SEM-V');
insert into Book(BName,Author,Category) values('Business Communication & Ethics','Dr. K.Alex','SEM-V');

insert into Book(BName,Author,Category) values('Software Engineering','Ian Sommerville','SEM-VI');
insert into Book(BName,Author,Category) values('Distributed System','Andrew S. & Marteen Steen','SEM-VI');
insert into Book(BName,Author,Category) values('System & Web Security','William Stallings','SEM-VI');
insert into Book(BName,Author,Category) values('Data Mining & Business Intelligance','G. Shmueli','SEM-VI');
insert into Book(BName,Author,Category) values('Advanced Internet Technology','WROX press','SEM-VI');

insert into Book(BName,Author,Category) values('Software Project Management','Hughes & Cornell','SEM-VII');
insert into Book(BName,Author,Category) values('Cloud Computing','Rajkumar B. Wiley','SEM-VII');
insert into Book(BName,Author,Category) values('Intelligent System','Stuart Rusell % Peter N','SEM-VII');
insert into Book(BName,Author,Category) values('Wireless Technology','Vijay K.Garg','SEM-VII');
insert into Book(BName,Author,Category) values('Image Processing','S.Shridhar','SEM-VII');
insert into Book(BName,Author,Category) values('Software Architecture','M.Shaw','SEM-VII');
insert into Book(BName,Author,Category) values('E-commerece & E-business','Henry Chan','SEM-VII');

insert into Book(BName,Author,Category) values('Storage Network Management & Retrieval','Robert Spalding','SEM-VIII');
insert into Book(BName,Author,Category) values('Big Data Analytics','Bill Franks','SEM-VIII');
insert into Book(BName,Author,Category) values('Computer Simulation & Modelling','Averill M.Law','SEM-VIII');
insert into Book(BName,Author,Category) values('Enterprice Resource Planning','Alex Leon','SEM-VIII');
insert into Book(BName,Author,Category) values('Wireless Sensor Networks','Edghar H.','SEM-VIII');
insert into Book(BName,Author,Category) values('Geographical Inforamtion Systems','M.N.DeMers','SEM-VIII');


insert into Admin(AName,Passwd) values('Ritik','ritik');
insert into Admin(AName,Passwd) values('Sahil','sahil');
insert into Admin(AName,Passwd) values('Paras','paras');
insert into Admin(AName,Passwd) values('Rohan','rohan');
select * from Admin;
select * from Student;
select * from Book;
insert into Lending(SId ,BId,BDate) Values(2,2,'2020-04-11');
insert into Lending(SId ,BId,BDate) Values(4,9,'2020-04-12');
insert into Lending(SId ,BId,BDate) Values(6,12,'2020-04-12');
insert into project.lending(SId,BId,BDate,RDate,isReturned) values(3,7,'2020-04-10','2020-04-13',1);
insert into project.lending(SId,BId,BDate,RDate,isReturned) values(8,5,'2020-04-10','2020-04-13',1);
select * from lending;
alter table book drop column AvailableCopies;
alter table book add column AvailableCopies int default 5 check(AvailableCopies>=0 );
update book set AvailableCopies=5;


