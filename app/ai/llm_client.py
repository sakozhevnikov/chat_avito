import aiohttp
from app.core.config import settings

class LLMClient:
    async def generate(self, user_message: str, context: str = "", state: dict = None) -> str:
        prompt = "Ты — вежливый ассистент по остеклению. Отвечай кратко и по делу.\n"
        if context:
            prompt += f"Информация: {context}\n"
        prompt += f"Пользователь: {user_message}\nАссистент:"

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{settings.OLLAMA_URL}/api/generate",
                json={"model": settings.MODEL_NAME, "prompt": prompt, "stream": False}
            ) as resp:
                data = await resp.json()
                return data["response"]