import abc


class Session(abc.ABC):

    @abc.abstractmethod
    def serialize(self) -> str:
        pass

    @classmethod
    @abc.abstractmethod
    def deserialize(cls, deserializable: str) -> 'Session':
        pass

    @property
    @abc.abstractmethod
    def platform(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def id(self) -> str:
        pass
