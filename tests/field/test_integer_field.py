from json_orm.field import IntegerField


def test_integer_field_should_always_get_integer() -> None:
    # Arrange
    class ClassWithIntegerField:
        integer = IntegerField()

    # Act
    obj = ClassWithIntegerField()
    obj.integer = '1'

    # Assert
    assert obj.integer == 1
