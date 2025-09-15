import hashlib
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class Hasher:
	"""Управление хэшированием"""
	def string_to_hash(self, string: str) -> str:
		"""
		Хэширует полученую строку
		
		Args:
			string (str): Исходная строка из которой получаем хэш

		Returns:
			str: Хэш исходной строки
		"""
		
		if not isinstance(string, str):
			raise TypeError(f"Ожидалась строка, получен {type(string).__name__}")
		
		try:
			hash_object = hashlib.md5()
			hash_object.update(string.encode("utf-8"))
			
			return hash_object.hexdigest()
		except Exception as e:
			logging.error(f"Получена неизвестная ошибка: {e}")

	def file_to_hash(self) -> str:
		"""Хэширует полученный файл"""
		...