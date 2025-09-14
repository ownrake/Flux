from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, User  # Явно импортируем нужные классы

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
        session = self.Session()
        try:
            user = User(name=name, email=email, passwd=passwd)
            session.add(user)
            session.commit()
            print(f"Пользователь {name} добавлен!")
            return user
        except Exception as e:
            session.rollback()
            print(f"Ошибка при добавлении пользователя: {e}")
            return None
        finally:
            session.close()