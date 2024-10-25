from __future__ import annotations
import pygame

pygameEventListeners: dict[int, list[PygameEventListener]] = dict()

class PygameEventListener:
    """a wrapper class for a function that should be called when its corresponding pygameEvent occurs

    note: if an instance is instantiated directly, it will not successfully listen for events
          to make it successfully listen for events use the createPygameEventListener function instead"""
    def __init__(self, eventToListenFor: int, onEvent: callable, *args):
        self.eventToListenFor = eventToListenFor
        self.onEvent = onEvent
        self.onEventArgs = args

    def executeFunction(self):
        self.onEvent(*self.onEventArgs)

def createPygameEventListener(eventToListenFor: int, onEvent: callable, *args):
    """create a PygameEventListener, add it to the pygameEventListeners dict, and return the PygameEventListener

    also see broadcastPygameEvents docstring

    :param eventToListenFor: the int representing which pygame event to listen for
    :param onEvent: the function to call when the event occurs
    :param args: the args for the onEvent function (optional)
    :return: the PygameEventListener this function creates and adds to the pygameEventListeners dict
    """
    listener = PygameEventListener(eventToListenFor, onEvent, *args)
    if eventToListenFor not in pygameEventListeners.keys():
        pygameEventListeners[eventToListenFor] = [listener]
    else:
        pygameEventListeners[eventToListenFor].append(listener)
    return listener

def broadcastPygameEvents(events: list[pygame.event.EventType]):
    """broadcast all events to their listeners

    uses the 'pygameEventListeners' dict to execute the functions of all PygameEventListeners for all pygame events
    """
    for event in events:
        if event.type in pygameEventListeners.keys():
            for listener in pygameEventListeners[event.type]:
                listener.executeFunction()
