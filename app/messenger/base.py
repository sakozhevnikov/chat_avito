from abc import ABC, abstractmethod

class MessengerAdapter(ABC):
    @abstractmethod
    async def send_message(self, chat_id: str, text: str) -> None:
        ...