#!/usr/bin/env python3

import db
from officer import officer_menu
from officer import auth

if __name__ == "__main__":
  print("Выберите действие:")
  print("1. Авторизация")
  print("0. Выход")
  try:
    while True:
      s = int(input("> "))
      db.connect()

      if s == 1:
        officer_id = auth()
        print(officer_id)
        if officer_id != 0:
          officer_menu(officer_id)
      elif s == 0:
        exit()
      else:
        print("Неверный ввод")
  except KeyboardInterrupt as e:
    exit()
