from faker import Faker
from tests.mocks import Product, mock_product
from typing import Callable
from unittest import TestCase, main
from unittest.mock import Mock
from validationpy.results.validation_state import ValidationState
from validationpy.rules.abstract_rule import AbstractRule
from validationpy.rules.rule_wrapper import RuleWrapper


class TestRuleWrapper(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
        self.product = mock_product(self.faker)
        self.mock_rule = Mock(spec=AbstractRule[Product, str])
        self.wrapper = RuleWrapper[Product, str](self.mock_rule)
    # endregion

    # region __init__
    def test_init_should_set_properties(self):
        # Assert
        self.assertEqual(self.mock_rule, self.wrapper.rule)
        self.assertIsNone(self.wrapper.condition)
    # endregion

    # region condition.setter
    def test_set_condition_should_set(self):
        # Arrange
        condition = Mock(spec=Callable[[Product], bool])

        # Act
        self.wrapper.condition = condition

        # Assert
        self.assertEqual(condition, self.wrapper.condition)
    # endregion

    # region validate
    def test_validate_should_call_rule_validate(self):
        # Arrange
        expected = self.faker.pybool()
        self.mock_rule.validate = Mock(return_value=expected)

        mock_state = Mock(spec=ValidationState[Product], object_to_validate=self.product)

        # Act
        actual = self.wrapper.validate(mock_state, self.product.name)

        # Assert
        self.assertEqual(expected, actual)
        self.mock_rule.validate.assert_called_once_with(mock_state, self.product.name)
    # endregion


if __name__ == '__main__':
    main()
