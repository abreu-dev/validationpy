"""
ValidationState module.
"""

from typing import Generic, TypeVar
from validationpy.results.validation_error import ValidationError
from validationpy.utils.attribute_chain import AttributeChain
from validationpy.utils.message_constructor import MessageConstructor

ObjectT = TypeVar("ObjectT")


class ValidationState(Generic[ObjectT]):
    """
    The state of a validation of any object.

    Attributes
    ----------
    _errors: list[ValidationError]
        A collection of errors.
    _object_to_validate: ObjectT
        Object being validated.
    _message_constructor: MessageConstructor
        The error messages constructor.
    _attribute_chain: AttributeChain
        The chain of attributes.
    """

    def __init__(self, object_to_validate: ObjectT) -> None:
        self._object_to_validate: ObjectT = object_to_validate
        self._errors: list[ValidationError] = []
        self._message_constructor: MessageConstructor = MessageConstructor()
        self._attribute_chain: AttributeChain = AttributeChain

    def add_error(self, error: ValidationError) -> None:
        """
        Adds a new validation error.

        Parameters
        ----------
        error: ValidationError
            The validation error to add.
        """

        self._errors.append(error)

    @property
    def errors(self) -> list[ValidationError]:
        """
        Returns
        -------
        list[ValidationError]
            A collection of errors.
        """

        return self._errors

    @property
    def object_to_validate(self) -> ObjectT:
        """
        Returns
        -------
        ObjectT
            Object being validated.
        """

        return self._object_to_validate

    @property
    def message_constructor(self) -> MessageConstructor:
        """
        Returns
        -------
        MessageConstructor
            The error messages constructor.
        """

        return self._message_constructor

    @property
    def attribute_chain(self) -> AttributeChain:
        """
        Returns
        -------
        AttributeChain
            The chain of attributes.
        """

        return self._attribute_chain
