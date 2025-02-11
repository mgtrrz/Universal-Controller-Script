"""
controlsurfaces > fader

Defines a fader control surface

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]
"""
from .knob import Knob, MasterKnob
from common.eventpattern.ieventpattern import IEventPattern
from controlsurfaces.valuestrategies.ivaluestrategy import IValueStrategy
from . import ControlSurface


class GenericFader(ControlSurface):
    """
    Defines a fader (slider) control surface.
    Faders are generally mapped to linear parameters, such as volumes or effect
    levels.
    """


class Fader(GenericFader):
    """
    Defines a fader (as opposed to the master fader)
    """
    @staticmethod
    def getControlAssignmentPriorities() -> tuple[type[ControlSurface], ...]:
        # Fader controls should be assigned to knobs if faders aren't available
        return (Knob, )

    def __init__(
        self,
        event_pattern: IEventPattern,
        value_strategy: IValueStrategy,
        coordinate: tuple[int, int],
        group: str = "generic faders"
    ) -> None:
        super().__init__(event_pattern, value_strategy, group, coordinate)


class MasterFader(GenericFader):
    """
    Defines a master fader (as opposed to a normal fader). A controller should
    only have one master fader, which will be bound independently to the normal
    faders.
    """
    @staticmethod
    def getControlAssignmentPriorities() -> tuple[type[ControlSurface], ...]:
        # Fader controls should be assigned to knobs if faders aren't available
        return (MasterKnob, )

    def __init__(
        self,
        event_pattern: IEventPattern,
        value_strategy: IValueStrategy
    ) -> None:
        super().__init__(event_pattern, value_strategy, "master fader")
