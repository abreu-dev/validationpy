"""Provide RuleComposite class.
"""

from typing import Any, Callable, Generic, TypeVar
from validationpy.results.validation_error import ValidationError
from validationpy.results.validation_state import ValidationState
from validationpy.rules.abstract_rule import AbstractRule
from validationpy.rules.rule_wrapper import RuleWrapper

ObjectT = TypeVar("ObjectT")
AttributeT = TypeVar("AttributeT")


class RuleComposite(Generic[ObjectT, AttributeT]):
    """Defines a list of rules associated with an attribute.

    Attributes
    ----------
    _attribute_accessor : Callable[[ObjectT], AttributeT]
        Lambda expression to get the attribute value.
    _rule_wrappers : list[RuleWrapper[ObjectT, AttributeT]]
        Collection of rule wrapper.
    _condition : Callable[[ValidationState[ObjectT]], bool] | None
        Condition to execute all rule wrappers.
    """

    def __init__(self, attribute_accessor: Callable[[ObjectT], AttributeT]) -> None:
        self._attribute_accessor = attribute_accessor
        self._rule_wrappers: list[RuleWrapper[ObjectT, AttributeT]] = []
        self._condition: Callable[[ValidationState[ObjectT]], bool] | None = None

    def add_rule(self, rule: AbstractRule[ObjectT, AttributeT]) -> None:
        """Adds a new rule.

        Parameters
        ----------
        rule : AbstractRule[ObjectT, AttributeT]
            The rule to add.
        """

        wrapper = RuleWrapper[ObjectT, AttributeT](rule)
        self._rule_wrappers.append(wrapper)

    def validate(self, state: ValidationState[ObjectT]) -> None:
        """Executes all rules added to the instance.

        Performs using validation state and adds validation errors to the state.

        Parameters
        ----------
        state : ValidationState[ObjectT]
        """

        if self._condition is not None:
            if not self._condition(state):
                return

        value = self._attribute_accessor(state.object_to_validate)

        for wrapper in self._rule_wrappers:
            valid = wrapper.validate(state, value)

            if not valid:
                error = self._create_validation_error(state, value, wrapper)
                state.add_error(error)

    @staticmethod
    def _create_validation_error(state: ValidationState[ObjectT],
                                 value: AttributeT,
                                 wrapper: RuleWrapper) -> ValidationError:
        """Creates a validation error.

        Parameters
        ----------
        state : ValidationState[ObjectT]
            The validation state.
        value : AttributeT
            The attribute value being validated.
        wrapper : RuleWrapper
            The rule wrapper associated with the error.

        Returns
        -------
        ValidationError
            The validation error created.
        """

        error = ValidationError("", "", value)

        return error


