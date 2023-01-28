from faker import Faker
from string import Template
from unittest import TestCase, main
from validationpy.utils.message_constructor import MessageConstructor


class TestMessageConstructor(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
        self.constructor = MessageConstructor()
    # endregion

    # region constants
    def test_should_have_constants(self):
        # Assert
        self.assertEqual("attribute_name", MessageConstructor.ATTRIBUTE_NAME_KEY)
        self.assertEqual("attribute_value", MessageConstructor.ATTRIBUTE_VALUE_KEY)
    # endregion

    # region __init__
    def test_init_should_set_attributes(self):
        # Assert
        self.assertIsNotNone(self.constructor.placeholders)
        self.assertFalse(self.constructor.placeholders)
    # endregion

    # region append_argument
    def test_append_argument_should_add_value(self):
        # Arrange
        key = "comparison_value"
        value = "value"

        # Act
        self.constructor.append_argument(key, value)

        # Assert
        self.assertEqual(1, len(self.constructor.placeholders.keys()))
        self.assertEqual(value, self.constructor.placeholders[key])
    # endregion

    # region append_attribute_name
    def test_append_attribute_name_should_add_value(self):
        # Arrange
        value = "value"

        # Act
        self.constructor.append_attribute_name(value)

        # Assert
        self.assertEqual(1, len(self.constructor.placeholders.keys()))
        self.assertEqual(value,
                         self.constructor.placeholders[MessageConstructor.ATTRIBUTE_NAME_KEY])
    # endregion

    # region append_attribute_value
    def test_append_attribute_value_should_add_value(self):
        # Arrange
        value = "value"

        # Act
        self.constructor.append_attribute_value(value)

        # Assert
        self.assertEqual(1, len(self.constructor.placeholders.keys()))
        self.assertEqual(value,
                         self.constructor.placeholders[MessageConstructor.ATTRIBUTE_VALUE_KEY])
    # endregion

    # region construct
    def test_construct_should_return_final_message(self):
        # Arrange
        self.constructor.append_argument("comparison_value", "value_1")
        self.constructor.append_attribute_name("comparison")
        self.constructor.append_attribute_value("value_2")
        template = Template("'$attribute_name' with value '$attribute_value' "
                            "must be equal to '$comparison_value'")

        # Act
        final_message = self.constructor.construct(template)

        # Assert
        self.assertEqual("'comparison' with value 'value_2' must be equal to 'value_1'",
                         final_message)
    # endregion

    # region clear
    def test_clear_should_clear_placeholders(self):
        # Arrange
        self.constructor.append_argument("comparison_value", "value_1")
        self.constructor.append_attribute_name("comparison")
        self.constructor.append_attribute_value("value_2")

        # Act
        self.constructor.clear()

        # Assert
        self.assertIsNotNone(self.constructor.placeholders)
        self.assertFalse(self.constructor.placeholders)
    # endregion


if __name__ == '__main__':
    main()
