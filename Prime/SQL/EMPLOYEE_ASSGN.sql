CREATE DATABASE office;

CREATE TABLE employee(
    
EmpID INT PRIMARY KEY,
FirstName VARCHAR(50) ,
LastName VARCHAR(50) ,
Department VARCHAR(50),
Salary INT,
HireDate DATETIME
);

INSERT INTO employee
VALUES
(101 ,"Alice","Johnson", "IT" ,6500 ,"2020-03-15"),
(102, "Mark" ,"Rivera" ,"HR" ,4800 ,"2019-07-22"),
(103, "Sophia", "Lee" ,"Finance" ,7200 ,"2021-01-10"),
(104, "Daniel" ,"Kim" ,"IT", 5800, "2018-11-05"),
(105, "Emma" ,"Brown" ,"Marketing" ,5300, "2022-04-18"),
(106 ,"Liam" ,"Patel", "Finance", 6900, "2020-09-29"),
(107 ,"Olivia" ,"Garcia","HR" ,4600, "2017-06-30"),
(108, "Noah","Thompson" ,"IT" ,7500 ,"2023-02-12"),
(109,"Ava" ,"Martinez" ,"Marketing", 5100, "2019-12-02"),
(110, "Ethan", "Davis" ,"Finance", 8000 ,"2016-05-14");


SELECT * FROM employee;

SELECT FirstName , LastName , salary
FROM employee;

SELECT * 
FROM employee
WHERE Department = "IT";

SELECT * 
FROM employee
WHERE salary > 6000;

SELECT * 
FROM employee
ORDER BY HireDate DESC;

SELECT DISTINCT Department
FROM employee
GROUP BY Department;

SELECT FirstName
FROM employee
WHERE FirstName LIKE 'A%';


SELECT FirstName, salary
FROM employee
WHERE salary BETWEEN 4000 AND 7000;

SELECT avg(salary) AS avg_salary
FROM employee;

SELECT Department , COUNT(*) AS employee_count
FROM employee
GROUP BY Department
HAVING COUNT(*) > 2;







 






