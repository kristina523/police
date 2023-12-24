import db

def exit():
  if db.conn is not None:
    db.conn.Close()
  exit()
