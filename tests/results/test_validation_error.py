import unittest
from faker import Faker
from validationpy.results.validation_error import ValidationError


class TestValidationError(unittest.TestCase):
    def setUp(self) -> None:
        self.faker = Faker()

    def test_init_shouldSetPropertiesAsExpected(self):
        # Arrange
        property_name = self.faker.word()
        message = self.faker.sentence()
        attempted_value = self.faker.word()

        # Act
        error = ValidationError(property_name, message, attempted_value)

        # Assert
        self.assertEqual(property_name, error.property_name)
        self.assertEqual(message, error.message)
        self.assertEqual(attempted_value, error.attempted_value)
        self.assertIsNone(error.code)
        self.assertFalse(error._template_placeholders)

    def test_init_whenInvalidPropertyNameType_shouldRaiseValueError(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(None, self.faker.sentence(), self.faker.word())

        with self.assertRaises(ValueError) as context2:
            ValidationError(1, self.faker.sentence(), self.faker.word())

        # Assert
        self.assertTrue(f"Property name must be of type {str}", context1.exception)
        self.assertTrue(f"Property name must be of type {str}", context2.exception)

    def test_init_whenInvalidMessageType_shouldRaiseValueError(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(self.faker.word(), None, self.faker.word())

        with self.assertRaises(ValueError) as context2:
            ValidationError(self.faker.word(), 1, self.faker.word())

        # Assert
        self.assertTrue(f"Message must be of type {str}", context1.exception)
        self.assertTrue(f"Message must be of type {str}", context2.exception)

    def test_init_whenInvalidAttemptedValueType_shouldRaiseValueError(self):
        # Act
        with self.assertRaises(ValueError) as context1:
            ValidationError(self.faker.word(), self.faker.sentence(), None)

        # Assert
        self.assertTrue("Attempted value must not be None", context1.exception)

    def test_str_shouldReturnExpected(self):
        # Arrange
        error = ValidationError(self.faker.word(), self.faker.sentence(), self.faker.word())

        # Assert
        self.assertEqual(error.message, str(error))


if __name__ == '__main__':
    unittest.main()
