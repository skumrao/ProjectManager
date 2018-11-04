--1. 
create table student(
     firstname varchar(20) not null, lastname varchar(20), rollno varchar(7) unique,
     email varchar(50) unique, password varchar(15),
     contact bigint(10), student_id varchar(15) primary key);

--2. 
create table course_instructor(
     ci_id varchar(20) primary key,
     firstname varchar(20) NOT NULL,
     lastname varchar(20), 
     email varchar(30) unique,
     password varchar(20),
     dept_name varchar(40) NOT NULL,
     contact bigint(10));

--3. 
create table reviewer(
     user_id varchar(20) primary key,
     firstname varchar(20) not null,
     lastname varchar(20),
     email varchar(40) unique,
     password varchar(20),
     contact bigint(10));

--4. 
create table course(
     course_id varchar(20) primary key,
     course_name varchar(50) not null,
     dept_name varchar(50) not null,
     user_id varchar(20), 
     constraint FK_CI foreign key(user_id) references course_instructor(ci_id));

--5. 
create table project(
     project_id varchar(20) PRIMARY KEY,
     project_name varchar(50) not null,
     project_idea varchar(1000),
     course_id varchar(20),
     constraint FK_C foreign key(course_id) references course(course_id));

--6. 
create table project_reports(
     report varchar(1000) not null,
     project_id varchar(20),
     report_id varchar(20) primary key,
     constraint FK_P foreign key(project_id) references project(project_id));

--7. 
create table teammembers(
     user_id varchar(20),
     project_id varchar(20),
     constraint FK_ST foreign key(user_id) references student(student_id),
     constraint FK_PT foreign key(project_id) references project(project_id));

--8. 
create table review(
     review_id varchar(20) PRIMARY KEY,
     review_content varchar(1000),
     project_id varchar(20),
     reviewer_id varchar(20),
     constraint FK_PR foreign key(project_id) references project(project_id),
     constraint FK_RR foreign key(reviewer_id) references reviewer(user_id));

--9. 
create table project_comment(
     comment varchar(1000),
     project_id varchar(20),
     constraint FK_PC foreign key(project_id) references project(project_id));

--10.
create table review_comment(
     comment varchar(1000),
     review_id varchar(20),
     constraint FK_Review foreign key(review_id) references review(review_id));



