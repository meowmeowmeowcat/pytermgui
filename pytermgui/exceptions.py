"""
Custom Exception-s used in pytermgui.
"""

from __future__ import annotations

from dataclasses import dataclass, field

__all__ = [
    "WidthExceededError",
    "LineLengthError",
    "AnsiSyntaxError",
    "MarkupSyntaxError",
]


class TimeoutException(Exception):
    """Raised when an action has timed out."""


class WidthExceededError(Exception):
    """Raised when an element's width is larger than the screen."""


class LineLengthError(Exception):
    """Raised when a widget line is not the expected length."""


class ColorSyntaxError(Exception):
    """Raised when a color string could not be parsed into a `pytermgui.colors.Color`"""


@dataclass
class ParserSyntaxError(Exception):
    """Parent exception for unparsable strings.

    This exception takes some basic parameters, and formats
    a message depending on the _delimiters value. This has to
    be supplied by each child, while the rest of the arguments
    are to be given at construction."""

    tag: str
    cause: str
    context: str
    _delimiters: tuple[str, str] = field(init=False)

    @property
    def message(self) -> str:
        """Create message from tag, context and cause."""

        start, end = self._delimiters
        full = start + self.tag + end

        escaped_context = ascii(self.context).strip("'")
        highlighted = escaped_context.replace(
            full, "\x1b[31m\x1b[1m" + full + "\x1b[0m", 1
        )

        return f'Tag "{start}{self.tag}{end}" in string "{highlighted}" {self.cause}.'

    def escape_message(self) -> str:
        """Return message with markup tags escaped."""

        char = self._delimiters[0]
        return self.message.replace(char, "\\" + char)

    def __str__(self) -> str:
        """Show message."""

        return self.message


class MarkupSyntaxError(ParserSyntaxError):
    """Raised when parsed markup text contains an error."""

    _delimiters = ("[", "]")


class AnsiSyntaxError(ParserSyntaxError):
    """Raised when parsed ANSI text contains an error."""

    _delimiters = ("\\x1b[", "m")
