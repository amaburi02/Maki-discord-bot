create database Unit01;
use Unit01;
create table User (
	userID int auto_increment,
	dID varchar(255),
    loveca int,
    bt int,
    primary key (userID)
);
create table Cards (
	cardID int,
    title varchar(255),
    cardset varchar(255),
    rarity varchar(255),
    idol varchar(255),
    img varchar(255),
    idolizedimg varchar(255),
    game varchar(255),
    primary key (cardID)
    );
create table UserCards (
	colID int,
    userID int,
    cardNo int,
    idolized boolean,
    primary key (colID),
    foreign key (userID) references User(userID),
    foreign key (cardNo) references Cards(cardID)
);

insert into User (userID, dID, loveca, bt)
values (1, 60044471485621834, 50, 0);
select * from User;

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (1, "Initial", "Initial", 'N', "Osaka Shizuku", "https://i.schoolido.lu/c/1Shizuku.png", "https://i.schoolido.lu/c/1idolizedShizuku.png", "SIF");
select * from Cards;