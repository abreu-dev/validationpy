"""
NotEmptyRule module.
"""

from string import Template
from typing import TypeVar
from validationpy.results.validation_state import ValidationState
from validationpy.rules.abstract_rule import AbstractRule

ObjectT = TypeVar("ObjectT")
AttributeT = TypeVar("AttributeT")


class NotEmptyRule(AbstractRule[ObjectT, AttributeT]):
    """
    Defines a not empty rule for any attribute type.
    """

    def validate(self, state: ValidationState[ObjectT], value: AttributeT) -> bool:
        if value is None:
            return False

        if isinstance(value, str):
            return bool(value) and bool(value.strip())

        return value != type(value)()

    def get_template_message(self) -> Template:
        return Template("'$attribute_name' must not be empty")
