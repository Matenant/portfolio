DROP TABLE IF EXISTS experience_technologie;

DROP TABLE IF EXISTS technologie;

DROP TABLE IF EXISTS remarque;

DROP TABLE IF EXISTS experience;

DROP TABLE IF EXISTS categorie;

CREATE TABLE categorie (
    categorie_id int auto_increment,
    primary key(categorie_id),
    created timestamp default current_timestamp,
    modified timestamp default current_timestamp,
    titre varchar(255) not null,
    ordre int,
    visible bool default true
);


CREATE TABLE experience (
    experience_id int auto_increment,
    categorie_id int,
    created timestamp default current_timestamp,
    modified timestamp default current_timestamp,
    titre varchar(255) not null,
    ordre int,
    visible bool default true,
    primary key(experience_id),
    foreign key(categorie_id) references categorie(categorie_id)
);


CREATE TABLE technologie (
    technologie_id int auto_increment,
    created timestamp default current_timestamp,
    modified timestamp default current_timestamp,
    titre varchar(255) not null,
    primary key(technologie_id)
);


CREATE TABLE experience_technologie (
    experience_technologie_id int auto_increment,
    primary key(experience_technologie_id),
    experience_id int not null,
    foreign key(experience_id) references experience(experience_id),
    technologie_id int not null,
    foreign key(technologie_id) references technologie(technologie_id)
);


CREATE TABLE remarque (
    remarque_id int auto_increment,
    primary key(remarque_id),
    created timestamp default current_timestamp,
    modified timestamp default current_timestamp,
    remarque varchar(255) not null,
    experience_id int not null,
    foreign key(experience_id) references experience(experience_id)
);

DROP TABLE IF EXISTS contact;
DROP TABLE IF EXISTS sujet;

CREATE TABLE sujet (
    sujet_id int auto_increment,
    primary key(sujet_id),
    created timestamp default current_timestamp,
    modified timestamp default current_timestamp,
    sujet varchar(255) not null
);

CREATE TABLE contact (
    contact_id int auto_increment,
    primary key(contact_id),
    created timestamp default current_timestamp,
    modified timestamp default current_timestamp,
    sujet_id int not null,
    foreign key(sujet_id) references sujet(sujet_id),
    soussujet varchar(255) not null default "",
    description varchar(255) not null,
    mail varchar(255) not null
);