from faker import Faker
from tests.mocks import mock_product
from unittest import TestCase, main
from unittest.mock import Mock
from validationpy.results.validation_state import ValidationState
from validationpy.results.validation_error import ValidationError


class TestValidationState(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
        self.product = mock_product(self.faker)
    # endregion

    # region __init__
    def test_init_should_set_attributes(self):
        # Arrange
        object_to_validate = self.product

        # Act
        state = ValidationState(object_to_validate)

        # Assert
        self.assertEqual(object_to_validate, state.object_to_validate)
        self.assertIsNotNone(state.errors)
        self.assertFalse(state.errors)
        self.assertIsNotNone(state.message_constructor)
        self.assertIsNotNone(state.attribute_chain)
    # endregion

    # region add_error
    def test_add_error_should_add_to_list(self):
        # Arrange
        state = ValidationState(self.product)
        error = Mock(spec=ValidationError)

        # Act
        state.add_error(error)

        # Assert
        self.assertTrue(error in state.errors)
    # endregion


if __name__ == '__main__':
    main()
