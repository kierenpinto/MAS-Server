/* Run as root
ie:
sudo mysql
*/
create user 'mas'@'localhost' identified by 'password';
grant create on *.* to 'mas'@'localhost';
grant all privileges on mas.* to 'mas'@'localhost';
create user r_mas identified by 'password';
grant select on mas.* to r_mas;