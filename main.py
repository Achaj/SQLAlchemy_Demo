import random
import Db
import names
if __name__ == '__main__':
    Session = Db.sessionmaker(bind=Db.engine)
    session = Session()


    # Tworzy tylko 100 obiektów klasy Person
    for i in range(1, 101):
        random_number = random.randint(20, 55)
        person = Db.Person(i, names.get_first_name(), names.get_last_name(), "M", random_number)
        session.add(person)

    # Lista słów, które będą służyć jako nazwy dla Twoich obiektów
    thing_names = ['Car', 'Book', 'Bike', 'Laptop', 'Phone', 'Chair', 'Table', 'Shoe', 'Bag', 'Hat']

    # Tworzy tylko 59 obiektów klasy Thing
    for i in range(1, 60):
        random_number = random.randint(1, 101)
        thing = Db.Thing(i, random.choice(thing_names), random_number)
        session.add(thing)

    session.commit()

    # rekord do aktualizacji
    record_to_update = session.query(Db.Thing).filter_by(tid=1).first()
    record_to_update.description = 'Bike'
    session.commit()

    ## usuwanie rekordu
    session.delete(record_to_update)
    session.commit()

    result = session.query(Db.Thing).all()
    for r in result:
        print(r)