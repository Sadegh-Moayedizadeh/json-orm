from typing import Any

from json_orm.field import FieldBase



def test_having_two_fields_of_the_same_type_should_not_override_one_another() -> None:  # noqa: E501
    # Arrange
    class ConcreteField(FieldBase):
        def type_factory(self, value: Any) -> Any:
            return value

    class ClassWithCharField:
        first_field = ConcreteField()
        second_field = ConcreteField()

    # Act
    obj = ClassWithCharField()
    obj.first_field = 1
    obj.second_field = 2

    # Assert
    assert obj.first_field == 1
    assert obj.second_field == 2


def test_modifying_a_field_should_not_affect_other_instances() -> None:
    # Arrange
    class ConcreteField(FieldBase):
        def type_factory(self, value: Any) -> Any:
            return value

    class ClassWithCharField:
        field = ConcreteField()

    first_instance = ClassWithCharField()
    second_instance = ClassWithCharField()

    # Act
    first_instance.field = 1
    second_instance.field = 2

    # Assert
    assert first_instance.field == 1
    assert second_instance.field == 2
