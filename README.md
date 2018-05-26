# mysql
```
docker volume create --name mysql_data
docker run --name mysql_server -v mysql_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
docker exec -it mysql_server mysql -u root -p
```

## SQL
```
create database flask;
use flask;
create table users (id int, name varchar(20));
insert into users values (1, 'shino');
insert into users values (2, 'moko');
```

# app
```
docker build -t flask .
docker run --name flask_app --link mysql_server:db -v `pwd`:/myapp/ -p 5000:5000 -d flask
```
