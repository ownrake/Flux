from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from db.models import Base, User

from core.hasher.hasher import Hasher

hasher = Hasher()

class DatabaseManager:
    def __init__(self, db_url='sqlite:///mydatabase.sqlite3'):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        # Создаем таблицы при инициализации менеджера
        self.create_tables()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Таблицы созданы/проверены")

    def add_user(self, name, email, passwd):
        with self.Session() as session:
            with session.begin():
                hash_passwd = hasher.hash_string(passwd)
                user = User(name=name, email=email, passwd=hash_passwd)
                session.add(user)
                print(f"Пользователь {name} добавлен в базу.")
    
    def login_user(self, name, passwd):
        with self.Session() as session:
            with session.begin():
                user = session.scalar(select(User).filter(User.name == name))

                try:
                    current_passwd = hasher.hash_string(passwd)

                    if current_passwd == user.passwd:
                        print("Вы успешно вошли в аккаунт!")
                    else:
                        print("Логин или пароль не верный!")
                except:
                    print("Произошла ошибка, попробуйте снова.")