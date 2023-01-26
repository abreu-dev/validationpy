import unittest
from tests import Fixtures
from validationpy.results.validation_error import ValidationError


class TestValidationError(unittest.TestCase):
    def setUp(self) -> None:
        self.fixtures = Fixtures()

    def test_init_should_set_attributes(self):
        # Arrange
        property_name = self.fixtures.faker.word()
        message = self.fixtures.faker.sentence()
        attempted_value = self.fixtures.faker.word()

        # Act
        error = ValidationError(property_name, message, attempted_value)

        # Assert
        self.assertEqual(property_name, error.property_name)
        self.assertEqual(message, error.message)
        self.assertEqual(attempted_value, error.attempted_value)
        self.assertIsNone(error.code)
        self.assertFalse(error.template_placeholders)

    def test_init_should_raise_value_error_when_invalid_property_name(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(None, self.fixtures.faker.sentence(), self.fixtures.faker.word())

        with self.assertRaises(ValueError) as context2:
            ValidationError(1, self.fixtures.faker.sentence(), self.fixtures.faker.word())

        # Assert
        self.assertEqual(f"Property name must be of type {str}", str(context1.exception))
        self.assertEqual(f"Property name must be of type {str}", str(context2.exception))

    def test_init_should_raise_value_error_when_invalid_message(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(self.fixtures.faker.word(), None, self.fixtures.faker.word())

        with self.assertRaises(ValueError) as context2:
            ValidationError(self.fixtures.faker.word(), 1, self.fixtures.faker.word())

        # Assert
        self.assertEqual(f"Message must be of type {str}", str(context1.exception))
        self.assertEqual(f"Message must be of type {str}", str(context2.exception))

    def test_init_should_raise_value_error_when_invalid_attempted_value(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(self.fixtures.faker.word(), self.fixtures.faker.sentence(), None)

        # Assert
        self.assertEqual("Attempted value must not be None", str(context1.exception))

    def test_str_should_return_custom(self):
        # Arrange
        error = ValidationError(self.fixtures.faker.word(),
                                self.fixtures.faker.sentence(),
                                self.fixtures.faker.word())

        # Assert
        self.assertEqual(error.message, str(error))


if __name__ == '__main__':
    unittest.main()
