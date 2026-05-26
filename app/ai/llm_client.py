import aiohttp
from app.core.config import settings

class LLMClient:
    async def generate(self, user_message: str, context: str = "", state: dict = None) -> str:
        # Если нашли релевантную информацию в базе знаний
        if context:
            prompt = (
                "Ты — ассистент по остеклению. Используй информацию из базы знаний для ответа. "
                "Если информации недостаточно, задай уточняющий вопрос.\n\n"
                f"База знаний:\n{context}\n\n"
                f"Пользователь: {user_message}\n"
                "Ассистент (отвечай строго на основе базы знаний):"
            )
        else:
            prompt = (
                "Ты — ассистент по остеклению. Ты не знаешь точного ответа на этот вопрос. "
                "Вежливо предложи пользователю задать вопрос о типах остекления, ценах, гарантиях или вызвать замерщика.\n\n"
                f"Пользователь: {user_message}\n"
                "Ассистент:"
            )

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{settings.OLLAMA_URL}/api/generate",
                json={
                    "model": settings.MODEL_NAME,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1,  # низкая температура для точных ответов
                        "max_tokens": 300,
                    }
                }
            ) as resp:
                data = await resp.json()
                return data["response"].strip()