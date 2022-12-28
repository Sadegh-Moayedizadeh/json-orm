from json_orm.model import CharField, create_base

Base = create_base('examples/simple_user_model/database')


class User(Base):
    table_name = 'user'

    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True)
    phone_number = CharField(unique=True)
