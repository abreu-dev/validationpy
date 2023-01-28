from unittest import TestCase, main
from faker import Faker
from validationpy.results.validation_error import ValidationError


class TestValidationError(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
    # endregion

    # region __init__
    def test_init_should_set_attributes(self):
        # Arrange
        attribute_name = self.faker.word()
        message = self.faker.sentence()
        attempted_value = self.faker.word()

        # Act
        error = ValidationError(attribute_name, message, attempted_value)

        # Assert
        self.assertEqual(attribute_name, error.attribute_name)
        self.assertEqual(message, error.message)
        self.assertEqual(attempted_value, error.attempted_value)
        self.assertIsNone(error.code)
        self.assertFalse(error.template_placeholders)
    # endregion

    # region __str__
    def test_str_should_return_custom(self):
        # Arrange
        error = ValidationError(self.faker.word(),
                                self.faker.sentence(),
                                self.faker.word())

        # Assert
        self.assertEqual(error.message, str(error))
    # endregion


if __name__ == '__main__':
    main()
