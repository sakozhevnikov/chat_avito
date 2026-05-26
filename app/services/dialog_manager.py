class DialogManager:
    def __init__(self, chat_id: str):
        self.chat_id = chat_id

    async def get_state(self) -> dict:
        # Пока без состояния
        return {}