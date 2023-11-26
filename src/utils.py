import json
from datetime import datetime
import datetime

from config import OPERATIONS_PATH
from src.models import Operation


def load_operations() -> list[dict]:
    """
    Загружает список операций из файла.
    :return: json с операциями.
    """
    with open(OPERATIONS_PATH, encoding='utf-8') as file:
        return json.load(file)


def get_information_operations(operations: list[dict]) -> list[Operation]:
    """
    Создание экземпляра класса с информацией о всех операциях.
    :param operations: Список с операциями.
    :return: Информация о операциях.
    """
    information_operations = []
    for operation in operations:
        if operation:
            information_operations.append(Operation(
                pk=operation["id"],
                date=operation["date"],
                state=operation["state"],
                amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", None),
                to=operation["to"]))
    return information_operations


def get_executed_operations(operations: list[Operation]) -> list[Operation]:
    """
    Получение списка выполненых операций.
    :param operations: Информация о операциях.
    :return: Список выполненых операций.
    """
    executed_operations = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_sorted_operations(operations: list[Operation]) -> list:
    """
    Получение отсортированных по дате операций.
    :param operations: Список операций.
    :return: Отсортированный список.
    """
    sorted_operation = []
    operations.sort(key=lambda x: datetime.datetime.strptime(x.get_date(), "%d.%m.%Y"), reverse=True)
    for operation in operations:
        sorted_operation.append(operation)
    return sorted_operation
