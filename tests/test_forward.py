"""
tests > test_forward

Tests for forwarded messages, including encoding and decoding

Authors:
* Miguel Guthridge
"""

import pytest
from fl_context import FlContext

from tests.helpers import DummyDevice2, DummyDeviceContext

from common.exceptions import (
    EventEncodeError,
    EventInspectError,
    # EventDecodeError,
    # EventDispatchError,
)
from common.types import EventData
from common.util.events import (
    encodeForwardedEvent,
    decodeForwardedEvent,
    isEventForwarded,
    isEventForwardedHere,
    isEventForwardedHereFrom,
    forwardEvent,
)


def test_encode_decode():
    """When an event is encoded then decoded, is it still equivalent?"""
    with DummyDeviceContext():
        e = EventData(1, 2, 3)
        assert e == decodeForwardedEvent(EventData(encodeForwardedEvent(e, 1)))

        e = EventData([5, 2, 7, 4, 1])
        assert e == decodeForwardedEvent(EventData(encodeForwardedEvent(e, 1)))


def test_invalid_event_forward():
    """Test that forwarding an event without specifying a target fails from
    the main script
    """
    with DummyDeviceContext():
        with pytest.raises(EventEncodeError):
            encodeForwardedEvent(EventData(1, 2, 3))


def test_invalid_event_receive():
    """Test that receiving a forwarded event fails on the main script when
    no from index is specified
    """
    with DummyDeviceContext(2):
        e = EventData(encodeForwardedEvent(EventData(1, 2, 3)))

    with DummyDeviceContext(1):
        with pytest.raises(EventInspectError):
            assert isEventForwardedHereFrom(e)


def test_isEventForwarded():
    """Make sure the forwarded event type checker is working"""
    with DummyDeviceContext():
        assert isEventForwarded(EventData(
            encodeForwardedEvent(EventData(1, 2, 3), 1)
        ))

        assert not isEventForwarded(EventData(1, 2, 3))


def test_isEventForwardedHere():
    with DummyDeviceContext(2):
        e = EventData(encodeForwardedEvent(EventData(1, 2, 3)))

    with DummyDeviceContext(1):
        assert isEventForwardedHere(e)

    with DummyDeviceContext(2, DummyDevice2):
        assert not isEventForwardedHere(e)


def test_isEventForwardedHereFrom():
    with DummyDeviceContext(2):
        e = EventData(encodeForwardedEvent(EventData(1, 2, 3)))

    with DummyDeviceContext(1):
        assert isEventForwardedHereFrom(e, 2)
        assert not isEventForwardedHereFrom(e, 3)


def test_isEventForwardedHereFrom_target():
    with DummyDeviceContext(1):
        e = EventData(encodeForwardedEvent(EventData(1, 2, 3), 2))

    with DummyDeviceContext(2):
        assert isEventForwardedHereFrom(e)


def testForwardChecking():
    """Make sure checks are put into place before we forward an event"""
    with DummyDeviceContext(2):
        with FlContext({"dispatch_targets": [1]}):
            forwardEvent(EventData(7, 8, 9))
