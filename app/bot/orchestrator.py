from app.services.dialog_manager import DialogManager
from app.ai.llm_client import LLMClient
from app.retrieval.retriever import Retriever

async def process_message(chat_id: str, user_message: str) -> str:
    # 1. Поиск по базе знаний (пока пусто)
    context = await Retriever.search(user_message)

    # 2. Состояние диалога (пока пусто)
    dialog = DialogManager(chat_id)
    state = await dialog.get_state()

    # 3. Генерация ответа
    llm = LLMClient()
    reply = await llm.generate(
        user_message=user_message,
        context=context,
        state=state
    )

    # 4. Сохранение в БД (пока пропускаем, чтобы не усложнять)
    # async with get_db_session() as session: ...

    return reply