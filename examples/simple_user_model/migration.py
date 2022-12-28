from examples.simple_user_model.config import DATABASE_PATH
from examples.simple_user_model.model import User
from json_orm.migration import create_table

if __name__ == '__main__':
    create_table(User, DATABASE_PATH)
