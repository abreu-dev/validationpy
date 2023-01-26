"""
PropertyRule module.
"""

from abc import abstractmethod
from string import Template
from typing import Generic, TypeVar
from validationpy.results.validation_state import ValidationState

ObjectT = TypeVar("ObjectT")
AttributeT = TypeVar("AttributeT")


class AttributeRule(Generic[ObjectT, AttributeT]):
    """
    The abstract class of an attribute rule of any object and attribute.
    """

    @abstractmethod
    def is_valid(self, state: ValidationState[ObjectT], value: AttributeT) -> bool:
        """
        Validates a specific attribute value.

        Parameters
        ----------
        state: ValidationState[ObjectT]
            The validation state.
        value: AttributeT
            The current attribute value to validate.

        Returns
        -------
        bool
            True if valid.
            False if not valid.
        """

    @abstractmethod
    def get_template_message(self) -> Template:
        """
        Returns
        -------
        str
            The message template for this rule.
        """
