CREATE DATABASE IF NOT EXISTS instagram ;

USE instagram;

CREATE TABLE users(
age INT,
user_id INT ,
name VARCHAR(50) NOT NULL ,
email VARCHAR(50) UNIQUE ,
followers INT DEFAULT 0,
following INT DEFAULT 0,
CONSTRAINT age_check CHECK (age>13),
PRIMARY KEY (user_id)
);



CREATE TABLE post(
id INT ,
content VARCHAR(50),
user_id INT ,
PRIMARY KEY(id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
	
);

INSERT INTO users
(user_id , age, name , email , followers , following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob123@gmail.com", 200, 200),
(3, 16, "casey", "casey@email.com", 300, 306),
(4, 17, "donald", "donald@gmail.com", 200, 105);

ALTER TABLE users ADD age INT ;

	
SELECT * FROM users;
SELECT name, email FROM users;
SELECT DISTINCT age FROM users;

SELECT *
FROM users 
WHERE age BETWEEN 15 AND 17;-- 


SELECT *
FROM users 
WHERE email IN ("adam@yahoo.in" , "bob123@gmail.com" );--

INSERT INTO users
(user_id, age, name, email, followers, following)
VALUES
(5, 14, "eve", "eve@yahoo.in", 400, 145),
(6, 16, "farah", "farah@gmail.com", 10000, 1000);


SELECT name ,age
FROM users
WHERE age NOT IN (14,16);

SELECT name ,age , email, following ,  followers
FROM users
WHERE age>14
LIMIT 3;

SELECT name , age  , followers
FROM users
ORDER BY followers DESC ;

SELECT COUNT(age)
FROM users 
WHERE age>15;

SELECT AVG(age)
FROM users;

SELECT age,MAX(followers)
FROM users
GROUP BY age;

SELECT age,MAX(followers)
FROM users
GROUP BY age
HAVING max(followers) > 200
ORDER BY age DESC;

UPDATE users
SET followers = 600
WHERE age = 16;

SET SQL_SAFE_UPDATES = 0;

SELECT * FROM users;

DELETE from users
WHERE age = 14;

ALTER TABLE users
ADD COLUMN city VARCHAR(50) DEFAULT "Delhi";

ALTER TABLE users
DROP COLUMN age;

ALTER TABLE users
RENAME TO instauser;

SELECT * FROM instauser;

INSERT INTO post
(id , content , user_id)
VALUES
(101 , "Hello World" , 3),
(102 , "Bye Bye" , 1),
(103, "Hiiii" , 3);

SELECT * FROM post;


DROP TABLE post;
TRUNCATE TABLE instauser;



