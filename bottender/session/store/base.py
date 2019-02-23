import abc

from ..base import Session


class SessionStore(abc.ABC):

    @abc.abstractmethod
    async def init(self):
        pass

    @abc.abstractmethod
    async def read(key: str):
        pass

    @abc.abstractmethod
    async def all(self):
        pass

    @abc.abstractmethod
    async def write(self, key: str, sess: Session):
        pass

    @abc.abstractmethod
    async def destroy(self, key: str):
        pass
