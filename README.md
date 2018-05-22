# build
docker build -t flask .
docker images

# run
docker run --name flask_app -p 5000:5000 -d flask
docker ps
docker stop flask_app
docker rm flask_app
docker logs flask_app

# mysql
docker build -t mysql_storage docker/db
docker create --name mysql_storage mysql_storage

docker run --volumes-from mysql_storage --name mysql_server -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
docker exec -it mysql_server bash
mysql -u root -p

## SQL
create database flask;
use flask;
create table users (id int, name varchar(20));
insert into users values (1, 'shino');
insert into users values (2, 'moko');

# link
docker run -it --link mysql_server:db flask bash
apt-get update
apt-get -y install mysql-client
mysql -h db -u root -p

# app
docker run --name flask_app --link mysql_server:db -p 5000:5000 -d flask
