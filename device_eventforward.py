# name=Universal Event Forwarder
# url=https://forum.image-line.com/viewtopic.php?f=1994&t=274277
# receiveFrom=Universal Controller
"""
device_eventforward

This script packages events into a format where they can be distinguished
and forwards the event on to the main controller. It can be used to link
multiple ports of a device together in a way such that overlapping event
IDs can be distinguished. The additional forwarding takes less than 1 ms, so
performance impact is negligible.

Authors:
* Miguel Guthridge
"""
# flake8: noqa

# Add our additional includes to the Python environment
import fl_typing

from common import consts
from common.contextmanager import catchContextResetException
from common.extensionmanager import ExtensionManager
from common.states import WaitingForDevice, ForwardState

from common import log, verbosity
from common import getContext
from common.consts import getVersionString

class OverallDevice:
    @catchContextResetException
    def onInit(self) -> None:
        getContext().initialise(WaitingForDevice(ForwardState))

    @catchContextResetException
    def onMidiIn(self, event) -> None:
        getContext().processEvent(event)

    @catchContextResetException
    def onIdle(self) -> None:
        getContext().tick()

    @catchContextResetException
    def bootstrap(self):
        log("bootstrap.initialize", "Load success", verbosity.INFO)
        print(consts.ASCII_HEADER_ART)
        print(f"Universal Event Forwarder: v{getVersionString()}")
        print(ExtensionManager.getInfo())

dev = OverallDevice()

def OnInit():
    dev.onInit()

def OnMidiIn(event):
    dev.onMidiIn(event)

def OnIdle():
    dev.onIdle()

def OnRefresh(flags: int):
    dev.onIdle()

def bootstrap():
    dev.bootstrap()

if __name__ == "__main__":
    bootstrap()
