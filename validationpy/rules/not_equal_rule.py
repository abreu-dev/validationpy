"""
NotEmptyRule module.
"""

from string import Template
from typing import TypeVar
from validationpy.results.validation_state import ValidationState
from validationpy.rules.attribute_rule import AttributeRule

ObjectT = TypeVar("ObjectT")
AttributeT = TypeVar("AttributeT")


class NotEqualRule(AttributeRule[ObjectT, AttributeT]):
    """
    Defines a not equal rule for any attribute type.

    Attributes
    ----------
    _value_to_compare: AttributeT
        The value to compare with the attribute being validated.
    """

    def __init__(self, value_to_compare: AttributeT) -> None:
        self._value_to_compare = value_to_compare

    def is_valid(self, state: ValidationState[ObjectT], value: AttributeT) -> bool:
        success = not value == self._value_to_compare

        if not success:
            state.message_constructor.append_argument('comparison_value', self._value_to_compare)
            return False

        return True

    def get_template_message(self) -> Template:
        return Template("'$attribute_name' must not be equal to '$comparison_value'")
