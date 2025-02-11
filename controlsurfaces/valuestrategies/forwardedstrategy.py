"""
controlsurfaces > valuestrategies > forwardedstrategy

Contains the definition for the ForwardedStrategy strategy for getting values
from forwarded events

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]
"""

from common.types import EventData
from common.util.events import decodeForwardedEvent, isEventForwarded
from . import IValueStrategy


class ForwardedStrategy(IValueStrategy):
    """
    Value strategy used to get data out of
    forwarded events.
    """

    def __init__(self, strat: IValueStrategy) -> None:
        self._strat = strat

    def getValueFromEvent(self, event: EventData):
        # The value is already matching, so we can cheat somewhat with getting
        # the data out
        return self._strat.getValueFromEvent(decodeForwardedEvent(event))

    def getChannelFromEvent(self, event: EventData):
        return self._strat.getChannelFromEvent(decodeForwardedEvent(event))

    def getValueFromFloat(self, f: float):
        return self._strat.getValueFromFloat(f)

    def getFloatFromValue(self, value) -> float:
        return self._strat.getFloatFromValue(value)


class ForwardedUnionStrategy(IValueStrategy):
    """
    Value strategy for getting values from events that could be either
    forwarded or not
    """

    def __init__(self, strat: IValueStrategy) -> None:
        self._strat = strat
        self._strat_forward = ForwardedStrategy(strat)

    def getValueFromEvent(self, event: EventData):
        if isEventForwarded(event):
            return self._strat_forward.getValueFromEvent(event)
        else:
            return self._strat.getValueFromEvent(event)

    def getChannelFromEvent(self, event: EventData):
        if isEventForwarded(event):
            return self._strat_forward.getChannelFromEvent(event)
        else:
            return self._strat.getChannelFromEvent(event)

    def getValueFromFloat(self, f: float):
        return self._strat.getValueFromFloat(f)

    def getFloatFromValue(self, value) -> float:
        return self._strat.getFloatFromValue(value)
