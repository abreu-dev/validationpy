from faker import Faker
from unittest import TestCase, main
from unittest.mock import Mock
from validationpy.results.validation_error import ValidationError
from validationpy.results.validation_result import ValidationResult


class TestValidationResult(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
    # endregion

    # region __init__
    def test_init_should_set_attributes(self):
        # Arrange
        errors = [Mock(spec=ValidationError), Mock(spec=ValidationError), None]

        # Act
        result = ValidationResult(errors)

        # Assert
        self.assertListEqual([errors[0], errors[1]], result.errors)

    def test_init_should_set_errors_empty_when_errors_is_none(self):
        # Arrange
        errors = None

        # Act
        result = ValidationResult(errors)

        # Assert
        self.assertIsNotNone(result.errors)
        self.assertFalse(result.errors)
    # endregion

    # region is_valid
    def test_is_valid_should_return_false_when_empty_errors(self):
        # Arrange
        result = ValidationResult(None)

        # Assert
        self.assertFalse(result.is_valid)

    def test_is_valid_should_return_true_when_any_errors(self):
        # Arrange
        result = ValidationResult([Mock(spec=ValidationError)])

        # Assert
        self.assertTrue(result.is_valid)
    # endregion

    # region __str__
    def test_str_should_return_custom(self):
        # Arrange
        result = ValidationResult([
            Mock(spec=ValidationError, str="Message1"),
            Mock(spec=ValidationError, str="Message2")
        ])
        expected_message = f"{str(result.errors[0])}\n{str(result.errors[1])}"

        # Assert
        self.assertEqual(expected_message, str(result))
    # endregion


if __name__ == '__main__':
    main()
