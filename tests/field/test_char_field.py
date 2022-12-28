from json_orm.field import CharField


def test_char_field_should_always_get_string() -> None:
    # Arrange
    class ClassWithCharField:
        char = CharField()

    # Act
    obj = ClassWithCharField()
    obj.char = 1

    # Assert
    assert obj.char == '1'
