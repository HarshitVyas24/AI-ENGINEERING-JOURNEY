SELECT * FROM accounts;

DELIMITER $$
CREATE PROCEDURE check_balance(	IN id INT , OUT bal DECIMAL(10,2))
BEGIN 
	SELECT balance INTO bal
    FROM accounts
    WHERE account_id = id;
END$$

DELIMITER ;

CALL check_balance(1 , @balance);
SELECT @balance;