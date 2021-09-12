from __future__ import annotations

from typing import Any
from enum import Enum, auto

defaults = {}


class DefaultEnum(Enum):
    """An Enum class that can return its default value"""

    @classmethod
    def get_default(cls) -> Enum | None:
        """Get default value"""

        return defaults.get(cls)


class SizePolicy(DefaultEnum):
    """Values according to which Widget sizes are assigned

    FILL: keep the Widget's width set exactly to its parent
    STATIC: always use the set `width` value, don't adjust on resize
    RELATIVE: adjust the Widget's size to be a percentage of the parent
    """

    FILL = auto()
    STATIC = auto()
    RELATIVE = auto()


class WidgetAlignment(DefaultEnum):
    """Values to align widgets by.

    These are applied by the parent object, and are
    relative to them."""

    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


defaults[SizePolicy] = SizePolicy.FILL
defaults[WidgetAlignment] = WidgetAlignment.CENTER
