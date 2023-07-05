create database Unit01;
use Unit01;
create table User (
	userID varchar(255),
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

insert into User (userID, loveca, bt)
values (600444714856218634, 50, 0);
select * from User;

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (1, "Initial", "Initial", 'N', "Osaka Shizuku", "https://i.schoolido.lu/c/1Shizuku.png", "https://i.schoolido.lu/c/1idolizedShizuku.png", "SIF");
select * from Cards;

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (2, "Initial", "Initial", 'N', "Miyashita Coco", "https://i.schoolido.lu/c/2Coco.png", "https://i.schoolido.lu/c/2idolizedCoco.png", "SIF"),
(3, "Initial", "Initial", 'N', "Aizawa Yuu", "https://i.schoolido.lu/c/3Yuu.png", "https://i.schoolido.lu/c/3idolizedYuu.png", "SIF"),
(4, "Initial", "Initial", 'N', "Ichinose Marika", "https://i.schoolido.lu/c/4Marika.png", "https://i.schoolido.lu/c/4idolizedMarika.png", "SIF"),
(5, "Initial", "Initial", 'N', "Yuuki Sana", "https://i.schoolido.lu/c/5Sana.png", "https://i.schoolido.lu/c/5idolizedSana.png", "SIF"),
(6, "Initial", "Initial", 'N', "Nishimura Fumie", "https://i.schoolido.lu/c/6Fumie.png", "https://i.schoolido.lu/c/6idolizedFumie.png", "SIF"),
(7, "Initial", "Initial", 'N', "Nagayama Minami", "https://i.schoolido.lu/c/7Minami.png", "https://i.schoolido.lu/c/7idolizedMinami.png", "SIF"),
(8, "Initial", "Initial", 'N', "Christina", "https://i.schoolido.lu/c/8Christina.png", "https://i.schoolido.lu/c/8idolizedChristina.png", "SIF"),
(9, "Initial", "Initial", 'N', "Kikuchi Akemi", "https://i.schoolido.lu/c/9Akemi.png", "https://i.schoolido.lu/c/9idolizedAkemi.png", "SIF"),
(10, "Initial", "Initial", 'N', "Suda Iruka", "https://i.schoolido.lu/c/10Iruka.png", "https://i.schoolido.lu/c/10idolizedIruka.png", "SIF"),
(11, "Initial", "Initial", 'N', "Sugisaki Aya", "https://i.schoolido.lu/c/11Aya.png", "https://i.schoolido.lu/c/11idolizedAya.png", "SIF"),
(12, "Initial", "Initial", 'N', "Midou Yuuri", "https://i.schoolido.lu/c/12Yuuri.png", "https://i.schoolido.lu/c/12idolizedYuuri.png", "SIF"),
(13, "Initial", "Initial", 'N', "Saeki Reine", "https://i.schoolido.lu/c/13Reine.png", "https://i.schoolido.lu/c/13idolizedReine.png", "SIF"),
(14, "Initial", "Initial", 'N', "Torii Ayumi", "https://i.schoolido.lu/c/14Ayumi.png", "https://i.schoolido.lu/c/14idolizedAyumi.png", "SIF"),
(15, "Initial", "Initial", 'N', "Kamiya Rika", "https://i.schoolido.lu/c/15Rika.png", "https://i.schoolido.lu/c/15idolizedRika.png", "SIF"),
(16, "Initial", "Initial", 'N', "Morishima Nanaka", "https://i.schoolido.lu/c/16Nanaka.png", "https://i.schoolido.lu/c/16idolizedNanaka.png", "SIF"),
(17, "Initial", "Initial", 'N', "Kujou Seira", "https://i.schoolido.lu/c/17Seira.png", "https://i.schoolido.lu/c/17idolizedSeira.png", "SIF"),
(18, "Initial", "Initial", 'N', "Konoe Kanata", "https://i.schoolido.lu/c/18Kanata.png", "https://i.schoolido.lu/c/18idolizedKanata.png", "SIF"),
(19, "Initial", "Initial", 'N', "Konoe Haruka", "https://i.schoolido.lu/c/19Haruka.png", "https://i.schoolido.lu/c/19idolizedHaruka.png", "SIF"),
(20, "Initial", "Initial", 'N', "Shimozono Saki", "https://i.schoolido.lu/c/20Saki.png", "https://i.schoolido.lu/c/20idolizedSaki.png", "SIF"),
(21, "Initial", "Initial", 'N', "Tanaka Sachiko", "https://i.schoolido.lu/c/21Sachiko.png", "https://i.schoolido.lu/c/21idolizedSachiko.png", "SIF"),
(22, "Initial", "Initial", 'N', "Hasekura Kasane", "https://i.schoolido.lu/c/22Kasane.png", "https://i.schoolido.lu/c/22idolizedKasane.png", "SIF"),
(23, "Initial", "Initial", 'N', "Tatara Ruu", "https://i.schoolido.lu/c/23Ruu.png", "https://i.schoolido.lu/c/23idolizedRuu.png", "SIF"),
(24, "Initial", "Initial", 'N', "Shinomiya Akiru", "https://i.schoolido.lu/c/24Akiru.png", "https://i.schoolido.lu/c/24idolizedAkiru.png", "SIF"),
(25, "Initial", "Initial", 'N', "Kikkawa Mizuki", "https://i.schoolido.lu/c/25Mizuki.png", "https://i.schoolido.lu/c/25idolizedMizuki.png", "SIF"),
(26, "Initial", "Initial", 'N', "Shiraki Nagi", "https://i.schoolido.lu/c/26Nagi.png", "https://i.schoolido.lu/c/26idolizedNagi.png", "SIF"),
(27, "Initial", "Initial", 'N', "Fujishiro Yumi", "https://i.schoolido.lu/c/27Yumi.png", "https://i.schoolido.lu/c/27idolizedYumi.png", "SIF");

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (28, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Kosaka Honoka", "https://i.schoolido.lu/c/28Honoka.png", "https://i.schoolido.lu/c/28idolizedHonoka.png", "SIF"),
(29, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Ayase Eli", "https://i.schoolido.lu/c/29Eli.png", "https://i.schoolido.lu/c/29idolizedEli.png", "SIF"),
(30, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Minami Kotori", "https://i.schoolido.lu/c/30Kotori.png", "https://i.schoolido.lu/c/30idolizedKotori.png", "SIF"),
(31, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Sonoda Umi", "https://i.schoolido.lu/c/31Umi.png", "https://i.schoolido.lu/c/31idolizedUmi.png", "SIF"),
(32, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Hoshizora Rin", "https://i.schoolido.lu/c/32Rin.png", "https://i.schoolido.lu/c/32idolizedRin.png", "SIF"),
(33, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Nishikino Maki", "https://i.schoolido.lu/c/33Maki.png", "https://i.schoolido.lu/c/33idolizedMaki.png", "SIF"),
(34, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Tojo Nozomi", "https://i.schoolido.lu/c/34Nozomi.png", "https://i.schoolido.lu/c/34idolizedNozomi.png", "SIF"),
(35, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Koizumi Hanayo", "https://i.schoolido.lu/c/35Hanayo.png", "https://i.schoolido.lu/c/35idolizedHanayo.png", "SIF"),
(36, "Initial", "Natsuiro Egao de 1, 2, Jump!", 'R', "Yazawa Nico", "https://i.schoolido.lu/c/36Nico.png", "https://i.schoolido.lu/c/36idolizedNico.png", "SIF");

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (37, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Kosaka Honoka", "https://i.schoolido.lu/c/37Honoka.png", "https://i.schoolido.lu/c/37idolizedHonoka.png", "SIF"),
(38, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Ayase Eli", "https://i.schoolido.lu/c/38Eli.png", "https://i.schoolido.lu/c/38idolizedEli.png", "SIF"),
(39, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Minami Kotori", "https://i.schoolido.lu/c/39Kotori.png", "https://i.schoolido.lu/c/39idolizedKotori.png", "SIF"),
(40, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Sonoda Umi", "https://i.schoolido.lu/c/40Umi.png", "https://i.schoolido.lu/c/40idolizedUmi.png", "SIF"),
(41, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Hoshizora Rin", "https://i.schoolido.lu/c/41Rin.png", "https://i.schoolido.lu/c/41idolizedRin.png", "SIF"),
(42, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Nishikino Maki", "https://i.schoolido.lu/c/42Maki.png", "https://i.schoolido.lu/c/42idolizedMaki.png", "SIF"),
(43, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Tojo Nozomi", "https://i.schoolido.lu/c/43Nozomi.png", "https://i.schoolido.lu/c/43idolizedNozomi.png", "SIF"),
(44, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Koizumi Hanayo", "https://i.schoolido.lu/c/44Hanayo.png", "https://i.schoolido.lu/c/44idolizedHanayo.png", "SIF"),
(45, "Initial", "Mogyutto 'love' de Sekkinchuu!", 'R', "Yazawa Nico", "https://i.schoolido.lu/c/45Nico.png", "https://i.schoolido.lu/c/45idolizedNico.png", "SIF");

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (46, "Initial", "Wonderful Rush", 'R', "Kosaka Honoka", "https://i.schoolido.lu/c/46Honoka.png", "https://i.schoolido.lu/c/46idolizedHonoka.png", "SIF"),
(47, "Initial", "Wonderful Rush", 'R', "Ayase Eli", "https://i.schoolido.lu/c/47Eli.png", "https://i.schoolido.lu/c/47idolizedEli.png", "SIF"),
(48, "Initial", "Wonderful Rush", 'R', "Minami Kotori", "https://i.schoolido.lu/c/48Kotori.png", "https://i.schoolido.lu/c/48idolizedKotori.png", "SIF"),
(49, "Initial", "Wonderful Rush", 'R', "Sonoda Umi", "https://i.schoolido.lu/c/49Umi.png", "https://i.schoolido.lu/c/49idolizedUmi.png", "SIF"),
(50, "Initial", "Wonderful Rush", 'R', "Hoshizora Rin", "https://i.schoolido.lu/c/50Rin.png", "https://i.schoolido.lu/c/50idolizedRin.png", "SIF"),
(51, "Initial", "Wonderful Rush", 'R', "Nishikino Maki", "https://i.schoolido.lu/c/51Maki.png", "https://i.schoolido.lu/c/51idolizedMaki.png", "SIF"),
(52, "Initial", "Wonderful Rush", 'R', "Tojo Nozomi", "https://i.schoolido.lu/c/52Nozomi.png", "https://i.schoolido.lu/c/52idolizedNozomi.png", "SIF"),
(53, "Initial", "Wonderful Rush", 'R', "Koizumi Hanayo", "https://i.schoolido.lu/c/53Hanayo.png", "https://i.schoolido.lu/c/53idolizedHanayo.png", "SIF"),
(54, "Initial", "Wonderful Rush", 'R', "Yazawa Nico", "https://i.schoolido.lu/c/54Nico.png", "https://i.schoolido.lu/c/54idolizedNico.png", "SIF");

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (55, "笑顔全開！", "Initial", 'SR', "Kosaka Honoka", "https://i.schoolido.lu/c/55Honoka.png", "https://i.schoolido.lu/c/55idolizedHonoka.png", "SIF"),
(56, "ハラショー♪", "Initial", 'SR', "Ayase Eli", "https://i.schoolido.lu/c/56Eli.png", "https://i.schoolido.lu/c/56idolizedEli.png", "SIF"),
(57, "癒しの女神", "Initial", 'SR', "Minami Kotori", "https://i.schoolido.lu/c/57Kotori.png", "https://i.schoolido.lu/c/57idolizedKotori.png", "SIF"),
(58, "精神統一", "Initial", 'SR', "Sonoda Umi", "https://i.schoolido.lu/c/58Umi.png", "https://i.schoolido.lu/c/58idolizedUmi.png", "SIF"),
(59, "μ'ｓの元気印", "Initial", 'SR', "Hoshizora Rin", "https://i.schoolido.lu/c/59Rin.png", "https://i.schoolido.lu/c/59idolizedRin.png", "SIF"),
(60, "放課後の歌姫", "Initial", 'SR', "Nishikino Maki", "https://i.schoolido.lu/c/60Maki.png", "https://i.schoolido.lu/c/60idolizedMaki.png", "SIF"),
(61, "スピリチュアルパワー", "Initial", 'SR', "Tojo Nozomi", "https://i.schoolido.lu/c/61Nozomi.png", "https://i.schoolido.lu/c/61idolizedNozomi.png", "SIF"),
(62, "炊き立てご飯です♪", "Initial", 'SR', "Koizumi Hanayo", "https://i.schoolido.lu/c/62Hanayo.png", "https://i.schoolido.lu/c/62idolizedHanayo.png", "SIF"),
(63, "にっこにっこにー", "Initial", 'SR', "Yazawa Nico", "https://i.schoolido.lu/c/63Nico.png", "https://i.schoolido.lu/c/63idolizedNico.png", "SIF");

insert into Cards (cardID, title, cardset, rarity, idol, img, idolizedimg, game)
values (64, "アイドルへの想い", "Initial", 'UR', "Koizumi Hanayo", "https://i.schoolido.lu/c/64Hanayo.png", "https://i.schoolido.lu/c/64idolizedHanayo.png", "SIF"),
(65, "リズミカルチャーム", "Season 1 BD Bonus", 'UR', "Kosaka Honoka", null, "https://i.schoolido.lu/c/65idolizedHonoka.png", "SIF"),
(66, "小悪魔ガール", "Initial", 'UR', "Yazawa Nico", "https://i.schoolido.lu/c/66Nico.png", "https://i.schoolido.lu/c/66idolizedNico.png", "SIF"),
(67, "リズミカルエール", "Season 1 BD Bonus", 'UR', "Minami Kotori", null, "https://i.schoolido.lu/c/67idolizedKotori.png", "SIF"),
(68, "パーフェクトチャーム", "Season 1 BD Bonus", 'UR', "Sonoda Umi", null, "https://i.schoolido.lu/c/68idolizedUmi.png", "SIF");