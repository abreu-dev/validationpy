import unittest
from faker import Faker
from tests.mocks import mock_product, Product
from validationpy.results.validation_state import ValidationState
from validationpy.rules.not_empty_rule import NotEmptyRule


class TestNotEmptyRule(unittest.TestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        self.product = mock_product(self.faker)

    # region validate
    # region StringTypes
    def test_validate_should_return_true_when_valid_str(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, str]()

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.name))

    def test_validate_should_return_false_when_invalid_str(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, str]()

        # Act & Assert
        self.assertFalse(rule.validate(state, None))
        self.assertFalse(rule.validate(state, ""))
        self.assertFalse(rule.validate(state, " "))
    # endregion

    # region NumericTypes
    def test_validate_should_return_true_when_valid_int(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, int]()

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.identifier))

    def test_validate_should_return_false_when_invalid_int(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, int]()

        # Act & Assert
        self.assertFalse(rule.validate(state, None))
        self.assertFalse(rule.validate(state, 0))

    def test_validate_should_return_true_when_valid_float(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, float]()

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.quantity_available))

    def test_validate_should_return_false_when_invalid_float(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, float]()

        # Act & Assert
        self.assertFalse(rule.validate(state, None))
        self.assertFalse(rule.validate(state, 0.0))

    def test_validate_should_return_true_when_valid_complex(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, complex]()

        # Act & Assert
        self.assertTrue(rule.validate(state, 1 + 1j))
        self.assertTrue(rule.validate(state, -1 + 1j))

    def test_validate_should_return_false_when_invalid_complex(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, complex]()

        # Act & Assert
        self.assertFalse(rule.validate(state, None))
        self.assertFalse(rule.validate(state, 0 + 0j))
    # endregion

    # region SequenceTypes
    def test_validate_should_return_true_when_valid_list(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        rule = NotEmptyRule[Product, list]()

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.orders))

    def test_validate_should_return_false_when_invalid_list(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        rule = NotEmptyRule[Product, list]()

        # Act & Assert
        self.assertFalse(rule.validate(state, None))
        self.assertFalse(rule.validate(state, []))

    def test_validate_should_return_true_when_valid_tuple(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        rule = NotEmptyRule[Product, tuple]()

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.currency))

    def test_validate_should_return_false_when_invalid_tuple(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        rule = NotEmptyRule[Product, tuple]()

        # Act & Assert
        self.assertFalse(rule.validate(state, None))
        self.assertFalse(rule.validate(state, ()))
    # endregion

    # region MappingType
    def test_validate_should_return_true_when_valid_dict(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        rule = NotEmptyRule[Product, dict]()

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.locale_names))

    def test_validate_should_return_false_when_invalid_dict(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        rule = NotEmptyRule[Product, dict]()

        # Act & Assert
        self.assertFalse(rule.validate(state, None))
        self.assertFalse(rule.validate(state, {}))
    # endregion
    # endregion

    # region get_template_message
    def test_get_template_message_should_return_template(self):
        # Arrange
        rule = NotEmptyRule[object, object]()

        # Act
        template = rule.get_template_message()

        # Assert
        self.assertEqual("'$attribute_name' must not be empty", template.template)
    # endregion


if __name__ == '__main__':
    unittest.main()
