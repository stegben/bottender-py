import abc


class Connector(abc.ABC):

    @abc.abstractmethod
    def map_request_to_contexts(self, body):
        pass

    @abc.abstractmethod
    def get_unique_session_key(self, body):
        pass

    @abc.abstractmethod
    def create_context(
            self,
            event,
            session,
            initial_state,
            request_context=None,
        ):
        pass

    @abc.abstractmethod
    def update_session(self, session, body):
        pass
