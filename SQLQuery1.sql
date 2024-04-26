CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    commission DECIMAL(4, 2)
);

select * from salesman ; 


INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen', NULL, 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);

-- Task 1
-- Find the average commision of a salesman from Paris

select avg(commission) as AvgCommission from salesman where city = 'Paris' ; 

-- Task 2
-- Find out if there are cities with only one salesman and list them

select city from salesman where city is not null group by city having count(city) < 2;

-- Task 3
-- To find the maximum commission in each city

select salesman.name, salesman.city, salesman.commission 
from salesman inner join 
(select city, max(commission) as maxcom 
from salesman where city is not null  group by city) 
as commtable on salesman.city = commtable.city and salesman.commission = commtable.maxcom ; 

CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);
 
 
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.5, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70004, 110.5, '2012-08-17', 3009, 5003),
(70007, 948.5, '2012-09-10', 3005, 5002),
(70005, 2400.6, '2012-07-27', 3007, 5001),
(70008, 5760, '2012-09-10', 3002, 5001),
(70010, 1983.43, '2012-10-10', 3004, 5006),
(70003, 2480.4, '2012-10-10', 3009, 5003),
(70012, 250.45, '2012-06-27', 3008, 5002),
(70011, 75.29, '2012-08-17', 3003, 5007),
(70013, 3045.6, '2012-04-25', 3002, 5001);

--Task 4 Sub query
-- Display all the orders from the orders table issued by Paul Adam

select * from orders where salesman_id = ( select salesman_id from salesman where name = 'Paul Adam' ) ;


--Task 5 
-- write a query to display all the orders which values are greater than the average order value for 10th october 2012 

select * from orders where purch_amt > ( select avg(purch_amt) from orders where ord_date = '2012-10-10' );

--Task 6
-- Query to find all orders with order amounts which are above average amounts for their customers

select customer_id, avg(purch_amt) from orders group by customer_id;

select * from orders inner join 
(select customer_id, avg(purch_amt) as avgg from orders i group by customer_id) 
as avgtable on orders.customer_id = avgtable.customer_id where orders.purch_amt > avgtable.avgg; 

select * from orders o 
where purch_amt > (select avg(purch_amt)
					from orders i where o.customer_id = i.customer_id) ;

--Task 7
-- Query to find all orders attributed to a salesamn in Paris

select * from orders;
select * from salesman;

select * from orders o 
where salesman_id = (select 
						salesman_id from salesman i where city = 'Paris' 
						and o.salesman_id = i.salesman_id); 

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT NULL,
    salesman_id INT
);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', NULL, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, 5003),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidor', 'Moscow', 200, 5007);

-- Task 8 
-- Write a query to find the name and id of all salesmen who had more than one customer

select * from salesman;
select * from customer;

select salesman_id from customer group by salesman_id having count(customer_id)>1;

--method 1
select salesman_id, name from salesman o where 
salesman_id = (select salesman_id from customer i 
group by salesman_id having count(customer_id)>1 and o.salesman_id = i.salesman_id);

--method 2
select salesman_id, name from salesman where 
salesman_id in (select salesman_id from customer i 
group by salesman_id having count(customer_id)>1);

-- All & Any
-- all the orders which are greater than the poojitas orders

select purch_amt from orders
where customer_id = 3005;

select * from orders where purch_amt > All(
						select purch_amt
						from orders
						where customer_id = 3005
						);
select * from orders;
--The above query using group by
select * from orders where purch_amt > ( select max(purch_amt) from orders
where customer_id = 3005 group by customer_id);

-- Any
-- Any acts like min or "atleast greater than any one order of poojitha"

select * from orders where purch_amt > Any(
						select purch_amt
						from orders
						where customer_id = 3005
						);

-- Task 9
-- Write a query to display only those customer whose grade are in fact higher than every customer in 
--New York

select * from customer;

select * from customer where grade > All (
						select grade from customer
						where city = 'New York'
						);
--Task 10
--Write a query to find all orders with an amount smaller than any amount for a customer in London.

select * from orders;
select * from customer;
select * from salesman;

select orders.purch_amt from customer inner join orders on customer.customer_id = orders.customer_id where city = 'London';

select * from orders where purch_amt < any (
select orders.purch_amt from customer inner join orders on customer.customer_id = orders.customer_id 
where city = 'London');

--Task 10 with more than one sub query
select * from orders where purch_amt< Any(select purch_amt 
from orders where customer_id In (select customer_id  from customer 
where city='London'));


CREATE TABLE EmployeeData (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT,
    StartDate DATE
);

INSERT INTO EmployeeData (EmployeeID, FirstName, LastName, Salary, StartDate) VALUES
(1, 'John', 'Doe', 70000, '2020-05-01'),
(2, 'Jane', 'Smith', 85000, '2018-08-15'),
(3, 'Emily', 'Jones', 94000, '2019-12-30'),
(4, 'Chris', 'Brown', 62000, '2021-03-22');

--Task 1
-- Sort the employees by the length of their first names in descending order

select len(FirstName) from EmployeeData;

select * from EmployeeData order by len(FirstName) desc;

--Task 2
-- Get the initials

select concat(left(FirstName,1),left(LastName,1)) as Initials from EmployeeData;

--Task 3
--Extract and Display the first three letters of each employee's last name and Display it in upper case

select upper(substring(LastName,1,3)) as LastNameUpper from EmployeeData;

--Task 4
--Write a query to calculate the tenure of each employee in complete years as of today.