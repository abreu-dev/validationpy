"""
MessageConstructor module.
"""

from string import Template
from typing import Any


class MessageConstructor:
    """
    Helps in the construction of message template.

    Attributes
    ----------
    _placeholders: dict[str, Any]
        A dictionary of placeholders to use in validation message template
    """

    ATTRIBUTE_NAME_KEY: str = "attribute_name"
    ATTRIBUTE_VALUE_KEY: str = "attribute_value"

    def __init__(self) -> None:
        self._placeholders: dict[str, Any] = {}

    def append_argument(self, key: str, value: Any) -> None:
        """
        Adds a value to the placeholders.

        Parameters
        ----------
        key: str
            The placeholder key.
        value: Any
            The placeholder value.
        """

        self._placeholders[key] = value

    def append_attribute_name(self, name: str) -> None:
        """
        Appends an attribute name to the placeholders.

        Parameters
        ----------
        name: str
            The name of the attribute.
        """

        self.append_argument(self.ATTRIBUTE_NAME_KEY, name)

    def append_attribute_value(self, value: Any) -> None:
        """
        Appends an attribute value to the placeholders.

        Parameters
        ----------
        value: Any
            The value of the attribute.
        """

        self.append_argument(self.ATTRIBUTE_VALUE_KEY, value)

    def construct(self, raw_template: Template) -> str:
        """
        Constructs the final message from the specified template applying placeholders.

        ...

        Parameters
        ----------
        raw_template: Template
            The message template.

        Returns
        -------
        str
            The message with applied placeholders.
        """

        return raw_template.substitute(self._placeholders)

    def clear(self) -> None:
        """
        Clear the placeholders.
        """

        self._placeholders.clear()

    @property
    def placeholders(self) -> dict[str, Any]:
        """
        Returns
        -------
        dict[str, Any]
            A dictionary of placeholders to use in validation message template
        """

        return self._placeholders
