# Police
## Install requirements

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Database

```sh
docker-compose up -d  # запустить базу
docker-compose down   # остановить базу
```

## Step 1

```sh
docker exec -it police-db-1 bash
psql -U postgres
```

```sql
CREATE TABLE police_station (id SERIAL PRIMARY KEY, number int NOT NULL, addr varchar(50) NOT NULL);

INSERT INTO police_station (number, addr) VALUES (777, 'Петровка') RETURNING id;
```

```sql
CREATE TABLE officer (id SERIAL PRIMARY KEY, name varchar(40) NOT NULL, password varchar NOT NULL, rank varchar(20) NOT NULL, station_id int NOT NULL);

INSERT INTO officer (name, password, rank, station_id) VALUES ('kris', '21', 'general', 1) RETURNING id;
```

```sql
CREATE TABLE reason (id SERIAL PRIMARY KEY, title varchar(50) NOT NULL);
```

```sql
CREATE TABLE detention (id SERIAL PRIMARY KEY, firstname varchar(40) NOT NULL, surname varchar(40) NOT NULL, patronymic varchar(40) NOT NULL, age int NOT NULL, reason_id int NOT NULL, officer_id int NOT NULL, police_station_id int NOT NULL);
```

## Step 2

```sh
./main.py
```

- Добавить причину ареста
- Можно добавлять Задержание
