"""
ValidationError module.
"""

from typing import Any


class ValidationError:
    """
    Represents a validation error.

    Attributes
    ----------
    _attribute_name: str
        The name of the attribute.
    _message: str
        The error message.
    _attempted_value: Any
        The attribute value that caused the error.
    _code: str | None, default None
        The code associated with the error.
    _template_placeholders: dict[str, Any], default {}
        The placeholders used with the message.
    """

    def __init__(self, attribute_name: str, message: str, attempted_value: Any) -> None:
        self._attribute_name: str = attribute_name
        self._message: str = message
        self._attempted_value: Any = attempted_value
        self._code: str | None = None
        self._template_placeholders: dict[str, Any] = {}

    @property
    def attribute_name(self) -> str:
        """
        Returns
        -------
        str
            The name of the attribute.
        """

        return self._attribute_name

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
            The attribute value that caused the error.
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
        dict[str, Any]
            The placeholders used with the message.
        """

        return self._template_placeholders

    def __str__(self) -> str:
        return self.message
