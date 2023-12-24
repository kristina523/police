import db
import tools
import getpass
from detention import detention
from detention import print_detentions
from delete import delete_menu

def officer_menu(officer_id: int):
  while True:
    print()
    print("Выберите действие:")
    print("1, Добавить участок")
    print("2, Список участков")
    print("3. Добавить нового сотрудника")
    print("4. Посмотреть список сотрудников")
    print("5. Добавть причину задержания")
    print("6. Список причин задержания")
    print("7. Добавить задержание")
    print("8. Список задержаний")
    print("9. Удаления")
    print("0. Выход")
    s = int(input("> "))

    if s == 1:
      add_police_station()
    elif s == 2:
      print_police_station()
    elif s == 3:
      new_officer()
    elif s == 4:
      print_officers()
    elif s == 5:
      add_reason()
    elif s == 6:
      print_reasons()
    elif s == 7:
      detention(officer_id)
    elif s == 8:
      print_detentions()
    elif s == 9:
      delete_menu()
    elif s == 0:
      tools.exit()
    else:
      print("Неверный ввод")

def auth() -> int:
  user = []
  user.append(str(input('Имя: ')))
  user.append(str(getpass.getpass('Пароль: ')))
  sql = 'SELECT * FROM officer WHERE name = %s AND password = %s'
  data = db.conn.Select(sql, *user)

  if data is not None:
    print('Авторизация успешна')
    return data[0][0]
  else:
    return 0

def add_police_station():
  station = []
  station.append(str(input('Номер участка: ')))
  station.append(str(input('Адрес участка: ')))
  sql = 'INSERT INTO police_station (number, addr) VALUES (%s, %s)'

  if db.conn.Insert(sql, *station):
    print("Участок успешно добавлен")
  else:
    print("Участок не добавлен")

def print_police_station():
  for item in db.conn.Select("SELECT * FROM police_station"):
    print(item)

def new_officer():
  user = []
  user.append(str(input('Имя: ')))
  user.append(str(getpass.getpass('Пароль: ')))
  user.append(str(input('Должность: ')))
  user.append(str(input('ID участка: ')))
  sql = 'INSERT INTO officer (name, password, rank, station_id) VALUES (%s, %s, %s, %s)'

  if db.conn.Insert(sql, *user):
    print("Сотрудник успешно добавлен")
  else:
    print("Сотрудник не добавлен")

def print_officers():
  for item in db.conn.Select("SELECT id, name, rank, station_id FROM officer"):
    print(item)

def add_reason():
  reason = []
  reason.append(str(input('Причина: ')))
  sql = 'INSERT INTO reason (title) VALUES (%s)'

  if db.conn.Insert(sql, *reason):
    print("Причина успешно добавлена")
  else:
    print("Причина не добавлена")

def print_reasons():
  for item in db.conn.Select("SELECT * FROM reason"):
    print(item)
