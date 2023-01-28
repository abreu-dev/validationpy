"""Provide AbstractValidator class.
"""

from abc import ABC
from typing import Callable, Generic, TypeVar
from validationpy.results.validation_result import ValidationResult
from validationpy.results.validation_state import ValidationState
from validationpy.rules.rule_composite import RuleComposite

ObjectT = TypeVar("ObjectT")
AttributeT = TypeVar("AttributeT")


class AbstractValidator(ABC, Generic[ObjectT]):
    """Base class for object validators.

    Attributes
    ----------
    _composites : list[RuleComposite[ObjectT]]
        A collection of composite rules.
    """

    def __init__(self) -> None:
        self._composites: list[RuleComposite[ObjectT]] = []

    def _rule_for(self, attribute_accessor: Callable[[ObjectT], AttributeT]) -> None:
        """Defines a rule composite for the specified attribute.

        Parameters
        ----------
        attribute_accessor : Callable[[ObjectT], AttributeT]
            Lambda expression used to get the attribute value.
        """

        composite = RuleComposite[ObjectT](attribute_accessor)
        self._composites.append(composite)

        return None

    def validate(self, object_to_validate: ObjectT) -> ValidationResult:
        """Validates the specified object.

        Parameters
        ----------
        object_to_validate : ObjectT
            The object to validate.

        Returns
        -------
        ValidationResult
            A ValidationResult object containing validation errors found in composites.
        """

        state = ValidationState[ObjectT](object_to_validate)

        for composite in self._composites:
            composite.validate(state)

        result = ValidationResult(state.errors)

        return result
