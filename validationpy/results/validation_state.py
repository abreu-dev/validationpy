"""
ValidationState module.
"""

from typing import Generic, TypeVar
from validationpy.results.validation_error import ValidationError

ObjectT = TypeVar("ObjectT")


class ValidationState(Generic[ObjectT]):
    """
    The state of a validation.

    Attributes
    ----------
    _errors: list[ValidationError]
        A collection of errors.
    _object_to_validate: ObjectT
        Object being validated.
    """

    def __init__(self, object_to_validate: ObjectT) -> None:
        if object_to_validate is None:
            raise ValueError("Object to validate must not be None")

        self._object_to_validate: ObjectT = object_to_validate
        self._errors: list[ValidationError] = []

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
