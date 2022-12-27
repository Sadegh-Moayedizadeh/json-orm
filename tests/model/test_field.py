from json_orm.model import CharField, IntegerField


def test_char_field_should_always_get_string() -> None:
    # Arrange
    class ClassWithCharField:
        char = CharField()

    # Act
    obj = ClassWithCharField()
    obj.char = 1

    # Assert
    assert obj.char == '1'


def test_float_field_should_always_get_float() -> None:
    # Arrange
    class ClassWithFloatField:
        float_num = IntegerField()

    # Act
    obj = ClassWithFloatField()
    obj.float_num = '1'

    # Assert
    assert obj.float_num == 1.0


def test_integer_field_should_always_get_integer() -> None:
    # Arrange
    class ClassWithIntegerField:
        integer = IntegerField()

    # Act
    obj = ClassWithIntegerField()
    obj.integer = '1'

    # Assert
    assert obj.integer == 1


def test_having_two_fields_of_the_same_type_should_not_override_one_another() -> None:  # noqa: E501
    # Arrange
    class ClassWithCharField:
        first_char = CharField()
        second_char = CharField()

    # Act
    obj = ClassWithCharField()
    obj.first_char = 1
    obj.second_char = 2

    # Assert
    assert obj.first_char == '1'
    assert obj.second_char == '2'


def test_modifying_a_field_should_not_affect_other_instances() -> None:
    # Arrange
    class ClassWithCharField:
        char = CharField()

    first_instance = ClassWithCharField()
    second_instance = ClassWithCharField()

    # Act
    first_instance.char = 1
    second_instance.char = 2

    # Assert
    assert first_instance.char == '1'
    assert second_instance.char == '2'
