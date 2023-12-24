import db
import tools

def delete_menu():
  while True:
    print()
    print("Выберите действие:")
    print("1. Удалить участок")
    print("2. Удалить сотрудника")
    print("3. Удалить причину задержания")
    print("4. Удалить задержание")
    print("5. Вернуться в главное меню")
    print("0. Выход")
    s = int(input("> "))

    if s == 1:
      delete_police_station()
    elif s == 2:
      delete_officer()
    elif s == 3:
      delete_reason()
    elif s == 4:
      delete_detention()
    elif s == 5:
      return
    elif s == 0:
      tools.exit()
    else:
      print("Неверный ввод")

def delete_police_station():
  for item in db.conn.Select('SELECT * FROM police_station'):
    print(item)

  print()
  print('Введите id участка')
  id = [int(input('> '))]
  sql = 'DELETE FROM police_station WHERE id = %s'

  if db.conn.Delete(sql, *id):
    print('Участок удален')
  else:
    print('Участок не удален')

def delete_officer():
  for item in db.conn.Select('SELECT * FROM officer'):
    print(item)

  print()
  print('Введите id сотрудника')

  id = [int(input('> '))]
  sql = 'DELETE FROM officer WHERE id = %s'

  if db.conn.Delete(sql, *id):
    print('Сотрудник удален')
  else:
    print('Сотрудник не удален')

def delete_reason():
  for item in db.conn.Select('SELECT * FROM reason'):
    print(item)

  print()
  print('Введите id причины')

  id = [int(input('> '))]
  sql = 'DELETE FROM reason WHERE id = %s'

  if db.conn.Delete(sql, *id):
    print('Причина удалена')
  else:
    print('Причина не удалена')

def delete_detention():
  for item in db.conn.Select('SELECT * FROM detention'):
    print(item)

  print()
  print('Введите id задержания')

  id = [int(input('> '))]
  sql = 'DELETE FROM detention WHERE id = %s'

  if db.conn.Delete(sql, *id):
    print('Задержание удалено')
  else:
    print('Задержание не удалено')
