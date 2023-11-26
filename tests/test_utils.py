from src.models import Operation
from src.utils import get_information_operations, get_executed_operations, get_sorted_operations


def test_get_information_operations(operation_dict):
    operation = get_information_operations(operation_dict)
    assert len(operation) == 1
    assert operation[0].pk == 147815167
    assert isinstance(operation, list)
    assert isinstance(operation[0], Operation)


def test_get_executed_operations(test_operation):
    operation = get_executed_operations(test_operation)
    assert len(operation) == 1
    assert isinstance(operation, list)
    assert isinstance(operation[0], Operation)
    assert operation[0].state == "EXECUTED"


def test_get_sorted_operations(test_operation):
    operation = get_sorted_operations(test_operation)
    assert len(operation) == 2
    assert isinstance(operation, list)
    assert isinstance(operation[0], Operation)
    assert operation[0].date > operation[1].date
