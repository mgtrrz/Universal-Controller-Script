"""
controlsurfaces > valuestrategies > ivaluestrategy

Contains IValueStrategy: the interface for value strategies.

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]
"""

from abc import abstractmethod
from typing import Generic, TypeVar

from common.types import EventData

T = TypeVar("T")


class IValueStrategy(Generic[T]):
    """
    Represents a strategy for getting a value from an event and storing it.

    This can be used alongside basic control surface definitions to define
    relatively simple event types.
    """
    @abstractmethod
    def getValueFromEvent(self, event: EventData) -> T:
        """
        Returns a value for internal use given a MIDI event.

        This value is only used by the strategy, and therefore can be of any
        reasonable type, as long as that type can be converted to a float
        value.

        ### Args:
        * `event` (`eventData`): event to get value from

        ### Returns:
        * `T`: any type representing the internal value of the event
        """
        raise NotImplementedError("This function needs to be overridden by "
                                  "child classes")

    @abstractmethod
    def getChannelFromEvent(self, event: EventData) -> int:
        """
        Return the channel number associated with an event

        ### Args:
        * `event` (`EventData`): event to analyse

        ### Returns:
        * `int`: channel number or `-1` for no channel
        """
        raise NotImplementedError("This function needs to be overridden by "
                                  "child classes")

    @abstractmethod
    def getValueFromFloat(self, f: float) -> T:
        """
        Convert a float between 0-1 to the internal value used by this
        strategy.

        ### Args:
        * `f` (`float`): A floating point value between 0-1

        ### Returns:
        * `T`: any type representing the internal value of the event
        """
        raise NotImplementedError("This function needs to be overridden by "
                                  "child classes")

    @abstractmethod
    def getFloatFromValue(self, value: T) -> float:
        """
        Convert an internal value into a floating point value between 0-1

        ### Args:
        * `value` (`T`): the type representing the internal value of the event

        ### Returns:
        * `float`: A floating point value between 0-1
        """
        raise NotImplementedError("This function needs to be overridden by "
                                  "child classes")
