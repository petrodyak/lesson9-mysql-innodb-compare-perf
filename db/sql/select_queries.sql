EXPLAIN select date_of_birth, count(*) from users 
         group by  date_of_birth
         having count(*)>100
         
EXPLAIN   select * from users 		where date_of_birth = '2006-07-02'
         
show variables like '%innodb_log_file_size%'

-- 0.1%  40400
select * from users u where date_of_birth = '1996-05-12';
-- 1%  - 404000 rows
select * from users u where date_of_birth >='1996-03-11' and date_of_birth  <='1996-03-20';
-- 10%  - 3999600 rows
select * from users u where date_of_birth >='1996-03-12' and date_of_birth  <='1996-06-18'
-- 54%  - 21593600 rows
select * from users u where date_of_birth  >='1996-06-20' and date_of_birth  <='2011-06-25'