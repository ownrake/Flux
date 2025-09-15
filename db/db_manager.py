import logging

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from db.models import *
from core.hasher import Hasher

hasher = Hasher()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class DatabaseManager():
	"""Менеджер управления БД"""
	def __init__(self, db_url="sqlite:///mydatabase.sqlite3") -> None:
		"""
		Подключение и инициализирование БД
		
		Args:
			db_url (str): Ссылка на подключение в БД
		"""
		self.engine = create_engine(db_url)
		self.session = sessionmaker(bind=self.engine)

		# Создаем таблицы при инициализации менеджера
		self.create_tables()

	def create_tables(self) -> None:
		"""Создает таблицы БД"""
		Base.metadata.create_all(self.engine)

	def add_user(self, username: str, email: str, passwd: str) -> bool:
		"""
		Добавляет пользователя в БД

		Args:
			username (str): Имя пользователя
			email (str): Электронная почта пользователя
			passwd (str): Пароль пользователя

		Returns:
			bool: True если пользователь успешно добавлен, False если не получилось добавить
		"""
		with self.session() as session:
			try:
				hash_passwd = hasher.string_to_hash(passwd)
				user = User(username=username, email=email, passwd=hash_passwd)
				session.add(user)
				session.commit()
				logging.info(f"Пользователь {username} успешно добавлен")

				return True
			except Exception as e:
				logging.error(f"Произошла неизвестная ошибка при добавлении пользователя в БД: {e}")
				session.rollback()

				return False
			
	def auth_user(self, username, passwd) -> bool:
		"""
		Аутенцификация пользователя
		
		Args:
			username (str): Имя пользователя
			passwd (str): Пароль пользователя

		Returns:
			bool: True если пользователь авторизован, False если пользователь не авторизован
		"""
		with self.session() as session:
			try:
				user = session.scalar(select(User).filter(User.username == username))
				
				if user == None:
					logging.warning(f"Попытка входа с несуществующим username: {username}")
					return False

				current_passwd = hasher.string_to_hash(passwd)

				if current_passwd == user.passwd:
					logging.info(f"Пользователь {user.username} успешно вошел в аккаунт")
					return True
				else:
					logging.info(f"Неверный пароль для пользователя: {user.username}")
					return False

			except Exception as e:
				logging.error(f"Ошибка при аутентификации пользователя: {e}")
				session.rollback()

				return False