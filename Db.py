from builtins import print

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# obsluga zarządzania tabelami
Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", String)
    age = Column("age", Integer)

    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.firstname = first_name
        self.lastname = last_name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn},{self.firstname},{self.lastname},{self.gender},{self.age})"


class Thing(Base):
    __tablename__ = 'things'
    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid},{self.description},{self.owner})"


# inicjalizacja połaczenia z bazą danych
engine = create_engine("sqlite:///mydb.db", echo=True)

# tworzenie tabel
Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Tworzy tylko 100 obiektów klasy Person
# for i in range(1, 101):
#     random_number = random.randint(20, 55)
#     person = Person(i, names.get_first_name(), names.get_last_name(), "M", random_number)
#     session.add(person)
#
# # Lista słów, które będą służyć jako nazwy dla Twoich obiektów
# thing_names = ['Car', 'Book', 'Bike', 'Laptop', 'Phone', 'Chair', 'Table', 'Shoe', 'Bag', 'Hat']
#
# # Tworzy tylko 59 obiektów klasy Thing
# for i in range(1, 60):
#     random_number = random.randint(1, 101)
#     thing = Thing(i, random.choice(thing_names), random_number)
#     session.add(thing)
#
# session.commit()
#
# # rekord do aktualizacji
# record_to_update = session.query(Thing).filter_by(tid=1).first()
# record_to_update.description = 'Bike'
# session.commit()
#
#
# ## usuwanie rekordu
# session.delete(record_to_update)
# session.commit()
#
# result = session.query(Thing).all()
# for r in result:
#     print(r)
