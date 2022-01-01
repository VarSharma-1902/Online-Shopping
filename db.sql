use market;
create table customer (
			cname varchar(255),
            dob date,
            gender varchar(10),
            address varchar(300),
            pin int,
            contact int,
            email varchar(255),
            pswd varchar(255));
select * from customer;
select exists (select * from customer where email = 'abc@example.com');
alter table customer modify contact bigint;

create table vegetables (
	item_code varchar(6),
    item_name varchar(30),
    cost int,
    quantity int);

insert into vegetables values ('VEG001', 'Potato', 60, 300);
insert into vegetables values ('VEG002', 'Tomato', 50, 200);
insert into vegetables values ('VEG003', 'Onion', 30, 300);
insert into vegetables values ('VEG004', 'Ladyfingers', 50, 100);
insert into vegetables values ('VEG005', 'Brinjal', 70, 200);
insert into vegetables values ('VEG006', 'Cauliflower', 30, 270);
insert into vegetables values ('VEG007', 'Cabbage', 70, 300);
insert into vegetables values ('VEG008', 'Capsicum', 60, 200);
insert into vegetables values ('VEG009', 'Garlic', 40, 200);
insert into vegetables values ('VEG010', 'Ginger', 30, 200);
insert into vegetables values ('VEG011', 'Cucumber', 50, 250);
insert into vegetables values ('VEG012', 'Mushrooms', 80, 100);    
select * from vegetables;

create table fruits (
	item_code varchar(6),
    item_name varchar(30),
    cost int,
    quantity int);
insert into fruits values ('FRU001', 'Apple', 40, 200);
insert into fruits values ('FRU002', 'Banana', 20, 200);
insert into fruits values ('FRU003', 'Watermelon', 30, 200);
insert into fruits values ('FRU004', 'Muskmelon', 50, 200);
insert into fruits values ('FRU005', 'Grapes', 30, 200);
insert into fruits values ('FRU006', 'Pomegranate', 60, 200);
insert into fruits values ('FRU007', 'Mango', 40, 200);

create table bodycare (
	item_code varchar(6),
    item_name varchar(30),
    cost int,
    quantity int);
insert into bodycare values('BCP001', 'Talcum Powder', 140, 150);
insert into bodycare values('BCP002', 'Bodywash', 200, 150);
insert into bodycare values('BCP003', 'Soap', 160, 150);
insert into bodycare values('BCP004', 'Body Lotion', 470, 150);
insert into bodycare values('BCP005', 'Sunscreen', 550, 150);
insert into bodycare values('BCP006', 'Deodrants', 340, 150);
insert into bodycare values('BCP007', 'Shaving Cream', 250, 150);
insert into bodycare values('BCP008', 'Face Cream', 150, 150);

create table oralcare (
	item_code varchar(6),
    item_name varchar(30),
    cost int,
    quantity int);
insert into oralcare values('OCP001', 'Electric Toothbrush', 1300, 800);
insert into oralcare values('OCP002', 'Manual Toothbrush', 125, 800);
insert into oralcare values('OCP003', 'Toothpaste', 500, 800);
insert into oralcare values('OCP004', 'Dental Floss', 1100, 800);
insert into oralcare values('OCP005', 'Mouthwash', 270, 800);
drop table oralcare;

create table haircare (
	item_code varchar(6),
    item_name varchar(30),
    cost int);
insert into haircare values ('HCP001', 'Shampoo', 120);
insert into haircare values ('HCP002', 'Conditioner', 500);
insert into haircare values ('HCP003', 'Hair Colour', 423);
insert into haircare values ('HCP004', 'Hair Brush', 475);
insert into haircare values ('HCP005', 'Hair Comb', 160);
insert into haircare values ('HCP006', 'Hair Oil', 125);

create table snacks (
	item_code varchar(6),
    item_name varchar(30),
    cost int);
    
insert into snacks values ('SAF001', 'Chips', 10);
insert into snacks values ('SAF002', 'Cookies', 50);
insert into snacks values ('SAF003', 'Chocolates', 15);
insert into snacks values ('SAF004', 'Biscuits', 25);
insert into snacks values ('SAF005', 'Cornflakes', 320);
insert into snacks values ('SAF006', 'Juice', 99);
insert into snacks values ('SAF007', 'Popcorn', 29);

create table stationery (
	item_code varchar(6),
    item_name varchar(30),
    cost int);

insert into stationery values ('SAF001', 'Pens', 30);
insert into stationery values ('SAF002', 'Notebooks', 20);
insert into stationery values ('SAF003', 'Writing Pad', 10);
insert into stationery values ('SAF004', 'Adhesive', 396);
insert into stationery values ('SAF005', 'Files and Folders', 200);
insert into stationery values ('SAF006', 'Calculator', 420);
insert into stationery values ('SAF007', 'Highlighters and Markers', 99);
insert into stationery values ('SAF008', 'Scissors', 40);
insert into stationery values ('SAF009', 'Stapler', 275);
insert into stationery values ('SAF010', 'Pencils', 40);
insert into stationery values ('SAF011', 'Erasers', 50);
insert into stationery values ('SAF012', 'Sketch Pens', 82);
insert into stationery values ('SAF013', 'Water Colours', 70);
insert into stationery values ('SAF014', 'Crayons', 350);
insert into stationery values ('SAF015', 'Paper Cutter', 30);

select * from customer;


    

