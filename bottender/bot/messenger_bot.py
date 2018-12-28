from .base import Bot
from .connector import MessengerConnector


class MessengerBot(Bot):

    def __init__(
            self,
            access_token,
            verify_token,
            app_id,
            app_secret,
            session_store,
            loop=None,
        ):
        connector = MessengerConnector(
            access_token=access_token,
        )
        super().__init__(connector, session_store)
