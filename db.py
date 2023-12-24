import psycopg2
# from psycopg2.extras import NamedTupleCursor

class DB:
  conn = None

  def __init__(self):
    try:
      self.conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
    except:
      print('База данных не найдена')

  def Select(self, sql: str, *values: list) -> None:
    try:
      with self.conn.cursor() as cursor:
        cursor.execute(sql, values)
        return cursor.fetchall()
    except Exception as e:
      print('SELECT ERROR: ', e)
      return None

  def Insert(self, sql: str, *values) -> bool:
    try:
      with self.conn.cursor() as cursor:
        cursor.execute(sql, values)
        self.conn.commit()

        if cursor.rowcount != 0:
          return True
        else:
          return False
    except Exception as e:
      print('INSERT ERROR: ', e)
      return False

  def Delete(self, sql: str, *values: list) -> bool:
    try:
      with self.conn.cursor() as cursor:
        cursor.execute(sql, values)
        self.conn.commit()

        if cursor.rowcount != 0:
          return True
        else:
          return False
    except Exception as e:
      print('DELETE ERROR: ', e)
      return False

  def Close(self) -> bool:
    try:
      self.conn.close()
    except:
      print('Ошибка закрытия соединения')

def connect():
  global conn
  conn = DB()
