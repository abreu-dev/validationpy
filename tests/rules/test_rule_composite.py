from faker import Faker
from tests.mocks import Product, mock_product
from typing import Callable
from unittest import TestCase, main
from unittest.mock import Mock
from validationpy.results.validation_error import ValidationError
from validationpy.results.validation_state import ValidationState
from validationpy.rules.abstract_rule import AbstractRule
from validationpy.rules.rule_composite import RuleComposite
from validationpy.rules.rule_wrapper import RuleWrapper


class TestRuleComposite(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
        self.product = mock_product(self.faker)

        self.mock_attribute_accessor = Mock(spec=Callable[[Product], str], return_value=self.product.name)
        self.composite = RuleComposite[Product, str](self.mock_attribute_accessor)
    # endregion

    # region __init__
    def test_init_should_set_properties(self):
        # Assert
        self.assertEqual(self.mock_attribute_accessor, self.composite._attribute_accessor)
        self.assertIsNotNone(self.composite._rule_wrappers)
        self.assertFalse(self.composite._rule_wrappers)
        self.assertIsNone(self.composite._condition)
    # endregion

    # region add_rule
    def test_add_rule_should_append_to_list(self):
        # Arrange
        mock_rule = Mock(spec=AbstractRule[Product, str])

        # Act
        self.composite.add_rule(mock_rule)

        # Assert
        self.assertTrue(any(mock_rule == wrapper.rule for wrapper in self.composite._rule_wrappers))
    # endregion

    # region validate
    def test_validate_should_stop_when_condition_not_met(self):
        # Arrange
        mock_condition = Mock(spec=Callable[[Product], bool], return_value=False)
        self.composite._condition = mock_condition

        mock_state = Mock(spec=ValidationState[Product], object_to_validate=self.product)

        # Act
        self.composite.validate(mock_state)

        # Assert
        mock_condition.assert_called_once_with(mock_state)
        self.mock_attribute_accessor.assert_not_called()

    def test_validate_should_do_nothing_when_condition_met_but_have_no_rules(self):
        # Arrange
        mock_condition = Mock(spec=Callable[[Product], bool], return_value=True)
        self.composite._condition = mock_condition

        mock_state = Mock(spec=ValidationState[Product], object_to_validate=self.product)

        # Act
        self.composite.validate(mock_state)

        # Assert
        mock_condition.assert_called_once_with(mock_state)
        self.mock_attribute_accessor.assert_called_once_with(mock_state.object_to_validate)

    def test_validate_should_call_rule_validator_and_do_nothing_when_validation_succeed(self):
        # Arrange
        mock_condition = Mock(spec=Callable[[Product], bool], return_value=True)
        self.composite._condition = mock_condition

        mock_rule = Mock(spec=AbstractRule[Product, str])
        mock_wrapper = Mock(spec=RuleWrapper[Product, str], rule=mock_rule)
        mock_wrapper.validate = Mock(return_value=True)
        self.composite._rule_wrappers.append(mock_wrapper)

        mock_state = Mock(spec=ValidationState[Product], object_to_validate=self.product)

        # Act
        self.composite.validate(mock_state)

        # Assert
        mock_condition.assert_called_once_with(mock_state)
        self.mock_attribute_accessor.assert_called_once_with(mock_state.object_to_validate)
        mock_wrapper.validate.assert_called_once_with(mock_state, self.product.name)

    def test_validate_should_call_rule_validator_and_add_error_when_validation_fail(self):
        # Arrange
        mock_condition = Mock(spec=Callable[[Product], bool], return_value=True)
        self.composite._condition = mock_condition

        mock_rule = Mock(spec=AbstractRule[Product, str])
        mock_wrapper = Mock(spec=RuleWrapper[Product, str], rule=mock_rule)
        mock_wrapper.validate = Mock(return_value=False)
        self.composite._rule_wrappers.append(mock_wrapper)

        mock_validation_error = Mock(spec=ValidationError)
        mock_create_validation_error = Mock(return_value=mock_validation_error)
        self.composite._create_validation_error = mock_create_validation_error

        mock_state = Mock(spec=ValidationState[Product], object_to_validate=self.product)

        # Act
        self.composite.validate(mock_state)

        # Assert
        mock_condition.assert_called_once_with(mock_state)
        self.mock_attribute_accessor.assert_called_once_with(mock_state.object_to_validate)
        mock_wrapper.validate.assert_called_once_with(mock_state, self.product.name)
        mock_create_validation_error.assert_called_once_with(mock_state, self.product.name, mock_wrapper)
        mock_state.add_error.assert_called_once_with(mock_validation_error)
    # endregion

    # region _create_validation_error
    def test_create_validation_error_should_return_expected(self):
        # Arrange
        mock_state = Mock(spec=ValidationState[Product], object_to_validate=self.product)
        mock_value = self.product.name
        mock_rule = Mock(spec=AbstractRule[Product, str])
        mock_wrapper = Mock(spec=RuleWrapper[Product, str], rule=mock_rule)

        # Act
        error = self.composite._create_validation_error(mock_state, mock_value, mock_wrapper)

        # Assert
        self.assertEqual("", error.attribute_name)
        self.assertEqual("", error.message)
        self.assertEqual(mock_value, error.attempted_value)
    # endregion


if __name__ == '__main__':
    main()
