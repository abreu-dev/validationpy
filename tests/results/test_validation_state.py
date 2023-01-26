import unittest
from tests import Fixtures
from validationpy.results.validation_state import ValidationState


class TestValidationState(unittest.TestCase):
    def setUp(self) -> None:
        self.fixtures = Fixtures()

    def test_init_should_set_attributes(self):
        # Arrange
        object_to_validate = self.fixtures.person()

        # Act
        state = ValidationState(object_to_validate)

        # Assert
        self.assertEqual(object_to_validate, state.object_to_validate)
        self.assertIsNotNone(state.errors)
        self.assertFalse(state.errors)

    def test_init_should_raise_value_error_when_invalid_object_to_validate(self):
        #
        with self.assertRaises(ValueError) as context:
            ValidationState(None)

        # Assert
        self.assertEqual("Object to validate must not be None", str(context.exception))

    def test_add_error_should_add_to_list(self):
        # Arrange
        state = ValidationState(self.fixtures.person())
        error = self.fixtures.validation_error()

        # Act
        state.add_error(error)

        # Assert
        self.assertTrue(error in state.errors)


if __name__ == '__main__':
    unittest.main()
