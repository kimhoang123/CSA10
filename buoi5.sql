create database school;
use school;

alter database school
read only = 0;

create table students (
	id varchar(12) primary key ,
    email varchar(255) unique not null ,
    firstname varchar(255) not null
);

select *
from students ;

alter table students
add column lastname varchar(100);

alter table students
modify  lastname varchar(100) 
after firstname ;

alter table students
rename column id to student_id;

select *
from students ;

create table classes (
	class_id varchar(12) primary key ,
	title varchar(1000) not null ,
    description varchar(5000) not null
);

select *
from classes ;

--

create table  enrollments(
	enrollment_id varchar(12) primary key,
	student_id varchar(12) not null ,
    class_id varchar(12) not null ,
    constraint foreign key (student_id)
    references students(student_id),
	constraint foreign key (class_id)
    references classes(class_id)
);

select * from enrollments;
-- xoa,sua
drop table classes;
drop table enrollments;

-- tai lai bang enrollment
create table  enrollments(
	enrollment_id varchar(12) primary key,
	student_id varchar(12) not null ,
    class_id varchar(12) not null 
);

alter table enrollments 
add constraint foreign key (student_id)
references students(student_id);

alter table enrollments 
add constraint foreign key (class_id)
references classes(class_id);

-- tao du lieu
insert into student(student_id , firstname , lastname )
values ('000111' , 'Nguyen' , 'Van A');

update students
set email = 'anguyen@gamil.com'
where student_id = '000111';

insert into students
values ('Van B','000112' , 'bnguyen@gamil.com', 'Nguyen' );

select * from students;