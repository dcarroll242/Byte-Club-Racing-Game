from __future__ import annotations
import pygame

pygameEventListeners: dict[int, list[PygameEventListener]] = dict()

class PygameEventListener:

    def __init__(self, eventToListenFor: int, onEvent: callable, *args):
        self.eventToListenFor = eventToListenFor
        self.onEvent = onEvent
        self.onEventArgs = args

    def executeFunction(self):
        self.onEvent(*self.onEventArgs)

def createPygameEventListener(eventToListenFor: int, onEvent: callable, *args):
    if eventToListenFor not in pygameEventListeners.keys():
        pygameEventListeners[eventToListenFor] = [PygameEventListener(eventToListenFor, onEvent, *args)]
    else:
        pygameEventListeners[eventToListenFor].append(PygameEventListener(eventToListenFor, onEvent, *args))

def broadcastPygameEvents(events: list[pygame.event.EventType]):
    for event in events:
        if event.type in pygameEventListeners.keys():
            for listener in pygameEventListeners[event.type]:
                listener.executeFunction()
