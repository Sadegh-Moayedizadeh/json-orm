from json_orm.field import FloatField


def test_float_field_should_always_get_float() -> None:
    # Arrange
    class ClassWithFloatField:
        float_num = FloatField()

    # Act
    obj = ClassWithFloatField()
    obj.float_num = '1'

    # Assert
    assert obj.float_num == 1.0
