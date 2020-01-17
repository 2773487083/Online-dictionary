# author : bjq
# email : 2773487083@qq.com
# env : python3.6
# 建立数据库

# 创建数据库
create database dict charset = utf8;
# 创建单词表
create table `words`
(
    `id`   int(11) PRIMARY KEY auto_increment,
    `word` varchar(50) default null,
    `mean` text,
    KEY `word_index` (`word`)
);
# 创建用户表
create table user
(
    id     int primary key auto_increment,
    name   varchar(20) not null,
    passwd char(64)    not null
);
# 创建查询记录表
create table hist
(
    id     int primary key auto_increment,
    name   varchar(20) not null,
    word   varchar(30),
    `time` datetime default now()
);