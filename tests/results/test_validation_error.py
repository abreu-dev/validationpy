import unittest
from faker import Faker
from validationpy.results.validation_error import ValidationError


class TestValidationError(unittest.TestCase):
    def setUp(self) -> None:
        self.faker = Faker()

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

    def test_init_should_raise_value_error_when_invalid_attribute_name(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(None, self.faker.sentence(), self.faker.word())

        with self.assertRaises(ValueError) as context2:
            ValidationError(1, self.faker.sentence(), self.faker.word())

        # Assert
        self.assertEqual(f"Attribute name must be of type {str}", str(context1.exception))
        self.assertEqual(f"Attribute name must be of type {str}", str(context2.exception))

    def test_init_should_raise_value_error_when_invalid_message(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(self.faker.word(), None, self.faker.word())

        with self.assertRaises(ValueError) as context2:
            ValidationError(self.faker.word(), 1, self.faker.word())

        # Assert
        self.assertEqual(f"Message must be of type {str}", str(context1.exception))
        self.assertEqual(f"Message must be of type {str}", str(context2.exception))

    def test_init_should_raise_value_error_when_invalid_attempted_value(self):
        # Act
        with self.assertRaises(ValueError) as context:
            ValidationError(self.faker.word(), self.faker.sentence(), None)

        # Assert
        self.assertEqual("Attempted value must not be None", str(context.exception))

    def test_str_should_return_custom(self):
        # Arrange
        error = ValidationError(self.faker.word(),
                                self.faker.sentence(),
                                self.faker.word())

        # Assert
        self.assertEqual(error.message, str(error))


if __name__ == '__main__':
    unittest.main()
