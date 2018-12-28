import abc
import asyncio as aio


class Bot(abc.ABC):

    _handler = None

    def __init__(self, connector, session_store, loop=None):
        self._connector = connector
        self._session_store = session_store
        self._loop = loop

    def create_request_handler(self):
        if self._handler is None:
            raise RuntimeError("Handler has not been set yet. Use bot.on_event")
        return self._request_handler

    async def _request_handler(self, request_body, request_context=None):
        contexts = self._connector.map_request_to_contexts(request_body)
        for context in contexts:
            await self._handler(context)

    def on_event(self, handler):
        if not aio.iscoroutinefunction(handler):
            raise TypeError("Handler should be a coroutine function")
        self._handler = handler
