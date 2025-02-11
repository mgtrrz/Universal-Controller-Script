"""
devices > controlgenerators

Contains definitions for helper functions for creating and binding common
controls quickly

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]
"""

__all__ = [
    'NoteMatcher',
    'NoteAfterTouchMatcher',
    'PedalMatcher',
]

from .notes import NoteMatcher, NoteAfterTouchMatcher
from .pedals import PedalMatcher
