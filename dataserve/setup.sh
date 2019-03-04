# To be run on ubuntu 18.04 LTS Server
sudo apt update
sudo apt install python3-pip
pip3 install pipenv
pipenv install
sudo apt install mysql-server
sudo mysql_secure_installation
sudo sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf
sudo service mysql restart
            # setting the bind address in /etc/mysql/mysql.conf.d/mysqld.cnf:
            # bind-address            = 0.0.0.0
            # then restarting the mysql daemon:
            # service mysql restart
sudo mysql < ./setup_mysql.sql > /dev/null/