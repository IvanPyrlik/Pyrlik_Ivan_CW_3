import pytest

from src.models import Operation


@pytest.fixture
def test_operation():
    operation_1 = Operation(
        pk=716496732,
        date="2018-04-26T15:40:13.413061",
        state="EXECUTED",
        amount={
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        description="Перевод организации",
        from_="Visa Gold 5999414228426353",
        to="Счет 72731966109147704472")
    operation_2 = Operation(
        pk=615064591,
        date="2018-01-24T17:33:34.701093",
        state="CANCELED",
        amount={
            "amount": "77751.04",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="Перевод с карты на счет",
        from_="Maestro 3928549031574026",
        to="Счет 84163357546688983493")
    return [operation_1, operation_2]


@pytest.fixture
def operation_dict():
    return [{
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2018-01-26T15:40:13.413061",
        "operationAmount": {
            "amount": "50870.71",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 4598300720424501",
        "to": "Счет 43597928997568165086"
    }, {}]
