"""Provide RuleWrapper class.
"""

from typing import Callable, Generic, TypeVar
from validationpy.results.validation_state import ValidationState
from validationpy.rules.abstract_rule import AbstractRule

ObjectT = TypeVar("ObjectT")
AttributeT = TypeVar("AttributeT")


class RuleWrapper(Generic[ObjectT, AttributeT]):
    """Defines a rule associated with a condition."""

    def __init__(self, rule: AbstractRule[ObjectT, AttributeT]) -> None:
        self._rule = rule
        self._condition: Callable[[ObjectT], bool] | None = None

    @property
    def rule(self) -> AbstractRule[ObjectT, AttributeT]:
        """Rule to apply.

        Returns
        -------
        AbstractRule[ObjectT, AttributeT]
            The rule.
        """

        return self._rule

    @property
    def condition(self) -> Callable[[ObjectT], bool] | None:
        """Condition to execute the rule.

        Returns
        -------
        Callable[[Any], bool] | None
            The condition.
        """

        return self._condition

    @condition.setter
    def condition(self, condition: Callable[[ObjectT], bool]) -> None:
        """Sets the condition to execute the rule.

        Parameters
        ----------
        condition : Callable[[ObjectT], bool]
            The condition.
        """

        self._condition = condition

    def validate(self, state: ValidationState[ObjectT], value: AttributeT) -> bool:
        """Validates the specified value through the rule.

        Parameters
        ----------
        state : ValidationState[ObjectT]
            The validation state.
        value : AttributeT
            The value to validate.

        Returns
        -------
        bool
            Result of the rule validation.
        """

        return self._rule.validate(state, value)
