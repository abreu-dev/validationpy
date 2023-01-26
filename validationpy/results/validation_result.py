"""
ValidationResult module.
"""

from validationpy.results.validation_error import ValidationError


class ValidationResult:
    """
    The result of a validator.

    Attributes
    ----------
    _errors: list[ValidationError]
        A collection of errors.
    """

    def __init__(self, errors: list[ValidationError] | None = None) -> None:
        if errors is None:
            self._errors: list[ValidationError] = []
        else:
            self._errors = list(filter(lambda error: error is not None, errors))

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
    def is_valid(self) -> bool:
        """
        Check if contains any errors.

        Returns
        -------
        bool
            False when length of errors is zero.
            True when length of errors is greater than zero.
        """

        return len(self._errors) > 0

    def __str__(self) -> str:
        separator: str = "\n"
        return separator.join(list(map(lambda error: error.message, self._errors)))
