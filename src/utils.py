import json

from src.config import OPERATIONS_PATH


def load_operations() -> list[dict]:
    """
    Загружает список операций из файла
    :return: json с операциями
    """
    with open(OPERATIONS_PATH, encoding='utf-8') as file:
        return json.load(file)
