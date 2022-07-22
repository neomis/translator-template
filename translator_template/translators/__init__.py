"""Translator Import method."""
from __future__ import annotations
import sys
from typing import Callable
from .example import main as translate_example

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points

__all__ = ('TRANSLATORS',)
TRANSLATORS: dict[str, Callable[[str], None]] = {
    'TRANSLATE_EXAMPLE': translate_example}
translators = entry_points(group='translator_template.translators')
for translator in translators:
    TRANSLATORS[f"TRANSLATE_{translator.name.upper()}"] = translator.load()
