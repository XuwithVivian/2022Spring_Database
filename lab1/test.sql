create database test;
use test;
#drop table tab1;
create table tab1 (
ID int not null,
name varchar(10)
);
insert into tab1 (ID, name) values (1, 'aaa');
insert into tab1 (ID, name) values (2, 'bbb');
insert into tab1 (ID, name) values (3, 'ccc');
select ID from tab1;