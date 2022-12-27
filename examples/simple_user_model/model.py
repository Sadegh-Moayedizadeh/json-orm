from json_orm.model import create_base, CharField


Base = create_base('examples/simple_user_model/database')


class User(Base):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    phone_number = CharField()
