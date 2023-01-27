"""
AttributeChain module.
"""

from inspect import getsource
from typing import Any, Callable


class AttributeChain:
    """
    Helps in the construction of attribute.

    Attributes
    ----------
    _path_in_parts: list[str]
        A collection of attribute path parts.
    """

    def __init__(self, path_in_parts: list[str] | None = None) -> None:
        if path_in_parts is not None:
            self._path_in_parts = path_in_parts
        else:
            self._path_in_parts = []

    @property
    def path_in_parts(self) -> list[str]:
        """
        Returns
        -------
        list[str]
            A collection of attribute path parts.
        """

        return self._path_in_parts

    def __str__(self) -> str:
        separator = "."
        return separator.join(self._path_in_parts)

    @staticmethod
    def from_lambda_expression(lambda_expression: Callable[[Any], Any]) -> 'AttributeChain':
        """
        Creates a new attribute chain from a lambda expression.

        Parameters
        ----------
        lambda_expression: Callable[[Any], Any]
            A lambda expression accessing an attribute.

        Returns
        -------
        AttributeChain
            The attribute chain with path in parts obtained from expression.
        """

        path_in_parts: list[str] = []

        expression_source = getsource(lambda_expression)
        expression_content = expression_source.split(':')[1].split(')')[0].strip()

        for path_part in expression_content.split('.')[1:]:
            path_in_parts.append(path_part)

        return AttributeChain(path_in_parts)
