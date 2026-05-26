import os
from pathlib import Path

class Retriever:
    # Кэш для хранения загруженных данных
    _cache: dict = {}
    _data_loaded: bool = False

    @classmethod
    async def _load_data(cls):
        """Загружает все FAQ-файлы в память"""
        if cls._data_loaded:
            return

        data_dir = Path("data/faq")
        if not data_dir.exists():
            cls._data_loaded = True
            return

        all_qa = []
        for file_path in data_dir.glob("*.txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Разделяем на блоки "Вопрос-Ответ"
                blocks = content.strip().split("\n\n")
                for block in blocks:
                    lines = block.strip().split("\n")
                    if len(lines) >= 2:
                        question = lines[0].replace("Вопрос:", "").strip()
                        answer = lines[1].replace("Ответ:", "").strip()
                        all_qa.append({"question": question, "answer": answer})

        cls._cache["faq"] = all_qa
        cls._data_loaded = True

    @classmethod
    async def search(cls, query: str) -> str:
        """Ищет наиболее релевантный ответ"""
        await cls._load_data()

        faq = cls._cache.get("faq", [])
        if not faq:
            return ""

        # Простой поиск по ключевым словам
        query_lower = query.lower()
        best_match = None
        best_score = 0

        for item in faq:
            # Считаем, сколько слов из запроса есть в вопросе
            question_lower = item["question"].lower()
            score = sum(1 for word in query_lower.split() if word in question_lower)

            if score > best_score:
                best_score = score
                best_match = item

        if best_match and best_score > 0:
            return f"Вопрос: {best_match['question']}\nОтвет: {best_match['answer']}"

        return ""