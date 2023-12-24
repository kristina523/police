import db

def detention(officer_id: int) -> None:

  police_station = db.conn.Select("SELECT * FROM police_station")
  reason = db.conn.Select("SELECT * FROM reason")

  print("Введите данные о задержанном:")
  detainee = []
  detainee.append(str(input("Имя: ")))
  detainee.append(str(input("Фамилия: ")))
  detainee.append(str(input("Отчество: ")))
  detainee.append(int(input("Возраст задержанного: ")))
  print()
  print(reason)
  print()
  detainee.append(str(input("Причина задержания: ")))
  print()
  print('Выберите участок: ', police_station)
  print()
  detainee.append(str(input("Участок (укажите ID участка): ")))
  detainee.append(officer_id)

  sql = "INSERT INTO detention (firstname, surname, patronymic, age, reason_id, officer_id, police_station_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

  if db.conn.Insert(sql, *detainee):
    print("Задержание успешно добавлено")
  else:
    print("Задержание не добавлено")
  return None


def print_detentions():
  print('Введите id сотрудника (0 если надо вывести все задержания)')
  officer_id = [int(input('> '))]
  sql = "SELECT * FROM detention"

  if 0 not in officer_id:
    sql = "SELECT * FROM detention WHERE officer_id = %s"

  data = db.conn.Select(sql, *officer_id)

  if len(data) == 0:
    print('Задержаний не найдено либо неверный id сотрудника')
  else:
    for item in data:
      print(item)
