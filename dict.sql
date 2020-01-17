create table user(
    id int primary key auto_increment,
    name varchar(20) not null,
    passwd char(64) not null
);

create table hist(
    id int primary key auto_increment,
    name varchar(20) not null,
    word varchar(30),
    `time` datetime default now()
);