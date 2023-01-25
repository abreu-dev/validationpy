import unittest
from faker import Faker
from tests import Fixtures
from validationpy.results.validation_result import ValidationResult


class TestValidationResult(unittest.TestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        self.fixture = Fixtures(self.faker)

    def test_init_shouldSetPropertiesAsExpected(self):
        # Arrange
        errors = [self.fixture.validation_error(), self.fixture.validation_error(), None]

        # Act
        result = ValidationResult(errors)

        # Assert
        self.assertListEqual([errors[0], errors[1]], result.errors)

    def test_init_whenErrorsIsNone_shouldSetErrorsAsEmptyList(self):
        # Arrange
        errors = None

        # Act
        result = ValidationResult(errors)

        # Assert
        self.assertIsNotNone(result.errors)
        self.assertFalse(result.errors)

    def test_isValid_whenEmptyErrors_shouldReturnFalse(self):
        # Arrange
        result = ValidationResult(None)

        # Assert
        self.assertFalse(result.is_valid)

    def test_isValid_whenAnyErrors_shouldReturnTrue(self):
        # Arrange
        result = ValidationResult([self.fixture.validation_error()])

        # Assert
        self.assertTrue(result.is_valid)

    def test_str_shouldReturnExpected(self):
        # Arrange
        result = ValidationResult([self.fixture.validation_error(), self.fixture.validation_error()])
        expected_message = f"{str(result.errors[0])}\n{str(result.errors[1])}"

        # Assert
        self.assertEqual(expected_message, str(result))


if __name__ == '__main__':
    unittest.main()
