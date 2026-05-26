class LLMClient:
    async def generate(self, user_message: str, context: str = "", state: dict = None) -> str:
        # Временная заглушка
        return f"Вы написали: {user_message}"