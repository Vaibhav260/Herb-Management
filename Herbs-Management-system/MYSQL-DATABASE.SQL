Herbs-Management-system
Create database herbm;
Use herbm



Create table admin(
admin_id int auto_increment,
admin_name varchar(30),
admin_pass  varchar(8),
Primary key (admin_id)
);


alter table admin auto_increment=100001; create table Herbs (
herb_id int auto_increment,
common_name varchar(50),
botanical_name varchar(50),
uses varchar(200),
quantity_in_stock int(5),
country_of_origin varchar(30),
herb_price int(5),
Primary key(herb_id)
);
alter table herbs auto_increment=101;

create table orders(
order_id int auto_increment,
order_date date,
total_price int(10),
customer_id int,
primary key(order_id)
);
 create table customer (
customer_id int(10),
customer_name varchar(10),
customer_pass varchar(10),
customer_address varchar(10),
customer_region varchar(50),
primary key(customer_id)
); 
create table monitors(
customer_id int(10),
order_id int,
primary key(customer_id, order_id)
);

create table contain (
order_herb_id int not null auto_increment,
herb_id int,
order_id int,
quantity_ordered int(10),
primary key(order_herb_id)
 );

insert into contain(herb_id, order_id, quantity_ordered) values(101,1002,3),
(103, 1004, 10),
(102, 1002, 13),
(103, 1005, 17),
(101, 1001, 20);
alter table contain auto_increment=10;
insert into customer (customer_id,customer_name,customer_pass,customer_address,customer_region)
values("1","Rishabh","1234","Miraroad","India");

insert into customer(customer_id,customer_name,customer_pass,customer_address,customer_region)
values("2","Vaibhav","2345","Pratapgarh","India");

insert into customer(customer_id,customer_name,customer_pass,customer_address,customer_region)
values("3","Abhishek","1235","Ambala","India");

alter table orders auto_increment=1001;
insert into orders(order_date, total_price, customer_id) values('2021-03-25',500,3),
('2021-03-26',800,1),
('2021-03-27',700,2),
('2021-03-28',1000,1),
('2021-03-29',1200,1);

insert into Herbs (common_name, botanical_name, uses, Quantity_in_Stock,country_of_origin, herb_price)
values('Kaith','Acacia','digestive','78','All','37');

insert into Herbs (common_name, botanical_name, uses, Quantity_in_Stock,country_of_origin, herb_price)
values ('Atis','Aconitum Heterophyllum','Anti-diabetic','4','Uttranchal Himachal Pradesh','1209');

insert into Herbs (common_name, botanical_name, uses, Quantity_in_Stock,country_of_origin, herb_price)
values ('Gurbaj','Acorus calamus','Aromatic','6','Himachal Pradesh','30');



alter table orders add constraint places foreign key (customer_id) references customer (customer_id) on update cascade on delete cascade;
alter table monitors add constraint mon_emp foreign key (customer_id) references customer(customer_id) on update cascade on delete cascade;
alter table monitors add constraint mon_ord foreign key (order_id) references orders (order_id) on update cascade on delete cascade;
alter table contain add constraint con_item foreign key (herb_id) references herbs (herb_id) on update cascade on delete cascade;
alter table contain add constraint con_order foreign key (order_id) references orders (order_id) on update cascade on delete cascade;
insert into admin (admin_name,admin_pass) values("Rohit","admin");
insert into admin (admin_name,admin_pass) values("Virat","abcd");
insert into admin (admin_name,admin_pass) values("Dhoni","xyz");


