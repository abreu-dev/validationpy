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

    def test_str_should_return_custom(self):
        # Arrange
        error = ValidationError(self.faker.word(),
                                self.faker.sentence(),
                                self.faker.word())

        # Assert
        self.assertEqual(error.message, str(error))


if __name__ == '__main__':
    unittest.main()
