import json

from config import OPERATIONS_PATH
from src.models import Operation


def load_operations() -> list[dict]:
    """
    Загружает список операций из файла.
    :return: json с операциями.
    """
    with open(OPERATIONS_PATH, encoding='utf-8') as file:
        return json.load(file)


def get_information_operation(operations: list[dict]) -> list[Operation]:
    """
    Получение информации о всех операциях.
    :param operations: Список с операциями.
    :return: Информация о операциях.
    """
    information_operation = []
    for operation in operations:
        if operation:
            information_operation.append(Operation(pk=operation["id"],
                                                   date=operation["date"],
                                                   state=operation["state"],
                                                   amount=operation["operationAmount"],
                                                   description=operation["description"],
                                                   from_=operation.get("from", "Нет информации"),
                                                   to=operation["to"]))
    return information_operation
