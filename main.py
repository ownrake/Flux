import asyncio

from gui.login import app
from db.db_manager import DatabaseManager


def main():
	# Создаем менеджер БД - он автоматически создаст таблицы
	db_manager = DatabaseManager()
    
	app.mainloop()

	# Теперь можно добавлять пользователей
	db_manager.add_user("aryose", "aryose@temp.mail", "lskdjflksjdflkjsdf")

if __name__ == "__main__":
    main()