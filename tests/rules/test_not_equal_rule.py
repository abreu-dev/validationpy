from faker import Faker
from tests.mocks import mock_product, Product, mock_orders, mock_locale_names
from unittest import TestCase, main
from unittest.mock import Mock
from validationpy.results.validation_state import ValidationState
from validationpy.rules.not_equal_rule import NotEqualRule
from validationpy.utils.message_constructor import MessageConstructor


class TestNotEqualRule(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
        self.product = mock_product(self.faker)

        self.mock_append_argument = Mock()
        self.mock_message_constructor = Mock(spec=MessageConstructor)
        self.mock_message_constructor.append_argument = self.mock_append_argument
        self.mock_state = Mock(spec=ValidationState[Product], object_to_validate=self.product)
        self.mock_state.message_constructor = self.mock_message_constructor
    # endregion

    # region __init__
    def test_init_should_set_attributes(self):
        # Arrange
        value_to_compare = self.faker.name()

        # Act
        rule = NotEqualRule[Product, str](value_to_compare)

        # Assert
        self.assertEqual(value_to_compare, rule._value_to_compare)

    # endregion

    # region validate
    # region StringTypes
    def test_validate_should_return_true_when_equal_str(self):
        # Arrange
        value_to_compare = self.faker.name()
        rule = NotEqualRule[Product, str](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(self.mock_state, self.product.name))
        self.mock_append_argument.assert_not_called()

    def test_validate_should_return_false_when_not_equal_str(self):
        # Arrange
        value_to_compare = self.product.name
        rule = NotEqualRule[Product, str](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(self.mock_state, self.product.name))
        self.mock_append_argument.assert_called_once_with('comparison_value', value_to_compare)
    # endregion

    # region NumericTypes
    def test_validate_should_return_true_when_equal_int(self):
        # Arrange
        value_to_compare = self.faker.pyint(min_value=1)
        rule = NotEqualRule[Product, int](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(self.mock_state, self.product.identifier))
        self.mock_append_argument.assert_not_called()

    def test_validate_should_return_false_when_not_equal_int(self):
        # Arrange
        value_to_compare = self.product.identifier
        rule = NotEqualRule[Product, int](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(self.mock_state, self.product.identifier))
        self.mock_append_argument.assert_called_once_with('comparison_value', value_to_compare)

    def test_validate_should_return_true_when_equal_float(self):
        # Arrange
        value_to_compare = self.faker.pyfloat(min_value=0.1)
        rule = NotEqualRule[Product, float](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(self.mock_state, self.product.quantity_available))
        self.mock_append_argument.assert_not_called()

    def test_validate_should_return_false_when_not_equal_float(self):
        # Arrange
        value_to_compare = self.product.quantity_available
        rule = NotEqualRule[Product, float](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(self.mock_state, self.product.quantity_available))
        self.mock_append_argument.assert_called_once_with('comparison_value', value_to_compare)

    def test_validate_should_return_true_when_equal_complex(self):
        # Arrange
        value_to_compare = 2+1j
        rule = NotEqualRule[Product, complex](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(self.mock_state, 1 + 1j))
        self.mock_append_argument.assert_not_called()

    def test_validate_should_return_false_when_not_equal_complex(self):
        # Arrange
        value_to_compare = 1+1j
        rule = NotEqualRule[Product, complex](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(self.mock_state, 1 + 1j))
        self.mock_append_argument.assert_called_once_with('comparison_value', value_to_compare)
    # endregion

    # region SequenceTypes
    def test_validate_should_return_true_when_equal_list(self):
        # Arrange
        value_to_compare = mock_orders(self.product.identifier, self.faker, 5)
        rule = NotEqualRule[Product, list](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(self.mock_state, self.product.orders))
        self.mock_append_argument.assert_not_called()

    def test_validate_should_return_false_when_not_equal_list(self):
        # Arrange
        value_to_compare = self.product.orders
        rule = NotEqualRule[Product, list](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(self.mock_state, self.product.orders))
        self.mock_append_argument.assert_called_once_with('comparison_value', value_to_compare)

    def test_validate_should_return_true_when_equal_tuple(self):
        # Arrange
        value_to_compare = (self.faker.pyfloat(min_value=0.1), self.faker.currency_code())
        rule = NotEqualRule[Product, tuple](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(self.mock_state, self.product.currency))
        self.mock_append_argument.assert_not_called()

    def test_validate_should_return_false_when_not_equal_tuple(self):
        # Arrange
        value_to_compare = self.product.currency
        rule = NotEqualRule[Product, tuple](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(self.mock_state, self.product.currency))
        self.mock_append_argument.assert_called_once_with('comparison_value', value_to_compare)
    # endregion

    # region MappingType
    def test_validate_should_return_true_when_equal_dict(self):
        # Arrange
        value_to_compare = mock_locale_names(self.faker, 5)
        rule = NotEqualRule[Product, dict](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(self.mock_state, self.product.locale_names))
        self.mock_append_argument.assert_not_called()

    def test_validate_should_return_false_when_not_equal_dict(self):
        # Arrange
        value_to_compare = self.product.locale_names
        rule = NotEqualRule[Product, dict](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(self.mock_state, self.product.locale_names))
        self.mock_append_argument.assert_called_once_with('comparison_value', value_to_compare)
    # endregion
    # endregion

    # region get_template_message
    def test_get_template_message_should_return_template(self):
        # Arrange
        rule = NotEqualRule[object, object](object)

        # Act
        template = rule.get_template_message()

        # Assert
        self.assertEqual("'$attribute_name' must not be equal to '$comparison_value'",
                         template.template)
    # endregion


if __name__ == '__main__':
    main()
