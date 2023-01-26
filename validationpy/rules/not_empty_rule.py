"""
NotEmptyRule module.
"""

from string import Template
from typing import TypeVar
from validationpy.results.validation_state import ValidationState
from validationpy.rules.attribute_rule import AttributeRule

ObjectT = TypeVar("ObjectT")
AttributeT = TypeVar("AttributeT")


class NotEmptyRule(AttributeRule[ObjectT, AttributeT]):
    """
    Defines a not empty rule for any attribute type.
    """

    def is_valid(self, state: ValidationState[ObjectT], value: AttributeT) -> bool:
        if value is None:
            return False

        if type(value) == str:
            return bool(value) and bool(value.strip())

        return value != type(value)()

    def get_template_message(self) -> Template:
        return Template("'$attribute_name' must not be empty")
