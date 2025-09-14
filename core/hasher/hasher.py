import hashlib
import shutil


class Hasher:
	def hash_string(self, string):
		hash_object = hashlib.md5()
		hash_object.update(string.encode("utf-8"))

		md5_hash = hash_object.hexdigest()

		return md5_hash

	def hash_file(self, file):
		pass