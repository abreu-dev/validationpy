"""
ValidationError module.
"""

from typing import Any


class ValidationError:
    """
    Represents a validation error.

    Attributes
    ----------
    _property_name : str
        The name of the property.
    _message : str
        The error message.
    _attempted_value : Any
        The property value that caused the error.
    _code : str | None, default None
        The code associated with the error.
    _template_placeholders : dict[str, str], default {}
        The placeholders used with the message.
    """

    def __init__(self, property_name: str, message: str, attempted_value: Any) -> None:
        if not isinstance(property_name, str):
            raise ValueError(f"Property name must be of type {str}")

        if not isinstance(message, str):
            raise ValueError(f"Message must be of type {str}")

        if attempted_value is None:
            raise ValueError("Attempted value must not be None")

        self._property_name: str = property_name
        self._message: str = message
        self._attempted_value: Any = attempted_value
        self._code: str | None = None
        self._template_placeholders: dict[str, str] = {}

    @property
    def property_name(self) -> str:
        """
        Returns
        -------
        str
            The name of the property.
        """

        return self._property_name

    @property
    def message(self) -> str:
        """
        Returns
        -------
        str
            The error message.
        """

        return self._message

    @property
    def attempted_value(self) -> Any:
        """
        Returns
        -------
        Any
            The property value that caused the error.
        """

        return self._attempted_value

    @property
    def code(self) -> str | None:
        """
        Returns
        -------
        str | None
            The code associated with the error.
            Or None if not set.
        """

        return self._code

    @property
    def template_placeholders(self) -> dict[str, str]:
        """
        Returns
        -------
        dict[str, str]
            The placeholders used with the message.
        """

        return self._template_placeholders

    def __str__(self) -> str:
        return self.message
